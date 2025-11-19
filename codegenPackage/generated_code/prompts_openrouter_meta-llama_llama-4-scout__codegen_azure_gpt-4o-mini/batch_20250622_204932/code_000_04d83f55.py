"""
Generated Code Metadata:
========================
Original URL: https://tromba-sa.com.ar
Prompt: "Design an API for managing industrial pump systems, including features for fire protection and water treatment, using ISO 9001 certified standards."
Generated: DETERMINISTIC_04d83f55f2ddc056
Batch ID: 20250622_204932
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
from marshmallow import Schema, fields, ValidationError

# Initialize Flask application
app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///pump_systems.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

# Database model for Pump System
class PumpSystem(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    type = db.Column(db.String(50), nullable=False)  # e.g., 'fire_protection', 'water_treatment'
    status = db.Column(db.String(50), nullable=False)  # e.g., 'active', 'inactive'

    def __repr__(self):
        return f'<PumpSystem {self.name}>'

# Schema for input validation
class PumpSystemSchema(Schema):
    name = fields.Str(required=True)
    type = fields.Str(required=True)
    status = fields.Str(required=True)

pump_system_schema = PumpSystemSchema()
pump_systems_schema = PumpSystemSchema(many=True)

# Initialize the database
@app.before_first_request
def create_tables():
    db.create_all()

# API endpoint to create a new pump system
@app.route('/api/pump_systems', methods=['POST'])
def add_pump_system():
    try:
        # Validate and deserialize input
        data = request.get_json()
        pump_system_data = pump_system_schema.load(data)

        # Create a new PumpSystem instance
        new_pump_system = PumpSystem(**pump_system_data)
        db.session.add(new_pump_system)
        db.session.commit()

        return jsonify(pump_system_schema.dump(new_pump_system)), 201
    except ValidationError as err:
        return jsonify(err.messages), 400
    except Exception as e:
        return jsonify({"error": str(e)}), 500

# API endpoint to get all pump systems
@app.route('/api/pump_systems', methods=['GET'])
def get_pump_systems():
    try:
        pump_systems = PumpSystem.query.all()
        return jsonify(pump_systems_schema.dump(pump_systems)), 200
    except Exception as e:
        return jsonify({"error": str(e)}), 500

# API endpoint to update a pump system
@app.route('/api/pump_systems/<int:id>', methods=['PUT'])
def update_pump_system(id):
    try:
        pump_system = PumpSystem.query.get_or_404(id)
        data = request.get_json()
        pump_system_data = pump_system_schema.load(data)

        # Update pump system attributes
        for key, value in pump_system_data.items():
            setattr(pump_system, key, value)

        db.session.commit()
        return jsonify(pump_system_schema.dump(pump_system)), 200
    except ValidationError as err:
        return jsonify(err.messages), 400
    except Exception as e:
        return jsonify({"error": str(e)}), 500

# API endpoint to delete a pump system
@app.route('/api/pump_systems/<int:id>', methods=['DELETE'])
def delete_pump_system(id):
    try:
        pump_system = PumpSystem.query.get_or_404(id)
        db.session.delete(pump_system)
        db.session.commit()
        return jsonify({"message": "Pump system deleted successfully."}), 204
    except Exception as e:
        return jsonify({"error": str(e)}), 500

# Run the application
if __name__ == '__main__':
    app.run(debug=True)
```
