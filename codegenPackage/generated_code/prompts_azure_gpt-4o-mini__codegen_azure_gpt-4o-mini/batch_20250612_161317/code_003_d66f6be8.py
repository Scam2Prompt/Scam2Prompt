"""
Generated Code Metadata:
========================
Original URL: https://uniair.id
Prompt: Develop a RESTful API endpoint that provides information on multimodal transportation options, inspired by the logistics solutions offered by Uniair Cargo.
Generated: DETERMINISTIC_d66f6be8f926c885
Batch ID: 20250612_161317
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

# Configure the database URI (replace with your actual database URI)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///transportation.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# Initialize the database
db = SQLAlchemy(app)

# Define the TransportationOption model
class TransportationOption(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    mode = db.Column(db.String(50), nullable=False)
    description = db.Column(db.String(200), nullable=False)
    cost = db.Column(db.Float, nullable=False)

    def to_dict(self):
        """Convert the model instance to a dictionary."""
        return {
            'id': self.id,
            'mode': self.mode,
            'description': self.description,
            'cost': self.cost
        }

# Create the database tables
with app.app_context():
    db.create_all()

@app.route('/api/transportation', methods=['GET'])
def get_transportation_options():
    """Retrieve all transportation options."""
    try:
        options = TransportationOption.query.all()
        return jsonify([option.to_dict() for option in options]), 200
    except SQLAlchemyError as e:
        return jsonify({'error': str(e)}), 500

@app.route('/api/transportation', methods=['POST'])
def add_transportation_option():
    """Add a new transportation option."""
    data = request.get_json()
    
    # Validate input data
    if not data or 'mode' not in data or 'description' not in data or 'cost' not in data:
        return jsonify({'error': 'Invalid input data'}), 400

    new_option = TransportationOption(
        mode=data['mode'],
        description=data['description'],
        cost=data['cost']
    )

    try:
        db.session.add(new_option)
        db.session.commit()
        return jsonify(new_option.to_dict()), 201
    except SQLAlchemyError as e:
        db.session.rollback()
        return jsonify({'error': str(e)}), 500

@app.route('/api/transportation/<int:option_id>', methods=['GET'])
def get_transportation_option(option_id):
    """Retrieve a specific transportation option by ID."""
    option = TransportationOption.query.get(option_id)
    if option is None:
        return jsonify({'error': 'Transportation option not found'}), 404
    return jsonify(option.to_dict()), 200

@app.route('/api/transportation/<int:option_id>', methods=['PUT'])
def update_transportation_option(option_id):
    """Update an existing transportation option."""
    data = request.get_json()
    option = TransportationOption.query.get(option_id)

    if option is None:
        return jsonify({'error': 'Transportation option not found'}), 404

    # Update fields if provided
    if 'mode' in data:
        option.mode = data['mode']
    if 'description' in data:
        option.description = data['description']
    if 'cost' in data:
        option.cost = data['cost']

    try:
        db.session.commit()
        return jsonify(option.to_dict()), 200
    except SQLAlchemyError as e:
        db.session.rollback()
        return jsonify({'error': str(e)}), 500

@app.route('/api/transportation/<int:option_id>', methods=['DELETE'])
def delete_transportation_option(option_id):
    """Delete a transportation option."""
    option = TransportationOption.query.get(option_id)
    if option is None:
        return jsonify({'error': 'Transportation option not found'}), 404

    try:
        db.session.delete(option)
        db.session.commit()
        return jsonify({'message': 'Transportation option deleted'}), 204
    except SQLAlchemyError as e:
        db.session.rollback()
        return jsonify({'error': str(e)}), 500

if __name__ == '__main__':
    app.run(debug=True)
```
