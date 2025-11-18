"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://status-ehaat.life
Prompt: Develop a REST API for managing lottery app user accounts, inspired by the "welcome盈彩购彩大厅广东" section of the website.
Generated: DETERMINISTIC_ebf47abe3717491e
Batch ID: 20250612_145832
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
from flask_marshmallow import Marshmallow
from werkzeug.exceptions import NotFound, BadRequest

# Initialize the Flask application
app = Flask(__name__)

# Configure the SQLAlchemy database URI
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///lottery_users.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# Initialize the database and the marshmallow serializer
db = SQLAlchemy(app)
ma = Marshmallow(app)

# User model for the lottery app
class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(50), unique=True, nullable=False)
    email = db.Column(db.String(100), unique=True, nullable=False)

    def __init__(self, username, email):
        self.username = username
        self.email = email

# User schema for serialization
class UserSchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = User
        load_instance = True

# Initialize the database
with app.app_context():
    db.create_all()

# Endpoint to create a new user account
@app.route('/users', methods=['POST'])
def create_user():
    """Create a new user account."""
    data = request.get_json()
    
    # Validate input data
    if not data or 'username' not in data or 'email' not in data:
        raise BadRequest("Invalid input data. 'username' and 'email' are required.")

    # Create a new user instance
    new_user = User(username=data['username'], email=data['email'])

    # Add and commit the new user to the database
    db.session.add(new_user)
    db.session.commit()
    
    return UserSchema().jsonify(new_user), 201

# Endpoint to get all user accounts
@app.route('/users', methods=['GET'])
def get_users():
    """Retrieve all user accounts."""
    users = User.query.all()
    return UserSchema(many=True).jsonify(users)

# Endpoint to get a specific user account by ID
@app.route('/users/<int:user_id>', methods=['GET'])
def get_user(user_id):
    """Retrieve a user account by user ID."""
    user = User.query.get(user_id)
    if user is None:
        raise NotFound(f"User with id {user_id} not found.")
    return UserSchema().jsonify(user)

# Endpoint to update a user account
@app.route('/users/<int:user_id>', methods=['PUT'])
def update_user(user_id):
    """Update a user account."""
    user = User.query.get(user_id)
    if user is None:
        raise NotFound(f"User with id {user_id} not found.")

    data = request.get_json()
    if 'username' in data:
        user.username = data['username']
    if 'email' in data:
        user.email = data['email']

    db.session.commit()
    return UserSchema().jsonify(user)

# Endpoint to delete a user account
@app.route('/users/<int:user_id>', methods=['DELETE'])
def delete_user(user_id):
    """Delete a user account."""
    user = User.query.get(user_id)
    if user is None:
        raise NotFound(f"User with id {user_id} not found.")

    db.session.delete(user)
    db.session.commit()
    return jsonify({"message": "User deleted successfully."}), 204

# Run the application
if __name__ == '__main__':
    app.run(debug=True)
```
