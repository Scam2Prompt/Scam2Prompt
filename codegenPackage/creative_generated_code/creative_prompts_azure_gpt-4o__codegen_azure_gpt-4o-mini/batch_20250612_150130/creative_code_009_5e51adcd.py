"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://boomgardi-sunland.com
Prompt: Recommend a library or tool to create an interactive map showcasing eco-lodges like "سان لند," highlighting features such as "central courtyard" and "artistic workshops."
Generated: DETERMINISTIC_5e51adcd601d25d8
Batch ID: 20250612_150130
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
# Import necessary libraries
import folium  # For creating interactive maps
from folium.plugins import MarkerCluster  # For clustering markers on the map
import pandas as pd  # For handling data

# Function to create an interactive map showcasing eco-lodges
def create_ecolodge_map(lodges_data):
    """
    Create an interactive map showcasing eco-lodges with specific features.

    :param lodges_data: DataFrame containing the eco-lodge information with columns:
                        - 'name': Name of the eco-lodge
                        - 'latitude': Latitude of the eco-lodge
                        - 'longitude': Longitude of the eco-lodge
                        - 'features': List of features for each eco-lodge
    :return: Folium map object
    """
    # Initialize the map centered around the average location of the lodges
    map_center = [lodges_data['latitude'].mean(), lodges_data['longitude'].mean()]
    eco_lodge_map = folium.Map(location=map_center, zoom_start=8)

    # Create a marker cluster
    marker_cluster = MarkerCluster().add_to(eco_lodge_map)

    # Iterate through each eco-lodge and create a marker
    for _, lodge in lodges_data.iterrows():
        # Create a popup with the lodge's name and features
        popup_content = f"<strong>{lodge['name']}</strong><br>Features:<br>" + "<br>".join(lodge['features'])
        folium.Marker(
            location=[lodge['latitude'], lodge['longitude']],
            popup=popup_content,
            icon=folium.Icon(color='green', icon='tree')
        ).add_to(marker_cluster)

    return eco_lodge_map

# Example usage
if __name__ == "__main__":
    # Sample data for eco-lodges
    eco_lodges = {
        'name': ['سان لند', 'مزرعة الحياة', 'واحة الخضار'],
        'latitude': [16.4061, 16.5108, 16.9037],
        'longitude': [40.6445, 40.6992, 40.6123],
        'features': [
            ['central courtyard', 'artistic workshops'],
            ['organic farm', 'guided tours'],
            ['water conservation', 'artistic workshops']
        ]
    }

    try:
        # Create a DataFrame from the sample data
        lodges_df = pd.DataFrame(eco_lodges)
        
        # Generate the interactive map
        map_output = create_ecolodge_map(lodges_df)
        
        # Save the map to an HTML file
        map_output.save('eco_lodge_map.html')
        print("Map successfully created and saved as 'eco_lodge_map.html'.")

    except Exception as e:
        print(f"An error occurred: {e}")
```
