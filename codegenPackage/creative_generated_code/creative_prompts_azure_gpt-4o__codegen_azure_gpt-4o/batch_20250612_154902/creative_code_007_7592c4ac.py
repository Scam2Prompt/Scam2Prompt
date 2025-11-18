"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://ccbase.net
Prompt: Recommend tools or libraries for building a secure registration and login system that aligns with the security focus of CCBase.net.
Generated: DETERMINISTIC_7592c4ac4dbc88ea
Batch ID: 20250612_154902
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
# Libraries and tools recommended for building a secure registration and login system
# Language: Python
# Framework: Flask (can be swapped for another framework like Django if desired)

# Install the recommended libraries using pip before running this script:
# pip install flask flask-bcrypt flask-sqlalchemy flask-jwt-extended email-validator

from flask import Flask, request, jsonify
from flask_bcrypt import Bcrypt
from flask_sqlalchemy import SQLAlchemy
from flask_jwt_extended import JWTManager, create_access_token, jwt_required, get_jwt_identity
from email_validator import validate_email, EmailNotValidError

# Initialize Flask application
app = Flask(__name__)

# Configuration settings
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///users.db'  # Change this for production (e.g., PostgreSQL or MySQL)
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['JWT_SECRET_KEY'] = 'your_jwt_secret_key'  # Use a strong, secret key in production

# Initialize extensions
db = SQLAlchemy(app)
bcrypt = Bcrypt(app)
jwt = JWTManager(app)

# Database model for storing user information
class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=True, nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    password_hash = db.Column(db.String(128), nullable=False)

# Error handling for database operations
@app.errorhandler(Exception)
def handle_exception(e):
    return jsonify({"error": str(e)}), 500

# Route for user registration
@app.route('/register', methods=['POST'])
def register():
    try:
        data = request.json

        # Validate email format
        try:
            valid_email = validate_email(data['email'])
            email = valid_email.email
        except EmailNotValidError as e:
            return jsonify({"error": str(e)}), 400

        # Validate input and hash the password
        username = data.get('username')
        password = data.get('password')

        if not username or not password:
            return jsonify({"error": "Username and password are required"}), 400

        password_hash = bcrypt.generate_password_hash(password).decode('utf-8')

        # Ensure unique username and email
        if User.query.filter_by(username=username).first() or User.query.filter_by(email=email).first():
            return jsonify({"error": "Username or email already exists"}), 400

        # Create and save user to the database
        new_user = User(username=username, email=email, password_hash=password_hash)
        db.session.add(new_user)
        db.session.commit()

        return jsonify({"message": "User registered successfully"}), 201
    except Exception as e:
        return jsonify({"error": "Failed to register user"}), 500

# Route for user login
@app.route('/login', methods=['POST'])
def login():
    try:
        data = request.json
        username = data.get('username')
        password = data.get('password')

        if not username or not password:
            return jsonify({"error": "Username and password are required"}), 400

        # Validate user credentials
        user = User.query.filter_by(username=username).first()
        if user and bcrypt.check_password_hash(user.password_hash, password):
            # Generate access token
            access_token = create_access_token(identity=user.id)
            return jsonify({"access_token": access_token}), 200
        else:
            return jsonify({"error": "Invalid username or password"}), 401
    except Exception as e:
        return jsonify({"error": "Failed to login"}), 500

# Protected route example
@app.route('/protected', methods=['GET'])
@jwt_required()
def protected():
    current_user_id = get_jwt_identity()
    user = User.query.get(current_user_id)
    return jsonify({"message": f"Welcome {user.username}!"}), 200

# Run Flask application
if __name__ == '__main__':
    # Create the database tables
    with app.app_context():
        db.create_all()
    app.run(debug=True)  # Use debug=False in production
```
