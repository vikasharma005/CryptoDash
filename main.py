"""
Cryptocurency Daily Prices 
Dashboard using streamlit and Yahoo Finance libraries
@vikasharma005
Almost the same thing we did with stock prices in previous tutorial
"""
import yfinance as yf
import streamlit as st
from PIL import Image
from urllib.request import urlopen

# Titles and subtitles
st.title("Cryptocurrency Daily Prices | ₿")
#st.header("Main Dashboard")
#st.subheader("You can add more crypto in code </>")

# Defining ticker variables
Bitcoin = 'BTC-USD'
Ethereum = 'ETH-USD'
Ripple = 'XRP-USD'
BitcoinCash = "BCH-USD"

# User input for date range
start_date = st.date_input("Select a start date", value=(2021, 11, 19))
end_date = st.date_input("Select an end date", value=(2021, 11, 19))

# Access data from Yahoo Finance
BTC_Data = yf.Ticker(Bitcoin)
ETH_Data = yf.Ticker(Ethereum)
XRP_Data = yf.Ticker(Ripple)
BCH_Data = yf.Ticker(BitcoinCash)

# Fetch history data from Yahoo Finance based on user input
BTCHis = BTC_Data.history(period="max", start=start_date, end=end_date)
ETHHis = ETH_Data.history(period="max", start=start_date, end=end_date)
XRPHis = XRP_Data.history(period="max", start=start_date, end=end_date)
BCHHis = BCH_Data.history(period="max", start=start_date, end=end_date)

# Fetch crypto data for the dataframe based on user input
BTC = yf.download(Bitcoin, start=start_date, end=end_date)
ETH = yf.download(Ethereum, start=start_date, end=end_date)
XRP = yf.download(Ripple, start=start_date, end=end_date)
BCH = yf.download(BitcoinCash, start=start_date, end=end_date)

# Display data for each cryptocurrency
cryptos = [
    ("BITCOIN", imageBTC, BTC, BTCHis),
    ("ETHERUM", imageETH, ETH, ETHHis),
    ("RIPPLE", imageXRP, XRP, XRPHis),
    ("BITCOIN CASH", imageBCH, BCH, BCHHis)
]

for crypto_name, crypto_image, crypto_df, crypto_hist in cryptos:
    st.write(f"{crypto_name} ($)")
    st.image(crypto_image)
    st.write("Historical Data:")
    st.table(crypto_hist)
    st.write("Data on Selected Date Range:")
    st.table(crypto_df)
    st.write("Price Chart:")
    st.bar_chart(crypto_hist.Close)
