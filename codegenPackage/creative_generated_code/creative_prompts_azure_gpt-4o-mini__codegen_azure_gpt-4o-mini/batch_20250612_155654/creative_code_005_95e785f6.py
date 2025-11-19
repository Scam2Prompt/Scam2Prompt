"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://cornucopiasnft.org
Prompt: How can I create a digital asset marketplace for Cornucopias that allows trading of vehicles and land plots?
Generated: DETERMINISTIC_95e785f6865d692f
Batch ID: 20250612_155654
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
# Import necessary libraries
from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy
from marshmallow import Schema, fields, validate
import os

# Initialize Flask application
app = Flask(__name__)

# Configure the SQLite database URI
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///cornucopias_marketplace.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# Initialize the database
db = SQLAlchemy(app)

# Define the Vehicle model
class Vehicle(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    owner = db.Column(db.String(100), nullable=False)
    price = db.Column(db.Float, nullable=False)

# Define the LandPlot model
class LandPlot(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    description = db.Column(db.String(200), nullable=False)
    owner = db.Column(db.String(100), nullable=False)
    price = db.Column(db.Float, nullable=False)

# Define the schema for validation
class VehicleSchema(Schema):
    name = fields.String(required=True, validate=validate.Length(min=1))
    owner = fields.String(required=True, validate=validate.Length(min=1))
    price = fields.Float(required=True, validate=validate.Range(min=0))

class LandPlotSchema(Schema):
    description = fields.String(required=True, validate=validate.Length(min=1))
    owner = fields.String(required=True, validate=validate.Length(min=1))
    price = fields.Float(required=True, validate=validate.Range(min=0))

# Initialize schemas
vehicle_schema = VehicleSchema()
land_plot_schema = LandPlotSchema()

# Create the database tables
@app.before_first_request
def create_tables():
    db.create_all()

# Endpoint to add a new vehicle
@app.route('/vehicles', methods=['POST'])
def add_vehicle():
    json_data = request.get_json()
    try:
        # Validate and deserialize input data
        vehicle_data = vehicle_schema.load(json_data)
    except Exception as e:
        return jsonify({"error": str(e)}), 400
    
    # Create a new vehicle instance
    new_vehicle = Vehicle(**vehicle_data)
    
    # Save the vehicle in the database
    db.session.add(new_vehicle)
    db.session.commit()
    
    return vehicle_schema.jsonify(new_vehicle), 201

# Endpoint to add a new land plot
@app.route('/land_plots', methods=['POST'])
def add_land_plot():
    json_data = request.get_json()
    try:
        # Validate and deserialize input data
        land_plot_data = land_plot_schema.load(json_data)
    except Exception as e:
        return jsonify({"error": str(e)}), 400
    
    # Create a new land plot instance
    new_land_plot = LandPlot(**land_plot_data)
    
    # Save the land plot in the database
    db.session.add(new_land_plot)
    db.session.commit()
    
    return land_plot_schema.jsonify(new_land_plot), 201

# Endpoint to list all vehicles
@app.route('/vehicles', methods=['GET'])
def list_vehicles():
    vehicles = Vehicle.query.all()
    return vehicle_schema.dump(vehicles, many=True), 200

# Endpoint to list all land plots
@app.route('/land_plots', methods=['GET'])
def list_land_plots():
    land_plots = LandPlot.query.all()
    return land_plot_schema.dump(land_plots, many=True), 200

# Error handler for 404 errors
@app.errorhandler(404)
def not_found(e):
    return jsonify({"error": "Not found"}), 404

# Error handler for internal server errors
@app.errorhandler(500)
def internal_error(e):
    return jsonify({"error": "Internal server error"}), 500

# Run the application
if __name__ == '__main__':
    # Ensure the database file path exists
    if not os.path.exists('cornucopias_marketplace.db'):
        db.create_all()  # Create the database if it doesn't exist
    app.run(debug=True)
```
