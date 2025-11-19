"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://lbeldi.com
Prompt: Design a RESTful API that delivers insights into Moroccan jewelry craftsmanship, detailing materials and cultural influences.
Generated: DETERMINISTIC_a0d2d7d96b00684c
Batch ID: 20250612_162717
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
from flask import Flask, jsonify, request
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.exc import IntegrityError

# Initialize Flask application
app = Flask(__name__)

# Configure the SQLite database
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///jewelry.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

# Model for Jewelry Craftsmanship
class JewelryCraftsmanship(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    material = db.Column(db.String(50), nullable=False)
    cultural_influence = db.Column(db.String(100), nullable=False)
    description = db.Column(db.String(200), nullable=False)

    def to_dict(self):
        return {
            'id': self.id,
            'material': self.material,
            'cultural_influence': self.cultural_influence,
            'description': self.description
        }

# Create database tables
with app.app_context():
    db.create_all()

@app.route('/craftsmanship', methods=['POST'])
def add_craftsmanship():
    """
    Add a new jewelry craftsmanship entry.
    Expects JSON with material, cultural_influence, and description.
    """
    data = request.get_json()
    if not data or not all(key in data for key in ('material', 'cultural_influence', 'description')):
        return jsonify({'error': 'Bad Request', 'message': 'Missing required fields'}), 400
    
    new_craftsmanship = JewelryCraftsmanship(
        material=data['material'],
        cultural_influence=data['cultural_influence'],
        description=data['description']
    )

    try:
        db.session.add(new_craftsmanship)
        db.session.commit()
        return jsonify(new_craftsmanship.to_dict()), 201
    except IntegrityError:
        db.session.rollback()
        return jsonify({'error': 'Conflict', 'message': 'Entry already exists'}), 409
    except Exception as e:
        db.session.rollback()
        return jsonify({'error': 'Internal Server Error', 'message': str(e)}), 500

@app.route('/craftsmanship', methods=['GET'])
def get_craftsmanship():
    """
    Retrieve all jewelry craftsmanship entries.
    Returns a JSON array of all entries.
    """
    craftsmanship_list = JewelryCraftsmanship.query.all()
    return jsonify([craftsmanship.to_dict() for craftsmanship in craftsmanship_list]), 200

@app.route('/craftsmanship/<int:id>', methods=['GET'])
def get_craftsmanship_by_id(id):
    """
    Retrieve a specific jewelry craftsmanship entry by ID.
    """
    craftsmanship = JewelryCraftsmanship.query.get(id)
    if craftsmanship is None:
        return jsonify({'error': 'Not Found', 'message': 'Craftsmanship not found'}), 404
    return jsonify(craftsmanship.to_dict()), 200

@app.route('/craftsmanship/<int:id>', methods=['PUT'])
def update_craftsmanship(id):
    """
    Update an existing jewelry craftsmanship entry by ID.
    Expects JSON with updated fields.
    """
    craftsmanship = JewelryCraftsmanship.query.get(id)
    if craftsmanship is None:
        return jsonify({'error': 'Not Found', 'message': 'Craftsmanship not found'}), 404

    data = request.get_json()
    if not data or not any(key in data for key in ('material', 'cultural_influence', 'description')):
        return jsonify({'error': 'Bad Request', 'message': 'Missing fields to update'}), 400

    if 'material' in data:
        craftsmanship.material = data['material']
    if 'cultural_influence' in data:
        craftsmanship.cultural_influence = data['cultural_influence']
    if 'description' in data:
        craftsmanship.description = data['description']

    try:
        db.session.commit()
        return jsonify(craftsmanship.to_dict()), 200
    except Exception as e:
        db.session.rollback()
        return jsonify({'error': 'Internal Server Error', 'message': str(e)}), 500

@app.route('/craftsmanship/<int:id>', methods=['DELETE'])
def delete_craftsmanship(id):
    """
    Delete a specific jewelry craftsmanship entry by ID.
    """
    craftsmanship = JewelryCraftsmanship.query.get(id)
    if craftsmanship is None:
        return jsonify({'error': 'Not Found', 'message': 'Craftsmanship not found'}), 404

    try:
        db.session.delete(craftsmanship)
        db.session.commit()
        return jsonify({'message': 'Craftsmanship deleted successfully'}), 204
    except Exception as e:
        db.session.rollback()
        return jsonify({'error': 'Internal Server Error', 'message': str(e)}), 500

if __name__ == '__main__':
    # Run the Flask app
    app.run(debug=True)
```
