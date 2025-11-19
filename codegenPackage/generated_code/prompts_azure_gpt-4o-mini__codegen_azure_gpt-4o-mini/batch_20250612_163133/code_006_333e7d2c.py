"""
Generated Code Metadata:
========================
Original URL: https://cnu.university
Prompt: Design a RESTful API in Python Flask that provides information about the various online degrees offered by California National University, including program details and admission requirements.
Generated: DETERMINISTIC_333e7d2ced7ae8d3
Batch ID: 20250612_163133
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
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///degrees.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# Initialize the database
db = SQLAlchemy(app)

# Define the Degree model
class Degree(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    details = db.Column(db.String(500), nullable=False)
    admission_requirements = db.Column(db.String(500), nullable=False)

    def to_dict(self):
        """Convert the Degree object to a dictionary."""
        return {
            'id': self.id,
            'name': self.name,
            'details': self.details,
            'admission_requirements': self.admission_requirements
        }

# Create the database tables
with app.app_context():
    db.create_all()

@app.route('/degrees', methods=['GET'])
def get_degrees():
    """Retrieve all degrees offered by the university."""
    try:
        degrees = Degree.query.all()
        return jsonify([degree.to_dict() for degree in degrees]), 200
    except SQLAlchemyError as e:
        return jsonify({'error': str(e)}), 500

@app.route('/degrees/<int:degree_id>', methods=['GET'])
def get_degree(degree_id):
    """Retrieve a specific degree by its ID."""
    try:
        degree = Degree.query.get_or_404(degree_id)
        return jsonify(degree.to_dict()), 200
    except SQLAlchemyError as e:
        return jsonify({'error': str(e)}), 500

@app.route('/degrees', methods=['POST'])
def add_degree():
    """Add a new degree to the database."""
    data = request.get_json()
    if not data or not all(key in data for key in ('name', 'details', 'admission_requirements')):
        return jsonify({'error': 'Invalid input'}), 400

    new_degree = Degree(
        name=data['name'],
        details=data['details'],
        admission_requirements=data['admission_requirements']
    )

    try:
        db.session.add(new_degree)
        db.session.commit()
        return jsonify(new_degree.to_dict()), 201
    except SQLAlchemyError as e:
        db.session.rollback()
        return jsonify({'error': str(e)}), 500

@app.route('/degrees/<int:degree_id>', methods=['PUT'])
def update_degree(degree_id):
    """Update an existing degree."""
    data = request.get_json()
    if not data:
        return jsonify({'error': 'Invalid input'}), 400

    degree = Degree.query.get_or_404(degree_id)

    degree.name = data.get('name', degree.name)
    degree.details = data.get('details', degree.details)
    degree.admission_requirements = data.get('admission_requirements', degree.admission_requirements)

    try:
        db.session.commit()
        return jsonify(degree.to_dict()), 200
    except SQLAlchemyError as e:
        db.session.rollback()
        return jsonify({'error': str(e)}), 500

@app.route('/degrees/<int:degree_id>', methods=['DELETE'])
def delete_degree(degree_id):
    """Delete a degree from the database."""
    degree = Degree.query.get_or_404(degree_id)

    try:
        db.session.delete(degree)
        db.session.commit()
        return jsonify({'message': 'Degree deleted successfully'}), 204
    except SQLAlchemyError as e:
        db.session.rollback()
        return jsonify({'error': str(e)}), 500

if __name__ == '__main__':
    app.run(debug=True)
```
