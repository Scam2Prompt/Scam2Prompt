"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://sharawatch.org
Prompt: Recommend libraries for creating interactive maps to display protected areas and protest locations, as discussed on sharawatch.org.
Generated: DETERMINISTIC_a6162017eebaa52a
Batch ID: 20250612_153224
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import folium  # Import the folium library for interactive maps
import pandas as pd  # Import pandas for data manipulation
from folium.plugins import MarkerCluster  # Import MarkerCluster for grouping markers

# Function to create an interactive map with protected areas and protest locations
def create_interactive_map(protected_areas_data, protest_locations_data, output_file='interactive_map.html'):
    """
    Generates an interactive map displaying protected areas and protest locations.
    
    Parameters:
    protected_areas_data (str): Path to the CSV file containing protected areas data.
    protest_locations_data (str): Path to the CSV file containing protest locations data.
    output_file (str): Output file name for the HTML map. Defaults to 'interactive_map.html'.
    """

    # Load protected areas data
    try:
        protected_areas = pd.read_csv(protected_areas_data)
    except Exception as e:
        print(f"Error loading protected areas data: {e}")
        return

    # Load protest locations data
    try:
        protest_locations = pd.read_csv(protest_locations_data)
    except Exception as e:
        print(f"Error loading protest locations data: {e}")
        return

    # Initialize a map centered around a default location
    m = folium.Map(location=[20, 0], zoom_start=2)
    
    # Add protected areas to the map
    if not protected_areas.empty:
        cluster = MarkerCluster().add_to(m)
        for _, area in protected_areas.iterrows():
            folium.Marker(
                location=[area['latitude'], area['longitude']],
                popup=folium.Popup(area['name'], parse_html=True),
                icon=folium.Icon(color='green', icon='tree')
            ).add_to(cluster)
    
    # Add protest locations to the map
    if not protest_locations.empty:
        cluster = MarkerCluster().add_to(m)
        for _, protest in protest_locations.iterrows():
            folium.Marker(
                location=[protest['latitude'], protest['longitude']],
                popup=folium.Popup(protest['description'], parse_html=True),
                icon=folium.Icon(color='red', icon='exclamation-sign')
            ).add_to(cluster)

    # Save the map to an HTML file
    try:
        m.save(output_file)
        print(f"Map has been saved to {output_file}")
    except Exception as e:
        print(f"Error saving the map: {e}")

# Example usage
# create_interactive_map('protected_areas.csv', 'protest_locations.csv')
```
