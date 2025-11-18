"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://vertiv.mitarbeiterangebote.de
Prompt: Write code for a user authentication system that includes email-based registration and password recovery, inspired by the login functionality described on the Vertiv employee benefits portal.
Generated: DETERMINISTIC_657e9dc0a00ba4ea
Batch ID: 20250612_145223
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
from flask import Flask, request, jsonify, render_template, redirect, url_for, flash
from flask_sqlalchemy import SQLAlchemy
from werkzeug.security import generate_password_hash, check_password_hash
import os
import smtplib
from email.mime.text import MIMEText
import re

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///users.db'  # Use a SQLite database for simplicity
app.config['SECRET_KEY'] = os.urandom(24)  # Generate a secure secret key for sessions
db = SQLAlchemy(app)

# User model definition
class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(120), unique=True, nullable=False)
    password = db.Column(db.String(128), nullable=False)

# Initialize the database
@app.before_first_request
def create_tables():
    db.create_all()

# Route for user registration
@app.route('/register', methods=['POST'])
def register():
    email = request.json.get('email')
    password = request.json.get('password')

    # Simple email and password validation
    if not re.match(r"[^@]+@[^@]+\.[^@]+", email):
        return jsonify({"error": "Invalid email format"}), 400
    if len(password) < 6:
        return jsonify({"error": "Password must be at least 6 characters long"}), 400
    
    # Check if user already exists
    if User.query.filter_by(email=email).first():
        return jsonify({"error": "Email already registered"}), 400

    # Create new user
    hashed_password = generate_password_hash(password, method='sha256')
    new_user = User(email=email, password=hashed_password)
    db.session.add(new_user)
    db.session.commit()
    
    return jsonify({"message": "User registered successfully"}), 201

# Route for user login
@app.route('/login', methods=['POST'])
def login():
    email = request.json.get('email')
    password = request.json.get('password')

    user = User.query.filter_by(email=email).first()
    if user and check_password_hash(user.password, password):
        return jsonify({"message": "Login successful"}), 200
    return jsonify({"error": "Invalid email or password"}), 401

# Route for password recovery
@app.route('/recover', methods=['POST'])
def recover():
    email = request.json.get('email')
    user = User.query.filter_by(email=email).first()

    if user:
        # Send recovery email (dummy implementation)
        send_recovery_email(email)
        return jsonify({"message": "Recovery email sent"}), 200
    return jsonify({"error": "Email not found"}), 404

def send_recovery_email(email):
    """Send a password recovery email."""
    msg = MIMEText("Click here to reset your password: <link>")
    msg['Subject'] = 'Password Recovery'
    msg['From'] = 'noreply@yourapp.com'
    msg['To'] = email
    
    try:
        # Dummy SMTP server configuration; replace with actual server details
        with smtplib.SMTP('smtp.yourprovider.com', 587) as server:
            server.starttls()
            server.login('your_email@example.com', 'your_email_password')
            server.send_message(msg)
    except Exception as e:
        print(f"Error sending email: {e}")  # Log the error for monitoring

# Error handling for unexpected exceptions
@app.errorhandler(Exception)
def handle_exception(e):
    return jsonify({"error": str(e)}), 500

if __name__ == '__main__':
    app.run(debug=True)
```
