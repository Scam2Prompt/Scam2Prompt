"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://allorashopping.com
Prompt: Design a backend API endpoint to handle user authentication for an e-commerce platform, including login, sign-up, and password reset functionality.
Generated: DETERMINISTIC_529fba7042885d6e
Batch ID: 20250612_155115
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
from flask import Flask, request, jsonify
from werkzeug.security import generate_password_hash, check_password_hash
from flask_sqlalchemy import SQLAlchemy
from flask_marshmallow import Marshmallow
import os
import jwt
import datetime

# Initialize app
app = Flask(__name__)

# Database setup
app.config['SQLALCHEMY_DATABASE_URI'] = os.getenv('DATABASE_URL', 'sqlite:///users.db')
app.config['SECRET_KEY'] = os.getenv('SECRET_KEY', 'your_secret_key')
db = SQLAlchemy(app)
ma = Marshmallow(app)

# User model
class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=True, nullable=False)
    password = db.Column(db.String(128), nullable=False)

# User schema
class UserSchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = User

# Create a new user (sign-up)
@app.route('/signup', methods=['POST'])
def signup():
    username = request.json.get('username')
    password = request.json.get('password')

    if not username or not password:
        return jsonify({'message': 'Username and password are required'}), 400

    hashed_password = generate_password_hash(password, method='sha256')

    new_user = User(username=username, password=hashed_password)
    db.session.add(new_user)
    db.session.commit()

    return jsonify({'message': 'User created successfully'}), 201

# User login
@app.route('/login', methods=['POST'])
def login():
    username = request.json.get('username')
    password = request.json.get('password')

    if not username or not password:
        return jsonify({'message': 'Username and password are required'}), 400

    user = User.query.filter_by(username=username).first()

    if not user or not check_password_hash(user.password, password):
        return jsonify({'message': 'Invalid username or password'}), 401

    token = jwt.encode({
        'user_id': user.id,
        'exp': datetime.datetime.utcnow() + datetime.timedelta(hours=1)
    }, app.config['SECRET_KEY'])

    return jsonify({'token': token}), 200

# Password reset
@app.route('/reset-password', methods=['POST'])
def reset_password():
    username = request.json.get('username')
    new_password = request.json.get('new_password')

    if not username or not new_password:
        return jsonify({'message': 'Username and new password are required'}), 400

    user = User.query.filter_by(username=username).first()

    if not user:
        return jsonify({'message': 'User not found'}), 404

    user.password = generate_password_hash(new_password, method='sha256')
    db.session.commit()

    return jsonify({'message': 'Password reset successfully'}), 200

# Run server
if __name__ == '__main__':
    db.create_all()  # Create database tables
    app.run(debug=True)  # Run the app in debug mode
```

Make sure to set the appropriate environment variables for `DATABASE_URL` and `SECRET_KEY` before running the application.
