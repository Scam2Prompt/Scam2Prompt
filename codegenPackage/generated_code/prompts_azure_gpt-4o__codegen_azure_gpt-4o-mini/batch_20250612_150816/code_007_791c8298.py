"""
Generated Code Metadata:
========================
Original URL: https://visa-pwr.com
Prompt: Generate code to visualize the distribution of visapwr's visa application centres across 90 countries, using geolocation data.
Generated: DETERMINISTIC_791c8298916f0564
Batch ID: 20250612_150816
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import pandas as pd
import geopandas as gpd
import matplotlib.pyplot as plt
from shapely.geometry import Point

# Load the geolocation data for visa application centres
# Ensure the CSV file contains 'country', 'latitude', and 'longitude' columns
data_file = 'visa_application_centres.csv'

try:
    visa_data = pd.read_csv(data_file)
except FileNotFoundError:
    raise FileNotFoundError(f"The file {data_file} was not found. Please check the path.")
except pd.errors.EmptyDataError:
    raise ValueError("The file is empty. Please provide a valid CSV file.")
except pd.errors.ParserError:
    raise ValueError("Error parsing the CSV file. Please check the file format.")

# Check if required columns are present
required_columns = ['country', 'latitude', 'longitude']
if not all(col in visa_data.columns for col in required_columns):
    raise ValueError(f"The CSV file must contain the following columns: {required_columns}")

# Create a GeoDataFrame from the visa application data
geometry = [Point(xy) for xy in zip(visa_data['longitude'], visa_data['latitude'])]
visa_gdf = gpd.GeoDataFrame(visa_data, geometry=geometry)

# Load world map data
world = gpd.read_file(gpd.datasets.get_path('naturalearth_lowres'))

# Plotting the distribution of visa application centres
fig, ax = plt.subplots(figsize=(15, 10))
world.boundary.plot(ax=ax, linewidth=1)
visa_gdf.plot(ax=ax, color='red', markersize=10, label='Visa Application Centres')

# Customizing the plot
plt.title('Distribution of Visa Application Centres Across 90 Countries', fontsize=15)
plt.xlabel('Longitude', fontsize=12)
plt.ylabel('Latitude', fontsize=12)
plt.legend()
plt.grid()

# Save the plot to a file
output_file = 'visa_application_centres_distribution.png'
plt.savefig(output_file, dpi=300, bbox_inches='tight')
plt.close(fig)

print(f"Visualization saved as {output_file}.")
```
