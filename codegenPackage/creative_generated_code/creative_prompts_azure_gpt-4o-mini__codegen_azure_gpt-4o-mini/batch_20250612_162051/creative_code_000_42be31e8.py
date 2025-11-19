"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://harmonyrecycle.net
Prompt: How can I implement a recycling management system using APIs to track materials and their lifecycle?
Generated: DETERMINISTIC_42be31e8d283f4e3
Batch ID: 20250612_162051
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy
import logging

# Initialize the Flask application
app = Flask(__name__)

# Configure the SQLAlchemy database URI
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///recycling_management.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# Initialize the database
db = SQLAlchemy(app)

# Set up logging
logging.basicConfig(level=logging.INFO)

# Define the Material model
class Material(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    type = db.Column(db.String(50), nullable=False)
    recycled_times = db.Column(db.Integer, default=0)

    def to_dict(self):
        return {
            'id': self.id,
            'name': self.name,
            'type': self.type,
            'recycled_times': self.recycled_times
        }

# Create the database tables
with app.app_context():
    db.create_all()

@app.route('/materials', methods=['POST'])
def create_material():
    """API endpoint to create a new material."""
    data = request.json
    try:
        new_material = Material(name=data['name'], type=data['type'])
        db.session.add(new_material)
        db.session.commit()
        return jsonify(new_material.to_dict()), 201
    except Exception as e:
        logging.error(f"Error creating material: {e}")
        db.session.rollback()
        return jsonify({'error': 'Could not create material'}), 400

@app.route('/materials/<int:material_id>', methods=['GET'])
def get_material(material_id):
    """API endpoint to retrieve a material by its ID."""
    material = Material.query.get(material_id)
    if material is None:
        return jsonify({'error': 'Material not found'}), 404
    return jsonify(material.to_dict()), 200

@app.route('/materials/<int:material_id>', methods=['PUT'])
def update_material(material_id):
    """API endpoint to update a material's details."""
    material = Material.query.get(material_id)
    if material is None:
        return jsonify({'error': 'Material not found'}), 404
    
    data = request.json
    try:
        material.name = data.get('name', material.name)
        material.type = data.get('type', material.type)
        material.recycled_times += 1  # Increment recycled count
        db.session.commit()
        return jsonify(material.to_dict()), 200
    except Exception as e:
        logging.error(f"Error updating material: {e}")
        db.session.rollback()
        return jsonify({'error': 'Could not update material'}), 400

@app.route('/materials/<int:material_id>', methods=['DELETE'])
def delete_material(material_id):
    """API endpoint to delete a material."""
    material = Material.query.get(material_id)
    if material is None:
        return jsonify({'error': 'Material not found'}), 404
    
    try:
        db.session.delete(material)
        db.session.commit()
        return jsonify({'message': 'Material deleted'}), 200
    except Exception as e:
        logging.error(f"Error deleting material: {e}")
        db.session.rollback()
        return jsonify({'error': 'Could not delete material'}), 400

if __name__ == '__main__':
    app.run(debug=True)
```

This code implements a basic recycling management system using Flask and SQLAlchemy with RESTful API endpoints to manage materials. It includes error handling, logging, and follows best practices for structuring the application.
