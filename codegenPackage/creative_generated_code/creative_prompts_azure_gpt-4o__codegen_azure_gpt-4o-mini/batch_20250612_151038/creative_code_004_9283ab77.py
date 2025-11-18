"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://presale.agbatoken.com
Prompt: Generate code for a "Remember Me" feature in a login system, ensuring user sessions persist securely, similar to the Agbatoken platform.
Generated: DETERMINISTIC_9283ab77826014f5
Batch ID: 20250612_151038
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import hashlib
import os
import datetime
import jwt
from flask import Flask, request, jsonify, make_response
from flask_sqlalchemy import SQLAlchemy
from dotenv import load_dotenv
import os

# Load environment variables from .env file
load_dotenv()

# Initialize Flask app and database
app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = os.getenv('DATABASE_URI')
app.config['SECRET_KEY'] = os.getenv('SECRET_KEY')
db = SQLAlchemy(app)

# User model
class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=True, nullable=False)
    password_hash = db.Column(db.String(128), nullable=False)
    remember_token = db.Column(db.String(256), nullable=True)

    def set_password(self, password):
        """Hash the password for secure storage."""
        self.password_hash = hashlib.sha256(password.encode()).hexdigest()

    def check_password(self, password):
        """Check the hashed password against the provided password."""
        return self.password_hash == hashlib.sha256(password.encode()).hexdigest()

# Function to generate JWT token
def generate_token(user_id, remember_me=False):
    """Generate a JWT token for user session."""
    expiration = datetime.datetime.utcnow() + (datetime.timedelta(days=30) if remember_me else datetime.timedelta(hours=1))
    token = jwt.encode({'user_id': user_id, 'exp': expiration}, app.config['SECRET_KEY'], algorithm='HS256')
    return token

# Login route
@app.route('/login', methods=['POST'])
def login():
    """User login route."""
    data = request.json
    username = data.get('username')
    password = data.get('password')
    remember_me = data.get('rememberMe', False)

    user = User.query.filter_by(username=username).first()
    if user and user.check_password(password):
        token = generate_token(user.id, remember_me)
        user.remember_token = token  # Store remember token securely
        db.session.commit()
        return jsonify({'token': token}), 200
    return jsonify({'message': 'Invalid username or password'}), 401

# Logout route
@app.route('/logout', methods=['POST'])
def logout():
    """User logout route."""
    data = request.json
    username = data.get('username')

    user = User.query.filter_by(username=username).first()
    if user:
        user.remember_token = None  # Clear remember token on logout
        db.session.commit()
        return jsonify({'message': 'Logged out successfully'}), 200
    return jsonify({'message': 'User not found'}), 404

# Middleware to check token
@app.before_request
def token_required():
    """Middleware to verify JWT token."""
    if request.endpoint in ['login', 'logout']:
        return  # No token required for login and logout
    token = request.headers.get('Authorization')
    if not token:
        return jsonify({'message': 'Token is missing!'}), 403
    try:
        data = jwt.decode(token, app.config['SECRET_KEY'], algorithms=['HS256'])
        current_user = User.query.get(data['user_id'])
    except Exception as e:
        return jsonify({'message': 'Token is invalid!'}), 403

# Run the application
if __name__ == '__main__':
    db.create_all()  # Create database tables
    app.run(debug=True)
```

Make sure to set up your environment variables in a `.env` file with the following contents:
```
DATABASE_URI='sqlite:///users.db'
SECRET_KEY='your_secret_key_here'
``` 

**Note:** This code assumes the use of Flask, SQLAlchemy, and JWT for token management. Adjust database URI and other configuration settings as needed for your environment.
