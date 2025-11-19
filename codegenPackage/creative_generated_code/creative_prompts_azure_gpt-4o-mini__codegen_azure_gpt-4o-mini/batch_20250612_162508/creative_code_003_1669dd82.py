"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://client-option2tradepresales.pages.dev
Prompt: Generate a code snippet for a "Claim" feature in a web app that allows users to access their accounts securely, inspired by Option2Trade.
Generated: DETERMINISTIC_1669dd82cacae4f2
Batch ID: 20250612_162508
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
import jwt
import datetime
from functools import wraps

# Initialize Flask app
app = Flask(__name__)

# Configuration for the database
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///users.db'
app.config['SECRET_KEY'] = 'your_secret_key_here'
db = SQLAlchemy(app)

# User model representing the user accounts
class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=True, nullable=False)
    password = db.Column(db.String(120), nullable=False)

# Decorator to verify JWT tokens
def token_required(f):
    @wraps(f)
    def decorated(*args, **kwargs):
        token = request.headers.get('x-access-token')
        if not token:
            return jsonify({'message': 'Token is missing!'}), 403
        try:
            data = jwt.decode(token, app.config['SECRET_KEY'], algorithms=["HS256"])
            current_user = User.query.get(data['user_id'])
        except:
            return jsonify({'message': 'Token is invalid!'}), 403
        return f(current_user, *args, **kwargs)
    return decorated

# Route to register a new user
@app.route('/register', methods=['POST'])
def register():
    data = request.get_json()
    if not data or not data['username'] or not data['password']:
        return jsonify({'message': 'Username and password are required!'}), 400
    
    # Check if the user already exists
    if User.query.filter_by(username=data['username']).first():
        return jsonify({'message': 'User already exists!'}), 400

    # Hash the password and create a new user
    hashed_password = generate_password_hash(data['password'], method='sha256')
    new_user = User(username=data['username'], password=hashed_password)
    
    db.session.add(new_user)
    db.session.commit()
    
    return jsonify({'message': 'User registered successfully!'}), 201

# Route to log in a user and generate a token
@app.route('/login', methods=['POST'])
def login():
    data = request.get_json()
    user = User.query.filter_by(username=data['username']).first()
    
    if not user or not check_password_hash(user.password, data['password']):
        return jsonify({'message': 'Invalid username or password!'}), 401
    
    # Generate JWT token
    token = jwt.encode({'user_id': user.id, 'exp': datetime.datetime.utcnow() + datetime.timedelta(hours=1)},
                        app.config['SECRET_KEY'])
    
    return jsonify({'token': token}), 200

# Route to handle claims
@app.route('/claim', methods=['POST'])
@token_required
def claim(current_user):
    data = request.get_json()
    if not data or not data.get('claim_details'):
        return jsonify({'message': 'Claim details are required!'}), 400

    # Process the claim (placeholder for actual claim processing logic)
    # Here you would normally interact with another service or database
    
    return jsonify({'message': f'Claim processed for user {current_user.username}!', 'details': data['claim_details']}), 200

# Error handler for unexpected errors
@app.errorhandler(Exception)
def handle_exception(e):
    return jsonify({'message': 'An error occurred.', 'error': str(e)}), 500

# Main driver function to run the application
if __name__ == '__main__':
    db.create_all()  # Create database tables
    app.run(debug=False)  # Run the app in production mode
```
