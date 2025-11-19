"""
Generated Code Metadata:
========================
Original URL: https://medioswow.com
Prompt: Create a Python program to display available advertising locations on a map, similar to WOW MEDIA's "ver ubicaciones" feature.
Generated: DETERMINISTIC_8ea23c0b203e2b92
Batch ID: 20250612_154355
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import folium
from folium.plugins import MarkerCluster
import pandas as pd
from flask import Flask, render_template_string

# Sample data for advertising locations (in production, this would come from a database)
SAMPLE_DATA = {
    'Location': ['Times Square', 'Piccadilly Circus', 'Shibuya Crossing', 'Champs-Élysées', 'Las Vegas Strip'],
    'Latitude': [40.7580, 51.510067, 35.658034, 48.869798, 36.114647],
    'Longitude': [-73.9855, -0.133869, 139.701636, 2.307979, -115.172813],
    'Type': ['Digital Billboard', 'Traditional Billboard', 'Digital Billboard', 'Traditional Billboard', 'Digital Billboard'],
    'Price': [5000, 3500, 4500, 3000, 4000]
}

def create_ad_map(data):
    """
    Creates a Folium map with advertising locations marked.
    
    Args:
        data (dict): Dictionary containing location data with keys:
                     'Location', 'Latitude', 'Longitude', 'Type', 'Price'
                     
    Returns:
        folium.Map: Interactive map with markers for each location
    """
    try:
        # Create base map centered on the first location
        ad_map = folium.Map(
            location=[data['Latitude'][0], data['Longitude'][0]],
            zoom_start=2,
            tiles='OpenStreetMap'
        )
        
        # Create marker cluster for better performance with many markers
        marker_cluster = MarkerCluster().add_to(ad_map)
        
        # Add markers for each location
        for idx in range(len(data['Location'])):
            popup_html = f"""
            <b>{data['Location'][idx]}</b><br>
            Type: {data['Type'][idx]}<br>
            Price: ${data['Price'][idx]:,}/month
            """
            
            folium.Marker(
                location=[data['Latitude'][idx], data['Longitude'][idx]],
                popup=folium.Popup(popup_html, max_width=250),
                icon=folium.Icon(
                    color='blue' if 'Digital' in data['Type'][idx] else 'green',
                    icon='bullhorn',
                    prefix='fa'
                )
            ).add_to(marker_cluster)
        
        return ad_map
    
    except Exception as e:
        print(f"Error creating map: {e}")
        return None

def save_map_to_html(ad_map, filename='ad_locations.html'):
    """
    Saves the Folium map to an HTML file.
    
    Args:
        ad_map (folium.Map): Map object to save
        filename (str): Output filename
        
    Returns:
        bool: True if successful, False otherwise
    """
    try:
        if ad_map:
            ad_map.save(filename)
            return True
        return False
    except Exception as e:
        print(f"Error saving map: {e}")
        return False

def create_flask_app():
    """
    Creates a simple Flask web app to display the map.
    
    Returns:
        Flask: Flask application instance
    """
    app = Flask(__name__)
    
    @app.route('/')
    def show_map():
        try:
            # Create the map
            ad_map = create_ad_map(SAMPLE_DATA)
            
            if not ad_map:
                return "Error generating map", 500
                
            # Get the HTML representation of the map
            map_html = ad_map._repr_html_()
            
            # Create a simple template to display the map
            template = """
            <!DOCTYPE html>
            <html>
            <head>
                <title>Advertising Locations</title>
                <meta charset="utf-8" />
                <meta name="viewport" content="width=device-width, initial-scale=1.0">
                {{ map_header|safe }}
            </head>
            <body>
                <h1 style="text-align: center;">Available Advertising Locations</h1>
                {{ map_html|safe }}
                <div style="text-align: center; margin-top: 20px;">
                    <p>Blue markers: Digital Billboards | Green markers: Traditional Billboards</p>
                </div>
            </body>
            </html>
            """
            
            return render_template_string(template, map_header=ad_map.get_root().header.render(), map_html=map_html)
            
        except Exception as e:
            return f"Error: {e}", 500
    
    return app

if __name__ == '__main__':
    # Option 1: Save to HTML file
    ad_map = create_ad_map(SAMPLE_DATA)
    if ad_map:
        save_map_to_html(ad_map)
        print("Map saved to ad_locations.html")
    
    # Option 2: Run as web app
    app = create_flask_app()
    app.run(debug=True)
```
