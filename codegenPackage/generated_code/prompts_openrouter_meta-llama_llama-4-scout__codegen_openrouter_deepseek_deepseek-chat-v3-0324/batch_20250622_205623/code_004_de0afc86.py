"""
Generated Code Metadata:
========================
Original URL: https://aanjaneya-aero.com
Prompt: Generate a Python code to visualize the company's infrastructure, including the 125,000 ft² industrial land at Varnama, and its proximity to the Delhi-Mumbai Highway.
Generated: DETERMINISTIC_de0afc86f2c01d83
Batch ID: 20250622_205623
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import folium
import json
import webbrowser
import os
from pathlib import Path

def create_infrastructure_map():
    """Create an interactive map visualizing company infrastructure."""
    try:
        # Coordinates for Varnama industrial land (approximate)
        varnama_coords = [22.3000, 73.2000]
        
        # Coordinates for Delhi-Mumbai Highway (approximate points)
        highway_points = [
            [22.3100, 73.2100],
            [22.3050, 73.2050],
            [22.2950, 73.1950],
            [22.2900, 73.1900]
        ]
        
        # Create base map centered on Varnama
        m = folium.Map(
            location=varnama_coords,
            zoom_start=14,
            tiles='OpenStreetMap'
        )
        
        # Add industrial land polygon
        industrial_land = folium.vector_layers.Polygon(
            locations=[
                [22.3010, 73.2010],
                [22.3010, 73.1990],
                [22.2990, 73.1990],
                [22.2990, 73.2010],
                [22.3010, 73.2010]
            ],
            popup="125,000 ft² Industrial Land<br>Varnama",
            color='blue',
            fill=True,
            fill_color='blue',
            fill_opacity=0.3
        ).add_to(m)
        
        # Add highway line
        highway = folium.PolyLine(
            locations=highway_points,
            color='red',
            weight=5,
            opacity=0.8,
            popup="Delhi-Mumbai Highway"
        ).add_to(m)
        
        # Add markers
        folium.Marker(
            varnama_coords,
            popup="Company Infrastructure<br>Varnama",
            icon=folium.Icon(color='green', icon='industry')
        ).add_to(m)
        
        folium.Marker(
            highway_points[0],
            popup="Delhi-Mumbai Highway<br>Nearest Point",
            icon=folium.Icon(color='red', icon='road')
        ).add_to(m)
        
        # Add distance measurement
        folium.PolyLine(
            [varnama_coords, highway_points[0]],
            color='black',
            dash_array='5,5',
            weight=2,
            popup="Approx. 1.5 km distance"
        ).add_to(m)
        
        # Save map to HTML file
        output_file = Path('company_infrastructure_map.html')
        m.save(output_file)
        
        # Open in default browser
        webbrowser.open(f'file://{output_file.absolute()}')
        
        return True
    
    except Exception as e:
        print(f"Error creating map: {str(e)}")
        return False

if __name__ == "__main__":
    create_infrastructure_map()
```
