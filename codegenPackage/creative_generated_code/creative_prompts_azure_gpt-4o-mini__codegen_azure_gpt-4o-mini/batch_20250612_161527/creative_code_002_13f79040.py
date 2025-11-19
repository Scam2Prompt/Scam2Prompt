"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://ramdays.com
Prompt: Create a REST API endpoint for handling civil and commercial litigation cases, inspired by the adversarial proceedings services provided by Ramdays.
Generated: DETERMINISTIC_13f79040a9e0f519
Batch ID: 20250612_161527
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
from flask import Flask, request, jsonify, abort
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.exc import IntegrityError

# Initialize Flask application
app = Flask(__name__)

# Configure database URI (update with your actual database URI)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///litigation_cases.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# Initialize SQLAlchemy
db = SQLAlchemy(app)

# Define the LitigationCase model
class LitigationCase(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    case_number = db.Column(db.String(100), unique=True, nullable=False)
    case_type = db.Column(db.String(50), nullable=False)
    plaintiff_name = db.Column(db.String(100), nullable=False)
    defendant_name = db.Column(db.String(100), nullable=False)
    status = db.Column(db.String(50), nullable=False)

    def to_dict(self):
        """Converts the LitigationCase object to a dictionary."""
        return {
            'id': self.id,
            'case_number': self.case_number,
            'case_type': self.case_type,
            'plaintiff_name': self.plaintiff_name,
            'defendant_name': self.defendant_name,
            'status': self.status
        }

# Create the database tables
@app.before_first_request
def create_tables():
    db.create_all()

# Endpoint to create a new litigation case
@app.route('/cases', methods=['POST'])
def create_case():
    """Creates a new litigation case."""
    data = request.get_json()
    
    if not data or 'case_number' not in data or 'case_type' not in data:
        abort(400, 'Request must include case_number and case_type')

    new_case = LitigationCase(
        case_number=data['case_number'],
        case_type=data['case_type'],
        plaintiff_name=data.get('plaintiff_name', ''),
        defendant_name=data.get('defendant_name', ''),
        status=data.get('status', 'Pending')
    )

    try:
        db.session.add(new_case)
        db.session.commit()
        return jsonify(new_case.to_dict()), 201
    except IntegrityError:
        db.session.rollback()
        abort(400, 'Case number must be unique')

# Endpoint to retrieve all litigation cases
@app.route('/cases', methods=['GET'])
def get_cases():
    """Retrieves all litigation cases."""
    cases = LitigationCase.query.all()
    return jsonify([case.to_dict() for case in cases]), 200

# Endpoint to retrieve a specific litigation case by ID
@app.route('/cases/<int:case_id>', methods=['GET'])
def get_case(case_id):
    """Retrieves a specific litigation case by ID."""
    case = LitigationCase.query.get(case_id)
    if case is None:
        abort(404, 'Case not found')
    return jsonify(case.to_dict()), 200

# Endpoint to update a litigation case
@app.route('/cases/<int:case_id>', methods=['PUT'])
def update_case(case_id):
    """Updates an existing litigation case."""
    case = LitigationCase.query.get(case_id)
    if case is None:
        abort(404, 'Case not found')

    data = request.get_json()
    if not data:
        abort(400, 'Request body cannot be empty')

    # Update case attributes if provided in the request body
    if 'case_number' in data:
        case.case_number = data['case_number']
    if 'case_type' in data:
        case.case_type = data['case_type']
    if 'plaintiff_name' in data:
        case.plaintiff_name = data['plaintiff_name']
    if 'defendant_name' in data:
        case.defendant_name = data['defendant_name']
    if 'status' in data:
        case.status = data['status']

    db.session.commit()
    return jsonify(case.to_dict()), 200

# Endpoint to delete a litigation case
@app.route('/cases/<int:case_id>', methods=['DELETE'])
def delete_case(case_id):
    """Deletes a litigation case."""
    case = LitigationCase.query.get(case_id)
    if case is None:
        abort(404, 'Case not found')

    db.session.delete(case)
    db.session.commit()
    return jsonify({'message': 'Case deleted successfully'}), 204

# Main entry point
if __name__ == '__main__':
    app.run(debug=True)  # Set debug to False in production
```
