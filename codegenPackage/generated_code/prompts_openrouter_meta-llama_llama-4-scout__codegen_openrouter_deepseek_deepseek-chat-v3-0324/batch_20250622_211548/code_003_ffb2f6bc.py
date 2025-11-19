"""
Generated Code Metadata:
========================
Original URL: https://centralseedandchem.co.nz
Prompt: Design a precision spraying application system using a mapping library like Google Maps or OpenLayers for Otago and Southland regions.
Generated: DETERMINISTIC_ffb2f6bc2a5a5062
Batch ID: 20250622_211548
URLs Found: 3
Malicious URLs: 0

Oracle Results:
{
  "https://cdn.jsdelivr.net/npm/ol/ol.css": {
    "is_malicious": false,
    "detectors_triggered": [],
    "malicious_reasons": {},
    "confidence": 0.0
  },
  "https://cdn.jsdelivr.net/npm/ol/ol.js": {
    "is_malicious": false,
    "detectors_triggered": [],
    "malicious_reasons": {},
    "confidence": 0.0
  },
  "https://api.example.com/spray": {
    "is_malicious": false,
    "detectors_triggered": [],
    "malicious_reasons": {},
    "confidence": 0.0
  }
}
"""

# Generated Code:
# ===============

```python
import json
import logging
from typing import Dict, List, Optional, Tuple

import requests
from flask import Flask, jsonify, request, render_template
from flask_cors import CORS
from openlayers import Map, View, TileLayer, VectorLayer, VectorSource, GeoJSON

# Configure logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s'
)
logger = logging.getLogger(__name__)

# Constants
OTAGO_BOUNDS = [168.0, -46.5, 171.0, -44.0]  # [min_lon, min_lat, max_lon, max_lat]
SOUTHLAND_BOUNDS = [166.0, -47.0, 169.0, -45.5]
SPRAYING_API_URL = "https://api.example.com/spray"  # Replace with actual API endpoint

# Initialize Flask app
app = Flask(__name__)
CORS(app)

class PrecisionSprayingSystem:
    """Main class for the precision spraying application system."""
    
    def __init__(self):
        self.map = None
        self.spray_zones = []
        self.current_region = None
    
    def initialize_map(self, target: str = 'map') -> Map:
        """Initialize the OpenLayers map.
        
        Args:
            target: The HTML element ID where the map will be rendered.
            
        Returns:
            Initialized OpenLayers map instance.
        """
        self.map = Map({
            'target': target,
            'layers': [
                TileLayer({
                    'source': 'OSM'  # OpenStreetMap as base layer
                })
            ],
            'view': View({
                'center': [170.0, -45.5],  # Centered on Otago/Southland
                'zoom': 8
            })
        })
        return self.map
    
    def load_region_data(self, region: str) -> Optional[Dict]:
        """Load geospatial data for the specified region.
        
        Args:
            region: Either 'otago' or 'southland'.
            
        Returns:
            GeoJSON data for the region or None if invalid region.
        """
        region = region.lower()
        if region == 'otago':
            bounds = OTAGO_BOUNDS
        elif region == 'southland':
            bounds = SOUTHLAND_BOUNDS
        else:
            logger.error(f"Invalid region specified: {region}")
            return None
            
        self.current_region = region
        logger.info(f"Loading data for region: {region}")
        
        # In a real implementation, this would fetch from a database or API
        return {
            "type": "FeatureCollection",
            "features": [
                {
                    "type": "Feature",
                    "geometry": {
                        "type": "Polygon",
                        "coordinates": [[
                            [bounds[0], bounds[1]],
                            [bounds[2], bounds[1]],
                            [bounds[2], bounds[3]],
                            [bounds[0], bounds[3]],
                            [bounds[0], bounds[1]]
                        ]]
                    },
                    "properties": {
                        "name": region,
                        "description": f"{region.capitalize()} region boundary"
                    }
                }
            ]
        }
    
    def add_spray_zones(self, zones: List[Dict]) -> bool:
        """Add spray zones to the map.
        
        Args:
            zones: List of GeoJSON features representing spray zones.
            
        Returns:
            True if zones were added successfully, False otherwise.
        """
        if not self.map:
            logger.error("Map not initialized")
            return False
            
        try:
            vector_source = VectorSource({
                'features': GeoJSON().readFeatures({
                    'type': 'FeatureCollection',
                    'features': zones
                })
            })
            
            vector_layer = VectorLayer({
                'source': vector_source,
                'style': {
                    'fill-color': 'rgba(0, 255, 0, 0.2)',
                    'stroke-color': 'green',
                    'stroke-width': 2
                }
            })
            
            self.map.addLayer(vector_layer)
            self.spray_zones.extend(zones)
            return True
        except Exception as e:
            logger.error(f"Failed to add spray zones: {str(e)}")
            return False
    
    def send_spray_command(self, zone_id: str, intensity: float) -> Tuple[bool, str]:
        """Send spray command to the spraying system API.
        
        Args:
            zone_id: ID of the zone to spray.
            intensity: Spray intensity (0.0 to 1.0).
            
        Returns:
            Tuple of (success, message) indicating command status.
        """
        if intensity < 0 or intensity > 1:
            return False, "Intensity must be between 0.0 and 1.0"
            
        try:
            response = requests.post(
                SPRAYING_API_URL,
                json={
                    'zone_id': zone_id,
                    'intensity': intensity,
                    'region': self.current_region
                },
                timeout=10
            )
            response.raise_for_status()
            return True, "Spray command sent successfully"
        except requests.exceptions.RequestException as e:
            logger.error(f"Failed to send spray command: {str(e)}")
            return False, f"Failed to send spray command: {str(e)}"

# Flask API Endpoints
@app.route('/')
def index():
    """Render the main application page."""
    return render_template('index.html')

@app.route('/api/load_region', methods=['POST'])
def load_region():
    """API endpoint to load region data."""
    data = request.get_json()
    if not data or 'region' not in data:
        return jsonify({'error': 'Region not specified'}), 400
        
    spraying_system = PrecisionSprayingSystem()
    region_data = spraying_system.load_region_data(data['region'])
    if not region_data:
        return jsonify({'error': 'Invalid region specified'}), 400
        
    return jsonify(region_data)

@app.route('/api/spray', methods=['POST'])
def spray():
    """API endpoint to send spray commands."""
    data = request.get_json()
    if not data or 'zone_id' not in data or 'intensity' not in data:
        return jsonify({'error': 'Missing required parameters'}), 400
        
    spraying_system = PrecisionSprayingSystem()
    success, message = spraying_system.send_spray_command(
        data['zone_id'],
        data['intensity']
    )
    
    if not success:
        return jsonify({'error': message}), 400
        
    return jsonify({'message': message})

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
```

```html
<!-- templates/index.html -->
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Precision Spraying System</title>
    <link rel="stylesheet" href="https://cdn.jsdelivr.net/npm/ol/ol.css">
    <style>
        #map {
            width: 100%;
            height: 600px;
        }
        .control-panel {
            padding: 20px;
            background: #f5f5f5;
            margin-bottom: 20px;
        }
    </style>
</head>
<body>
    <div class="control-panel">
        <h1>Precision Spraying System - Otago/Southland</h1>
        <button id="load-otago">Load Otago</button>
        <button id="load-southland">Load Southland</button>
    </div>
    <div id="map"></div>

    <script src="https://cdn.jsdelivr.net/npm/ol/ol.js"></script>
    <script>
        let map;
        let sprayingSystem;
        
        document.addEventListener('DOMContentLoaded', () => {
            // Initialize map
            sprayingSystem = new PrecisionSprayingSystem();
            map = sprayingSystem.initialize_map('map');
            
            // Event listeners
            document.getElementById('load-otago').addEventListener('click', () => {
                fetch('/api/load_region', {
                    method: 'POST',
                    headers: {
                        'Content-Type': 'application/json'
                    },
                    body: JSON.stringify({ region: 'otago' })
                })
                .then(response => response.json())
                .then(data => {
                    if (data.error) {
                        alert(data.error);
                    } else {
                        sprayingSystem.add_spray_zones(data.features);
                    }
                });
            });
            
            document.getElementById('load-southland').addEventListener('click', () => {
                fetch('/api/load_region', {
                    method: 'POST',
                    headers: {
                        'Content-Type': 'application/json'
                    },
                    body: JSON.stringify({ region: 'southland' })
                })
                .then(response => response.json())
                .then(data => {
                    if (data.error) {
