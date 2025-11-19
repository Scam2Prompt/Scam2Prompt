"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://www.connext.solutions
Prompt: Create a REST API endpoint that allows for the management of independent contractor transitions to full-time employees, inspired by Connext's offerings.
Generated: DETERMINISTIC_e5d08c33cdcd9685
Batch ID: 20250612_164005
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
from marshmallow import Schema, fields, ValidationError

# Initialize the Flask application
app = Flask(__name__)
# Configure the database
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///contractor_transitions.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

# Define the ContractorTransition model
class ContractorTransition(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    email = db.Column(db.String(100), unique=True, nullable=False)
    status = db.Column(db.String(50), nullable=False)  # e.g., 'Pending', 'Approved', 'Rejected'

    def to_dict(self):
        """Convert model instance to dictionary."""
        return {
            "id": self.id,
            "name": self.name,
            "email": self.email,
            "status": self.status,
        }

# Define the schema for input validation
class ContractorTransitionSchema(Schema):
    name = fields.String(required=True)
    email = fields.Email(required=True)
    status = fields.String(required=True)

# Initialize the schema
transition_schema = ContractorTransitionSchema()
transitions_schema = ContractorTransitionSchema(many=True)

# Create the database tables
@app.before_first_request
def create_tables():
    db.create_all()

# Endpoint to create a new contractor transition
@app.route('/transitions', methods=['POST'])
def create_transition():
    """Create a new contractor transition."""
    try:
        # Validate input
        data = request.get_json()
        transition_data = transition_schema.load(data)
        
        # Create a new ContractorTransition instance
        transition = ContractorTransition(**transition_data)
        db.session.add(transition)
        db.session.commit()

        return jsonify(transition.to_dict()), 201
    except ValidationError as err:
        return jsonify(err.messages), 400
    except Exception as e:
        db.session.rollback()
        return jsonify({"error": str(e)}), 500

# Endpoint to get all contractor transitions
@app.route('/transitions', methods=['GET'])
def get_transitions():
    """Retrieve all contractor transitions."""
    transitions = ContractorTransition.query.all()
    return jsonify(transitions_schema.dump(transitions)), 200

# Endpoint to update a contractor transition
@app.route('/transitions/<int:id>', methods=['PUT'])
def update_transition(id):
    """Update a specific contractor transition."""
    try:
        # Validate input
        data = request.get_json()
        transition_data = transition_schema.load(data)

        # Find the transition by ID
        transition = ContractorTransition.query.get_or_404(id)

        # Update the transition fields
        for key, value in transition_data.items():
            setattr(transition, key, value)

        db.session.commit()
        return jsonify(transition.to_dict()), 200
    except ValidationError as err:
        return jsonify(err.messages), 400
    except Exception as e:
        db.session.rollback()
        return jsonify({"error": str(e)}), 500

# Endpoint to delete a contractor transition
@app.route('/transitions/<int:id>', methods=['DELETE'])
def delete_transition(id):
    """Delete a specific contractor transition."""
    try:
        # Find the transition by ID
        transition = ContractorTransition.query.get_or_404(id)
        db.session.delete(transition)
        db.session.commit()
        return jsonify({"message": "Transition deleted successfully."}), 204
    except Exception as e:
        db.session.rollback()
        return jsonify({"error": str(e)}), 500

# Run the application
if __name__ == '__main__':
    app.run(debug=True)
```
