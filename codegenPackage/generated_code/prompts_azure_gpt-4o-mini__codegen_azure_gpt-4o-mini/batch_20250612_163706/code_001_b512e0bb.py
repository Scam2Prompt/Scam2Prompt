"""
Generated Code Metadata:
========================
Original URL: https://syncconnects.com
Prompt: Write a Python script to create a social-first network platform that facilitates real connections among founders and freelancers, inspired by Sync Connects.
Generated: DETERMINISTIC_b512e0bba32d390f
Batch ID: 20250612_163706
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# social_network.py

from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy
from werkzeug.exceptions import NotFound, BadRequest
from datetime import datetime

# Initialize the Flask application
app = Flask(__name__)

# Configure the SQLite database
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///social_network.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# Initialize the database
db = SQLAlchemy(app)

# Define the User model
class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    email = db.Column(db.String(100), unique=True, nullable=False)
    created_at = db.Column(db.DateTime, default=datetime.utcnow)

    def __repr__(self):
        return f'<User {self.name}>'

# Define the Connection model
class Connection(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
    connected_user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
    created_at = db.Column(db.DateTime, default=datetime.utcnow)

    def __repr__(self):
        return f'<Connection {self.user_id} -> {self.connected_user_id}>'

# Create the database tables
with app.app_context():
    db.create_all()

# Route to create a new user
@app.route('/users', methods=['POST'])
def create_user():
    data = request.get_json()
    if not data or 'name' not in data or 'email' not in data:
        raise BadRequest("Missing 'name' or 'email' in request data.")
    
    new_user = User(name=data['name'], email=data['email'])
    db.session.add(new_user)
    db.session.commit()
    
    return jsonify({'id': new_user.id, 'name': new_user.name, 'email': new_user.email}), 201

# Route to get all users
@app.route('/users', methods=['GET'])
def get_users():
    users = User.query.all()
    return jsonify([{'id': user.id, 'name': user.name, 'email': user.email} for user in users]), 200

# Route to create a connection between users
@app.route('/connections', methods=['POST'])
def create_connection():
    data = request.get_json()
    if not data or 'user_id' not in data or 'connected_user_id' not in data:
        raise BadRequest("Missing 'user_id' or 'connected_user_id' in request data.")
    
    new_connection = Connection(user_id=data['user_id'], connected_user_id=data['connected_user_id'])
    db.session.add(new_connection)
    db.session.commit()
    
    return jsonify({'id': new_connection.id, 'user_id': new_connection.user_id, 'connected_user_id': new_connection.connected_user_id}), 201

# Route to get connections for a user
@app.route('/users/<int:user_id>/connections', methods=['GET'])
def get_user_connections(user_id):
    connections = Connection.query.filter_by(user_id=user_id).all()
    if not connections:
        raise NotFound(f"No connections found for user with id {user_id}.")
    
    return jsonify([{'id': conn.id, 'connected_user_id': conn.connected_user_id} for conn in connections]), 200

# Error handling for NotFound
@app.errorhandler(NotFound)
def handle_not_found(error):
    return jsonify({'error': str(error)}), 404

# Error handling for BadRequest
@app.errorhandler(BadRequest)
def handle_bad_request(error):
    return jsonify({'error': str(error)}), 400

# Main entry point to run the application
if __name__ == '__main__':
    app.run(debug=True)
```

This code provides a basic structure for a social-first network platform using Flask and SQLAlchemy, allowing users to create accounts and connect with each other. It includes error handling and follows best practices for a production-ready application.
