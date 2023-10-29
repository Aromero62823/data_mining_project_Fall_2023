import numpy as np
import pandas as pd
import plotly.express as pex

# Step 1: Read and preprocess the data
df = pd.read_csv('data_sets/CO2 Emissions Around the World/CO2_emission.csv')
years = [str(1990+i) for i in range(26)]

# # TODO:
# 1. Fill values that are [Nan or None] with mean value
# 2. Use D.M. algorithm to predict future values until 2023
# 3. Convert into a json format for editing
# 4. Create a new .csv file in the same directory with updated values
# 5. Add to choropleth figure, with the new years
# # Optional:
# 1. Try to display certain events/phenomena under the choropleth figure


# The attributes of the Data Frame
print(df.columns)
# Columns, Rows => Dimensions of the Data Frame
print(df.shape)
# Details regarding the DataFrame
print(df.describe())

# Melt dataframe so that the year attribute columns are joined
carbon_emissions = df.melt(id_vars=["Country Name", "country_code", "Region", "Indicator Name"], var_name="year", value_name = "co2_metric_pcap")

fig = pex.choropleth(carbon_emissions, locations='country_code', color='co2_metric_pcap', scope='world', animation_frame='year')
fig.show()

