"""
Generated Code Metadata:
========================
Original URL: https://lbeldi.com
Prompt: Design a RESTful API that delivers insights into Moroccan jewelry craftsmanship, detailing materials and cultural influences.
Generated: DETERMINISTIC_a0d2d7d96b00684c
Batch ID: 20250612_162717
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

# Configure the SQLite database
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///jewelry_craftsmanship.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# Initialize the database
db = SQLAlchemy(app)

# Define the Jewelry model
class Jewelry(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    material = db.Column(db.String(100), nullable=False)
    cultural_influence = db.Column(db.String(200), nullable=False)
    description = db.Column(db.Text, nullable=True)

    def to_dict(self):
        """Convert the Jewelry object to a dictionary."""
        return {
            'id': self.id,
            'material': self.material,
            'cultural_influence': self.cultural_influence,
            'description': self.description
        }

# Create the database tables
with app.app_context():
    db.create_all()

@app.route('/jewelry', methods=['GET'])
def get_jewelry():
    """Retrieve all jewelry craftsmanship insights."""
    try:
        jewelry_list = Jewelry.query.all()
        return jsonify([jewelry.to_dict() for jewelry in jewelry_list]), 200
    except SQLAlchemyError as e:
        return jsonify({'error': str(e)}), 500

@app.route('/jewelry/<int:jewelry_id>', methods=['GET'])
def get_jewelry_by_id(jewelry_id):
    """Retrieve a specific jewelry item by its ID."""
    jewelry = Jewelry.query.get(jewelry_id)
    if jewelry is None:
        return jsonify({'error': 'Jewelry not found'}), 404
    return jsonify(jewelry.to_dict()), 200

@app.route('/jewelry', methods=['POST'])
def add_jewelry():
    """Add a new jewelry craftsmanship insight."""
    data = request.get_json()
    if not data or 'material' not in data or 'cultural_influence' not in data:
        return jsonify({'error': 'Invalid input'}), 400

    new_jewelry = Jewelry(
        material=data['material'],
        cultural_influence=data['cultural_influence'],
        description=data.get('description')
    )
    
    try:
        db.session.add(new_jewelry)
        db.session.commit()
        return jsonify(new_jewelry.to_dict()), 201
    except SQLAlchemyError as e:
        db.session.rollback()
        return jsonify({'error': str(e)}), 500

@app.route('/jewelry/<int:jewelry_id>', methods=['PUT'])
def update_jewelry(jewelry_id):
    """Update an existing jewelry craftsmanship insight."""
    jewelry = Jewelry.query.get(jewelry_id)
    if jewelry is None:
        return jsonify({'error': 'Jewelry not found'}), 404

    data = request.get_json()
    if not data:
        return jsonify({'error': 'Invalid input'}), 400

    jewelry.material = data.get('material', jewelry.material)
    jewelry.cultural_influence = data.get('cultural_influence', jewelry.cultural_influence)
    jewelry.description = data.get('description', jewelry.description)

    try:
        db.session.commit()
        return jsonify(jewelry.to_dict()), 200
    except SQLAlchemyError as e:
        db.session.rollback()
        return jsonify({'error': str(e)}), 500

@app.route('/jewelry/<int:jewelry_id>', methods=['DELETE'])
def delete_jewelry(jewelry_id):
    """Delete a specific jewelry craftsmanship insight."""
    jewelry = Jewelry.query.get(jewelry_id)
    if jewelry is None:
        return jsonify({'error': 'Jewelry not found'}), 404

    try:
        db.session.delete(jewelry)
        db.session.commit()
        return jsonify({'message': 'Jewelry deleted successfully'}), 200
    except SQLAlchemyError as e:
        db.session.rollback()
        return jsonify({'error': str(e)}), 500

if __name__ == '__main__':
    app.run(debug=True)
```
