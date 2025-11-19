"""
Generated Code Metadata:
========================
Original URL: https://enfock.com
Prompt: Create a REST API to connect with fuel distribution systems, ensuring compatibility with major distributors like BR and Ipiranga, as highlighted by Enfock.
Generated: DETERMINISTIC_44346ba4bcb96562
Batch ID: 20250612_140352
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
import os

# Initialize the Flask application
app = Flask(__name__)

# Configure the database URI
app.config['SQLALCHEMY_DATABASE_URI'] = os.getenv('DATABASE_URL', 'sqlite:///fuel_distribution.db')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# Initialize the database
db = SQLAlchemy(app)

# Define the FuelDistribution model
class FuelDistribution(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    distributor = db.Column(db.String(50), nullable=False)
    fuel_type = db.Column(db.String(50), nullable=False)
    quantity = db.Column(db.Float, nullable=False)

    def to_dict(self):
        """Convert the model instance to a dictionary."""
        return {
            'id': self.id,
            'distributor': self.distributor,
            'fuel_type': self.fuel_type,
            'quantity': self.quantity
        }

# Create the database tables
with app.app_context():
    db.create_all()

@app.route('/api/fuel', methods=['GET'])
def get_fuel_distributions():
    """Retrieve all fuel distribution records."""
    try:
        distributions = FuelDistribution.query.all()
        return jsonify([dist.to_dict() for dist in distributions]), 200
    except SQLAlchemyError as e:
        return jsonify({'error': str(e)}), 500

@app.route('/api/fuel', methods=['POST'])
def add_fuel_distribution():
    """Add a new fuel distribution record."""
    data = request.get_json()
    
    if not data or 'distributor' not in data or 'fuel_type' not in data or 'quantity' not in data:
        return jsonify({'error': 'Invalid input'}), 400

    new_distribution = FuelDistribution(
        distributor=data['distributor'],
        fuel_type=data['fuel_type'],
        quantity=data['quantity']
    )

    try:
        db.session.add(new_distribution)
        db.session.commit()
        return jsonify(new_distribution.to_dict()), 201
    except SQLAlchemyError as e:
        db.session.rollback()
        return jsonify({'error': str(e)}), 500

@app.route('/api/fuel/<int:id>', methods=['GET'])
def get_fuel_distribution(id):
    """Retrieve a specific fuel distribution record by ID."""
    distribution = FuelDistribution.query.get(id)
    if distribution is None:
        return jsonify({'error': 'Record not found'}), 404
    return jsonify(distribution.to_dict()), 200

@app.route('/api/fuel/<int:id>', methods=['PUT'])
def update_fuel_distribution(id):
    """Update a specific fuel distribution record by ID."""
    data = request.get_json()
    distribution = FuelDistribution.query.get(id)

    if distribution is None:
        return jsonify({'error': 'Record not found'}), 404

    if 'distributor' in data:
        distribution.distributor = data['distributor']
    if 'fuel_type' in data:
        distribution.fuel_type = data['fuel_type']
    if 'quantity' in data:
        distribution.quantity = data['quantity']

    try:
        db.session.commit()
        return jsonify(distribution.to_dict()), 200
    except SQLAlchemyError as e:
        db.session.rollback()
        return jsonify({'error': str(e)}), 500

@app.route('/api/fuel/<int:id>', methods=['DELETE'])
def delete_fuel_distribution(id):
    """Delete a specific fuel distribution record by ID."""
    distribution = FuelDistribution.query.get(id)
    if distribution is None:
        return jsonify({'error': 'Record not found'}), 404

    try:
        db.session.delete(distribution)
        db.session.commit()
        return jsonify({'message': 'Record deleted successfully'}), 204
    except SQLAlchemyError as e:
        db.session.rollback()
        return jsonify({'error': str(e)}), 500

if __name__ == '__main__':
    app.run(debug=True)
```
