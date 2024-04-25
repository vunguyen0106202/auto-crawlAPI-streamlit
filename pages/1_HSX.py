import streamlit as st
import pandas as pd
import numpy as np
import sqlite3
import matplotlib.pyplot as plt
import plotly.graph_objs as go
import plotly.express as px
import time
import altair as alt
from datetime import datetime
st.write(f'<div style="text-align:center;font-size:40px;font-weight:bold;"> HSX</div>',
    unsafe_allow_html=True
)
alt.themes.enable("dark")
d=[ "MBB","FPT", "NVL","VND","SSI","DIG","SHB","STB","DXG","TPB","HPG","MWG","TCH","DBC","EIB","GEX","VHM","VPB","HDB","HAG"]
fire_Ant = st.selectbox("Select", pd.unique(d))
placeholder = st.empty()

while True:
    path="D:/tai/csdl.db"
    connection=sqlite3.connect(path)
    table_name = "chung_khoan_" + fire_Ant
    query = "SELECT * FROM {}".format(table_name)
    df = pd.read_sql(query, connection)
    current_datetime = datetime.now()
    current_date = current_datetime.date()
    current_date=str(current_date)+'T00:00:00Z'
    #current_date='2024-01-26T00:00:00Z'
    dff = df[df['date']==current_date]
    with placeholder.container():
        kpi1, kpi2, kpi3,kpi4,kpi7 = st.columns(5)
        kpi1.metric(label="close ", value=round(dff['close'].iloc[0]))
        kpi2.metric(label="high ", value=round (dff['high'].iloc[0]))
        kpi3.metric(label="low ", value=round (dff['low'].iloc[0]))
        kpi4.metric(label="open ", value=round (dff['open'].iloc[0]))
        #kpi5.metric(label="volume ", value=round (df['openInt'].iloc[0]))
        #kpi6.metric(label="volume ", value=round (df['value'].iloc[0]))
        kpi7.metric(label="volume ", value= round(dff['volume'].iloc[0]) )
        
        fig = go.Figure()
        fig.add_trace(go.Scatter(x=df['date'], y=df['volume'], mode='lines', name='Volume'))
        fig.update_layout(title='Biểu đồ Volume', xaxis_title='Ngày', yaxis_title='Volume')
        st.plotly_chart(fig)

        fig = go.Figure()
        fig.add_trace(go.Bar(x=df['date'], y=df['open'], name='Open', marker_color='blue'))
        fig.add_trace(go.Bar(x=df['date'], y=df['close'], name='Close', marker_color='orange'))
        fig.update_layout(barmode='group', title='Biểu đồ Open và Close', xaxis_title='Ngày', yaxis_title='Giá trị')
        st.plotly_chart(fig)

        fig = go.Figure()
        fig.add_trace(go.Bar(x=df['date'], y=df['high'], name='High', marker_color='green'))
        fig.add_trace(go.Bar(x=df['date'], y=df['low'], name='Low', marker_color='red'))
        fig.update_layout(barmode='group', title='Biểu đồ High và Low', xaxis_title='Ngày', yaxis_title='Giá trị')
        st.plotly_chart(fig)
        time.sleep(45)