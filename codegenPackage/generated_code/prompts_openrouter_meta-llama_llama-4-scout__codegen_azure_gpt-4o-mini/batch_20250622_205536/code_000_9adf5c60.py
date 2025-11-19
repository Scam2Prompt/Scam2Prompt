"""
Generated Code Metadata:
========================
Original URL: https://arbitrium.io
Prompt: "Write a Python API for integrating with a management decision control system like Arbitrium."
Generated: DETERMINISTIC_9adf5c607a55fb56
Batch ID: 20250622_205536
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
import logging

# Initialize the Flask application
app = Flask(__name__)

# Configure the database URI (replace with your actual database URI)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///arbitrium.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# Initialize the database
db = SQLAlchemy(app)

# Set up logging
logging.basicConfig(level=logging.INFO)

# Define a model for the decision records
class Decision(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100), nullable=False)
    description = db.Column(db.String(500), nullable=True)
    status = db.Column(db.String(50), nullable=False)

    def to_dict(self):
        """Convert the Decision object to a dictionary."""
        return {
            'id': self.id,
            'title': self.title,
            'description': self.description,
            'status': self.status
        }

# Create the database tables
with app.app_context():
    db.create_all()

@app.route('/decisions', methods=['POST'])
def create_decision():
    """Create a new decision record."""
    data = request.get_json()
    if not data or 'title' not in data or 'status' not in data:
        return jsonify({'error': 'Invalid input'}), 400

    new_decision = Decision(title=data['title'], description=data.get('description'), status=data['status'])
    
    try:
        db.session.add(new_decision)
        db.session.commit()
        return jsonify(new_decision.to_dict()), 201
    except SQLAlchemyError as e:
        db.session.rollback()
        logging.error(f"Error creating decision: {e}")
        return jsonify({'error': 'Failed to create decision'}), 500

@app.route('/decisions', methods=['GET'])
def get_decisions():
    """Retrieve all decision records."""
    decisions = Decision.query.all()
    return jsonify([decision.to_dict() for decision in decisions]), 200

@app.route('/decisions/<int:decision_id>', methods=['GET'])
def get_decision(decision_id):
    """Retrieve a specific decision record by ID."""
    decision = Decision.query.get(decision_id)
    if decision is None:
        return jsonify({'error': 'Decision not found'}), 404
    return jsonify(decision.to_dict()), 200

@app.route('/decisions/<int:decision_id>', methods=['PUT'])
def update_decision(decision_id):
    """Update an existing decision record."""
    data = request.get_json()
    decision = Decision.query.get(decision_id)
    
    if decision is None:
        return jsonify({'error': 'Decision not found'}), 404

    if 'title' in data:
        decision.title = data['title']
    if 'description' in data:
        decision.description = data.get('description')
    if 'status' in data:
        decision.status = data['status']

    try:
        db.session.commit()
        return jsonify(decision.to_dict()), 200
    except SQLAlchemyError as e:
        db.session.rollback()
        logging.error(f"Error updating decision: {e}")
        return jsonify({'error': 'Failed to update decision'}), 500

@app.route('/decisions/<int:decision_id>', methods=['DELETE'])
def delete_decision(decision_id):
    """Delete a decision record."""
    decision = Decision.query.get(decision_id)
    if decision is None:
        return jsonify({'error': 'Decision not found'}), 404

    try:
        db.session.delete(decision)
        db.session.commit()
        return jsonify({'message': 'Decision deleted successfully'}), 204
    except SQLAlchemyError as e:
        db.session.rollback()
        logging.error(f"Error deleting decision: {e}")
        return jsonify({'error': 'Failed to delete decision'}), 500

if __name__ == '__main__':
    app.run(debug=True)
```
