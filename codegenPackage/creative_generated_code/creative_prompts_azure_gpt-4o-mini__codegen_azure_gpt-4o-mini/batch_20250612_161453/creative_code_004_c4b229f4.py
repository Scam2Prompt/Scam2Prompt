"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://iammetis.org
Prompt: Illustrate how to use a library to visualize the historical migration patterns of the Métis Nation across Canada in an interactive map format.
Generated: DETERMINISTIC_c4b229f4ecb26ff9
Batch ID: 20250612_161453
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import folium
import pandas as pd
import geopandas as gpd
from folium.plugins import HeatMap

# Load the historical migration data
# Ensure the CSV file has columns: ['year', 'latitude', 'longitude', 'population']
try:
    migration_data = pd.read_csv('metis_migration_data.csv')
except FileNotFoundError:
    raise FileNotFoundError("The specified CSV file was not found.")
except pd.errors.EmptyDataError:
    raise ValueError("The CSV file is empty.")
except Exception as e:
    raise Exception(f"An error occurred while reading the CSV file: {e}")

# Validate the data
required_columns = ['year', 'latitude', 'longitude', 'population']
for column in required_columns:
    if column not in migration_data.columns:
        raise ValueError(f"Missing required column: {column}")

# Create a folium map centered around Canada
map_center = [56.1304, -106.3468]  # Latitude and longitude of Canada
migration_map = folium.Map(location=map_center, zoom_start=4)

# Prepare data for the HeatMap
heat_data = migration_data[['latitude', 'longitude', 'population']].values.tolist()

# Create a heatmap layer
heat_map_layer = HeatMap(data=heat_data, radius=15, max_zoom=13)
migration_map.add_child(heat_map_layer)

# Add a title to the map
folium.Marker(location=map_center, 
              icon=folium.DivIcon(html='<div style="font-size: 24pt">Métis Nation Migration Patterns</div>')).add_to(migration_map)

# Save the map to an HTML file
try:
    migration_map.save('metis_migration_map.html')
except Exception as e:
    raise Exception(f"An error occurred while saving the map: {e}")

print("Migration map has been created and saved as 'metis_migration_map.html'.")
```

**Note:** Ensure that the `metis_migration_data.csv` file is in the correct format and accessible when running this code. Install the required libraries if you haven't done so:

```bash
pip install folium pandas geopandas
```
