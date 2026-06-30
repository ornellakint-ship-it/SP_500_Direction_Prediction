
import streamlit as st
import yfinance as yf
import pandas as pd
import numpy as np
import joblib
from ta.trend import SMAIndicator, EMAIndicator, MACD
from ta.momentum import RSIIndicator
from ta.volatility import BollingerBands

# Load model and scaler
model = joblib.load('sp500_model.pkl')
scaler = joblib.load('sp500_scaler.pkl')

st.title("📈 S&P 500 Next-Day Direction Predictor")
st.write("Predicts whether the S&P 500 will close UP or DOWN tomorrow, based on technical indicators.")

# Fetch latest data
@st.cache_data(ttl=3600)  # refresh every hour
def get_data():
    df = yf.download("^GSPC", period="1y")
    if isinstance(df.columns, pd.MultiIndex):
        df.columns = df.columns.get_level_values(0)
    df['Close'] = df['Close'].astype(float)
    return df

df = get_data()

# Feature engineering (same as training)
df['SMA_20'] = SMAIndicator(close=df['Close'], window=20).sma_indicator()
df['EMA_20'] = EMAIndicator(close=df['Close'], window=20).ema_indicator()
df['RSI'] = RSIIndicator(close=df['Close'], window=14).rsi()
macd = MACD(close=df['Close'])
df['MACD'] = macd.macd()
df['MACD_signal'] = macd.macd_signal()
bb = BollingerBands(close=df['Close'])
df['BB_high'] = bb.bollinger_hband()
df['BB_low'] = bb.bollinger_lband()
df['log_return'] = np.log(df['Close'] / df['Close'].shift(1))
df['return_1'] = df['Close'].pct_change(1)
df['return_2'] = df['Close'].pct_change(2)
df['return_3'] = df['Close'].pct_change(3)
df['return_5'] = df['Close'].pct_change(5)
df['volume_change'] = df['Volume'].pct_change(1)
df['dist_SMA20'] = (df['Close'] - df['SMA_20']) / df['SMA_20']

df.replace([np.inf, -np.inf], np.nan, inplace=True)
df.dropna(inplace=True)

# Get latest row for prediction
features = ['SMA_20', 'EMA_20', 'RSI', 'MACD', 'MACD_signal', 
            'BB_high', 'BB_low', 'log_return',
            'return_1', 'return_2', 'return_3', 'return_5',
            'volume_change', 'dist_SMA20']

latest = df[features].iloc[-1:]
latest_scaled = scaler.transform(latest)

prediction = model.predict(latest_scaled)[0]
probability = model.predict_proba(latest_scaled)[0]

# Display results
st.subheader("Latest Prediction")
last_close = df['Close'].iloc[-1]
last_date = df.index[-1].strftime('%Y-%m-%d')

st.write(f"**Last available close ({last_date}):** {last_close:.2f}")

if prediction == 1:
    st.success(f"📈 Predicted direction: **UP** (confidence: {probability[1]*100:.1f}%)")
else:
    st.error(f"📉 Predicted direction: **DOWN** (confidence: {probability[0]*100:.1f}%)")

# Show recent price chart
st.subheader("Recent Price History")
st.line_chart(df['Close'].tail(60))

# Show raw data (optional)
with st.expander("See raw data"):
    st.dataframe(df.tail(10))