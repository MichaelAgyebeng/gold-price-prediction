🌟 Gold Price Prediction App

A fully interactive Streamlit web application that predicts gold prices using financial market indicators such as SPX, USO, SLV, and EUR/USD.
This app features real-time predictions, beautiful Plotly interactive charts, multi-tab navigation, and optional banner graphics.

Deployable for free on Streamlit Community Cloud.

📌 Features
✅ Gold Price Prediction

Predict gold prices using:

SPX – S&P 500 Index

USO – United States Oil Fund

SLV – iShares Silver Trust

EUR/USD – Euro to USD exchange rate

The model used is a Random Forest Regression model trained on historical market data.

📈 Interactive Plotly Chart

View an interactive comparison of:

Actual Gold Prices

Predicted Gold Prices

Features include zoom, hover, pan, and dynamic legend control.

🎨 Modern Multi-Tab UI

The interface uses Streamlit’s tabs() functionality:

Prediction tab

Interactive chart tab

About tab

🖼️ Optional Banner Image

Place a banner named:

gold_banner.jpg


in your project root to show a header image.
If not provided, the app shows a friendly message instead of crashing.

📁 Project Structure

Your GitHub repo should contain:

gold-price-prediction/
│
├── streamlit_app.py           # Main Streamlit application
├── requirements.txt           # Python dependencies
├── RF_regression_model.pkl    # Trained Random Forest model
├── gld_price_data.csv         # Dataset with GLD and feature columns
└── gold_banner.jpg            # (Optional) banner image

🚀 Deployment (FREE)
1. Upload your files to GitHub

Create a repository and upload all items listed above.

2. Go to Streamlit Cloud

Visit:

🔗 https://share.streamlit.io

3. Deploy the App

Click New App

Choose your GitHub repo

Set the file path to:

streamlit_app.py


Click Deploy

Your app will be publicly available at:

https://your-username-your-repo.streamlit.app

🛠️ Requirements

Your requirements.txt must include:

streamlit
pandas
numpy
scikit-learn
joblib
plotly


Add any additional packages your model needs.

📊 Dataset

The app expects a file named:

gld_price_data.csv


This must include:

GLD (actual gold price)

Predictor features:

SPX, USO, SLV, EUR/USD

And any additional features used by your model.

🧠 Model

This app uses:

Random Forest Regression (RF_regression_model.pkl)

Exported via joblib.

The model must include feature_names_in_ (automatically added by scikit-learn 1.2+).

💬 Support

If you'd like help:

✔ Adding forecasting (7-day / 30-day)
✔ Adding candlestick charts
✔ Improving the UI
✔ Adding animations
✔ Automating dataset updates

Just open an issue or request enhancements!

⭐️ Want to contribute?

Pull requests are welcome!
Improving the model, UI, or documentation is encouraged
