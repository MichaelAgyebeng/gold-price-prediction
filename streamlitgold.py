import joblib
import pandas as pd
import streamlit as st
import plotly.graph_objects as go
import os

# -----------------------
# Load Model & Data
# -----------------------
regressor = joblib.load(r"F:\Gold price prediction ML\RF_regression_model.pkl")
data = pd.read_csv(r"F:\Gold price prediction ML\gld_price_data.csv")  # <-- update path

st.set_page_config(page_title="Gold Price Prediction", layout="wide")

# Optional banner image

banner_path = r"F:\Gold price prediction ML\gold_banner.jpg"

if os.path.exists(banner_path):
    st.image(banner_path, width="stretch")
else:
    st.info("💡 Add 'gold_banner.jpg' to show a banner image here.")
    
st.title("💰 Gold Price Prediction App (Interactive)")

tabs = st.tabs(["📈 Prediction", "📊 Interactive Chart", "ℹ About"])



# ===========================================================
# TAB 1 — Prediction UI
# ===========================================================
with tabs[0]:
    st.header("Enter Market Indicators")

    spx = st.number_input("S&P 500 Index (500–3000)", min_value=500.0, max_value=3000.0, value=1500.0)
    uso = st.number_input("USO ETF (5–150)", min_value=5.0, max_value=150.0, value=50.0)
    slv = st.number_input("SLV ETF (5–60)", min_value=5.0, max_value=60.0, value=25.0)
    eur_usd = st.number_input("EUR/USD (1.0–2.0)", min_value=1.0, max_value=2.0, value=1.2)

    if hasattr(regressor, "feature_names_in_"):
        expected_features = regressor.feature_names_in_
    else:
        st.error("Model missing feature names.")
        st.stop()

    if st.button("Predict Gold Price"):
        try:
            input_dict = {"SPX": spx, "USO": uso, "SLV": slv, "EUR/USD": eur_usd}
            full_input = {f: input_dict.get(f, 0) for f in expected_features}
            input_df = pd.DataFrame([full_input])
            prediction = regressor.predict(input_df)
            st.success(f"💵 Predicted Gold Price: **${prediction[0]:.2f}**")
        except Exception as e:
            st.error(f"Error: {e}")

# ===========================================================
# TAB 2 — Interactive Plotly Chart
# ===========================================================
with tabs[1]:
    st.header("📊 Interactive Predicted vs Actual Gold Price Chart")

    try:
        features = regressor.feature_names_in_
        X = data[features]
        data["Predicted_GLD"] = regressor.predict(X)

        fig = go.Figure()

        # Actual GLD line
        fig.add_trace(go.Scatter(
            x=data.index,
            y=data["GLD"],
            mode="lines",
            name="Actual GLD Price",
            line=dict(color="gold", width=3)
        ))

        # Predicted GLD line
        fig.add_trace(go.Scatter(
            x=data.index,
            y=data["Predicted_GLD"],
            mode="lines",
            name="Predicted GLD Price",
            line=dict(color="royalblue", width=2, dash="dash")
        ))

        fig.update_layout(
            title="Interactive Predicted vs Actual Gold Prices",
            xaxis_title="Index (Time)",
            yaxis_title="Gold Price (USD)",
            template="plotly_dark",
            height=500,
            hovermode="x unified"
        )

        st.plotly_chart(fig, use_container_width=True)

    except Exception as e:
        st.error(f"Could not generate chart: {e}")

# ===========================================================
# TAB 3 — About
# ===========================================================
with tabs[2]:
    st.header("About This App")
    st.write("""
    This app predicts gold prices using:
    • SPX (S&P 500 Index)  
    • USO (Oil ETF)  
    • SLV (Silver ETF)  
    • EUR/USD exchange rate  

    Features:
    • 📈 Real-time predictions  
    • 📊 Interactive Plotly charts  
    • ⚠️ Exception handling for invalid inputs  
    • 🎨 Modern multi-tab UI  
    """)

    st.write("Developed by Your Michael. © 2024")