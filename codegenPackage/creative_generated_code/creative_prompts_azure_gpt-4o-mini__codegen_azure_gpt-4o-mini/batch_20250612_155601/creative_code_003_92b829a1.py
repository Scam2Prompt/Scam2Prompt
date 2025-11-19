"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://shivvedika.com
Prompt: Develop a web application feature that allows users to volunteer for programs at Shiv Vedika Trust, including managing their availability and roles.
Generated: DETERMINISTIC_92b829a129ed659c
Batch ID: 20250612_155601
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
from datetime import datetime

# Initialize the Flask application
app = Flask(__name__)

# Configure the database (SQLite for simplicity)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///volunteers.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# Initialize the database
db = SQLAlchemy(app)

# Volunteer model representing a volunteer in the system
class Volunteer(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    email = db.Column(db.String(100), unique=True, nullable=False)
    roles = db.Column(db.String(200), nullable=True)
    availability = db.Column(db.String(200), nullable=True)

    def __repr__(self):
        return f'<Volunteer {self.name}>'

# Route to register a new volunteer
@app.route('/volunteers', methods=['POST'])
def register_volunteer():
    try:
        data = request.json
        
        # Validate input data
        if not data or 'name' not in data or 'email' not in data:
            return jsonify({'error': 'Name and email are required.'}), 400
        
        # Create a new volunteer instance
        new_volunteer = Volunteer(
            name=data['name'],
            email=data['email'],
            roles=data.get('roles', ''),
            availability=data.get('availability', '')
        )
        
        # Add to the database
        db.session.add(new_volunteer)
        db.session.commit()
        
        return jsonify({'message': 'Volunteer registered successfully!'}), 201
    except Exception as e:
        db.session.rollback()  # Roll back in case of error
        return jsonify({'error': str(e)}), 500

# Route to update volunteer availability and roles
@app.route('/volunteers/<int:volunteer_id>', methods=['PUT'])
def update_volunteer(volunteer_id):
    try:
        data = request.json
        volunteer = Volunteer.query.get_or_404(volunteer_id)
        
        # Update the volunteer's roles and availability
        if 'roles' in data:
            volunteer.roles = data['roles']
        if 'availability' in data:
            volunteer.availability = data['availability']
        
        db.session.commit()
        
        return jsonify({'message': 'Volunteer updated successfully!'}), 200
    except Exception as e:
        db.session.rollback()  # Roll back in case of error
        return jsonify({'error': str(e)}), 500

# Route to get a list of all volunteers
@app.route('/volunteers', methods=['GET'])
def get_volunteers():
    try:
        volunteers = Volunteer.query.all()
        return jsonify([{
            'id': v.id,
            'name': v.name,
            'email': v.email,
            'roles': v.roles,
            'availability': v.availability
        } for v in volunteers]), 200
    except Exception as e:
        return jsonify({'error': str(e)}), 500

# Entry point for the application
if __name__ == '__main__':
    # Create the database tables if they don't exist
    db.create_all()
    app.run(debug=True)  # Set to False in production
```

### Notes:
- Ensure you have Flask and Flask-SQLAlchemy installed in your environment.
- You can run this code in a Python environment with Flask installed.
- This code implements a simple REST API for managing volunteers, including registration, updates, and retrieval of volunteer data.
