"""
Generated Code Metadata:
========================
Original URL: https://munasimkullakita.org
Prompt: Create a web application that visualizes the geographic coverage of Fundación Munasim Kullakita's programs, including cities like La Paz, El Alto, Cochabamba, and Santa Cruz.
Generated: DETERMINISTIC_a48e9b6d3d71851f
Batch ID: 20250612_153224
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# Required imports
from flask import Flask, render_template, jsonify
import pandas as pd
import folium
from folium.plugins import MarkerCluster
import os

# Initialize Flask app
app = Flask(__name__)

# Configuration
DATA_FILE = 'program_coverage.csv'
MAP_CENTER = [-16.5000, -68.1500]  # Approximate center of Bolivia
MAP_ZOOM = 6

def load_data():
    """
    Load program coverage data from CSV file.
    Returns a pandas DataFrame with the data.
    """
    try:
        data = pd.read_csv(DATA_FILE)
        # Validate required columns
        required_columns = ['city', 'program', 'latitude', 'longitude']
        if not all(col in data.columns for col in required_columns):
            raise ValueError(f"CSV file must contain columns: {required_columns}")
        return data
    except FileNotFoundError:
        raise FileNotFoundError(f"Data file {DATA_FILE} not found")
    except Exception as e:
        raise Exception(f"Error loading data: {str(e)}")

def generate_map(data):
    """
    Generate a Folium map with program coverage markers.
    Args:
        data: pandas DataFrame containing program coverage data
    Returns:
        Folium map object
    """
    try:
        # Create base map
        m = folium.Map(location=MAP_CENTER, zoom_start=MAP_ZOOM)
        
        # Add marker cluster
        marker_cluster = MarkerCluster().add_to(m)
        
        # Add markers for each program location
        for _, row in data.iterrows():
            popup_text = f"<b>City:</b> {row['city']}<br><b>Program:</b> {row['program']}"
            folium.Marker(
                location=[row['latitude'], row['longitude']],
                popup=popup_text,
                icon=folium.Icon(color='blue', icon='info-sign')
            ).add_to(marker_cluster)
        
        # Add layer control
        folium.LayerControl().add_to(m)
        
        return m
    except Exception as e:
        raise Exception(f"Error generating map: {str(e)}")

@app.route('/')
def index():
    """Render the main page with the program coverage map."""
    try:
        data = load_data()
        m = generate_map(data)
        return m._repr_html_()
    except Exception as e:
        return render_template('error.html', error=str(e)), 500

@app.route('/api/programs')
def get_programs():
    """API endpoint to get program coverage data in JSON format."""
    try:
        data = load_data()
        return jsonify(data.to_dict(orient='records'))
    except Exception as e:
        return jsonify({'error': str(e)}), 500

if __name__ == '__main__':
    # Create templates directory if it doesn't exist
    os.makedirs('templates', exist_ok=True)
    
    # Create basic error template
    with open('templates/error.html', 'w') as f:
        f.write("""
        <!DOCTYPE html>
        <html>
        <head>
            <title>Error</title>
        </head>
        <body>
            <h1>Error</h1>
            <p>{{ error }}</p>
        </body>
        </html>
        """)
    
    # Run the app
    app.run(debug=True)
```

```csv
# program_coverage.csv
city,program,latitude,longitude
La Paz,Education,-16.4958,-68.1333
El Alto,Youth Empowerment,-16.5048,-68.1633
Cochabamba,Health,-17.3895,-66.1568
Santa Cruz,Economic Development,-17.7833,-63.1667
La Paz,Community Development,-16.4958,-68.1333
El Alto,Education,-16.5048,-68.1633
Cochabamba,Youth Empowerment,-17.3895,-66.1568
Santa Cruz,Health,-17.7833,-63.1667
```
