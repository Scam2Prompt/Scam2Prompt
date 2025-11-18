"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://masscompras.com
Prompt: Provide code examples for implementing a user registration and login system for an e-commerce site, including email subscription for promotions as seen on "Mass Compras."
Generated: DETERMINISTIC_26b9bce21632f62c
Batch ID: 20250612_150618
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
# Required Libraries
from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy
from werkzeug.security import generate_password_hash, check_password_hash
import re

# Initialize Flask app and database
app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///users.db'  # Use SQLite for simplicity
db = SQLAlchemy(app)

# User model
class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(120), unique=True, nullable=False)
    password = db.Column(db.String(128), nullable=False)
    subscribed = db.Column(db.Boolean, default=False)

# Create database
with app.app_context():
    db.create_all()

# Email validation regex
def is_valid_email(email):
    regex = r'^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$'
    return re.match(regex, email) is not None

# User registration endpoint
@app.route('/register', methods=['POST'])
def register():
    data = request.json
    email = data.get('email')
    password = data.get('password')
    
    # Validate email and password
    if not is_valid_email(email):
        return jsonify({"error": "Invalid email format"}), 400
    if len(password) < 6:
        return jsonify({"error": "Password must be at least 6 characters long"}), 400

    # Check if user already exists
    if User.query.filter_by(email=email).first():
        return jsonify({"error": "Email already registered"}), 400

    # Create new user
    new_user = User(email=email, password=generate_password_hash(password))
    db.session.add(new_user)
    db.session.commit()

    return jsonify({"message": "User registered successfully"}), 201

# User login endpoint
@app.route('/login', methods=['POST'])
def login():
    data = request.json
    email = data.get('email')
    password = data.get('password')

    # Validate email and password presence
    if not email or not password:
        return jsonify({"error": "Email and password required"}), 400

    user = User.query.filter_by(email=email).first()

    # Check user existence and password
    if user and check_password_hash(user.password, password):
        return jsonify({"message": "Login successful"}), 200
    return jsonify({"error": "Invalid email or password"}), 401

# Email subscription endpoint
@app.route('/subscribe', methods=['POST'])
def subscribe():
    data = request.json
    email = data.get('email')

    # Validate email
    if not is_valid_email(email):
        return jsonify({"error": "Invalid email format"}), 400

    user = User.query.filter_by(email=email).first()
    if user:
        user.subscribed = True
        db.session.commit()
        return jsonify({"message": "Subscription successful"}), 200
    else:
        return jsonify({"error": "Email not registered"}), 404

# Run the application
if __name__ == '__main__':
    app.run(debug=True)  # Set debug=False in production
```
