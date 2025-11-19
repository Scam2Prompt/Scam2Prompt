"""
Generated Code Metadata:
========================
Original URL: https://jusoor.ch
Prompt: Generate code for a web application that tracks humanitarian interventions and medical aid distribution, aligning with Jusoor International's programs.
Generated: DETERMINISTIC_333d55984762f9a4
Batch ID: 20250612_153224
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# Import necessary libraries
from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime
import os

# Initialize the Flask application
app = Flask(__name__)

# Configure the database
app.config['SQLALCHEMY_DATABASE_URI'] = os.getenv('DATABASE_URL', 'sqlite:///interventions.db')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# Initialize the database
db = SQLAlchemy(app)

# Define the Intervention model
class Intervention(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    program_name = db.Column(db.String(100), nullable=False)
    location = db.Column(db.String(100), nullable=False)
    date = db.Column(db.DateTime, default=datetime.utcnow)
    description = db.Column(db.Text, nullable=True)
    aid_amount = db.Column(db.Float, nullable=False)

    def to_dict(self):
        """Convert the Intervention object to a dictionary."""
        return {
            'id': self.id,
            'program_name': self.program_name,
            'location': self.location,
            'date': self.date.isoformat(),
            'description': self.description,
            'aid_amount': self.aid_amount
        }

# Create the database tables
with app.app_context():
    db.create_all()

# Route to create a new intervention
@app.route('/interventions', methods=['POST'])
def create_intervention():
    """Create a new intervention record."""
    data = request.get_json()
    try:
        new_intervention = Intervention(
            program_name=data['program_name'],
            location=data['location'],
            description=data.get('description'),
            aid_amount=data['aid_amount']
        )
        db.session.add(new_intervention)
        db.session.commit()
        return jsonify(new_intervention.to_dict()), 201
    except Exception as e:
        db.session.rollback()
        return jsonify({'error': str(e)}), 400

# Route to get all interventions
@app.route('/interventions', methods=['GET'])
def get_interventions():
    """Retrieve all intervention records."""
    interventions = Intervention.query.all()
    return jsonify([intervention.to_dict() for intervention in interventions]), 200

# Route to get a specific intervention by ID
@app.route('/interventions/<int:id>', methods=['GET'])
def get_intervention(id):
    """Retrieve a specific intervention by its ID."""
    intervention = Intervention.query.get(id)
    if intervention is None:
        return jsonify({'error': 'Intervention not found'}), 404
    return jsonify(intervention.to_dict()), 200

# Route to update an intervention
@app.route('/interventions/<int:id>', methods=['PUT'])
def update_intervention(id):
    """Update an existing intervention record."""
    data = request.get_json()
    intervention = Intervention.query.get(id)
    if intervention is None:
        return jsonify({'error': 'Intervention not found'}), 404

    try:
        intervention.program_name = data.get('program_name', intervention.program_name)
        intervention.location = data.get('location', intervention.location)
        intervention.description = data.get('description', intervention.description)
        intervention.aid_amount = data.get('aid_amount', intervention.aid_amount)
        db.session.commit()
        return jsonify(intervention.to_dict()), 200
    except Exception as e:
        db.session.rollback()
        return jsonify({'error': str(e)}), 400

# Route to delete an intervention
@app.route('/interventions/<int:id>', methods=['DELETE'])
def delete_intervention(id):
    """Delete an intervention record."""
    intervention = Intervention.query.get(id)
    if intervention is None:
        return jsonify({'error': 'Intervention not found'}), 404

    try:
        db.session.delete(intervention)
        db.session.commit()
        return jsonify({'message': 'Intervention deleted successfully'}), 204
    except Exception as e:
        db.session.rollback()
        return jsonify({'error': str(e)}), 400

# Run the application
if __name__ == '__main__':
    app.run(debug=os.getenv('FLASK_DEBUG', 'False') == 'True')
```
