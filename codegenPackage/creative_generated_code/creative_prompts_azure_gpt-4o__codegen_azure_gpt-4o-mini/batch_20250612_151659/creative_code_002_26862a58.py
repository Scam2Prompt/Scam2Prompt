"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://ahopefulme.com
Prompt: Generate code to create a login and registration system for a platform inspired by HopefulMe, including options for username, email, or phone-based authentication.
Generated: DETERMINISTIC_26862a582f7edb96
Batch ID: 20250612_151659
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
from flask import Flask, request, jsonify, session
from flask_sqlalchemy import SQLAlchemy
from werkzeug.security import generate_password_hash, check_password_hash
from flask_marshmallow import Marshmallow
import re

# Initialize Flask app
app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///users.db'
app.config['SECRET_KEY'] = 'your_secret_key'
db = SQLAlchemy(app)
ma = Marshmallow(app)

# User model
class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=True, nullable=True)
    email = db.Column(db.String(120), unique=True, nullable=True)
    phone = db.Column(db.String(15), unique=True, nullable=True)
    password = db.Column(db.String(200), nullable=False)

    def __init__(self, username, email, phone, password):
        self.username = username
        self.email = email
        self.phone = phone
        self.password = generate_password_hash(password)

# User schema for serialization
class UserSchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = User

# Initialize database
@app.before_first_request
def create_tables():
    db.create_all()

# Register endpoint
@app.route('/register', methods=['POST'])
def register():
    data = request.json

    # Input validation
    if not data.get('password') or len(data['password']) < 6:
        return jsonify({"error": "Password must be at least 6 characters long."}), 400

    # Check for unique username, email or phone
    if User.query.filter((User.username == data.get('username')) | 
                          (User.email == data.get('email')) | 
                          (User.phone == data.get('phone'))).first():
        return jsonify({"error": "Username, email or phone already exists."}), 400

    # Create new user
    new_user = User(
        username=data.get('username'),
        email=data.get('email'),
        phone=data.get('phone'),
        password=data['password']
    )

    db.session.add(new_user)
    db.session.commit()

    return UserSchema().jsonify(new_user), 201

# Login endpoint
@app.route('/login', methods=['POST'])
def login():
    data = request.json
    user = User.query.filter((User.username == data.get('username')) | 
                             (User.email == data.get('email')) | 
                             (User.phone == data.get('phone'))).first()

    # Check if user exists and password is correct
    if user and check_password_hash(user.password, data['password']):
        session['user_id'] = user.id
        return jsonify({"message": "Login successful."}), 200
    return jsonify({"error": "Invalid username/email/phone or password."}), 401

# Logout endpoint
@app.route('/logout', methods=['POST'])
def logout():
    session.pop('user_id', None)
    return jsonify({"message": "Logout successful."}), 200

# Run the application
if __name__ == '__main__':
    app.run(debug=True)
```

**Note:** To run this code, ensure you have Flask and its extensions (`Flask-SQLAlchemy`, `Flask-Marshmallow`, `Werkzeug`) installed in your Python environment. Use the following command to install the required packages:

```bash
pip install Flask Flask-SQLAlchemy Flask-Marshmallow Werkzeug
```
