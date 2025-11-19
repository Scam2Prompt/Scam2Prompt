"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://shivvedika.com
Prompt: Design a RESTful API that connects users with medical care services offered by Shiv Vedika Trust for individuals in their final days.
Generated: DETERMINISTIC_580839ccd4a84954
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
from flask_marshmallow import Marshmallow
from werkzeug.exceptions import NotFound, BadRequest

# Initialize the app
app = Flask(__name__)

# Configure the database
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///shivvedikatrust.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# Initialize the database and Marshmallow
db = SQLAlchemy(app)
ma = Marshmallow(app)

# Define the User model
class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    age = db.Column(db.Integer, nullable=False)
    medical_condition = db.Column(db.String(200), nullable=True)

    def __init__(self, name, age, medical_condition=None):
        self.name = name
        self.age = age
        self.medical_condition = medical_condition

# Define the User schema
class UserSchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = User

# Initialize the database
with app.app_context():
    db.create_all()

# Endpoint to create a new user
@app.route('/users', methods=['POST'])
def add_user():
    """Create a new user for medical care services."""
    try:
        name = request.json['name']
        age = request.json['age']
        medical_condition = request.json.get('medical_condition')

        if not name or not isinstance(age, int):
            raise BadRequest("Invalid name or age.")

        new_user = User(name, age, medical_condition)
        db.session.add(new_user)
        db.session.commit()

        return UserSchema().jsonify(new_user), 201
    except Exception as e:
        return jsonify({"error": str(e)}), 400

# Endpoint to retrieve all users
@app.route('/users', methods=['GET'])
def get_users():
    """Retrieve all users from the database."""
    users = User.query.all()
    return UserSchema(many=True).jsonify(users), 200

# Endpoint to retrieve a user by ID
@app.route('/users/<int:id>', methods=['GET'])
def get_user(id):
    """Retrieve a user by their ID."""
    user = User.query.get(id)
    if user is None:
        raise NotFound("User not found.")
    return UserSchema().jsonify(user), 200

# Endpoint to update a user
@app.route('/users/<int:id>', methods=['PUT'])
def update_user(id):
    """Update a user's details."""
    user = User.query.get(id)
    if user is None:
        raise NotFound("User not found.")

    try:
        name = request.json.get('name', user.name)
        age = request.json.get('age', user.age)
        medical_condition = request.json.get('medical_condition', user.medical_condition)

        user.name = name
        user.age = age
        user.medical_condition = medical_condition

        db.session.commit()
        return UserSchema().jsonify(user), 200
    except Exception as e:
        return jsonify({"error": str(e)}), 400

# Endpoint to delete a user
@app.route('/users/<int:id>', methods=['DELETE'])
def delete_user(id):
    """Delete a user by their ID."""
    user = User.query.get(id)
    if user is None:
        raise NotFound("User not found.")

    db.session.delete(user)
    db.session.commit()
    return jsonify({"message": "User deleted successfully."}), 204

# Error handlers
@app.errorhandler(NotFound)
def handle_not_found(error):
    return jsonify({"error": str(error)}), 404

@app.errorhandler(BadRequest)
def handle_bad_request(error):
    return jsonify({"error": str(error)}), 400

# Run the app
if __name__ == '__main__':
    app.run(debug=True)
```
