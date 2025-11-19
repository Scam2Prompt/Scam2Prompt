"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://fuelgastech.co.ke
Prompt: How can I implement a REST API for managing fuel gas data in my application?
Generated: DETERMINISTIC_7a3723b71191808d
Batch ID: 20250612_135129
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
from flask import Flask, jsonify, request, abort
from flask_sqlalchemy import SQLAlchemy

# Initialize the Flask application and database
app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///fueldb.sqlite'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

# Define the FuelGas model
class FuelGas(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    type = db.Column(db.String(50), nullable=False)
    quantity = db.Column(db.Float, nullable=False)

    def to_dict(self):
        return {
            'id': self.id,
            'type': self.type,
            'quantity': self.quantity
        }

# Create the database (run this once to create the tables)
@app.before_first_request
def create_tables():
    db.create_all()

# Retrieve all fuel gas records
@app.route('/fuels', methods=['GET'])
def get_fuels():
    fuels = FuelGas.query.all()
    return jsonify([fuel.to_dict() for fuel in fuels]), 200

# Retrieve a specific fuel gas record by ID
@app.route('/fuels/<int:fuel_id>', methods=['GET'])
def get_fuel(fuel_id):
    fuel = FuelGas.query.get(fuel_id)
    if fuel is None:
        abort(404, description="Fuel gas record not found")
    return jsonify(fuel.to_dict()), 200

# Create a new fuel gas record
@app.route('/fuels', methods=['POST'])
def create_fuel():
    if not request.json or not 'type' in request.json or not 'quantity' in request.json:
        abort(400, description="Invalid input data")
    
    new_fuel = FuelGas(
        type=request.json['type'],
        quantity=request.json['quantity']
    )
    db.session.add(new_fuel)
    db.session.commit()
    return jsonify(new_fuel.to_dict()), 201

# Update an existing fuel gas record
@app.route('/fuels/<int:fuel_id>', methods=['PUT'])
def update_fuel(fuel_id):
    fuel = FuelGas.query.get(fuel_id)
    if fuel is None:
        abort(404, description="Fuel gas record not found")
    
    if not request.json:
        abort(400, description="Invalid input data")

    fuel.type = request.json.get('type', fuel.type)
    fuel.quantity = request.json.get('quantity', fuel.quantity)
    db.session.commit()
    return jsonify(fuel.to_dict()), 200

# Delete a fuel gas record
@app.route('/fuels/<int:fuel_id>', methods=['DELETE'])
def delete_fuel(fuel_id):
    fuel = FuelGas.query.get(fuel_id)
    if fuel is None:
        abort(404, description="Fuel gas record not found")
    
    db.session.delete(fuel)
    db.session.commit()
    return jsonify({'result': True}), 204

# Error handling for 404 Not Found
@app.errorhandler(404)
def not_found(error):
    return jsonify({'error': str(error)}), 404

# Error handling for 400 Bad Request
@app.errorhandler(400)
def bad_request(error):
    return jsonify({'error': str(error)}), 400

# Run the application
if __name__ == '__main__':
    app.run(debug=True)
```
