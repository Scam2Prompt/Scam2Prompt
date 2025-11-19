"""
Generated Code Metadata:
========================
Original URL: https://boomgardi-sunland.com
Prompt: Recommend a library or tool to create an interactive map showcasing eco-lodges like "سان لند," highlighting features such as "central courtyard" and "artistic workshops."
Generated: DETERMINISTIC_5e51adcd601d25d8
Batch ID: 20250612_150130
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

def create_eco_lodge_map(lodges_data, output_file='eco_lodges_map.html'):
    """
    Creates an interactive map showcasing eco-lodges with their features.
    
    Args:
        lodges_data (list of dicts): List containing lodge information with keys:
            - 'name': Name of the lodge
            - 'latitude': Latitude coordinate
            - 'longitude': Longitude coordinate
            - 'features': List of features (e.g., ['central courtyard', 'artistic workshops'])
        output_file (str): Path to save the HTML map file
    
    Returns:
        folium.Map: The generated map object
    """
    try:
        # Create base map centered around the first lodge
        if not lodges_data:
            raise ValueError("No lodge data provided")
            
        base_location = [lodges_data[0]['latitude'], lodges_data[0]['longitude']]
        eco_map = folium.Map(location=base_location, zoom_start=12)
        
        # Add marker cluster for better visualization of multiple lodges
        marker_cluster = MarkerCluster().add_to(eco_map)
        
        # Add each lodge to the map
        for lodge in lodges_data:
            # Create popup content with lodge name and features
            features_html = "<br>• " + "<br>• ".join(lodge['features'])
            popup_content = f"""
                <strong>{lodge['name']}</strong><br>
                <em>Features:</em>{features_html}
            """
            
            # Add marker to cluster
            folium.Marker(
                location=[lodge['latitude'], lodge['longitude']],
                popup=folium.Popup(popup_content, max_width=300),
                icon=folium.Icon(color='green', icon='tree-conifer', prefix='glyphicon')
            ).add_to(marker_cluster)
        
        # Save the map to HTML file
        eco_map.save(output_file)
        print(f"Map successfully saved to {output_file}")
        
        return eco_map
    
    except Exception as e:
        print(f"Error creating map: {str(e)}")
        raise

# Example usage
if __name__ == "__main__":
    # Sample data - replace with your actual lodge data
    lodges = [
        {
            'name': 'سان لند',
            'latitude': 35.6895,
            'longitude': 51.3890,
            'features': ['central courtyard', 'artistic workshops', 'sustainable design']
        },
        {
            'name': 'Eco Haven',
            'latitude': 35.7000,
            'longitude': 51.4000,
            'features': ['organic garden', 'solar panels']
        }
    ]
    
    # Create and save the map
    create_eco_lodge_map(lodges)
```
