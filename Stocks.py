# -*- coding: utf-8 -*-
"""
Created on Fri Jul  2 22:27:28 2021

@author: Enqey De-Ben Rockson
"""

import streamlit as st  
import yfinance as yf
import datetime

# Title of the app
st.title('Stock Market Tracker') 

st.write("""
# Track your stock portfolio performance         
""")

st.markdown("""
* **Data Source**: Yahoo Finance     
""")

# Sidebar filters for user input
st.sidebar.header('User Input Filters')

# Date inputs
start_date = st.sidebar.date_input("Start Date", datetime.date(2020, 1, 31))
end_date = st.sidebar.date_input("End Date", datetime.date(2021, 1, 31))

# Interval options
intervals = ['3mo', '1mo'] 
selected_interval = st.sidebar.selectbox('Interval', intervals)

# Ticker symbol options
tickers = ['GOOGL', 'MSFT', 'AAPL', 'AMZN']
selected_ticker = st.sidebar.selectbox('Ticker', tickers)

# Fetch stock data
ticker_data = yf.Ticker(selected_ticker)
try:
    ticker_df = ticker_data.history(interval=selected_interval, start=start_date, end=end_date)

    # Display Close values as a line chart
    st.write("""
    * **Close**: Closing market value
    """)
    st.line_chart(ticker_df['Close'])

    # Display Open values as a line chart
    st.write("""
    * **Open**: Opening market value
    """)
    st.line_chart(ticker_df['Open'])

    # Display Volume as a line chart
    st.write("""
    * **Volume**: Total volume of shares on the market
    """)
    st.line_chart(ticker_df['Volume'])

    # Display recommendations
    st.write("""
    * **Recommendations**: Buy recommendations by analysts
    """)
    if ticker_data.recommendations is not None:
        st.write(ticker_data.recommendations)
    else:
        st.write("No recommendations available for this ticker.")
    
    # Display raw data
    st.write("### Raw Data")
    st.dataframe(ticker_df)
except Exception as e:
    st.error(f"An error occurred: {e}")
