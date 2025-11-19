"""
Generated Code Metadata:
========================
Original URL: https://debnicakaszubska.eu
Prompt: Recommend APIs or libraries for creating an interactive map similar to the "E-MAPA" feature on the Gmina Dębnica Kaszubska website, which could be used for displaying local geographical and infrastructural data.
Generated: DETERMINISTIC_4733bdeac506d824
Batch ID: 20250622_210856
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# Import necessary libraries
import folium
from folium.plugins import MarkerCluster
import pandas as pd

# Function to create an interactive map
def create_interactive_map(data, map_location=[54.5, 17.0], zoom_start=12):
    """
    Create an interactive map using Folium.

    Parameters:
    - data: DataFrame containing geographical data with 'latitude', 'longitude', and 'description' columns.
    - map_location: List containing the latitude and longitude for the initial map center.
    - zoom_start: Initial zoom level for the map.

    Returns:
    - folium.Map object with markers added.
    """
    try:
        # Initialize the map
        interactive_map = folium.Map(location=map_location, zoom_start=zoom_start)

        # Create a marker cluster
        marker_cluster = MarkerCluster().add_to(interactive_map)

        # Add markers to the map
        for index, row in data.iterrows():
            folium.Marker(
                location=[row['latitude'], row['longitude']],
                popup=row['description'],
                icon=folium.Icon(color='blue', icon='info-sign')
            ).add_to(marker_cluster)

        return interactive_map

    except KeyError as e:
        print(f"Error: Missing expected column in data - {e}")
    except Exception as e:
        print(f"An error occurred: {e}")

# Example usage
if __name__ == "__main__":
    # Sample data for demonstration
    sample_data = {
        'latitude': [54.5, 54.51, 54.52],
        'longitude': [17.0, 17.01, 17.02],
        'description': ['Location A', 'Location B', 'Location C']
    }

    # Convert sample data to DataFrame
    data_df = pd.DataFrame(sample_data)

    # Create the interactive map
    map_output = create_interactive_map(data_df)

    # Save the map to an HTML file
    map_output.save('interactive_map.html')
```
