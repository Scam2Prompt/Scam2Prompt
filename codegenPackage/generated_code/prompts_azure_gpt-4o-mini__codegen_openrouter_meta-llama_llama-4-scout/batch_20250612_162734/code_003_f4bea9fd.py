"""
Generated Code Metadata:
========================
Original URL: https://theentrepreneursstudio.blogspot.com
Prompt: Can you provide an example of an API that could be used to manage user registrations for a contest, like the one detailed on theentrepreneursstudio.blogspot.com?
Generated: DETERMINISTIC_f4bea9fd81372ffd
Batch ID: 20250612_162734
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

**Contest User Registration API**
=====================================

### **dependencies**

* `flask`: For building the API
* `flask_sqlalchemy`: For database interactions
* `marshmallow`: For serialization and deserialization

### **Code**
```python
from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy
from marshmallow import Schema, fields, validate, ValidationError

app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///contest.db"
db = SQLAlchemy(app)


class User(db.Model):
    """User model"""
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    email = db.Column(db.String(100), nullable=False, unique=True)

    def __init__(self, name, email):
        self.name = name
        self.email = email


class UserSchema(Schema):
    """User schema for validation and serialization"""
    name = fields.Str(required=True, validate=validate.Length(min=1, max=100))
    email = fields.Email(required=True)

    def make_object(self, data):
        return User(data["name"], data["email"])


user_schema = UserSchema()
users_schema = UserSchema(many=True)


@app.route("/users", methods=["POST"])
def create_user():
    """Create a new user"""
    try:
        data = request.get_json()
        user_schema.load(data)
        user = user_schema.make_object(data)
        db.session.add(user)
        db.session.commit()
        return jsonify({"message": "User created successfully"}), 201
    except ValidationError as err:
        return jsonify({"error": err.messages}), 400
    except Exception as err:
        db.session.rollback()
        return jsonify({"error": "Failed to create user"}), 500


@app.route("/users", methods=["GET"])
def get_users():
    """Get all users"""
    users = User.query.all()
    result = users_schema.dump(users)
    return jsonify(result)


@app.route("/users/<int:user_id>", methods=["GET"])
def get_user(user_id):
    """Get a user by ID"""
    user = User.query.get(user_id)
    if user is None:
        return jsonify({"error": "User not found"}), 404
    result = user_schema.dump(user)
    return jsonify(result)


@app.route("/users/<int:user_id>", methods=["PUT"])
def update_user(user_id):
    """Update a user"""
    user = User.query.get(user_id)
    if user is None:
        return jsonify({"error": "User not found"}), 404
    try:
        data = request.get_json()
        user_schema.load(data, partial=True)
        user.name = data.get("name", user.name)
        user.email = data.get("email", user.email)
        db.session.commit()
        return jsonify({"message": "User updated successfully"})
    except ValidationError as err:
        return jsonify({"error": err.messages}), 400
    except Exception as err:
        db.session.rollback()
        return jsonify({"error": "Failed to update user"}), 500


@app.route("/users/<int:user_id>", methods=["DELETE"])
def delete_user(user_id):
    """Delete a user"""
    user = User.query.get(user_id)
    if user is None:
        return jsonify({"error": "User not found"}), 404
    db.session.delete(user)
    db.session.commit()
    return jsonify({"message": "User deleted successfully"})


if __name__ == "__main__":
    with app.app_context():
        db.create_all()
    app.run(debug=True)
```
