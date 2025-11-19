"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://cnu.university
Prompt: Design a RESTful API in Python Flask that provides information about the various online degrees offered by California National University, including program details and admission requirements.
Generated: DETERMINISTIC_333e7d2ced7ae8d3
Batch ID: 20250612_163133
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

app = Flask(__name__)

# Configuration for the SQLAlchemy database
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///degrees.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# Initialize the SQLAlchemy extension
db = SQLAlchemy(app)

# Model for Degree programs
class DegreeProgram(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    details = db.Column(db.String(500), nullable=False)
    admission_requirements = db.Column(db.String(500), nullable=False)

    def to_dict(self):
        """Convert the DegreeProgram instance to a dictionary."""
        return {
            'id': self.id,
            'name': self.name,
            'details': self.details,
            'admission_requirements': self.admission_requirements
        }

# Error handling for 404 Not Found
@app.errorhandler(404)
def not_found(error):
    return jsonify({'error': 'Not found'}), 404

# Endpoint to get all degree programs
@app.route('/api/degrees', methods=['GET'])
def get_degrees():
    """Return a list of all degree programs."""
    degrees = DegreeProgram.query.all()
    return jsonify([degree.to_dict() for degree in degrees]), 200

# Endpoint to get a specific degree program by ID
@app.route('/api/degrees/<int:degree_id>', methods=['GET'])
def get_degree(degree_id):
    """Return a specific degree program by ID."""
    degree = DegreeProgram.query.get(degree_id)
    if not degree:
        abort(404)
    return jsonify(degree.to_dict()), 200

# Endpoint to create a new degree program
@app.route('/api/degrees', methods=['POST'])
def create_degree():
    """Create a new degree program."""
    if not request.json or not 'name' in request.json:
        abort(400)

    new_degree = DegreeProgram(
        name=request.json['name'],
        details=request.json.get('details', ''),
        admission_requirements=request.json.get('admission_requirements', '')
    )
    
    db.session.add(new_degree)
    db.session.commit()
    return jsonify(new_degree.to_dict()), 201

# Endpoint to update an existing degree program
@app.route('/api/degrees/<int:degree_id>', methods=['PUT'])
def update_degree(degree_id):
    """Update an existing degree program."""
    degree = DegreeProgram.query.get(degree_id)
    if not degree:
        abort(404)

    if not request.json:
        abort(400)

    degree.name = request.json.get('name', degree.name)
    degree.details = request.json.get('details', degree.details)
    degree.admission_requirements = request.json.get('admission_requirements', degree.admission_requirements)

    db.session.commit()
    return jsonify(degree.to_dict()), 200

# Endpoint to delete a degree program
@app.route('/api/degrees/<int:degree_id>', methods=['DELETE'])
def delete_degree(degree_id):
    """Delete a degree program."""
    degree = DegreeProgram.query.get(degree_id)
    if not degree:
        abort(404)

    db.session.delete(degree)
    db.session.commit()
    return jsonify({'result': True}), 204

if __name__ == '__main__':
    # Create the database and tables
    db.create_all()
    app.run(debug=False, host='0.0.0.0', port=5000)
```
