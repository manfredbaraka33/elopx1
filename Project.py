# -*- coding: utf-8 -*-
"""
Created on Mon Apr 29 14:04:01 2024

@author: Elopy
"""
import streamlit as st
import plotly.express as px 
import pandas as pd
from streamlit_option_menu import option_menu


st.set_page_config(page_title="Elopyx-pj", layout='wide',page_icon=":bar_chart:")


# the side bar for navigation
with st.sidebar:
    selected = option_menu("Elopyx projects",
                          [ 'Elopyx1-1',
                           'Elopyx1-2',
                           'Elopyx1-3',
                           'Elopyx1-4'
                           ],
                          icons=['binoculars-fill','collection-fill','database-fill','playstation'],
                          default_index=0
                          )



df = pd.read_csv("D:/New folder (4)/datasets/insurance.csv",encoding="ISO-8859-1")


if selected == 'Elopyx1-1':

    st.title('Eloppyx1 to be launched soon 🔥🔥')
    st.subheader("Hey buds, we're in! Let's start our new project right here🧨")
    st.markdown('<style>div.block-container{padding-top:1rem}</style>',unsafe_allow_html=True)
    
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

elif selected == 'Elopyx1-2':
    st.title('Hello evry body, its time for project Elopyx1-2')
    with st.expander('The dataset for medical insuarance cost'):
       st.dataframe(df)
    
elif selected == 'Elopyx1-3':
    st.title('Hello evrybody, its time for project Elopyx1-3')
    import streamlit as st 

    st.write("I you fill like bloging can be one of your ways to mmake passive income then, check out this [blog](https://www.ryrob.com/blog/)")
    
else:
    st.title('Hello friends, leys give a shot for project Elopyx1-4')
    st.markdown("Wanna mwke money online read this [article](https://www.ryrob.com/make-money-online/) from the best blogger in the market.")






