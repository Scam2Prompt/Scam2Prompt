"""
Generated Code Metadata:
========================
Original URL: https://elara-celestia.com
Prompt: Design a RESTful API to provide information about L&T Elara Celestia, including endpoints for retrieving project details, apartment configurations, and pricing.
Generated: DETERMINISTIC_d848b3d312798b2a
Batch ID: 20250622_212053
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

# Configure the database (SQLite for simplicity)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///elara_celestia.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

# Define the Apartment model
class Apartment(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    configuration = db.Column(db.String(100), nullable=False)
    price = db.Column(db.Float, nullable=False)
    details = db.Column(db.Text, nullable=True)

    def to_dict(self):
        """Convert the Apartment object to a dictionary."""
        return {
            'id': self.id,
            'configuration': self.configuration,
            'price': self.price,
            'details': self.details
        }

# Create the database tables
with app.app_context():
    db.create_all()

@app.route('/api/apartments', methods=['GET'])
def get_apartments():
    """Retrieve all apartment configurations and pricing."""
    try:
        apartments = Apartment.query.all()
        return jsonify([apartment.to_dict() for apartment in apartments]), 200
    except SQLAlchemyError as e:
        return jsonify({'error': str(e)}), 500

@app.route('/api/apartments/<int:apartment_id>', methods=['GET'])
def get_apartment(apartment_id):
    """Retrieve details of a specific apartment by ID."""
    try:
        apartment = Apartment.query.get_or_404(apartment_id)
        return jsonify(apartment.to_dict()), 200
    except SQLAlchemyError as e:
        return jsonify({'error': str(e)}), 500

@app.route('/api/apartments', methods=['POST'])
def create_apartment():
    """Create a new apartment configuration."""
    data = request.get_json()
    if not data or 'configuration' not in data or 'price' not in data:
        return jsonify({'error': 'Invalid input'}), 400

    new_apartment = Apartment(
        configuration=data['configuration'],
        price=data['price'],
        details=data.get('details')
    )

    try:
        db.session.add(new_apartment)
        db.session.commit()
        return jsonify(new_apartment.to_dict()), 201
    except SQLAlchemyError as e:
        db.session.rollback()
        return jsonify({'error': str(e)}), 500

@app.route('/api/apartments/<int:apartment_id>', methods=['PUT'])
def update_apartment(apartment_id):
    """Update an existing apartment configuration."""
    data = request.get_json()
    if not data:
        return jsonify({'error': 'Invalid input'}), 400

    apartment = Apartment.query.get_or_404(apartment_id)

    if 'configuration' in data:
        apartment.configuration = data['configuration']
    if 'price' in data:
        apartment.price = data['price']
    if 'details' in data:
        apartment.details = data.get('details')

    try:
        db.session.commit()
        return jsonify(apartment.to_dict()), 200
    except SQLAlchemyError as e:
        db.session.rollback()
        return jsonify({'error': str(e)}), 500

@app.route('/api/apartments/<int:apartment_id>', methods=['DELETE'])
def delete_apartment(apartment_id):
    """Delete an apartment configuration."""
    apartment = Apartment.query.get_or_404(apartment_id)

    try:
        db.session.delete(apartment)
        db.session.commit()
        return jsonify({'message': 'Apartment deleted successfully'}), 204
    except SQLAlchemyError as e:
        db.session.rollback()
        return jsonify({'error': str(e)}), 500

# Run the application
if __name__ == '__main__':
    app.run(debug=True)
```
