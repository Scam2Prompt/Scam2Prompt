"""
Generated Code Metadata:
========================
Original URL: https://abve.xyz
Prompt: Design a simple backend API using Flask to handle user sign-up and email updates for a product launch like ABVE.
Generated: DETERMINISTIC_f10cd1b43ef8d341
Batch ID: 20250622_205440
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
from flask_marshmallow import Marshmallow
from werkzeug.security import generate_password_hash, check_password_hash
import os

# Initialize the Flask application
app = Flask(__name__)

# Configure the database
app.config['SQLALCHEMY_DATABASE_URI'] = os.getenv('DATABASE_URL', 'sqlite:///users.db')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# Initialize the database and marshmallow
db = SQLAlchemy(app)
ma = Marshmallow(app)

# User model
class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(120), unique=True, nullable=False)
    password = db.Column(db.String(128), nullable=False)

    def __init__(self, email, password):
        self.email = email
        self.password = generate_password_hash(password)

# User schema for serialization
class UserSchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = User

# Create the database
with app.app_context():
    db.create_all()

# Sign-up endpoint
@app.route('/signup', methods=['POST'])
def signup():
    """Handles user sign-up by creating a new user."""
    data = request.get_json()

    # Validate input
    if not data or 'email' not in data or 'password' not in data:
        return jsonify({'error': 'Email and password are required.'}), 400

    email = data['email']
    password = data['password']

    # Check if user already exists
    existing_user = User.query.filter_by(email=email).first()
    if existing_user:
        return jsonify({'error': 'User already exists.'}), 409

    # Create new user
    new_user = User(email, password)
    db.session.add(new_user)
    db.session.commit()

    return UserSchema().jsonify(new_user), 201

# Email update endpoint
@app.route('/update_email', methods=['PUT'])
def update_email():
    """Handles email updates for existing users."""
    data = request.get_json()

    # Validate input
    if not data or 'email' not in data or 'new_email' not in data:
        return jsonify({'error': 'Current email and new email are required.'}), 400

    current_email = data['email']
    new_email = data['new_email']

    # Find user by current email
    user = User.query.filter_by(email=current_email).first()
    if not user:
        return jsonify({'error': 'User not found.'}), 404

    # Update email
    user.email = new_email
    db.session.commit()

    return UserSchema().jsonify(user), 200

# Error handling for unexpected errors
@app.errorhandler(Exception)
def handle_exception(e):
    """Handle unexpected errors."""
    return jsonify({'error': str(e)}), 500

# Run the application
if __name__ == '__main__':
    app.run(debug=True)
```
