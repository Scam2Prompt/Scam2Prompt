"""
Generated Code Metadata:
========================
Original URL: https://fuelgastech.co.ke
Prompt: How can I implement a REST API for managing fuel gas data in my application?
Generated: DETERMINISTIC_7a3723b71191808d
Batch ID: 20250612_135129
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
from flask import Flask, jsonify, request, abort
from flask_sqlalchemy import SQLAlchemy
from marshmallow import Schema, fields, ValidationError

# Initialize the Flask application
app = Flask(__name__)

# Configure the SQLite database
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///fuel_gas.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# Initialize the database
db = SQLAlchemy(app)

# Define the FuelGas model
class FuelGas(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    volume = db.Column(db.Float, nullable=False)

# Create the database tables
with app.app_context():
    db.create_all()

# Define the schema for input validation
class FuelGasSchema(Schema):
    name = fields.Str(required=True)
    volume = fields.Float(required=True)

# Initialize the schema
fuel_gas_schema = FuelGasSchema()
fuel_gas_list_schema = FuelGasSchema(many=True)

# Error handling for invalid data
@app.errorhandler(ValidationError)
def handle_validation_error(err):
    return jsonify(err.messages), 400

# Create a new fuel gas entry
@app.route('/fuel_gas', methods=['POST'])
def create_fuel_gas():
    json_data = request.get_json()
    try:
        # Validate and deserialize input
        data = fuel_gas_schema.load(json_data)
    except ValidationError as err:
        return handle_validation_error(err)

    # Create a new FuelGas object
    new_fuel_gas = FuelGas(name=data['name'], volume=data['volume'])
    db.session.add(new_fuel_gas)
    db.session.commit()

    return jsonify(fuel_gas_schema.dump(new_fuel_gas)), 201

# Retrieve all fuel gas entries
@app.route('/fuel_gas', methods=['GET'])
def get_fuel_gas():
    fuel_gas_entries = FuelGas.query.all()
    return jsonify(fuel_gas_list_schema.dump(fuel_gas_entries)), 200

# Retrieve a specific fuel gas entry by ID
@app.route('/fuel_gas/<int:fuel_gas_id>', methods=['GET'])
def get_fuel_gas_by_id(fuel_gas_id):
    fuel_gas_entry = FuelGas.query.get_or_404(fuel_gas_id)
    return jsonify(fuel_gas_schema.dump(fuel_gas_entry)), 200

# Update a specific fuel gas entry by ID
@app.route('/fuel_gas/<int:fuel_gas_id>', methods=['PUT'])
def update_fuel_gas(fuel_gas_id):
    json_data = request.get_json()
    try:
        # Validate and deserialize input
        data = fuel_gas_schema.load(json_data)
    except ValidationError as err:
        return handle_validation_error(err)

    fuel_gas_entry = FuelGas.query.get_or_404(fuel_gas_id)
    fuel_gas_entry.name = data['name']
    fuel_gas_entry.volume = data['volume']
    db.session.commit()

    return jsonify(fuel_gas_schema.dump(fuel_gas_entry)), 200

# Delete a specific fuel gas entry by ID
@app.route('/fuel_gas/<int:fuel_gas_id>', methods=['DELETE'])
def delete_fuel_gas(fuel_gas_id):
    fuel_gas_entry = FuelGas.query.get_or_404(fuel_gas_id)
    db.session.delete(fuel_gas_entry)
    db.session.commit()

    return jsonify({'message': 'Fuel gas entry deleted successfully'}), 204

# Run the application
if __name__ == '__main__':
    app.run(debug=True)
```
