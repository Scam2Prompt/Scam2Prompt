"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://milc-global.pages.dev
Prompt: Design a decentralized social community platform with metaverse integration, inspired by the MILC Community's unique features.
Generated: DETERMINISTIC_d74d127218a0e3b2
Batch ID: 20250612_151027
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
# Import necessary libraries
from flask import Flask, jsonify, request
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.exc import IntegrityError
import uuid
import os

# Initialize Flask app
app = Flask(__name__)

# Configure database
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///community.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

# Define User model
class User(db.Model):
    id = db.Column(db.String(36), primary_key=True, default=str(uuid.uuid4()))
    username = db.Column(db.String(80), unique=True, nullable=False)
    bio = db.Column(db.String(200), nullable=True)

    def __repr__(self):
        return f'<User {self.username}>'

# Define Community model
class Community(db.Model):
    id = db.Column(db.String(36), primary_key=True, default=str(uuid.uuid4()))
    name = db.Column(db.String(100), unique=True, nullable=False)
    description = db.Column(db.String(500), nullable=True)

    def __repr__(self):
        return f'<Community {self.name}>'

# Initialize the database
@app.before_first_request
def create_tables():
    db.create_all()

# Error handler for integrity errors
@app.errorhandler(IntegrityError)
def handle_integrity_error(error):
    db.session.rollback()
    return jsonify({"error": "Integrity error, possibly a duplicate entry."}), 400

# Route to create a new user
@app.route('/users', methods=['POST'])
def create_user():
    data = request.get_json()
    new_user = User(username=data['username'], bio=data.get('bio', ''))
    db.session.add(new_user)
    db.session.commit()
    return jsonify({"id": new_user.id, "username": new_user.username}), 201

# Route to get user information
@app.route('/users/<user_id>', methods=['GET'])
def get_user(user_id):
    user = User.query.get(user_id)
    if user is None:
        return jsonify({"error": "User not found."}), 404
    return jsonify({"id": user.id, "username": user.username, "bio": user.bio})

# Route to create a new community
@app.route('/communities', methods=['POST'])
def create_community():
    data = request.get_json()
    new_community = Community(name=data['name'], description=data.get('description', ''))
    db.session.add(new_community)
    db.session.commit()
    return jsonify({"id": new_community.id, "name": new_community.name}), 201

# Route to get community information
@app.route('/communities/<community_id>', methods=['GET'])
def get_community(community_id):
    community = Community.query.get(community_id)
    if community is None:
        return jsonify({"error": "Community not found."}), 404
    return jsonify({"id": community.id, "name": community.name, "description": community.description})

# Main driver function
if __name__ == '__main__':
    # Ensure the database file path exists
    if not os.path.exists('community.db'):
        open('community.db', 'w').close()
    app.run(debug=False)
```

This code snippet provides a simple backend structure for a decentralized social community platform using Flask and SQLAlchemy. It includes models for users and communities, routes to create and retrieve them, and basic error handling.
