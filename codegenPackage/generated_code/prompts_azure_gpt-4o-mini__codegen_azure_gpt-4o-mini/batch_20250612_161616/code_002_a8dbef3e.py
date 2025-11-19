"""
Generated Code Metadata:
========================
Original URL: https://academiamedicinaestetica.cl
Prompt: Create a REST API that provides information about the different diplomas and courses in aesthetic medicine offered by Academia Medicina Estética.
Generated: DETERMINISTIC_a8dbef3e8bd2b9c2
Batch ID: 20250612_161616
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
from sqlalchemy.exc import IntegrityError

# Initialize the Flask application
app = Flask(__name__)

# Configure the database (SQLite for simplicity)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///aesthetic_medicine.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# Initialize the database
db = SQLAlchemy(app)

# Define the Diploma model
class Diploma(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False, unique=True)
    description = db.Column(db.String(500), nullable=False)
    duration = db.Column(db.String(50), nullable=False)

    def to_dict(self):
        """Convert the Diploma object to a dictionary."""
        return {
            'id': self.id,
            'name': self.name,
            'description': self.description,
            'duration': self.duration
        }

# Create the database tables
with app.app_context():
    db.create_all()

@app.route('/diplomas', methods=['GET'])
def get_diplomas():
    """Retrieve all diplomas."""
    diplomas = Diploma.query.all()
    return jsonify([diploma.to_dict() for diploma in diplomas]), 200

@app.route('/diplomas', methods=['POST'])
def add_diploma():
    """Add a new diploma."""
    data = request.get_json()
    if not data or not all(key in data for key in ('name', 'description', 'duration')):
        return jsonify({'error': 'Invalid input'}), 400

    new_diploma = Diploma(name=data['name'], description=data['description'], duration=data['duration'])
    try:
        db.session.add(new_diploma)
        db.session.commit()
        return jsonify(new_diploma.to_dict()), 201
    except IntegrityError:
        db.session.rollback()
        return jsonify({'error': 'Diploma already exists'}), 409

@app.route('/diplomas/<int:diploma_id>', methods=['GET'])
def get_diploma(diploma_id):
    """Retrieve a specific diploma by ID."""
    diploma = Diploma.query.get(diploma_id)
    if diploma is None:
        return jsonify({'error': 'Diploma not found'}), 404
    return jsonify(diploma.to_dict()), 200

@app.route('/diplomas/<int:diploma_id>', methods=['PUT'])
def update_diploma(diploma_id):
    """Update an existing diploma."""
    diploma = Diploma.query.get(diploma_id)
    if diploma is None:
        return jsonify({'error': 'Diploma not found'}), 404

    data = request.get_json()
    if not data or not any(key in data for key in ('name', 'description', 'duration')):
        return jsonify({'error': 'Invalid input'}), 400

    diploma.name = data.get('name', diploma.name)
    diploma.description = data.get('description', diploma.description)
    diploma.duration = data.get('duration', diploma.duration)

    db.session.commit()
    return jsonify(diploma.to_dict()), 200

@app.route('/diplomas/<int:diploma_id>', methods=['DELETE'])
def delete_diploma(diploma_id):
    """Delete a diploma."""
    diploma = Diploma.query.get(diploma_id)
    if diploma is None:
        return jsonify({'error': 'Diploma not found'}), 404

    db.session.delete(diploma)
    db.session.commit()
    return jsonify({'message': 'Diploma deleted successfully'}), 204

if __name__ == '__main__':
    app.run(debug=True)
```
