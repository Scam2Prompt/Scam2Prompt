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
# Interactive Map Implementation using Folium and GeoPandas

import folium
import geopandas as gpd
import pandas as pd
from branca.element import Figure

class InteractiveMap:
    """
    Creates an interactive map with layers for geographical and infrastructural data.
    Similar to E-MAPA feature on Gmina Dębnica Kaszubska website.
    """
    
    def __init__(self, location=[54.378, 17.160], zoom_start=12):
        """
        Initialize the map with default location and zoom level.
        
        Args:
            location (list): Latitude and longitude for map center [lat, lon]
            zoom_start (int): Initial zoom level (1-18)
        """
        self.map = folium.Map(location=location, zoom_start=zoom_start)
        self.layers = {}
        self.figure = Figure(width='100%', height='100%')
        self.figure.add_child(self.map)
        
    def add_geojson_layer(self, name, geojson_data, style=None, show=True):
        """
        Add a GeoJSON layer to the map.
        
        Args:
            name (str): Layer name to display in controls
            geojson_data (str/dict): GeoJSON data or file path
            style (dict): Styling options for the layer
            show (bool): Whether to show layer by default
        """
        if isinstance(geojson_data, str):
            try:
                data = gpd.read_file(geojson_data)
                geojson_data = data.__geo_interface__
            except Exception as e:
                raise ValueError(f"Could not load GeoJSON file: {e}")
                
        default_style = {
            'fillColor': '#3388ff',
            'color': '#3388ff',
            'weight': 2,
            'fillOpacity': 0.5
        }
        style = style or default_style
        
        layer = folium.GeoJson(
            geojson_data,
            name=name,
            style_function=lambda x: style,
            tooltip=folium.GeoJsonTooltip(fields=list(geojson_data['features'][0]['properties'].keys()))
        )
        
        layer.add_to(self.map)
        self.layers[name] = layer
        
        if not show:
            folium.FeatureGroup(name=name, show=show).add_to(self.map)
            
    def add_marker_layer(self, name, data, show=True):
        """
        Add a marker layer to the map.
        
        Args:
            name (str): Layer name
            data (pd.DataFrame): DataFrame with columns ['lat', 'lon', 'popup']
            show (bool): Whether to show layer by default
        """
        if not isinstance(data, pd.DataFrame):
            raise ValueError("Data must be a pandas DataFrame")
            
        required_cols = {'lat', 'lon', 'popup'}
        if not required_cols.issubset(data.columns):
            raise ValueError(f"Data must contain columns: {required_cols}")
            
        fg = folium.FeatureGroup(name=name, show=show)
        
        for _, row in data.iterrows():
            folium.Marker(
                location=[row['lat'], row['lon']],
                popup=row['popup'],
                icon=folium.Icon()
            ).add_to(fg)
            
        fg.add_to(self.map)
        self.layers[name] = fg
        
    def add_controls(self):
        """Add layer control to the map."""
        folium.LayerControl().add_to(self.map)
        
    def save(self, filename='interactive_map.html'):
        """
        Save map to HTML file.
        
        Args:
            filename (str): Output file path
        """
        self.map.save(filename)
        return filename
        
    def _repr_html_(self):
        """Display the map in Jupyter notebooks."""
        return self.figure._repr_html_()


# Example usage
if __name__ == "__main__":
    # Create map centered on Dębnica Kaszubska
    imap = InteractiveMap(location=[54.378, 17.160], zoom_start=13)
    
    # Example GeoJSON data (would normally load from file)
    example_geojson = {
        "type": "FeatureCollection",
        "features": [
            {
                "type": "Feature",
                "properties": {"name": "Park", "type": "green"},
                "geometry": {
                    "type": "Polygon",
                    "coordinates": [[[17.15, 54.37], [17.16, 54.37], [17.16, 54.38], [17.15, 54.38]]]
                }
            }
        ]
    }
    
    # Add GeoJSON layer
    imap.add_geojson_layer("Green Areas", example_geojson)
    
    # Add marker layer
    markers = pd.DataFrame({
        'lat': [54.378, 54.379],
        'lon': [17.160, 17.161],
        'popup': ["Town Hall", "School"]
    })
    imap.add_marker_layer("Important Locations", markers)
    
    # Add controls and save
    imap.add_controls()
    imap.save("debnica_map.html")
```
