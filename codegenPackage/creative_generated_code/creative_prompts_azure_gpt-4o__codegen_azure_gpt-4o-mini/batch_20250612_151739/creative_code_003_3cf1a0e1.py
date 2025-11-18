"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://afco-federation.fr
Prompt: Write code to create an interactive map for locating SPS coordinators, similar to the AFCO Bretagne's "gogocarto" implementation.
Generated: DETERMINISTIC_3cf1a0e130890776
Batch ID: 20250612_151739
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
# Import necessary libraries
import folium
from folium.plugins import MarkerCluster
import pandas as pd

# Define a function to create an interactive map for locating SPS coordinators
def create_sps_coordinators_map(coordinators_data, map_file='sps_coordinators_map.html'):
    """
    Create an interactive map to locate SPS coordinators.

    Parameters:
    - coordinators_data: DataFrame containing coordinator information with 'name', 'latitude', and 'longitude' columns.
    - map_file: Output HTML file name for the interactive map.

    Returns:
    - Saves an HTML file with the interactive map.
    """
    # Validate input DataFrame
    if not isinstance(coordinators_data, pd.DataFrame):
        raise ValueError("coordinators_data must be a pandas DataFrame.")
    required_columns = ['name', 'latitude', 'longitude']
    for column in required_columns:
        if column not in coordinators_data.columns:
            raise ValueError(f"Missing required column: {column}")

    # Initialize a base map
    map_center = [coordinators_data['latitude'].mean(), coordinators_data['longitude'].mean()]
    sps_map = folium.Map(location=map_center, zoom_start=6)

    # Initialize MarkerCluster for better marker management
    marker_cluster = MarkerCluster().add_to(sps_map)

    # Add markers to the map for each coordinator
    for index, row in coordinators_data.iterrows():
        folium.Marker(
            location=[row['latitude'], row['longitude']],
            popup=row['name'],
            icon=folium.Icon(color='blue', icon='info-sign')
        ).add_to(marker_cluster)

    # Save the map to an HTML file
    try:
        sps_map.save(map_file)
        print(f"Map has been successfully created and saved to {map_file}.")
    except Exception as e:
        print(f"An error occurred while saving the map: {e}")

# Example usage
if __name__ == "__main__":
    # Sample data for SPS coordinators
    data = {
        'name': ['Coordinator A', 'Coordinator B', 'Coordinator C'],
        'latitude': [48.8566, 48.8560, 48.8570],
        'longitude': [2.3522, 2.3530, 2.3540]
    }
    sps_coordinators_df = pd.DataFrame(data)

    # Create the interactive map
    create_sps_coordinators_map(sps_coordinators_df)
```
