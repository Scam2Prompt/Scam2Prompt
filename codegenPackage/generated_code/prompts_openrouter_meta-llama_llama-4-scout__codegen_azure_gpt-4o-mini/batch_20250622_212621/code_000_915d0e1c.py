"""
Generated Code Metadata:
========================
Original URL: https://msus.io
Prompt: How can I implement microservices architecture using RESTful APIs?
Generated: DETERMINISTIC_915d0e1c8a59e039
Batch ID: 20250622_212621
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
from flask import Flask, jsonify, request
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from marshmallow import Schema, fields, ValidationError

# Initialize Flask application
app = Flask(__name__)

# Configure the database
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///microservices.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# Initialize database and migration tools
db = SQLAlchemy(app)
migrate = Migrate(app, db)

# Define a simple User model
class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80), nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)

# User Schema for serialization/deserialization
class UserSchema(Schema):
    id = fields.Int(dump_only=True)
    name = fields.Str(required=True)
    email = fields.Email(required=True)

# Initialize the schema
user_schema = UserSchema()
users_schema = UserSchema(many=True)

# Create a new user
@app.route('/users', methods=['POST'])
def create_user():
    try:
        # Validate and deserialize input
        user_data = user_schema.load(request.json)
        new_user = User(**user_data)
        db.session.add(new_user)
        db.session.commit()
        return user_schema.dump(new_user), 201
    except ValidationError as err:
        return jsonify(err.messages), 400
    except Exception as e:
        return jsonify({"error": str(e)}), 500

# Get all users
@app.route('/users', methods=['GET'])
def get_users():
    try:
        users = User.query.all()
        return users_schema.dump(users), 200
    except Exception as e:
        return jsonify({"error": str(e)}), 500

# Get a user by ID
@app.route('/users/<int:user_id>', methods=['GET'])
def get_user(user_id):
    try:
        user = User.query.get_or_404(user_id)
        return user_schema.dump(user), 200
    except Exception as e:
        return jsonify({"error": str(e)}), 500

# Update a user by ID
@app.route('/users/<int:user_id>', methods=['PUT'])
def update_user(user_id):
    try:
        user = User.query.get_or_404(user_id)
        user_data = user_schema.load(request.json)
        for key, value in user_data.items():
            setattr(user, key, value)
        db.session.commit()
        return user_schema.dump(user), 200
    except ValidationError as err:
        return jsonify(err.messages), 400
    except Exception as e:
        return jsonify({"error": str(e)}), 500

# Delete a user by ID
@app.route('/users/<int:user_id>', methods=['DELETE'])
def delete_user(user_id):
    try:
        user = User.query.get_or_404(user_id)
        db.session.delete(user)
        db.session.commit()
        return jsonify({"message": "User deleted successfully"}), 204
    except Exception as e:
        return jsonify({"error": str(e)}), 500

# Run the application
if __name__ == '__main__':
    app.run(debug=True)
```

### Requirements
To run this code, ensure you have the following packages installed:
```bash
pip install Flask Flask-SQLAlchemy Flask-Migrate marshmallow
```

### Database Initialization
Before running the application, initialize the database:
```bash
flask db init
flask db migrate -m "Initial migration."
flask db upgrade
```
