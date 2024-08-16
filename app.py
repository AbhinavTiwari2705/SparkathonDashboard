import streamlit as st
import pandas as pd
import plotly.express as px
import streamlit_option_menu as option_menu

with open("styles.css") as source_style:
    st.markdown(f"<style>{source_style.read()}</style>", unsafe_allow_html=True)

with st.sidebar:
    selected = option_menu.option_menu(menu_title="Main Menu", options=["EDA"])

if selected == "EDA":
    st.markdown("""<h style=" "> Exploratory Data Analysis </h>""", unsafe_allow_html=True)
    
    st.sidebar.subheader("Visualisation Settings")

    chart_select = st.sidebar.selectbox(
        label="Select the data",
        options=['synthetic_seasonal_product_sales','other data (Naam nhi pta)']
        # options=['other data (Naam nhi pta)']
    )
    
    if chart_select == 'synthetic_seasonal_product_sales':
        df1 = pd.read_csv('sales.csv')
        st.subheader('synthetic_seasonal_product_sales')
    elif chart_select =='other data (Naam nhi pta)':
        df1 = pd.read_csv('dataset.csv')
        st.subheader('Other Data')


    show_data = st.sidebar.checkbox("Show dataset")
    if show_data:
        st.write(df1)

    numeric_columns = list(df1.select_dtypes(['float', 'int']).columns)

    chart_select = st.sidebar.selectbox(
        label="Select the Chart Type",
        options=['Scatterplots', 'Lineplots', 'Histogram', 'Boxplot']
    )

    if chart_select == 'Scatterplots':
        st.sidebar.subheader('Scatterplot Settings')
        try:
            x_values = st.sidebar.selectbox('X axis', options=numeric_columns)
            y_values = st.sidebar.selectbox('Y axis', options=numeric_columns)
            plot = px.scatter(data_frame=df1, x=x_values, y=y_values)
            st.plotly_chart(plot)
        except Exception as e:
            st.error(f"Error: {e}")

    if chart_select == 'Lineplots':
        st.sidebar.subheader('Lineplots Settings')
        try:
            x_values = st.sidebar.selectbox('X axis', options=numeric_columns)
            y_values = st.sidebar.selectbox('Y axis', options=numeric_columns)
            plot = px.line(data_frame=df1, x=x_values, y=y_values)
            st.plotly_chart(plot)
        except Exception as e:
            st.error(f"Error: {e}")

    if chart_select == 'Boxplot':
        st.sidebar.subheader('Boxplot Settings')
        try:
            x_values = st.sidebar.selectbox('X axis', options=numeric_columns)
            y_values = st.sidebar.selectbox('Y axis', options=numeric_columns)
            plot = px.box(data_frame=df1, x=x_values, y=y_values)
            st.plotly_chart(plot)
        except Exception as e:
            st.error(f"Error: {e}")

    if chart_select == 'Histogram':
        st.sidebar.subheader('Histogram Settings')
        try:
            x_values = st.sidebar.selectbox('Select the variable to plot histogram', options=numeric_columns)
            bins = st.sidebar.slider("Select the number of bins", min_value=5, max_value=50, value=20, step=1)
            plot = px.histogram(data_frame=df1, x=x_values, nbins=bins)
            st.plotly_chart(plot)
        except Exception as e:
            st.error(f"Error: {e}")
