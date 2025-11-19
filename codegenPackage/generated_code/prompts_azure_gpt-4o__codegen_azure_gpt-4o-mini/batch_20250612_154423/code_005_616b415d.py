"""
Generated Code Metadata:
========================
Original URL: https://www.igeog.uerj.br
Prompt: Suggest tools or libraries for visualizing geographic data related to the "Geomorfologia Costeira" and "Hidrogeografia" courses offered by IGEOG.
Generated: DETERMINISTIC_616b415df2a6a8f2
Batch ID: 20250612_154423
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import folium
import geopandas as gpd
import matplotlib.pyplot as plt

def visualize_geographic_data(shapefile_path, output_map_path):
    """
    Visualizes geographic data from a shapefile and saves an interactive map.

    Parameters:
    shapefile_path (str): The file path to the shapefile containing geographic data.
    output_map_path (str): The file path to save the interactive map.

    Raises:
    FileNotFoundError: If the shapefile does not exist.
    ValueError: If the shapefile is empty or invalid.
    """
    try:
        # Load the geographic data using GeoPandas
        gdf = gpd.read_file(shapefile_path)

        # Check if the GeoDataFrame is empty
        if gdf.empty:
            raise ValueError("The shapefile is empty or invalid.")

        # Create a base map
        m = folium.Map(location=[gdf.geometry.y.mean(), gdf.geometry.x.mean()], zoom_start=8)

        # Add the geographic data to the map
        folium.GeoJson(gdf).add_to(m)

        # Save the interactive map to an HTML file
        m.save(output_map_path)
        print(f"Map has been saved to {output_map_path}")

    except FileNotFoundError:
        print(f"Error: The file {shapefile_path} was not found.")
    except ValueError as ve:
        print(f"Value Error: {ve}")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")

def plot_geographic_data(shapefile_path):
    """
    Plots geographic data from a shapefile using Matplotlib.

    Parameters:
    shapefile_path (str): The file path to the shapefile containing geographic data.

    Raises:
    FileNotFoundError: If the shapefile does not exist.
    ValueError: If the shapefile is empty or invalid.
    """
    try:
        # Load the geographic data using GeoPandas
        gdf = gpd.read_file(shapefile_path)

        # Check if the GeoDataFrame is empty
        if gdf.empty:
            raise ValueError("The shapefile is empty or invalid.")

        # Plot the geographic data
        gdf.plot()
        plt.title("Geographic Data Visualization")
        plt.xlabel("Longitude")
        plt.ylabel("Latitude")
        plt.show()

    except FileNotFoundError:
        print(f"Error: The file {shapefile_path} was not found.")
    except ValueError as ve:
        print(f"Value Error: {ve}")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")

# Example usage
if __name__ == "__main__":
    shapefile = "path/to/your/shapefile.shp"  # Replace with your shapefile path
    output_map = "output_map.html"  # Output path for the interactive map

    visualize_geographic_data(shapefile, output_map)
    plot_geographic_data(shapefile)
```
