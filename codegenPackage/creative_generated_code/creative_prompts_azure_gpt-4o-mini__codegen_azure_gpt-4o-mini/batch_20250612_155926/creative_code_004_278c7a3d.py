"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://ecoswap.us
Prompt: Suggest a RESTful API design for EcoSwap to enable users to check the availability of specific Apple devices in real-time.
Generated: DETERMINISTIC_278c7a3dac1e4182
Batch ID: 20250612_155926
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
from sqlalchemy.exc import SQLAlchemyError
from marshmallow import Schema, fields, ValidationError

# Initialize Flask application
app = Flask(__name__)

# Configuration for the SQLite database
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///ecoswap.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# Initialize the database
db = SQLAlchemy(app)

# Device model for the database
class Device(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50), nullable=False)
    availability = db.Column(db.Boolean, default=True)

# Schema for input validation
class DeviceSchema(Schema):
    name = fields.Str(required=True)

# Create the database if it doesn't exist
@app.before_first_request
def create_tables():
    db.create_all()

# Endpoint to check the availability of a specific Apple device
@app.route('/api/devices/availability', methods=['GET'])
def check_device_availability():
    # Validate query parameters
    schema = DeviceSchema()
    try:
        # Load and validate device name from query parameters
        args = schema.load(request.args)
    except ValidationError as err:
        return jsonify(err.messages), 400

    device_name = args['name']
    
    try:
        # Query the database for the device
        device = Device.query.filter_by(name=device_name).first()
        
        if device is None:
            return jsonify({"error": "Device not found"}), 404

        # Return the availability status of the device
        return jsonify({
            "device": device.name,
            "available": device.availability
        }), 200
        
    except SQLAlchemyError as e:
        # Handle database errors
        return jsonify({"error": "Database error occurred", "details": str(e)}), 500

# Run the application
if __name__ == '__main__':
    app.run(debug=False)
```
