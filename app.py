import streamlit as st
import pandas as pd
import numpy as np
import sqlite3
import matplotlib.pyplot as plt
import plotly.graph_objs as go
import plotly.express as px
st.set_page_config(
    page_title = 'FireAnt',
    page_icon = '✅',
    layout = 'wide'
)
st.write(f'<div style="text-align:center;font-size:40px;font-weight:bold;">"Hello FireAnt"</div>',
    unsafe_allow_html=True
)





# st.sidebar.title('Tổng quan')
# hsx_button = st.sidebar.button("HSX")
# hnx_button = st.sidebar.button("HNX")
# upcom_button = st.sidebar.button("UPCOM")
# if hsx_button:
#     current_page = "HSX"
# elif hnx_button:
#     current_page = "HNX"
# elif upcom_button:
#     current_page = "UPCOM"
# else:
#     current_page = "HSX"

# if current_page == "HSX":
#     st.write(
#     f'<div style="text-align:center;font-size:32px;font-weight:bold;">{current_page}</div>',
#     unsafe_allow_html=True
# )      
#     st.markdown(
#     """
#     <style>
#     .my-button {
#         background-color: #4CAF50;
#         border: none;
#         color: white;
#         padding: 15px 32px;
#         text-align: center;
#         text-decoration: none;
#         display: inline-block;
#         font-size: 16px;
#         margin: 4px 2px;
#         cursor: pointer;
#         border-radius: 10px;
#     }
#     </style>
#     """
#     , unsafe_allow_html=True
# )
#     if st.button("MBB", key="my_button", help="Custom Button", on_click=None, args=None, kwargs=None):
#        query = "SELECT * FROM chung_khoan2"
#        df = pd.read_sql(query, connection)
#        fig = go.Figure()
#        fig.add_trace(go.Scatter(x=df['date'], y=df['volume'], mode='lines', name='Volume'))
#        fig.update_layout(title='Biểu đồ Volume', xaxis_title='Ngày', yaxis_title='Volume')
#        st.plotly_chart(fig)

#        fig = go.Figure()
#        fig.add_trace(go.Bar(x=df['date'], y=df['open'], name='Open', marker_color='blue'))
#        fig.add_trace(go.Bar(x=df['date'], y=df['close'], name='Close', marker_color='orange'))
#        fig.update_layout(barmode='group', title='Biểu đồ Open và Close', xaxis_title='Ngày', yaxis_title='Giá trị')
#        st.plotly_chart(fig)

#        fig = go.Figure()
#        fig.add_trace(go.Bar(x=df['date'], y=df['high'], name='High', marker_color='green'))
#        fig.add_trace(go.Bar(x=df['date'], y=df['low'], name='Low', marker_color='red'))
#        fig.update_layout(barmode='group', title='Biểu đồ High và Low', xaxis_title='Ngày', yaxis_title='Giá trị')
#        st.plotly_chart(fig)
    
#     if st.button("SHB", key="my_button1", help="Custom Button", on_click=None, args=None, kwargs=None):
#         st.write("hello")
# elif current_page == "HNX":
#     st.write(
#     f'<div style="text-align:center;font-size:32px;font-weight:bold;">{current_page}</div>',
#     unsafe_allow_html=True
# )
# elif current_page == "UPCOM":
#     st.write(
#     f'<div style="text-align:center;font-size:32px;font-weight:bold;">{current_page}</div>',
#     unsafe_allow_html=True
#   )  