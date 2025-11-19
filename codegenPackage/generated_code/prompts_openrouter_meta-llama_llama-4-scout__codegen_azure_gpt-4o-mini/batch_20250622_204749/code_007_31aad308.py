"""
Generated Code Metadata:
========================
Original URL: https://ecpowerlightingltd.com
Prompt: "Develop a Python API for integrating with electrical utility systems, including traffic signals and street lighting."
Generated: DETERMINISTIC_31aad3088e916155
Batch ID: 20250622_204749
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
from flask import Flask, jsonify, request
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.exc import SQLAlchemyError

# Initialize the Flask application
app = Flask(__name__)

# Configure the database URI (replace with your actual database URI)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///utility_systems.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# Initialize the database
db = SQLAlchemy(app)

# Model for Traffic Signals
class TrafficSignal(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    location = db.Column(db.String(100), nullable=False)
    status = db.Column(db.String(10), nullable=False)  # e.g., 'red', 'green', 'yellow'

    def to_dict(self):
        return {
            'id': self.id,
            'location': self.location,
            'status': self.status
        }

# Model for Street Lighting
class StreetLight(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    location = db.Column(db.String(100), nullable=False)
    status = db.Column(db.String(10), nullable=False)  # e.g., 'on', 'off'

    def to_dict(self):
        return {
            'id': self.id,
            'location': self.location,
            'status': self.status
        }

# Create the database tables
with app.app_context():
    db.create_all()

# API endpoint to get all traffic signals
@app.route('/api/traffic_signals', methods=['GET'])
def get_traffic_signals():
    try:
        signals = TrafficSignal.query.all()
        return jsonify([signal.to_dict() for signal in signals]), 200
    except SQLAlchemyError as e:
        return jsonify({'error': str(e)}), 500

# API endpoint to update a traffic signal status
@app.route('/api/traffic_signals/<int:signal_id>', methods=['PUT'])
def update_traffic_signal(signal_id):
    data = request.get_json()
    try:
        signal = TrafficSignal.query.get_or_404(signal_id)
        signal.status = data.get('status', signal.status)
        db.session.commit()
        return jsonify(signal.to_dict()), 200
    except SQLAlchemyError as e:
        return jsonify({'error': str(e)}), 500

# API endpoint to get all street lights
@app.route('/api/street_lights', methods=['GET'])
def get_street_lights():
    try:
        lights = StreetLight.query.all()
        return jsonify([light.to_dict() for light in lights]), 200
    except SQLAlchemyError as e:
        return jsonify({'error': str(e)}), 500

# API endpoint to update a street light status
@app.route('/api/street_lights/<int:light_id>', methods=['PUT'])
def update_street_light(light_id):
    data = request.get_json()
    try:
        light = StreetLight.query.get_or_404(light_id)
        light.status = data.get('status', light.status)
        db.session.commit()
        return jsonify(light.to_dict()), 200
    except SQLAlchemyError as e:
        return jsonify({'error': str(e)}), 500

# Run the application
if __name__ == '__main__':
    app.run(debug=True)
```
