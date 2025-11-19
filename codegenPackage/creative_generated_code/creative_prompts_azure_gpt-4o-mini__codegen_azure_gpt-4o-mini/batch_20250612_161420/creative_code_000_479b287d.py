"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://bossasopetroleum.com
Prompt: Generate code for a web application that allows users to view and manage petrol station services similar to those offered by Bosasa Petroleum in Puntland Somalia.
Generated: DETERMINISTIC_479b287d0a1bd9b7
Batch ID: 20250612_161420
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
# Import necessary libraries
from flask import Flask, jsonify, request, render_template
from flask_sqlalchemy import SQLAlchemy
from marshmallow import Schema, fields, ValidationError

# Initialize Flask app and database
app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///petrol_stations.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

# Define the PetrolStation model
class PetrolStation(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    location = db.Column(db.String(100), nullable=False)
    services = db.Column(db.Text, nullable=False)

    def __repr__(self):
        return f'<PetrolStation {self.name}>'

# Define the schema for validation
class PetrolStationSchema(Schema):
    name = fields.Str(required=True)
    location = fields.Str(required=True)
    services = fields.Str(required=True)

# Create a schema instance
petrol_station_schema = PetrolStationSchema()
petrol_stations_schema = PetrolStationSchema(many=True)

# Initialize the database
@app.before_first_request
def create_tables():
    db.create_all()

# Route to get all petrol stations
@app.route('/petrol_stations', methods=['GET'])
def get_petrol_stations():
    try:
        petrol_stations = PetrolStation.query.all()
        return petrol_stations_schema.jsonify(petrol_stations), 200
    except Exception as e:
        return jsonify({"error": str(e)}), 500

# Route to add a new petrol station
@app.route('/petrol_stations', methods=['POST'])
def add_petrol_station():
    try:
        # Validate input data
        data = request.get_json()
        petrol_station_schema.load(data)
        new_station = PetrolStation(**data)
        db.session.add(new_station)
        db.session.commit()
        return petrol_station_schema.jsonify(new_station), 201
    except ValidationError as err:
        return jsonify({"errors": err.messages}), 400
    except Exception as e:
        return jsonify({"error": str(e)}), 500

# Route to update a petrol station
@app.route('/petrol_stations/<int:id>', methods=['PUT'])
def update_petrol_station(id):
    try:
        station = PetrolStation.query.get_or_404(id)
        data = request.get_json()
        petrol_station_schema.load(data)
        for key, value in data.items():
            setattr(station, key, value)
        db.session.commit()
        return petrol_station_schema.jsonify(station), 200
    except ValidationError as err:
        return jsonify({"errors": err.messages}), 400
    except Exception as e:
        return jsonify({"error": str(e)}), 500

# Route to delete a petrol station
@app.route('/petrol_stations/<int:id>', methods=['DELETE'])
def delete_petrol_station(id):
    try:
        station = PetrolStation.query.get_or_404(id)
        db.session.delete(station)
        db.session.commit()
        return jsonify({"message": "Petrol station deleted successfully"}), 204
    except Exception as e:
        return jsonify({"error": str(e)}), 500

# Run the application
if __name__ == '__main__':
    app.run(debug=True)
```
