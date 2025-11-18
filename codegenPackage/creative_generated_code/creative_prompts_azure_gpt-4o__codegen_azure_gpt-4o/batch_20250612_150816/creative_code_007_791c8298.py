"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://visa-pwr.com
Prompt: Generate code to visualize the distribution of visapwr's visa application centres across 90 countries, using geolocation data.
Generated: DETERMINISTIC_791c8298916f0564
Batch ID: 20250612_150816
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
# Import necessary libraries
import pandas as pd
import geopandas as gpd
import matplotlib.pyplot as plt
from shapely.geometry import Point

# Define the geolocation data for visa application centres (example data)
# Replace this with actual geolocation data from 'visapwr'
data = {
    "Country": ["India", "United States", "Germany", "Australia", "Brazil"],
    "Latitude": [20.5937, 37.0902, 51.1657, -25.2744, -14.2350],
    "Longitude": [78.9629, -95.7129, 10.4515, 133.7751, -51.9253]
}

# Create a DataFrame
df = pd.DataFrame(data)

# Convert Latitude and Longitude into Point objects for mapping
df['Coordinates'] = df.apply(lambda row: Point(row['Longitude'], row['Latitude']), axis=1)

# Create a GeoDataFrame
gdf = gpd.GeoDataFrame(df, geometry='Coordinates')

# Load a world map shapefile
world = gpd.datasets.get_path('naturalearth_lowres')
world_map = gpd.read_file(world)

# Create the plot
fig, ax = plt.subplots(figsize=(15, 10))
world_map.plot(ax=ax, color='lightgrey', edgecolor='black')  # Plot the world map
gdf.plot(ax=ax, color='red', markersize=50, label='Visa Application Centres')  # Plot visa centres

# Add title and legend
plt.title('Distribution of Visa Application Centres Across Countries', fontsize=16)
plt.legend(fontsize=12)

# Display the plot
plt.show()
```
