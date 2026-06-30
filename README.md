# S&P 500 Next-Day Direction Predictor

A machine learning web app that predicts whether the S&P 500 index will close **UP** or **DOWN** the next trading day, using technical indicators and live market data.

🔗 **Live demo:** _(https://sp500directionprediction-2iyk85hv8ut4mmu3auwrvc.streamlit.app/)_

---

## Overview

This project demonstrates an end-to-end ML pipeline applied to financial time series:

- Fetching live market data (`yfinance`)
- Engineering technical indicators (trend, momentum, volatility)
- Training and comparing classification models (Random Forest, LightGBM)
- Deploying a live, self-updating prediction dashboard with Streamlit

The app pulls fresh S&P 500 data on every run and produces an up-to-date prediction — it is not a static, one-time analysis.

---

## Features used

| Category | Indicators |
|---|---|
| Trend | SMA (20), EMA (20), MACD |
| Momentum | RSI (14) |
| Volatility | Bollinger Bands |
| Price action | Log return, lagged returns (1, 2, 3, 5 days) |
| Volume | Volume change |
| Distance from trend | Price distance from SMA 20 |

---

## Methodology

- **Time-respecting train/test split** — no random shuffling, since this is sequential market data
- **No data leakage** — scaler fitted on training data only, then applied to test data
- **Model comparison** — Random Forest and LightGBM were both tested; Random Forest with the extended feature set performed best (~51% accuracy)

### A note on accuracy

Financial markets are highly noisy and close to a random walk in the short term. An accuracy around 51–52% on next-day direction is consistent with what is generally observed in this kind of task — even small, consistent edges above 50% can be meaningful in trading contexts. This project is built to demonstrate methodology and deployment skills, not to provide financial advice.

---

## Tech stack

- Python
- yfinance — market data
- ta — technical indicators
- scikit-learn, LightGBM — modeling
- Streamlit — deployment
- pandas, numpy

---

## Running locally

```bash
pip install -r requirements.txt
streamlit run app.py
```

---

## Disclaimer

This project is for educational and portfolio purposes only. It does not constitute financial advice. Predictions are based on historical patterns and technical indicators, which have known limitations in forecasting financial markets.

---
---

# Prédicteur de Direction du S&P 500 (Jour Suivant)

Une application web de machine learning qui prédit si l'indice S&P 500 clôturera **À LA HAUSSE** ou **À LA BAISSE** le jour de bourse suivant, à partir d'indicateurs techniques et de données de marché en direct.

🔗 **Démo en ligne :** _(https://sp500directionprediction-2iyk85hv8ut4mmu3auwrvc.streamlit.app/)_

---

## Aperçu du projet

Ce projet illustre un pipeline de machine learning complet appliqué à une série temporelle financière :

- Récupération de données de marché en direct (`yfinance`)
- Création d'indicateurs techniques (tendance, momentum, volatilité)
- Entraînement et comparaison de modèles de classification (Random Forest, LightGBM)
- Déploiement d'un tableau de bord de prédiction en direct et auto-actualisé avec Streamlit

L'application récupère des données fraîches du S&P 500 à chaque exécution et produit une prédiction à jour — il ne s'agit pas d'une analyse statique réalisée une seule fois.

---

## Variables utilisées

| Catégorie | Indicateurs |
|---|---|
| Tendance | SMA (20), EMA (20), MACD |
| Momentum | RSI (14) |
| Volatilité | Bandes de Bollinger |
| Mouvement de prix | Rendement logarithmique, rendements décalés (1, 2, 3, 5 jours) |
| Volume | Variation du volume |
| Écart à la tendance | Distance du prix par rapport à la SMA 20 |

---

## Méthodologie

- **Découpage train/test respectant la chronologie** — pas de mélange aléatoire, car il s'agit de données de marché séquentielles
- **Aucune fuite de données** — le scaler est ajusté uniquement sur les données d'entraînement, puis appliqué aux données de test
- **Comparaison de modèles** — Random Forest et LightGBM ont été testés ; le Random Forest avec l'ensemble de variables étendu a obtenu les meilleurs résultats (~51% de précision)

### Une remarque sur la précision

Les marchés financiers sont très bruités et proches d'une marche aléatoire à court terme. Une précision d'environ 51 à 52% sur la direction du jour suivant est cohérente avec ce qui est généralement observé pour ce type de tâche — même un avantage faible mais constant au-dessus de 50% peut être significatif dans un contexte de trading. Ce projet vise à démontrer une méthodologie et des compétences de déploiement, et ne constitue pas un conseil financier.

---

## Stack technique

- Python
- yfinance — données de marché
- ta — indicateurs techniques
- scikit-learn, LightGBM — modélisation
- Streamlit — déploiement
- pandas, numpy

---

## Exécution en local

```bash
pip install -r requirements.txt
streamlit run app.py
```

---

## Avertissement

Ce projet est réalisé à des fins éducatives et de démonstration de compétences uniquement. Il ne constitue pas un conseil financier. Les prédictions reposent sur des tendances historiques et des indicateurs techniques, qui présentent des limites connues pour la prévision des marchés financiers.
