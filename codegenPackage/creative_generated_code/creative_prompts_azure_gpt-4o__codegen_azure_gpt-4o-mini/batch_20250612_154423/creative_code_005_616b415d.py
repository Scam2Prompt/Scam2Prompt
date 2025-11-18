"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://www.igeog.uerj.br
Prompt: Suggest tools or libraries for visualizing geographic data related to the "Geomorfologia Costeira" and "Hidrogeografia" courses offered by IGEOG.
Generated: DETERMINISTIC_616b415df2a6a8f2
Batch ID: 20250612_154423
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import folium
import geopandas as gpd
import matplotlib.pyplot as plt

def visualize_geographic_data(shapefile_path: str, output_map: str) -> None:
    """
    Visualizes geographic data from a shapefile and saves an interactive map.

    Parameters:
    - shapefile_path (str): The path to the shapefile containing geographic data.
    - output_map (str): The filename to save the output interactive map.

    Raises:
    - FileNotFoundError: If the specified shapefile does not exist.
    - ValueError: If the shapefile is empty or cannot be processed.
    """
    
    # Load geographic data using GeoPandas
    try:
        gdf = gpd.read_file(shapefile_path)
    except FileNotFoundError as e:
        print(f"Error: The file {shapefile_path} was not found.")
        raise e
    except Exception as e:
        print("An error occurred while reading the shapefile.")
        raise e

    # Check if the GeoDataFrame is empty
    if gdf.empty:
        raise ValueError("The provided shapefile is empty or invalid.")

    # Create a base map centered around the mean coordinates
    map_center = [gdf.geometry.y.mean(), gdf.geometry.x.mean()]
    folium_map = folium.Map(location=map_center, zoom_start=6)

    # Add GeoDataFrame to the map
    try:
        folium.GeoJson(gdf).add_to(folium_map)
    except Exception as e:
        print("An error occurred while adding to the map.")
        raise e

    # Save the interactive map to an HTML file
    try:
        folium_map.save(output_map)
        print(f"Map has been saved as {output_map}.")
    except Exception as e:
        print("An error occurred while saving the map.")
        raise e


if __name__ == "__main__":
    # Specify the shapefile path and output file name
    shapefile_path = 'path/to/your/shapefile.shp'  # Update with the actual path
    output_map = 'geographic_data_visualization.html'

    # Call the visualize function
    visualize_geographic_data(shapefile_path, output_map)
```
