import streamlit as st
from datetime import date
import os
import pandas as pd
import yfinance as yf
import plotly.graph_objects as go

START = "2018-01-01"
TODAY = date.today().strftime("%Y-%m-%d")

st.title("ForecastCryptoX")

cryptos = ("BTC-USD", "ETH-USD", "USDT-USD", "BNB-USD", "SOL-USD",
           "XRP-USD", "ADA-USD", "AVAX-USD", "DOGE-USD", "TRX-USD")
selected_crypto = st.selectbox("Select crypto for prediction: ", cryptos)

n_years = st.slider("Years of prediction: ", 1, 4)
period = n_years * 365


@st.cache_data
def load_data(ticker):
    data = yf.download(ticker, START, TODAY)
    data.reset_index(inplace=True)
    return data


data_load_state = st.text("Loading data...")
data = load_data(selected_crypto)
data_load_state.text("Loading data... done!")

st.subheader('Raw data')
st.write(data.tail())


def plot_raw_data():
    fig = go.Figure()
    fig .add_trace(go.Scatter(
        x=data['Date'], y=data['Open'], name='crypto_open'))
    fig .add_trace(go.Scatter(
        x=data['Date'], y=data['Close'], name='crypto_close', line=dict(color='red')))
    fig.layout.update(title_text="Time Series Data",
                      xaxis_rangeslider_visible=True)
    st.plotly_chart(fig)


plot_raw_data()
