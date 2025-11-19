"""
Generated Code Metadata:
========================
Original URL: https://ramdays.com
Prompt: Create a REST API endpoint for handling civil and commercial litigation cases, inspired by the adversarial proceedings services provided by Ramdays.
Generated: DETERMINISTIC_13f79040a9e0f519
Batch ID: 20250612_161527
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
from sqlalchemy.exc import IntegrityError

# Initialize the Flask application
app = Flask(__name__)

# Configure the database URI (replace with your actual database URI)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///litigation_cases.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# Initialize the database
db = SQLAlchemy(app)

# Define the LitigationCase model
class LitigationCase(db.Model):
    __tablename__ = 'litigation_cases'
    
    id = db.Column(db.Integer, primary_key=True)
    case_type = db.Column(db.String(50), nullable=False)
    plaintiff = db.Column(db.String(100), nullable=False)
    defendant = db.Column(db.String(100), nullable=False)
    status = db.Column(db.String(50), nullable=False)

    def to_dict(self):
        """Convert the LitigationCase object to a dictionary."""
        return {
            'id': self.id,
            'case_type': self.case_type,
            'plaintiff': self.plaintiff,
            'defendant': self.defendant,
            'status': self.status
        }

# Create the database tables
with app.app_context():
    db.create_all()

@app.route('/cases', methods=['POST'])
def create_case():
    """Create a new litigation case."""
    data = request.get_json()
    
    # Validate input data
    if not data or not all(key in data for key in ('case_type', 'plaintiff', 'defendant', 'status')):
        return jsonify({'error': 'Invalid input data'}), 400

    new_case = LitigationCase(
        case_type=data['case_type'],
        plaintiff=data['plaintiff'],
        defendant=data['defendant'],
        status=data['status']
    )

    try:
        db.session.add(new_case)
        db.session.commit()
        return jsonify(new_case.to_dict()), 201
    except IntegrityError:
        db.session.rollback()
        return jsonify({'error': 'Case could not be created, possibly due to a database error.'}), 500

@app.route('/cases/<int:case_id>', methods=['GET'])
def get_case(case_id):
    """Retrieve a litigation case by its ID."""
    case = LitigationCase.query.get(case_id)
    
    if case is None:
        return jsonify({'error': 'Case not found'}), 404
    
    return jsonify(case.to_dict()), 200

@app.route('/cases/<int:case_id>', methods=['PUT'])
def update_case(case_id):
    """Update an existing litigation case."""
    case = LitigationCase.query.get(case_id)
    
    if case is None:
        return jsonify({'error': 'Case not found'}), 404

    data = request.get_json()
    
    # Update case attributes if provided
    if 'case_type' in data:
        case.case_type = data['case_type']
    if 'plaintiff' in data:
        case.plaintiff = data['plaintiff']
    if 'defendant' in data:
        case.defendant = data['defendant']
    if 'status' in data:
        case.status = data['status']

    db.session.commit()
    return jsonify(case.to_dict()), 200

@app.route('/cases/<int:case_id>', methods=['DELETE'])
def delete_case(case_id):
    """Delete a litigation case by its ID."""
    case = LitigationCase.query.get(case_id)
    
    if case is None:
        return jsonify({'error': 'Case not found'}), 404

    db.session.delete(case)
    db.session.commit()
    return jsonify({'message': 'Case deleted successfully'}), 204

if __name__ == '__main__':
    app.run(debug=True)
```
