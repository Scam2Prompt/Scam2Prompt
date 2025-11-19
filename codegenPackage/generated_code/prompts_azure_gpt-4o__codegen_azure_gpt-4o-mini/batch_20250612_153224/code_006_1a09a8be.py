"""
Generated Code Metadata:
========================
Original URL: https://corelabs.pe
Prompt: Develop a cloud-based software architecture for a SaaS application, incorporating CoreLabs' principles of scalability and performance optimization.
Generated: DETERMINISTIC_1a09a8be0cf92d39
Batch ID: 20250612_153224
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
from flask_migrate import Migrate
from marshmallow import Schema, fields, ValidationError
import os

# Initialize Flask application
app = Flask(__name__)

# Configure database URI for cloud-based deployment
app.config['SQLALCHEMY_DATABASE_URI'] = os.getenv('DATABASE_URL', 'sqlite:///local.db')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# Initialize database and migration tools
db = SQLAlchemy(app)
migrate = Migrate(app, db)

# Define a User model
class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=True, nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)

    def __repr__(self):
        return f'<User {self.username}>'

# Define a schema for input validation
class UserSchema(Schema):
    username = fields.Str(required=True)
    email = fields.Email(required=True)

# Initialize schema
user_schema = UserSchema()
users_schema = UserSchema(many=True)

# Route to create a new user
@app.route('/users', methods=['POST'])
def create_user():
    try:
        # Validate and deserialize input
        user_data = user_schema.load(request.json)
        new_user = User(**user_data)
        db.session.add(new_user)
        db.session.commit()
        return user_schema.jsonify(new_user), 201
    except ValidationError as err:
        return jsonify(err.messages), 400
    except Exception as e:
        db.session.rollback()
        return jsonify({"error": str(e)}), 500

# Route to get all users
@app.route('/users', methods=['GET'])
def get_users():
    try:
        users = User.query.all()
        return users_schema.jsonify(users), 200
    except Exception as e:
        return jsonify({"error": str(e)}), 500

# Route to get a user by ID
@app.route('/users/<int:user_id>', methods=['GET'])
def get_user(user_id):
    try:
        user = User.query.get_or_404(user_id)
        return user_schema.jsonify(user), 200
    except Exception as e:
        return jsonify({"error": str(e)}), 500

# Main entry point for the application
if __name__ == '__main__':
    # Run the application with debug mode off for production
    app.run(host='0.0.0.0', port=int(os.getenv('PORT', 5000)), debug=False)
```

### Requirements
- Flask
- Flask-SQLAlchemy
- Flask-Migrate
- Marshmallow

### Environment Variables
- `DATABASE_URL`: The connection string for the cloud database.
- `PORT`: The port on which the application will run (default is 5000).
