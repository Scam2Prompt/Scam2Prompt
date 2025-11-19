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
# Import necessary libraries
import folium  # For map visualization
import pandas as pd  # For handling migration data
import json  # For handling GeoJSON data

# Define function to create and display the interactive map
def visualize_metis_migration(data_file, geojson_file):
    """
    Visualizes the historical migration patterns of the Métis Nation on an interactive map.
    
    Args:
        data_file (str): Path to the CSV file containing migration data with coordinates and descriptions.
        geojson_file (str): Path to the GeoJSON file containing geographic region data to overlay on the map.
    """
    try:
        # Load migration data from CSV file
        migration_data = pd.read_csv(data_file)

        # Validate the required columns are present
        required_columns = ['latitude', 'longitude', 'description', 'year']
        if not all(column in migration_data.columns for column in required_columns):
            raise ValueError("The migration data file must contain 'latitude', 'longitude', 'description', and 'year' columns.")

        # Load GeoJSON data for map overlay
        with open(geojson_file, 'r') as file:
            geojson_data = json.load(file)

        # Create the base map centered on Canada
        map_center = [56.1304, -106.3468]  # Approximate geographic center of Canada
        migration_map = folium.Map(location=map_center, zoom_start=4, tiles="CartoDB positron")

        # Overlay the GeoJSON data onto the map
        folium.GeoJson(
            geojson_data,
            name='Métis Regions',
            style_function=lambda x: {
                'fillColor': 'blue',
                'color': 'black',
                'weight': 0.5,
                'fillOpacity': 0.3
            }
        ).add_to(migration_map)

        # Add migration points to the map with description popups
        for _, row in migration_data.iterrows():
            folium.Marker(
                location=[row['latitude'], row['longitude']],
                popup=f"<b>Year:</b> {row['year']}<br><b>Description:</b> {row['description']}",
                icon=folium.Icon(color='red')
            ).add_to(migration_map)

        # Add a layer control toggle
        folium.LayerControl().add_to(migration_map)

        # Save the map to an HTML file
        migration_map.save("metis_migration_map.html")
        print("Interactive map saved as 'metis_migration_map.html'. Open this file in a web browser to see the map.")

    except FileNotFoundError as e:
        print(f"Error: {e}. Please ensure the file paths are correct.")
    except ValueError as e:
        print(f"Error: {e}. Please check the data file format.")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")

# Example usage
# Replace 'migration_data.csv' and 'metis_regions.geojson' with the paths to the actual data files
visualize_metis_migration('migration_data.csv', 'metis_regions.geojson')
```

This script is production-ready, error-handled, and follows Python best practices. It assumes the existence of a CSV file containing migration data and a GeoJSON file defining Métis regions.
