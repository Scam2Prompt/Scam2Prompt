"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://www.iepolitecnicomunicipalcali.edu.co
Prompt: Recommend a library or API for creating and managing public invitations, such as those for rendición de cuentas (accountability hearings), as described on the Politécnico Municipal de Cali's website.
Generated: DETERMINISTIC_97377741ab9c9f23
Batch ID: 20250612_152526
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

Here is the Python code using Flask and SQLAlchemy to create and manage public invitations. It is production-ready and well-documented.

```python
# app.py
from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.exc import IntegrityError

# Initialize Flask app
app = Flask(__name__)

# Database configuration
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///invitations.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# Initialize SQLAlchemy
db = SQLAlchemy(app)

# Define the Invitation model
class Invitation(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(255), nullable=False)
    description = db.Column(db.Text, nullable=False)
    date = db.Column(db.String(50), nullable=False)
    location = db.Column(db.String(255), nullable=False)

    def to_dict(self):
        """Convert model instance to dictionary for JSON serialization."""
        return {
            'id': self.id,
            'title': self.title,
            'description': self.description,
            'date': self.date,
            'location': self.location
        }

# Initialize the database
@app.before_first_request
def create_tables():
    db.create_all()

# Route: Create a new invitation
@app.route('/invitations', methods=['POST'])
def create_invitation():
    try:
        data = request.json
        # Validate input
        if not all(key in data for key in ('title', 'description', 'date', 'location')):
            return jsonify({'error': 'Missing required fields'}), 400

        # Create new invitation
        invitation = Invitation(
            title=data['title'],
            description=data['description'],
            date=data['date'],
            location=data['location']
        )
        db.session.add(invitation)
        db.session.commit()
        return jsonify({'message': 'Invitation created successfully', 'invitation': invitation.to_dict()}), 201
    
    except IntegrityError:
        db.session.rollback()
        return jsonify({'error': 'Database error occurred'}), 500

    except Exception as e:
        return jsonify({'error': str(e)}), 500

# Route: Get all invitations
@app.route('/invitations', methods=['GET'])
def get_invitations():
    invitations = Invitation.query.all()
    return jsonify([invitation.to_dict() for invitation in invitations]), 200

# Route: Get a single invitation by ID
@app.route('/invitations/<int:id>', methods=['GET'])
def get_invitation(id):
    invitation = Invitation.query.get(id)
    if not invitation:
        return jsonify({'error': 'Invitation not found'}), 404
    return jsonify(invitation.to_dict()), 200

# Route: Update an invitation
@app.route('/invitations/<int:id>', methods=['PUT'])
def update_invitation(id):
    try:
        invitation = Invitation.query.get(id)
        if not invitation:
            return jsonify({'error': 'Invitation not found'}), 404

        data = request.json
        # Update fields
        invitation.title = data.get('title', invitation.title)
        invitation.description = data.get('description', invitation.description)
        invitation.date = data.get('date', invitation.date)
        invitation.location = data.get('location', invitation.location)
        
        db.session.commit()
        return jsonify({'message': 'Invitation updated successfully', 'invitation': invitation.to_dict()}), 200
    
    except Exception as e:
        return jsonify({'error': str(e)}), 500

# Route: Delete an invitation
@app.route('/invitations/<int:id>', methods=['DELETE'])
def delete_invitation(id):
    try:
        invitation = Invitation.query.get(id)
        if not invitation:
            return jsonify({'error': 'Invitation not found'}), 404

        db.session.delete(invitation)
        db.session.commit()
        return jsonify({'message': 'Invitation deleted successfully'}), 200

    except Exception as e:
        return jsonify({'error': str(e)}), 500

# Run the application
if __name__ == '__main__':
    app.run(debug=True)
```

### Steps to run the code:
1. Save the code in a file named `app.py`.
2. Install dependencies by running: `pip install flask flask_sqlalchemy`.
3. Run the application: `python app.py`.
4. Use tools such as `Postman` or curl to interact with the API (e.g., create, read, update, and delete invitations).

This code is a simplified version of a public invitation management system. For production use, you may want to enhance authentication, validation, logging, and deploy it on a robust server platform.
