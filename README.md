# Dynamic Pricing Model for Seasonal Products

## Overview

This project is part of Team Gana's submission for Sparkathon 2024, focusing on optimizing pricing for seasonal products using data science techniques. Our solution features an interactive Streamlit app that allows users to explore data through visualizations and obtain price recommendations based on a machine learning model.

## Features

1. **Exploratory Data Analysis (EDA)**
   - Users can explore datasets using various visualization options, such as scatter plots, line plots, histograms, and box plots.
   - The app supports multiple datasets and provides dynamic data exploration.

2. **Dynamic Pricing Model**
   - A machine learning model (RandomForestRegressor) is used to recommend optimal prices for seasonal products.
   - The model takes into account various features, including product ID, store location, competitor prices, promotions, stock levels, and season.
   - Users can input these parameters to get a price recommendation along with predicted units sold and estimated revenue.

## Installation

To run the application locally, follow these steps:

1. **Clone the repository:**
   ```bash
   git clone https://github.com/your-repository.git
   cd your-repository
   ```

2. **Install the required packages:**
   ```bash
   pip install -r requirements.txt
   ```

3. **Run the Streamlit app:**
   ```bash
   streamlit run app.py
   ```

## Files

- `app.py`: The main file containing the Streamlit application code.
- `sales.csv` & `dataset.csv`: Example datasets used for EDA.
- `rf_model.pkl`: Pre-trained RandomForestRegressor model for price recommendations.
- `original_features.pkl`: Original features used for training the model.
- `styles.css`: Custom CSS styles for the Streamlit app.

## Usage

1. **Exploratory Data Analysis (EDA)**
   - Select "EDA" from the sidebar menu.
   - Choose the dataset and chart type for visualization.
   - Customize the visualization settings using the sidebar options.

2. **Price Recommendation**
   - Select "Model" from the sidebar menu.
   - Enter the required input parameters for the product.
   - Click "Recommend Price" to get the recommended price, predicted units sold, and estimated revenue.

## Demo Video

Check out our demonstration video on YouTube.

## Presentation

You can view our detailed presentation here: [Presentation Link](https://www.canva.com/design/DAGOCt10aJ0/p9SSofbIiOVGLH-VTFUdtA/view?utm_content=DAGOCt10aJ0&utm_campaign=designshare&utm_medium=link&utm_source=editor)

## Contributing

If you wish to contribute to this project, please fork the repository and submit a pull request. For major changes, please open an issue first to discuss what you would like to change.

## License

This project is licensed under the MIT License.

## Contact

For any inquiries or feedback, please reach out to us.

## Hashtags

#DynamicPricing #MachineLearning #StreamlitApp #DataScience #RetailTech #Sparkathon2024 #TeamGana #Innovation #RetailSolutions #DataScienceInRetail
