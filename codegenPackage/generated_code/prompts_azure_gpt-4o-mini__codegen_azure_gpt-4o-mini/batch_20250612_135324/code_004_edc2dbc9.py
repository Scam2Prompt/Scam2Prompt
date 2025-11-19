"""
Generated Code Metadata:
========================
Original URL: https://starkware.in
Prompt: Illustrate how to implement IoT solutions in a business context, drawing from Starkware's exploration of digital engineering and IoT technologies.
Generated: DETERMINISTIC_edc2dbc9837e5f47
Batch ID: 20250612_135324
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import json
import logging
from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime

# Initialize the Flask application
app = Flask(__name__)

# Configure the database
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///iot_data.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

# Set up logging
logging.basicConfig(level=logging.INFO)

# Define a model for IoT device data
class IoTDeviceData(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    device_id = db.Column(db.String(50), nullable=False)
    temperature = db.Column(db.Float, nullable=False)
    humidity = db.Column(db.Float, nullable=False)
    timestamp = db.Column(db.DateTime, default=datetime.utcnow)

    def to_dict(self):
        return {
            'id': self.id,
            'device_id': self.device_id,
            'temperature': self.temperature,
            'humidity': self.humidity,
            'timestamp': self.timestamp.isoformat()
        }

# Create the database tables
with app.app_context():
    db.create_all()

@app.route('/data', methods=['POST'])
def receive_data():
    """
    Endpoint to receive IoT device data.
    Expects JSON payload with device_id, temperature, and humidity.
    """
    try:
        data = request.get_json()
        if not data or 'device_id' not in data or 'temperature' not in data or 'humidity' not in data:
            return jsonify({'error': 'Invalid input'}), 400

        # Create a new IoTDeviceData instance
        new_data = IoTDeviceData(
            device_id=data['device_id'],
            temperature=data['temperature'],
            humidity=data['humidity']
        )

        # Add to the session and commit to the database
        db.session.add(new_data)
        db.session.commit()

        logging.info(f"Data received from device {data['device_id']}: {data['temperature']}°C, {data['humidity']}%")
        return jsonify(new_data.to_dict()), 201

    except Exception as e:
        logging.error(f"Error receiving data: {e}")
        return jsonify({'error': 'Internal server error'}), 500

@app.route('/data', methods=['GET'])
def get_data():
    """
    Endpoint to retrieve all IoT device data.
    Returns a JSON array of all recorded data.
    """
    try:
        all_data = IoTDeviceData.query.all()
        return jsonify([data.to_dict() for data in all_data]), 200

    except Exception as e:
        logging.error(f"Error retrieving data: {e}")
        return jsonify({'error': 'Internal server error'}), 500

if __name__ == '__main__':
    # Run the application
    app.run(debug=False)
```
