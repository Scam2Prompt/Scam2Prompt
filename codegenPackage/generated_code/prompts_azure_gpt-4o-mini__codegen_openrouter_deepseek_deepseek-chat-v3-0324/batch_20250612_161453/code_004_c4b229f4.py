"""
Generated Code Metadata:
========================
Original URL: https://iammetis.org
Prompt: Illustrate how to use a library to visualize the historical migration patterns of the Métis Nation across Canada in an interactive map format.
Generated: DETERMINISTIC_c4b229f4ecb26ff9
Batch ID: 20250612_161453
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import folium
import pandas as pd
from folium.plugins import TimestampedGeoJson
import json

def load_migration_data(filepath):
    """
    Load migration data from a CSV file.
    
    Args:
        filepath (str): Path to the CSV file containing migration data.
        
    Returns:
        pandas.DataFrame: DataFrame containing the migration data.
    """
    try:
        data = pd.read_csv(filepath)
        required_columns = ['latitude', 'longitude', 'year', 'population', 'location']
        if not all(col in data.columns for col in required_columns):
            raise ValueError("CSV file is missing required columns")
        return data
    except Exception as e:
        print(f"Error loading migration data: {e}")
        raise

def create_migration_map(data, output_file='metis_migration_map.html'):
    """
    Create an interactive TimestampedGeoJson map showing Métis migration patterns.
    
    Args:
        data (pandas.DataFrame): Migration data with coordinates and timestamps.
        output_file (str): Path to save the HTML map file.
    """
    try:
        # Convert DataFrame to GeoJSON format
        features = []
        for _, row in data.iterrows():
            feature = {
                'type': 'Feature',
                'geometry': {
                    'type': 'Point',
                    'coordinates': [row['longitude'], row['latitude']]
                },
                'properties': {
                    'time': str(row['year']),
                    'popup': f"<b>{row['location']}</b><br>Year: {row['year']}<br>Population: {row['population']}",
                    'icon': 'circle',
                    'iconstyle': {
                        'fillColor': '#FF5733',
                        'fillOpacity': 0.7,
                        'stroke': 'false',
                        'radius': row['population'] / 1000  # Scale marker size by population
                    }
                }
            }
            features.append(feature)
        
        geojson = {
            'type': 'FeatureCollection',
            'features': features
        }
        
        # Create base map centered on Canada
        m = folium.Map(location=[56.1304, -106.3468], zoom_start=4)
        
        # Add TimestampedGeoJson layer
        TimestampedGeoJson(
            geojson,
            period='P1Y',  # 1 year intervals
            add_last_point=True,
            auto_play=True,
            loop=True,
            max_speed=1,
            loop_button=True,
            date_options='YYYY',
            time_slider_drag_update=True
        ).add_to(m)
        
        # Add title
        title_html = '''
            <h3 align="center" style="font-size:16px"><b>Historical Migration Patterns of the Métis Nation</b></h3>
        '''
        m.get_root().html.add_child(folium.Element(title_html))
        
        # Save the map
        m.save(output_file)
        print(f"Map successfully saved to {output_file}")
        
    except Exception as e:
        print(f"Error creating migration map: {e}")
        raise

if __name__ == "__main__":
    # Example usage
    try:
        # Load sample data (replace with actual data file)
        data = load_migration_data('metis_migration_data.csv')
        
        # Create and save interactive map
        create_migration_map(data)
        
    except Exception as e:
        print(f"An error occurred: {e}")
```
