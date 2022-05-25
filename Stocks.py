# -*- coding: utf-8 -*-
"""
Created on Fri Jul  2 22:27:28 2021

@author: Enqey De-Ben Rockson
"""

import streamlit as st  
import yfinance as yf
import datetime

st.title ('Stock Market Tracker') 

st.write("""
# Track your stock portfolio performance         
         """)

st.markdown("""
 * **  Data Source:  Yahoo-Finance     
            """)

st.sidebar.header('User Input Filters')
#Period = st.sidebar.date_input(" Date range without default ", [datetime.date(2020,1,1),datetime.date(2021,7,8)])

Period_1 = st.sidebar.date_input("Start_date", datetime.date(2020,1,31) )
Period_2 = st.sidebar.date_input("End_date", datetime.date(2021,1,31))
inte     = ['3mo','1mo'] 
inte2    = st.sidebar.selectbox('inte',list(inte))

Tksign = ['GOOGL','MSFT','AAPL','AMZN']
Tk = st.sidebar.selectbox('Ticker', list(Tksign))


Tickerdata = yf.Ticker(Tk)
    #Tickerdf = Tickerdata.history(interval  'd',start = '2010-1-1', end = '2020-1-1' )
    
Tickerdf = Tickerdata.history(interval = inte2 ,start = Period_1 , end = Period_2 )

st.write("""
* ** Close **: Closing market value
         """)
st.line_chart(Tickerdf.Close)

st.write("""
* ** Open **: Opening market value
         """)
st.line_chart(Tickerdf.Open)

st.write("""
* ** Volume **: Total Volume of shares on the market
         """)
         
st.line_chart(Tickerdf.Volume)

st.write("""
* ** Recommendations ** : Buy recommendations by Analysts
         """)
Tickerdata.recommendations

Tickerdf


