import numpy as np
import pandas as pd
import plotly.express as pex
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from statsmodels.tsa.arima.model import ARIMA

# Step 1: Read and preprocess the data
df = pd.read_csv('data_sets/CO2 Emissions Around the World/CO2_emission.csv')
years = [str(1990+i) for i in range(26)]

# The attributes of the Data Frame
print(df.columns)
# Columns, Rows => Dimensions of the Data Frame
print(df.shape)
# Details regarding the DataFrame
print(df.describe())

# Melt dataframe so that the year attribute columns are joined
carbon_emissions = df.melt(id_vars=["Country Name", "country_code", "Region", "Indicator Name"], var_name="year", value_name = "co2_metric")

fig = pex.choropleth(carbon_emissions, locations='country_code', color='co2_metric', scope='world', animation_frame='year')
fig.show()

