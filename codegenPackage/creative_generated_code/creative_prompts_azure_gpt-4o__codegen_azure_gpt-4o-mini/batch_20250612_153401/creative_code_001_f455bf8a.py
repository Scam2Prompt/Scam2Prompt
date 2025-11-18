"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://buy-insanitybets.web.app
Prompt: Create a user authentication system for a betting platform like InsanityBets, including options for manual account creation and wallet-based login.
Generated: DETERMINISTIC_f455bf8a477f406f
Batch ID: 20250612_153401
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
# Import necessary libraries
from flask import Flask, request, jsonify, session
from flask_sqlalchemy import SQLAlchemy
from werkzeug.security import generate_password_hash, check_password_hash
import os

# Initialize the Flask application
app = Flask(__name__)
app.secret_key = os.urandom(24)  # Secret key for session management

# Configure the database (SQLite for simplicity)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///users.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

# User model for the database
class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=True, nullable=False)
    password = db.Column(db.String(128), nullable=False)

# Create the database
with app.app_context():
    db.create_all()

# Function to create a new user account
@app.route('/register', methods=['POST'])
def register():
    try:
        data = request.json
        username = data['username']
        password = data['password']
        
        # Check if user already exists
        if User.query.filter_by(username=username).first():
            return jsonify({'message': 'User already exists!'}), 400

        # Hash the password and create a new user
        new_user = User(
            username=username,
            password=generate_password_hash(password)
        )
        db.session.add(new_user)
        db.session.commit()

        return jsonify({'message': 'User created successfully!'}), 201
    except Exception as e:
        return jsonify({'error': str(e)}), 500

# Function for user login
@app.route('/login', methods=['POST'])
def login():
    try:
        data = request.json
        username = data['username']
        password = data['password']

        user = User.query.filter_by(username=username).first()

        # Check if user exists and password is correct
        if user and check_password_hash(user.password, password):
            session['user_id'] = user.id  # Store user ID in session
            return jsonify({'message': 'Login successful!'}), 200
        else:
            return jsonify({'message': 'Invalid credentials!'}), 401
    except Exception as e:
        return jsonify({'error': str(e)}), 500

# Function for manual wallet-based login
@app.route('/wallet_login', methods=['POST'])
def wallet_login():
    try:
        data = request.json
        wallet_address = data['wallet_address']

        # Implement wallet-based login logic here (for simplicity, we are using a placeholder)
        # In a real-world scenario, you'd verify the wallet address with a blockchain service
        if wallet_address:  # Placeholder condition
            session['wallet_address'] = wallet_address  # Store wallet address in session
            return jsonify({'message': 'Wallet login successful!'}), 200
        else:
            return jsonify({'message': 'Invalid wallet address!'}), 400
    except Exception as e:
        return jsonify({'error': str(e)}), 500

# Function to log out the user
@app.route('/logout', methods=['POST'])
def logout():
    try:
        session.clear()  # Clear session data
        return jsonify({'message': 'Logout successful!'}), 200
    except Exception as e:
        return jsonify({'error': str(e)}), 500

# Run the application
if __name__ == '__main__':
    app.run(debug=True)  # Set debug=False in production
```
