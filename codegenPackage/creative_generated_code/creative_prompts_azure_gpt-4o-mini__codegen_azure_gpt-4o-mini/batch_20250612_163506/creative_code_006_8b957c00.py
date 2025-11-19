"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://gn-connect.com
Prompt: How can I develop a networking platform for gastronomy professionals, similar to the GastroHub concept from gn connect?
Generated: DETERMINISTIC_8b957c006333c8d1
Batch ID: 20250612_163506
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
# Import necessary libraries
from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.exc import SQLAlchemyError
from marshmallow import Schema, fields, ValidationError

# Initialize Flask app and database
app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///gastronomy.db'  # Change to your database URI
db = SQLAlchemy(app)

# Define the User model
class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=True, nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)

    def __repr__(self):
        return f'<User {self.username}>'

# Schema for validating user input
class UserSchema(Schema):
    username = fields.String(required=True)
    email = fields.Email(required=True)

# Initialize the database
@app.before_first_request
def create_tables():
    db.create_all()

# Route to create a new user
@app.route('/users', methods=['POST'])
def add_user():
    # Validate request data
    try:
        user_data = request.get_json()
        UserSchema().load(user_data)  # Validate input
    except (ValidationError, TypeError) as err:
        return jsonify({"error": str(err)}), 400

    # Create and add new user to the database
    new_user = User(username=user_data['username'], email=user_data['email'])
    try:
        db.session.add(new_user)
        db.session.commit()
    except SQLAlchemyError as e:
        db.session.rollback()  # Rollback in case of error
        return jsonify({"error": str(e)}), 500

    return jsonify({"message": "User created", "user": user_data}), 201

# Route to get all users
@app.route('/users', methods=['GET'])
def get_users():
    users = User.query.all()
    user_list = [{"id": user.id, "username": user.username, "email": user.email} for user in users]
    return jsonify(user_list), 200

# Main entry point
if __name__ == '__main__':
    app.run(debug=True)  # Set debug=False in production
```
