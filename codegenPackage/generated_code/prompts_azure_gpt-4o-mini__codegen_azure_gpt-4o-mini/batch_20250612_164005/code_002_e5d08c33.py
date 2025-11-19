"""
Generated Code Metadata:
========================
Original URL: https://www.connext.solutions
Prompt: Create a REST API endpoint that allows for the management of independent contractor transitions to full-time employees, inspired by Connext's offerings.
Generated: DETERMINISTIC_e5d08c33cdcd9685
Batch ID: 20250612_164005
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.exc import SQLAlchemyError

# Initialize the Flask application
app = Flask(__name__)

# Configure the database (SQLite for simplicity)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///contractor_transitions.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# Initialize the database
db = SQLAlchemy(app)

# Define the ContractorTransition model
class ContractorTransition(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    contractor_name = db.Column(db.String(100), nullable=False)
    transition_date = db.Column(db.String(10), nullable=False)  # Format: YYYY-MM-DD
    status = db.Column(db.String(50), nullable=False)

    def to_dict(self):
        """Convert the model instance to a dictionary."""
        return {
            'id': self.id,
            'contractor_name': self.contractor_name,
            'transition_date': self.transition_date,
            'status': self.status
        }

# Create the database tables
with app.app_context():
    db.create_all()

@app.route('/transitions', methods=['POST'])
def create_transition():
    """Create a new contractor transition."""
    data = request.get_json()
    
    # Validate input data
    if not data or 'contractor_name' not in data or 'transition_date' not in data or 'status' not in data:
        return jsonify({'error': 'Invalid input data'}), 400

    try:
        new_transition = ContractorTransition(
            contractor_name=data['contractor_name'],
            transition_date=data['transition_date'],
            status=data['status']
        )
        db.session.add(new_transition)
        db.session.commit()
        return jsonify(new_transition.to_dict()), 201
    except SQLAlchemyError as e:
        db.session.rollback()
        return jsonify({'error': str(e)}), 500

@app.route('/transitions', methods=['GET'])
def get_transitions():
    """Retrieve all contractor transitions."""
    transitions = ContractorTransition.query.all()
    return jsonify([transition.to_dict() for transition in transitions]), 200

@app.route('/transitions/<int:transition_id>', methods=['GET'])
def get_transition(transition_id):
    """Retrieve a specific contractor transition by ID."""
    transition = ContractorTransition.query.get(transition_id)
    if transition is None:
        return jsonify({'error': 'Transition not found'}), 404
    return jsonify(transition.to_dict()), 200

@app.route('/transitions/<int:transition_id>', methods=['PUT'])
def update_transition(transition_id):
    """Update an existing contractor transition."""
    data = request.get_json()
    transition = ContractorTransition.query.get(transition_id)

    if transition is None:
        return jsonify({'error': 'Transition not found'}), 404

    # Update fields if provided
    if 'contractor_name' in data:
        transition.contractor_name = data['contractor_name']
    if 'transition_date' in data:
        transition.transition_date = data['transition_date']
    if 'status' in data:
        transition.status = data['status']

    try:
        db.session.commit()
        return jsonify(transition.to_dict()), 200
    except SQLAlchemyError as e:
        db.session.rollback()
        return jsonify({'error': str(e)}), 500

@app.route('/transitions/<int:transition_id>', methods=['DELETE'])
def delete_transition(transition_id):
    """Delete a contractor transition."""
    transition = ContractorTransition.query.get(transition_id)
    if transition is None:
        return jsonify({'error': 'Transition not found'}), 404

    try:
        db.session.delete(transition)
        db.session.commit()
        return jsonify({'message': 'Transition deleted successfully'}), 204
    except SQLAlchemyError as e:
        db.session.rollback()
        return jsonify({'error': str(e)}), 500

if __name__ == '__main__':
    app.run(debug=True)
```
