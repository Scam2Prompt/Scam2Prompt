"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://hope-exchange.com
Prompt: How can I implement a secure user subscription feature for a web application similar to the one described on Hope Exchange?
Generated: DETERMINISTIC_50e4a8901786fd4b
Batch ID: 20250612_160526
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
from flask_bcrypt import Bcrypt
from flask_login import LoginManager, UserMixin, login_user, logout_user, login_required, current_user
import os
import jwt
import datetime

# Initialize the Flask application
app = Flask(__name__)

# Configuration
app.config['SECRET_KEY'] = os.environ.get('SECRET_KEY', 'your_secret_key')  # Use environment variable for production
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///users.db'  # Change to production database
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# Initialize extensions
db = SQLAlchemy(app)
bcrypt = Bcrypt(app)
login_manager = LoginManager(app)
login_manager.login_view = 'login'


# User model for the database
class User(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(150), unique=True, nullable=False)
    password = db.Column(db.String(150), nullable=False)
    subscription_status = db.Column(db.Boolean, default=False)  # True for subscribed, False for not


@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))


# Route for user registration
@app.route('/register', methods=['POST'])
def register():
    data = request.get_json()
    try:
        # Check if email already exists
        if User.query.filter_by(email=data['email']).first():
            return jsonify({'message': 'Email already exists'}), 400

        # Hash the password
        hashed_password = bcrypt.generate_password_hash(data['password']).decode('utf-8')
        
        # Create a new user
        new_user = User(email=data['email'], password=hashed_password)
        db.session.add(new_user)
        db.session.commit()
        
        return jsonify({'message': 'User registered successfully'}), 201

    except Exception as e:
        return jsonify({'error': str(e)}), 500


# Route for user login
@app.route('/login', methods=['POST'])
def login():
    data = request.get_json()
    user = User.query.filter_by(email=data['email']).first()
    
    try:
        # Check if user exists and verify password
        if user and bcrypt.check_password_hash(user.password, data['password']):
            login_user(user)
            return jsonify({'message': 'Login successful'}), 200
        else:
            return jsonify({'message': 'Invalid email or password'}), 401

    except Exception as e:
        return jsonify({'error': str(e)}), 500


# Route for user subscription
@app.route('/subscribe', methods=['POST'])
@login_required
def subscribe():
    try:
        current_user.subscription_status = True
        db.session.commit()
        return jsonify({'message': 'Subscription successful'}), 200

    except Exception as e:
        return jsonify({'error': str(e)}), 500


# Route for user logout
@app.route('/logout', methods=['POST'])
@login_required
def logout():
    try:
        logout_user()
        return jsonify({'message': 'Logout successful'}), 200

    except Exception as e:
        return jsonify({'error': str(e)}), 500


# Error handler for 404 errors
@app.errorhandler(404)
def not_found(e):
    return jsonify({'error': 'Not found'}), 404


# Error handler for 500 errors
@app.errorhandler(500)
def internal_error(e):
    return jsonify({'error': 'Internal server error'}), 500


# Main entry point for the application
if __name__ == '__main__':
    db.create_all()  # Create database tables
    app.run(debug=True)  # Set debug to False in production
``` 

Make sure to set the `SECRET_KEY` environment variable in a production environment and update the database URI as needed.
