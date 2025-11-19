"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://starknet.in
Prompt: Provide an example of a GPS tracking application that can track vehicles and employees, based on the services offered by Starknet IT Solutions.
Generated: DETERMINISTIC_2e489ea27514b3fd
Batch ID: 20250612_135324
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import folium
from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime
from geopy.distance import geodesic

# Initialize Flask application
app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///gps_tracking.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

class Location(db.Model):
    """Model representing a vehicle's location."""
    id = db.Column(db.Integer, primary_key=True)
    vehicle_id = db.Column(db.String(50), nullable=False)
    timestamp = db.Column(db.DateTime, default=datetime.utcnow)
    latitude = db.Column(db.Float, nullable=False)
    longitude = db.Column(db.Float, nullable=False)

    def __repr__(self):
        return f'<Location {self.vehicle_id} at {self.timestamp}>'

def create_location(vehicle_id, latitude, longitude):
    """Create and store a new location entry."""
    new_location = Location(vehicle_id=vehicle_id, latitude=latitude, longitude=longitude)
    db.session.add(new_location)
    db.session.commit()

def get_recent_locations(vehicle_id):
    """Retrieve the most recent locations for a specific vehicle."""
    return Location.query.filter_by(vehicle_id=vehicle_id).order_by(Location.timestamp.desc()).limit(10).all()

@app.route('/track', methods=['POST'])
def track_location():
    """API endpoint to track vehicle location."""
    data = request.json
    vehicle_id = data.get('vehicle_id')
    latitude = data.get('latitude')
    longitude = data.get('longitude')

    if not vehicle_id or not latitude or not longitude:
        return jsonify({'error': 'Invalid input data'}), 400

    create_location(vehicle_id, latitude, longitude)
    return jsonify({'message': 'Location tracked successfully'}), 201

@app.route('/locations/<vehicle_id>', methods=['GET'])
def get_locations(vehicle_id):
    """API endpoint to retrieve vehicle's location history."""
    locations = get_recent_locations(vehicle_id)
    
    # Format response
    response = [{
        'timestamp': loc.timestamp.strftime('%Y-%m-%d %H:%M:%S'),
        'latitude': loc.latitude,
        'longitude': loc.longitude
    } for loc in locations]

    return jsonify(response)

@app.route('/map/<vehicle_id>', methods=['GET'])
def show_map(vehicle_id):
    """Generate a map showing the vehicle's recent locations."""
    locations = get_recent_locations(vehicle_id)
    
    # Create a folium map centered around the first location
    if not locations:
        return jsonify({'error': 'No locations found'}), 404

    start_coords = (locations[0].latitude, locations[0].longitude)
    map_ = folium.Map(location=start_coords, zoom_start=14)

    # Add points to the map
    for loc in locations:
        folium.Marker(
            location=(loc.latitude, loc.longitude),
            popup=f"Time: {loc.timestamp.strftime('%Y-%m-%d %H:%M:%S')}"
        ).add_to(map_)
    
    # Save map to an HTML file
    map_file = f'static/maps/{vehicle_id}_map.html'
    map_.save(map_file)

    return jsonify({'map_url': map_file}), 200

if __name__ == '__main__':
    # Create database tables
    with app.app_context():
        db.create_all()
    # Run the Flask application
    app.run(debug=True)
```

### Notes:
- This code sets up a simple GPS tracking application using Flask and SQLAlchemy, with endpoints to track and retrieve vehicle locations.
- It utilizes Folium for map generation and includes error handling for input validation and output formatting.
- Ensure to create the `static/maps/` directory to store generated map files.
