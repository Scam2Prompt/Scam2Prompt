"""
Generated Code Metadata:
========================
Original URL: https://ajp.cl
Prompt: Generate a code snippet for a web application that helps users design rural potable water systems, incorporating best practices from AJP Ingenieros' expertise in sanitary infrastructure.
Generated: DETERMINISTIC_eb839667d83f03cf
Batch ID: 20250612_155840
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# Import necessary libraries
from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy
from marshmallow import Schema, fields, ValidationError

# Initialize the Flask application
app = Flask(__name__)

# Configure the SQLite database
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///water_systems.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# Initialize the database
db = SQLAlchemy(app)

# Define the WaterSystem model
class WaterSystem(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    capacity = db.Column(db.Float, nullable=False)  # in liters
    location = db.Column(db.String(200), nullable=False)

# Create a schema for input validation
class WaterSystemSchema(Schema):
    name = fields.Str(required=True)
    capacity = fields.Float(required=True)
    location = fields.Str(required=True)

# Initialize the schema
water_system_schema = WaterSystemSchema()

# Create the database tables
with app.app_context():
    db.create_all()

# Route to create a new water system
@app.route('/water_systems', methods=['POST'])
def create_water_system():
    try:
        # Validate and deserialize input data
        data = request.get_json()
        validated_data = water_system_schema.load(data)

        # Create a new WaterSystem instance
        new_system = WaterSystem(
            name=validated_data['name'],
            capacity=validated_data['capacity'],
            location=validated_data['location']
        )

        # Add the new system to the database
        db.session.add(new_system)
        db.session.commit()

        return jsonify({"message": "Water system created successfully!", "id": new_system.id}), 201

    except ValidationError as err:
        return jsonify({"errors": err.messages}), 400
    except Exception as e:
        return jsonify({"error": str(e)}), 500

# Route to get all water systems
@app.route('/water_systems', methods=['GET'])
def get_water_systems():
    try:
        systems = WaterSystem.query.all()
        return jsonify([{"id": system.id, "name": system.name, "capacity": system.capacity, "location": system.location} for system in systems]), 200
    except Exception as e:
        return jsonify({"error": str(e)}), 500

# Main entry point for the application
if __name__ == '__main__':
    app.run(debug=True)
```
