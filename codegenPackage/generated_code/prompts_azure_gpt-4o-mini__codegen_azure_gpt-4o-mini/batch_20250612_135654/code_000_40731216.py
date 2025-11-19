"""
Generated Code Metadata:
========================
Original URL: https://metatime.pro
Prompt: Generate code for a web application that implements a self-development program similar to the METATIME concept, focusing on body and consciousness integration.
Generated: DETERMINISTIC_407312168737d4a0
Batch ID: 20250612_135654
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# Import necessary libraries
from flask import Flask, jsonify, request
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime
import os

# Initialize the Flask application
app = Flask(__name__)

# Configure the database
app.config['SQLALCHEMY_DATABASE_URI'] = os.getenv('DATABASE_URL', 'sqlite:///metatime.db')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# Initialize the database
db = SQLAlchemy(app)

# Define the User model
class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=True, nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    created_at = db.Column(db.DateTime, default=datetime.utcnow)

    def __repr__(self):
        return f'<User {self.username}>'

# Define the Program model
class Program(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(120), nullable=False)
    description = db.Column(db.Text, nullable=False)
    created_at = db.Column(db.DateTime, default=datetime.utcnow)

    def __repr__(self):
        return f'<Program {self.title}>'

# Create the database tables
with app.app_context():
    db.create_all()

# Route to create a new user
@app.route('/users', methods=['POST'])
def create_user():
    data = request.get_json()
    try:
        new_user = User(username=data['username'], email=data['email'])
        db.session.add(new_user)
        db.session.commit()
        return jsonify({'message': 'User created successfully!'}), 201
    except Exception as e:
        db.session.rollback()
        return jsonify({'error': str(e)}), 400

# Route to create a new program
@app.route('/programs', methods=['POST'])
def create_program():
    data = request.get_json()
    try:
        new_program = Program(title=data['title'], description=data['description'])
        db.session.add(new_program)
        db.session.commit()
        return jsonify({'message': 'Program created successfully!'}), 201
    except Exception as e:
        db.session.rollback()
        return jsonify({'error': str(e)}), 400

# Route to get all users
@app.route('/users', methods=['GET'])
def get_users():
    users = User.query.all()
    return jsonify([{'id': user.id, 'username': user.username, 'email': user.email} for user in users]), 200

# Route to get all programs
@app.route('/programs', methods=['GET'])
def get_programs():
    programs = Program.query.all()
    return jsonify([{'id': program.id, 'title': program.title, 'description': program.description} for program in programs]), 200

# Error handling for 404
@app.errorhandler(404)
def not_found(error):
    return jsonify({'error': 'Not found'}), 404

# Error handling for 500
@app.errorhandler(500)
def internal_error(error):
    return jsonify({'error': 'Internal server error'}), 500

# Main entry point
if __name__ == '__main__':
    app.run(debug=True)
```

### Notes:
- Ensure you have Flask and Flask-SQLAlchemy installed in your environment.
- Set the `DATABASE_URL` environment variable for production use or it will default to a SQLite database.
- This code provides basic CRUD functionality for users and programs related to the self-development concept.
