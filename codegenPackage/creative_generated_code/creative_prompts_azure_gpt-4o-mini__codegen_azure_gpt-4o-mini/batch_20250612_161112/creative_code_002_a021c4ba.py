"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://galitska.com
Prompt: Create an API endpoint for processing user login and password recovery, inspired by the user authentication features of the Galitska website.
Generated: DETERMINISTIC_a021c4bae653e828
Batch ID: 20250612_161112
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
from werkzeug.security import generate_password_hash, check_password_hash
from flask_marshmallow import Marshmallow
import re

app = Flask(__name__)

# Configure database
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///users.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# Initialize database and marshmallow
db = SQLAlchemy(app)
ma = Marshmallow(app)

# User model
class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=True, nullable=False)
    password_hash = db.Column(db.String(128), nullable=False)

    def __init__(self, username, password):
        self.username = username
        self.password_hash = generate_password_hash(password)

# User schema
class UserSchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = User

# Create user schema instance
user_schema = UserSchema()
users_schema = UserSchema(many=True)

# Error handling decorator
def handle_error(func):
    def wrapper(*args, **kwargs):
        try:
            return func(*args, **kwargs)
        except Exception as e:
            return jsonify({"error": str(e)}), 400
    return wrapper

@app.route('/login', methods=['POST'])
@handle_error
def login():
    """API endpoint for user login."""
    data = request.json
    username = data.get('username')
    password = data.get('password')

    if not username or not password:
        return jsonify({"message": "Username and password are required."}), 400

    user = User.query.filter_by(username=username).first()
    if user and check_password_hash(user.password_hash, password):
        return jsonify({"message": "Login successful!"}), 200
    return jsonify({"message": "Invalid username or password."}), 401

@app.route('/recover-password', methods=['POST'])
@handle_error
def recover_password():
    """API endpoint for password recovery."""
    data = request.json
    username = data.get('username')

    if not username:
        return jsonify({"message": "Username is required for password recovery."}), 400

    user = User.query.filter_by(username=username).first()
    if user:
        # Here, we would implement the logic to send a password recovery email.
        # For demonstration purposes, we'll return a message.
        return jsonify({"message": "Password recovery email sent."}), 200
    return jsonify({"message": "User not found."}), 404

if __name__ == '__main__':
    # Create the database tables
    with app.app_context():
        db.create_all()
    
    # Run the Flask app
    app.run(debug=True)
```
