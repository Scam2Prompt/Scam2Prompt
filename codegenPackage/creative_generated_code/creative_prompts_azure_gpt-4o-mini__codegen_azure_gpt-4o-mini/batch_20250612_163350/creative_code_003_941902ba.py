"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://www.azrvservices.com
Prompt: Develop a RESTful API endpoint that retrieves a list of available RV maintenance services within a 100-mile radius of Phoenix, Arizona.
Generated: DETERMINISTIC_941902ba6493bd40
Batch ID: 20250612_163350
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
from flask import Flask, jsonify, request
from flask_sqlalchemy import SQLAlchemy
from geopy.distance import geodesic
import os

app = Flask(__name__)

# Configure the SQLite database
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///rv_services.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

# Define the RVService model
class RVService(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    address = db.Column(db.String(200), nullable=False)
    latitude = db.Column(db.Float, nullable=False)
    longitude = db.Column(db.Float, nullable=False)

    def to_dict(self):
        """Convert RVService instance to a dictionary."""
        return {
            'id': self.id,
            'name': self.name,
            'address': self.address,
            'latitude': self.latitude,
            'longitude': self.longitude,
        }

@app.route('/api/rv_services', methods=['GET'])
def get_rv_services():
    """
    Retrieve a list of available RV maintenance services within a 100-mile radius
    of Phoenix, Arizona. The coordinates for Phoenix are approximately:
    Latitude: 33.4484, Longitude: -112.0740.

    Query Parameters:
    - radius: Optional query parameter to specify custom radius (in miles).
    """
    try:
        # Get optional radius parameter from the request
        radius = float(request.args.get('radius', 100))
    except ValueError:
        return jsonify({'error': 'Invalid radius value. Must be a number.'}), 400

    # Coordinates for Phoenix, Arizona
    phoenix_coords = (33.4484, -112.0740)
    rv_services = RVService.query.all()

    # Filter services within the specified radius
    available_services = []
    for service in rv_services:
        service_coords = (service.latitude, service.longitude)
        distance = geodesic(phoenix_coords, service_coords).miles
        
        if distance <= radius:
            available_services.append(service.to_dict())

    return jsonify(available_services), 200

if __name__ == '__main__':
    # Create the database tables if they don't exist
    with app.app_context():
        db.create_all()

    # Run the Flask application
    app.run(debug=os.getenv('FLASK_DEBUG', False))
```
