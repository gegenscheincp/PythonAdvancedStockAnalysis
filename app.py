import sys, os
sys.path.append(os.path.dirname(os.path.abspath(__file__)))
import streamlit as st
import plotly.express as px

from data.fetch_data import get_stock_data
from analysis.indicators import add_indicators
from scanners.rsi_oversold import rsi_oversold
from scanners.earnings_gap import earnings_gap
from scanners.dividend_growth import dividend_growth_5pct
from scanners.ai_momentum import ai_momentum_score

st.set_page_config(layout="wide")
st.title("📈 Advanced Python Stock Analysis App")

ticker = st.text_input("Ticker", "AAPL")

df = add_indicators(get_stock_data(ticker))

fig = px.line(df, x=df.index, y=["Close", "SMA50", "SMA200"])
st.plotly_chart(fig, use_container_width=True)

col1, col2, col3 = st.columns(3)

with col1:
    st.metric("RSI", round(df["RSI"].iloc[-1], 2))
    st.write("Oversold:", rsi_oversold(df))

with col2:
    st.write("Earnings Gap:", earnings_gap(df))
    st.write("Dividend Growth ≥5%:", dividend_growth_5pct(ticker))

with col3:
    st.metric("AI Momentum Score", ai_momentum_score(df))
