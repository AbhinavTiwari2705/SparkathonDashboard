import streamlit as st
import pandas as pd
import plotly.express as px
import streamlit_option_menu as option_menu
import joblib

# Load CSS styles
with open("styles.css") as source_style:
    st.markdown(f"<style>{source_style.read()}</style>", unsafe_allow_html=True)

# Sidebar menu
with st.sidebar:
    selected = option_menu.option_menu(menu_title="Main Menu", options=["EDA", "Model"])

if selected == "EDA":
    st.markdown("""<h style=" "> Exploratory Data Analysis </h>""", unsafe_allow_html=True)
    
    st.sidebar.subheader("Visualisation Settings")

    chart_select = st.sidebar.selectbox(
        label="Select the data",
        options=['synthetic_seasonal_product_sales','other data (Naam nhi pta)']
    )
    
    if chart_select == 'synthetic_seasonal_product_sales':
        df1 = pd.read_csv('sales.csv')
        st.subheader('synthetic_seasonal_product_sales')
    elif chart_select == 'other data (Naam nhi pta)':
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

# Model Section
if selected == "Model":
    # Load the model and original features
    rf_model = joblib.load('rf_model.pkl')
    original_features = joblib.load('original_features.pkl')

    def recommend_price(product_id, store_location, competitor_price, promotion, stock_level, season, rf_model, original_features):
        # Implement the recommendation logic here
        # Example placeholder implementation
        return {
            'product_id': product_id,
            'store_location': store_location,
            'predicted_units_sold': 100,  # Replace with actual prediction
            'recommended_price': 10.99,  # Replace with actual recommendation
            'estimated_revenue': 1000  # Replace with actual calculation
        }

    # Streamlit app interface
    st.title('Product Price Recommendation')

    product_id = st.number_input('Product ID', min_value=0)
    store_location = st.text_input('Store Location')
    competitor_price = st.number_input('Competitor Price', min_value=0.0, format="%.2f")
    promotion = st.selectbox('Promotion', [0, 1])
    stock_level = st.number_input('Stock Level', min_value=0)
    season = st.selectbox('Season', ['Winter', 'Spring', 'Summer', 'Autumn'])

    if st.button('Recommend Price'):
        result = recommend_price(
            product_id=product_id,
            store_location=store_location,
            competitor_price=competitor_price,
            promotion=promotion,
            stock_level=stock_level,
            season=season,
            rf_model=rf_model,
            original_features=original_features
        )

        st.write(f"Product ID: {result['product_id']}")
        st.write(f"Store Location: {result['store_location']}")
        st.write(f"Predicted Units Sold: {result['predicted_units_sold']}")
        st.write(f"Recommended Price: ${result['recommended_price']}")
        st.write(f"Estimated Revenue: ${result['estimated_revenue']}")
