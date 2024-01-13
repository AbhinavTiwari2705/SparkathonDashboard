import streamlit as st
import pandas as pd
import streamlit.components.v1 as components
import numpy as np
import chart_studio.plotly as py
import chart_studio.tools as tls
import plotly.graph_objs as go
import plotly.express as px
import streamlit_option_menu as option_menu

with open("styles.css") as source_style:
    st.markdown(f"<style>{source_style.read()}</style>",
                unsafe_allow_html=True)


with st.sidebar:
  selected = option_menu.option_menu(menu_title="Main Menu", options=["Home", "EDA"])

if selected == "Home":
  st.markdown("""<div style="line-height: 1.4; letter-spacing: 0.3px"> Monitoring the Water Quality in Bhopal Region using Satellite Imagery and GIS Techniques </div>""",
                unsafe_allow_html=True)
  
  st.markdown('\n')

  st.subheader('THE BACKGROUND:')

  st.markdown('In the 1980s, the Bhopal region experienced one of the worst industrial disasters marked to date. The catastrophe raised awareness about industrial pollution. The water quality of the lakes in Bhopal has been significantly impacted by the 1984 gas tragedy. The release of toxic chemicals from the Union Carbide India Limited (UCIL) pesticide plant has contaminated the ground and surface water in the area, including the lakes. Tests conducted on the groundwater in communities situated around the Union Carbide factory in Bhopal have revealed high levels of pollutants such as heavy metals like lead, mercury, cadmium, Gamma HCH, Lindane, Beta HCH, Styrene, Mercury, Alpha HCH, Alpha Naphthol, Phosgene, Dichlorobenzene, etc.\n\n In the years that followed, the Bhopal region dealt with environmental challenges, particularly regarding water quality. The lakes are also heavily polluted with volatile organic compounds (VOCs), such as benzene and toluene, pesticides, herbicides, and Polycyclic aromatic hydrocarbons, leading to a decline in fish and other aquatic life. The water is also not safe for swimming or other recreational activities.')

  st.markdown('\n')
  
  st.subheader('THE PROBLEM:')

  st.markdown('Bhopal is also known as “The City of Lakes”, which indicates that Bhopal has a significant quantity of Lakes. People who live in the area are constantly in contact with chemicals assimilated in the water bodies during Gas Tragedy.  Surveys done by the Bhopal campaign groups have shown that their environment contains six of the persistent organic pollutants banned by the United Nations for their highly poisonous impacts on the environment and human health, which has now reached 42 areas in Bhopal and continues to spread. According to the Surveyors, the situation is getting worse, and second and third-generation children are being born with disabilities.\n\n Apart from this, during the “Gas Tragedy”, MIC(methyl isocyanide) was released, which reacts with water exothermically and produces carbon dioxide, methylamine, dimethylurea, and/or trimethyl biuret, these chemicals cause adverse effects on human bodies while incorporating itself to water. Swiss lab results show chloroform concentrations as many as 3.5 times higher than drinking-water guidelines from the World Health Organization and U.S. EPA , and carbon tetrachloride at up to 2,400 times higher than the guidelines, which impels us to study various lakes of Bhopal.')

  st.markdown('\n')
  
  st.subheader('THE PROJECT GOALS:')

  st.markdown('This study aims to develop a Machine Learning system for monitoring the water quality of multiple lakes in the Bhopal region using satellite imagery and GIS techniques. The objective is to assess the water quality, detect the probable causes of water pollution and predict the potential impacts of different pollution sources on the environment and human health. The study will use a combination of remote sensing techniques, image processing methods, and GIS tools to extract relevant information from satellite data. Additionally, the system will enable real-time monitoring of water quality, allowing for timely intervention in case of any deterioration in water quality.')

 
elif selected == "EDA":
  st.markdown("""<h style = " "> Exploratory Data Analysis </h>""", unsafe_allow_html = True)
 
  st.sidebar.subheader("Visualisation Settings")


  chart_select = st.sidebar.selectbox(
    label = "Select the Lake",
    options = ['Hathaikheda dam', 'Sarangpani lake', 'Upper lake']
  )
  if chart_select == 'Hathaikheda dam':
      df = pd.read_csv('Hathaikheda.csv')
      st.subheader('Hathaikheda dam')
  elif chart_select == 'Sarangpani lake' :
     df = pd.read_csv('SarangpaniLakefinal.csv')
     st.subheader('Sarangpani lake')
  elif chart_select == 'Upper lake' :
     df = pd.read_csv('UPlake.csv')
     st.subheader('Upper Lake')


   
  show_data = st.sidebar.checkbox("Show dataset")

  if show_data:
    st.write(df)

  global numeric_columns
  try:
    numeric_columns  = list(df.select_dtypes(['float','int' ]).columns)
  except Exception as e:
    print(e)
    


  chart_select = st.sidebar.selectbox(
    label = "Select the Chart Type",
    options = ['Scatterplots', 'Lineplots', 'Histogram', 'Boxplot']
  )

  if chart_select == 'Scatterplots':
    st.sidebar.subheader('Scatterplot Settings')
    try:
        x_values = st.sidebar.selectbox('X axis', options = numeric_columns)
        y_values = st.sidebar.selectbox('Y axis', options = numeric_columns)
        plot = px.scatter(data_frame = df, x = x_values, y = y_values)
        st.plotly_chart(plot)
    except Exception as e:
        print(e)

  if chart_select == 'Lineplots':
    st.sidebar.subheader('Lineplots Settings')
    try:
        x_values = st.sidebar.selectbox('X axis', options = numeric_columns)
        y_values = st.sidebar.selectbox('Y axis', options = numeric_columns)
        plot = px.area(data_frame = df, x = x_values, y = y_values)
        st.plotly_chart(plot)
    except Exception as e:
        print(e)

  if chart_select == 'Boxplot':
    st.sidebar.subheader('Boxplot Settings')
    try:
        x_values = st.sidebar.selectbox('X axis', options = numeric_columns)
        y_values = st.sidebar.selectbox('Y axis', options = numeric_columns)
        plot = px.box(data_frame = df, x = x_values, y = y_values)
        st.plotly_chart(plot)
    except Exception as e:
        print(e)

  if chart_select == 'Histogram':
    st.sidebar.subheader('Histogram Settings')
    try:
        x_values = st.sidebar.selectbox('Select the variable to plot histogram', options = numeric_columns)
        bins = st.sidebar.slider("Select the number of bins", min_value=5, max_value=50, value=20, step=1)
        plot = px.histogram(data_frame = df, x = x_values, nbins=bins)
        st.plotly_chart(plot)
    except Exception as e:
        print(e)
