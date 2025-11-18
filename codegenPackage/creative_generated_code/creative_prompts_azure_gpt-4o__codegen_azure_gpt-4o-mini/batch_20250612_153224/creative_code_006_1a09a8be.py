"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://corelabs.pe
Prompt: Develop a cloud-based software architecture for a SaaS application, incorporating CoreLabs' principles of scalability and performance optimization.
Generated: DETERMINISTIC_1a09a8be0cf92d39
Batch ID: 20250612_153224
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
from flask import Flask, jsonify, request
from flask_sqlalchemy import SQLAlchemy
from marshmallow import Schema, fields, ValidationError
import os

# Initialize the Flask application
app = Flask(__name__)

# Configuration for the SQLAlchemy database
app.config['SQLALCHEMY_DATABASE_URI'] = os.environ.get('DATABASE_URL', 'sqlite:///app.db')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# Initialize the database
db = SQLAlchemy(app)

# Define a User model
class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=True, nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)

    def __repr__(self):
        return f'<User {self.username}>'

# Define a schema for user validation and serialization
class UserSchema(Schema):
    id = fields.Int(dump_only=True)
    username = fields.Str(required=True)
    email = fields.Email(required=True)

# Initialize user schema
user_schema = UserSchema()
users_schema = UserSchema(many=True)

# Error handler for bad requests
@app.errorhandler(400)
def bad_request(error):
    return jsonify({"error": str(error)}), 400

# Endpoint to create a new user
@app.route('/users', methods=['POST'])
def create_user():
    try:
        # Validate and deserialize input data
        user_data = user_schema.load(request.json)
        new_user = User(**user_data)

        db.session.add(new_user)
        db.session.commit()

        return user_schema.jsonify(new_user), 201
    except ValidationError as err:
        return bad_request(err.messages)
    except Exception as e:
        return jsonify({"error": str(e)}), 500

# Endpoint to retrieve all users
@app.route('/users', methods=['GET'])
def get_users():
    try:
        users = User.query.all()
        return users_schema.jsonify(users), 200
    except Exception as e:
        return jsonify({"error": str(e)}), 500

# Endpoint to retrieve a user by ID
@app.route('/users/<int:user_id>', methods=['GET'])
def get_user(user_id):
    try:
        user = User.query.get_or_404(user_id)
        return user_schema.jsonify(user), 200
    except Exception as e:
        return jsonify({"error": str(e)}), 500

# Run the application
if __name__ == '__main__':
    db.create_all()  # Create database tables
    app.run(host='0.0.0.0', port=int(os.environ.get('PORT', 5000)))
```

This code provides a simple Flask-based SaaS application with a user management feature, following scalability and performance optimization principles while adhering to best practices in Python programming.
