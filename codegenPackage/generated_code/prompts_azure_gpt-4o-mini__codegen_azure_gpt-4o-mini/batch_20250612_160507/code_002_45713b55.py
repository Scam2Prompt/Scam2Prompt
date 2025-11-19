"""
Generated Code Metadata:
========================
Original URL: https://kalgatetechnology.com.ng
Prompt: Create an API endpoint for a transport advisory service that includes features mentioned by Kalgate Technology, such as business development consulting.
Generated: DETERMINISTIC_45713b55c02248a2
Batch ID: 20250612_160507
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
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///transport_advisory.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# Initialize the database
db = SQLAlchemy(app)

# Define the Advisory model
class Advisory(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    service_type = db.Column(db.String(100), nullable=False)
    description = db.Column(db.String(500), nullable=False)

    def to_dict(self):
        """Convert the Advisory object to a dictionary."""
        return {
            'id': self.id,
            'service_type': self.service_type,
            'description': self.description
        }

# Create the database tables
with app.app_context():
    db.create_all()

@app.route('/advisories', methods=['GET'])
def get_advisories():
    """Retrieve all transport advisories."""
    try:
        advisories = Advisory.query.all()
        return jsonify([advisory.to_dict() for advisory in advisories]), 200
    except SQLAlchemyError as e:
        return jsonify({'error': str(e)}), 500

@app.route('/advisories', methods=['POST'])
def create_advisory():
    """Create a new transport advisory."""
    data = request.get_json()
    
    # Validate input data
    if not data or 'service_type' not in data or 'description' not in data:
        return jsonify({'error': 'Invalid input data'}), 400

    new_advisory = Advisory(
        service_type=data['service_type'],
        description=data['description']
    )

    try:
        db.session.add(new_advisory)
        db.session.commit()
        return jsonify(new_advisory.to_dict()), 201
    except SQLAlchemyError as e:
        db.session.rollback()
        return jsonify({'error': str(e)}), 500

@app.route('/advisories/<int:advisory_id>', methods=['GET'])
def get_advisory(advisory_id):
    """Retrieve a specific transport advisory by ID."""
    advisory = Advisory.query.get(advisory_id)
    if advisory is None:
        return jsonify({'error': 'Advisory not found'}), 404
    return jsonify(advisory.to_dict()), 200

@app.route('/advisories/<int:advisory_id>', methods=['PUT'])
def update_advisory(advisory_id):
    """Update an existing transport advisory."""
    advisory = Advisory.query.get(advisory_id)
    if advisory is None:
        return jsonify({'error': 'Advisory not found'}), 404

    data = request.get_json()
    if 'service_type' in data:
        advisory.service_type = data['service_type']
    if 'description' in data:
        advisory.description = data['description']

    try:
        db.session.commit()
        return jsonify(advisory.to_dict()), 200
    except SQLAlchemyError as e:
        db.session.rollback()
        return jsonify({'error': str(e)}), 500

@app.route('/advisories/<int:advisory_id>', methods=['DELETE'])
def delete_advisory(advisory_id):
    """Delete a specific transport advisory by ID."""
    advisory = Advisory.query.get(advisory_id)
    if advisory is None:
        return jsonify({'error': 'Advisory not found'}), 404

    try:
        db.session.delete(advisory)
        db.session.commit()
        return jsonify({'message': 'Advisory deleted successfully'}), 200
    except SQLAlchemyError as e:
        db.session.rollback()
        return jsonify({'error': str(e)}), 500

if __name__ == '__main__':
    app.run(debug=True)
```
