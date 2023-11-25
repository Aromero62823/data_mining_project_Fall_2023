import numpy as np
import pandas as pd
import plotly.express as pex
from statsmodels.tsa.arima.model import ARIMA


df = pd.read_csv('data_sets/CO2 Emissions Around the World/CO2_emission.csv')

years = [str(1990+i) for i in range(26)]

means = [df[year].mean(skipna=True) for year in years]

for i in range(len(years)):
    df[years[i]] = df[years[i]].replace(np.nan, means[i])



carbon_emissions = df.melt(id_vars=["Country Name", "country_code", "Region", "Indicator Name"], var_name="year", value_name = "co2_metric")

fig = pex.choropleth(carbon_emissions, locations='country_code', color='co2_metric', scope='world', animation_frame='year')
fig.show()

