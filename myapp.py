import yfinance as yf
import streamlit as st
import pandas as pd

st.write(""" 
# Stock Price App
### Shown are the stock closing price and volume of TESLA!
""")
tickerSymbol = 'TSLA'
tickerData = yf.Ticker(tickerSymbol)
tickerDf = tickerData.history(period='id', start='2020-7-15', end='2022-7-15')
st.line_chart(tickerDf.Close)
st.line_chart(tickerDf.Volume)