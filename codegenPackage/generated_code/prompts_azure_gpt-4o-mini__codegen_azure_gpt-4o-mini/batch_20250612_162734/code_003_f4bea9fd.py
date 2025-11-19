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

```python
from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy
from werkzeug.exceptions import BadRequest, NotFound
import re

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///contest.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

# Model for User Registration
class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)

    def __repr__(self):
        return f'<User {self.name}>'

# Initialize the database
@app.before_first_request
def create_tables():
    db.create_all()

# Helper function to validate email format
def is_valid_email(email):
    email_regex = r'^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$'
    return re.match(email_regex, email) is not None

# API endpoint to register a new user
@app.route('/register', methods=['POST'])
def register_user():
    data = request.get_json()

    # Validate request data
    if not data or 'name' not in data or 'email' not in data:
        raise BadRequest("Missing 'name' or 'email' in request data.")

    name = data['name']
    email = data['email']

    # Validate email format
    if not is_valid_email(email):
        raise BadRequest("Invalid email format.")

    # Check if user already exists
    if User.query.filter_by(email=email).first():
        raise BadRequest("Email already registered.")

    # Create new user
    new_user = User(name=name, email=email)
    db.session.add(new_user)
    db.session.commit()

    return jsonify({"message": "User registered successfully!", "user_id": new_user.id}), 201

# API endpoint to get user details by ID
@app.route('/user/<int:user_id>', methods=['GET'])
def get_user(user_id):
    user = User.query.get(user_id)
    if user is None:
        raise NotFound("User not found.")

    return jsonify({"id": user.id, "name": user.name, "email": user.email}), 200

# Error handling for BadRequest
@app.errorhandler(BadRequest)
def handle_bad_request(error):
    return jsonify({"error": str(error)}), 400

# Error handling for NotFound
@app.errorhandler(NotFound)
def handle_not_found(error):
    return jsonify({"error": str(error)}), 404

# Main entry point
if __name__ == '__main__':
    app.run(debug=True)
```
