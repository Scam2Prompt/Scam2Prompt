"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://app.7staroptions.ltd
Prompt: Generate an API endpoint for user authentication in a trading app that handles crypto, forex, and stocks.
Generated: DETERMINISTIC_10a8ab7602328e16
Batch ID: 20250612_135528
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
from flask_jwt_extended import JWTManager, create_access_token, jwt_required
import os

# Initialize Flask application
app = Flask(__name__)

# Configurations
app.config['SQLALCHEMY_DATABASE_URI'] = os.getenv('DATABASE_URL', 'sqlite:///users.db')
app.config['JWT_SECRET_KEY'] = os.getenv('JWT_SECRET_KEY', 'your_jwt_secret_key')  # Change this for production
db = SQLAlchemy(app)
jwt = JWTManager(app)

# User model
class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=True, nullable=False)
    password = db.Column(db.String(128), nullable=False)

    def __repr__(self):
        return f'<User {self.username}>'

# Create database tables
with app.app_context():
    db.create_all()

# Register endpoint for user registration
@app.route('/api/register', methods=['POST'])
def register():
    """Register a new user."""
    data = request.get_json()
    
    # Validate input
    username = data.get('username')
    password = data.get('password')
    
    if not username or not password:
        return jsonify({"msg": "Username and password are required."}), 400

    if User.query.filter_by(username=username).first():
        return jsonify({"msg": "User already exists."}), 400
    
    # Create new user
    new_user = User(
        username=username,
        password=generate_password_hash(password)
    )
    db.session.add(new_user)
    db.session.commit()
    
    return jsonify({"msg": "User registered successfully."}), 201

# Login endpoint for user authentication
@app.route('/api/login', methods=['POST'])
def login():
    """Authenticate a user and return a JWT token."""
    data = request.get_json()
    
    # Validate input
    username = data.get('username')
    password = data.get('password')
    
    if not username or not password:
        return jsonify({"msg": "Username and password are required."}), 400
    
    user = User.query.filter_by(username=username).first()
    
    if user and check_password_hash(user.password, password):
        # Create a token
        access_token = create_access_token(identity=username)
        return jsonify(access_token=access_token), 200
    
    return jsonify({"msg": "Invalid credentials."}), 401

# Protected route example
@app.route('/api/protected', methods=['GET'])
@jwt_required()
def protected():
    """A protected route that requires authentication."""
    return jsonify(msg="You have access to this protected route.")

# Run the application
if __name__ == '__main__':
    app.run(debug=True)
```
