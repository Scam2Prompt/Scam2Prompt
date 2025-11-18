"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://www.rararaibar.com
Prompt: Suggest a library for visualizing geographical data and write code to plot the locations mentioned in the "Rara Raibar" articles (e.g., Rara Lake, Mugu).
Generated: DETERMINISTIC_d72af7de3a14317a
Batch ID: 20250612_153224
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
# Import necessary libraries
import geopandas as gpd
import matplotlib.pyplot as plt
from shapely.geometry import Point

# Ensure you have the required libraries installed:
# pip install geopandas matplotlib shapely

def plot_locations(locations):
    """
    Function to plot geographical locations on a map using GeoPandas.
    
    Parameters:
    - locations (list of dict): List of dictionaries containing 'name', 'latitude', and 'longitude' keys.
    
    Example:
    locations = [
        {"name": "Rara Lake", "latitude": 29.5275, "longitude": 82.0814},
        {"name": "Mugu", "latitude": 29.4868, "longitude": 82.6161}
    ]
    """
    try:
        # Convert locations into GeoDataFrame
        geometry = [Point(loc["longitude"], loc["latitude"]) for loc in locations]
        gdf = gpd.GeoDataFrame(locations, geometry=geometry)
        
        # Plot the map
        world = gpd.read_file(gpd.datasets.get_path('naturalearth_lowres'))  # Load world map
        ax = world.plot(figsize=(10, 6), alpha=0.3, edgecolor='k')  # Plot base map
        
        # Plot locations on the map
        gdf.plot(ax=ax, color='red', markersize=50, label='Locations')
        
        # Add labels for the locations
        for x, y, label in zip(gdf.geometry.x, gdf.geometry.y, gdf["name"]):
            plt.text(x, y, label, fontsize=9, ha='right')
        
        # Customize and show the plot
        plt.title("Geographical Locations Mentioned in 'Rara Raibar' Articles")
        plt.legend()
        plt.show()
    except Exception as e:
        print(f"An error occurred while plotting locations: {str(e)}")


# Example data: Locations mentioned in "Rara Raibar" articles
locations = [
    {"name": "Rara Lake", "latitude": 29.5275, "longitude": 82.0814},
    {"name": "Mugu", "latitude": 29.4868, "longitude": 82.6161}
]

# Call the function to plot locations
plot_locations(locations)
```
