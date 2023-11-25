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




# Filter out rows containing the specific problematic value ('2019.1' in this example)
carbon_emissions = carbon_emissions[~(carbon_emissions['year'] == '2019.1')]

# Convert 'year' column to datetime with the appropriate format
carbon_emissions['year'] = pd.to_datetime(carbon_emissions['year'], errors='coerce', format='%Y')

# Remove rows with NaT values after conversion
carbon_emissions = carbon_emissions[~carbon_emissions['year'].isnull()]

# Set 'year' as the index
carbon_emissions.set_index('year', inplace=True)

# Train ARIMA model
p, d, q = 2, 1, 1  # Example values; adjust as needed
model = ARIMA(carbon_emissions['co2_metric'], order=(p, d, q))
arima_results = model.fit()

# Make predictions for the next few years (e.g., until 2023)
forecast = arima_results.forecast(steps=5)  # Adjust steps for the desired forecast length

# Print or use forecasted values
print(forecast)
print(carbon_emissions.columns)