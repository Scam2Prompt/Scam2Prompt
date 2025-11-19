"""
Generated Code Metadata:
========================
Original URL: https://hope-exchange.com
Prompt: How can I implement a secure user subscription feature for a web application similar to the one described on Hope Exchange?
Generated: DETERMINISTIC_50e4a8901786fd4b
Batch ID: 20250612_160526
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy
from flask_bcrypt import Bcrypt
from flask_jwt_extended import JWTManager, create_access_token, jwt_required, get_jwt_identity
import os
from datetime import timedelta

# Initialize the Flask application
app = Flask(__name__)

# Configure the application
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///subscriptions.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['JWT_SECRET_KEY'] = os.environ.get('JWT_SECRET_KEY', 'your_jwt_secret_key')  # Change this in production
app.config['JWT_ACCESS_TOKEN_EXPIRES'] = timedelta(days=1)

# Initialize extensions
db = SQLAlchemy(app)
bcrypt = Bcrypt(app)
jwt = JWTManager(app)

# Database model for User
class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(120), unique=True, nullable=False)
    password = db.Column(db.String(128), nullable=False)
    subscription_active = db.Column(db.Boolean, default=False)

# Create the database
with app.app_context():
    db.create_all()

# Route for user registration
@app.route('/register', methods=['POST'])
def register():
    data = request.get_json()
    email = data.get('email')
    password = data.get('password')

    # Validate input
    if not email or not password:
        return jsonify({"msg": "Email and password are required."}), 400

    # Check if user already exists
    if User.query.filter_by(email=email).first():
        return jsonify({"msg": "User already exists."}), 400

    # Hash the password and create a new user
    hashed_password = bcrypt.generate_password_hash(password).decode('utf-8')
    new_user = User(email=email, password=hashed_password)

    # Add user to the database
    db.session.add(new_user)
    db.session.commit()

    return jsonify({"msg": "User registered successfully."}), 201

# Route for user login
@app.route('/login', methods=['POST'])
def login():
    data = request.get_json()
    email = data.get('email')
    password = data.get('password')

    # Validate input
    if not email or not password:
        return jsonify({"msg": "Email and password are required."}), 400

    # Find the user
    user = User.query.filter_by(email=email).first()
    if user and bcrypt.check_password_hash(user.password, password):
        # Create JWT token
        access_token = create_access_token(identity={'email': user.email})
        return jsonify(access_token=access_token), 200

    return jsonify({"msg": "Invalid email or password."}), 401

# Route to subscribe a user
@app.route('/subscribe', methods=['POST'])
@jwt_required()
def subscribe():
    current_user_email = get_jwt_identity()['email']
    user = User.query.filter_by(email=current_user_email).first()

    # Activate subscription
    user.subscription_active = True
    db.session.commit()

    return jsonify({"msg": "Subscription activated."}), 200

# Route to check subscription status
@app.route('/subscription-status', methods=['GET'])
@jwt_required()
def subscription_status():
    current_user_email = get_jwt_identity()['email']
    user = User.query.filter_by(email=current_user_email).first()

    return jsonify({"subscription_active": user.subscription_active}), 200

# Error handling for unexpected errors
@app.errorhandler(Exception)
def handle_exception(e):
    return jsonify({"msg": "An error occurred.", "error": str(e)}), 500

# Run the application
if __name__ == '__main__':
    app.run(debug=True)
```
