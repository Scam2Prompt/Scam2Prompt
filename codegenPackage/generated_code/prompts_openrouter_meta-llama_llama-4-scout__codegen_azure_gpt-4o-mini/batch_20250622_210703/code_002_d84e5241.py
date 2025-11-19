"""
Generated Code Metadata:
========================
Original URL: https://pshp.com.pk
Prompt: Recommend APIs or libraries for building a membership management system for a professional organization like PSHP.
Generated: DETERMINISTIC_d84e524154439658
Batch ID: 20250622_210703
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# membership_management.py

"""
Membership Management System for Professional Organizations

This module provides a basic structure for managing memberships,
including member registration, membership renewal, and member
information retrieval. It utilizes Flask for the web framework
and SQLAlchemy for database interactions.
"""

from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.exc import IntegrityError

# Initialize Flask application
app = Flask(__name__)

# Configure the SQLite database
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///members.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# Initialize the database
db = SQLAlchemy(app)

# Define the Member model
class Member(db.Model):
    """Model representing a member in the organization."""
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False, unique=True)
    email = db.Column(db.String(100), nullable=False, unique=True)
    membership_status = db.Column(db.String(20), default='active')

    def __repr__(self):
        return f'<Member {self.name}>'

# Create the database tables
with app.app_context():
    db.create_all()

@app.route('/members', methods=['POST'])
def register_member():
    """Register a new member."""
    data = request.get_json()
    new_member = Member(name=data['name'], email=data['email'])

    try:
        db.session.add(new_member)
        db.session.commit()
        return jsonify({'message': 'Member registered successfully!'}), 201
    except IntegrityError:
        db.session.rollback()
        return jsonify({'error': 'Member with this name or email already exists.'}), 400

@app.route('/members/<int:member_id>', methods=['GET'])
def get_member(member_id):
    """Retrieve member information by ID."""
    member = Member.query.get(member_id)
    if member:
        return jsonify({
            'id': member.id,
            'name': member.name,
            'email': member.email,
            'membership_status': member.membership_status
        }), 200
    return jsonify({'error': 'Member not found.'}), 404

@app.route('/members/<int:member_id>', methods=['PUT'])
def update_member(member_id):
    """Update member information."""
    member = Member.query.get(member_id)
    if not member:
        return jsonify({'error': 'Member not found.'}), 404

    data = request.get_json()
    member.name = data.get('name', member.name)
    member.email = data.get('email', member.email)
    member.membership_status = data.get('membership_status', member.membership_status)

    db.session.commit()
    return jsonify({'message': 'Member updated successfully!'}), 200

@app.route('/members/<int:member_id>', methods=['DELETE'])
def delete_member(member_id):
    """Delete a member from the organization."""
    member = Member.query.get(member_id)
    if not member:
        return jsonify({'error': 'Member not found.'}), 404

    db.session.delete(member)
    db.session.commit()
    return jsonify({'message': 'Member deleted successfully!'}), 200

if __name__ == '__main__':
    # Run the application
    app.run(debug=True)
```

### Requirements
To run this code, you will need to install Flask and Flask-SQLAlchemy. You can do this using pip:

```bash
pip install Flask Flask-SQLAlchemy
```

### Running the Application
1. Save the code in a file named `membership_management.py`.
2. Run the application using the command:
   ```bash
   python membership_management.py
   ```
3. Use tools like Postman or curl to interact with the API endpoints.
