# -*- coding: utf-8 -*-
"""
Created on Mon Apr 29 14:04:01 2024

@author: Elopy
"""
import streamlit as st
import plotly.express as px 
import pandas as pd


st.title('Eloppyx1 to be launched soon 🔥🔥')
st.subheader("Hey buds, we're in! Let's start our new project right here🧨")
st.markdown('<style>div.block-container{padding-top:1rem}</style>',unsafe_allow_html=True)



df = pd.read_csv("insurance.csv",encoding="ISO-8859-1")
# Create a treemap based on Region, category, sub-Category
st.subheader("Hierarchical view of insurance cost using TreeMap",divider="green")
fig3 = px.treemap(df, path = ["region","sex","smoker"], values = "charges",hover_data = ["charges"],
                  color = "smoker")
fig3.update_layout(width = 800, height = 650)
st.plotly_chart(fig3, use_container_width=True)

chart1, chart2 = st.columns((2))
with chart1:
    st.subheader('Charges v smoking',divider="orange")
    fig = px.pie(df, values = "charges", names = "smoker", template = "plotly_dark",hole=0.5)
    fig.update_traces(text = df["smoker"], textposition = "inside")
    st.plotly_chart(fig,use_container_width=True)

with chart2:
    st.subheader('Charges v region',divider="green")
    fig = px.pie(df, values = "charges", names = "region", template = "gridon")
    fig.update_traces(text = df["region"], textposition = "inside")
    st.plotly_chart(fig,use_container_width=True)
    
    
chart3, chart4 = st.columns((2))
with chart3:
    st.subheader('Charges v gender',divider="orange")
    fig = px.pie(df, values = "charges", names = "sex", template = "plotly_dark",hole=0.5)
    fig.update_traces(text = df["sex"], textposition = "inside")
    st.plotly_chart(fig,use_container_width=True)

with chart4:
    st.success('Seems like men spend more!')
    
    
st.subheader('BMI v charges',divider="green")


fig2 = px.histogram(df, x = "bmi", y="charges", labels = {'bmi':'Body Mass Index',"charges": "Amount charged in USD"},height=500, width = 1000,template="gridon")
st.plotly_chart(fig2,use_container_width=True)








