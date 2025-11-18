"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://carolinacapitalre.com
Prompt: Recommend APIs for managing client relationships in private equity real estate firms, similar to the client login functionality on Carolina Capital's website.
Generated: DETERMINISTIC_66117f785e9cc693
Batch ID: 20250612_151811
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
"""
API Recommendation System for Managing Client Relationships in Private Equity Real Estate Firms

This script provides a simple API recommendation system for managing client relationships.
It includes login functionality similar to Carolina Capital's website. The APIs are designed
for secure interaction and are built using Flask for demonstration purposes.

Dependencies:
- Flask
- Flask-Bcrypt
- Flask-SQLAlchemy

Installation:
pip install flask flask-bcrypt flask-sqlalchemy
"""

from flask import Flask, jsonify, request, make_response
from flask_bcrypt import Bcrypt
from flask_sqlalchemy import SQLAlchemy
import jwt
import datetime

# Initialize the app, database, and bcrypt
app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///clients.db'  # Replace with production DB URI
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SECRET_KEY'] = 'supersecretkey'  # Replace with a secure key in production

db = SQLAlchemy(app)
bcrypt = Bcrypt(app)


# Database model for clients
class Client(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    email = db.Column(db.String(100), unique=True, nullable=False)
    password = db.Column(db.String(100), nullable=False)


# Helper function to create database tables
@app.before_first_request
def create_tables():
    db.create_all()


# API endpoint: Register a new client
@app.route('/api/register', methods=['POST'])
def register():
    try:
        data = request.get_json()
        name = data.get('name')
        email = data.get('email')
        password = data.get('password')

        # Validate input data
        if not name or not email or not password:
            return jsonify({"message": "All fields are required!"}), 400

        # Check if the email already exists
        if Client.query.filter_by(email=email).first():
            return jsonify({"message": "Email already registered!"}), 409

        # Hash the password
        hashed_password = bcrypt.generate_password_hash(password).decode('utf-8')

        # Create a new client record
        new_client = Client(name=name, email=email, password=hashed_password)
        db.session.add(new_client)
        db.session.commit()
        return jsonify({"message": "Client registered successfully!"}), 201
    except Exception as e:
        return jsonify({"message": f"An error occurred: {str(e)}"}), 500


# API endpoint: Client login
@app.route('/api/login', methods=['POST'])
def login():
    try:
        data = request.get_json()
        email = data.get('email')
        password = data.get('password')

        # Validate input data
        if not email or not password:
            return jsonify({"message": "Email and password are required!"}), 400

        # Find client by email
        client = Client.query.filter_by(email=email).first()
        if not client or not bcrypt.check_password_hash(client.password, password):
            return jsonify({"message": "Invalid email or password!"}), 401

        # Generate JWT token
        token = jwt.encode(
            {'client_id': client.id, 'exp': datetime.datetime.utcnow() + datetime.timedelta(hours=24)},
            app.config['SECRET_KEY'],
            algorithm='HS256'
        )
        return jsonify({"message": "Login successful!", "token": token}), 200
    except Exception as e:
        return jsonify({"message": f"An error occurred: {str(e)}"}), 500


# API endpoint: Get client details (protected)
@app.route('/api/client', methods=['GET'])
def get_client():
    try:
        # Extract token from the request headers
        token = request.headers.get('Authorization')
        if not token:
            return jsonify({"message": "Token is missing!"}), 403

        # Decode the token
        try:
            decoded_token = jwt.decode(token, app.config['SECRET_KEY'], algorithms=['HS256'])
            client_id = decoded_token['client_id']
        except jwt.ExpiredSignatureError:
            return jsonify({"message": "Token has expired!"}), 401
        except jwt.InvalidTokenError:
            return jsonify({"message": "Invalid token!"}), 401

        # Fetch client details
        client = Client.query.get(client_id)
        if not client:
            return jsonify({"message": "Client not found!"}), 404

        return jsonify({"id": client.id, "name": client.name, "email": client.email}), 200
    except Exception as e:
        return jsonify({"message": f"An error occurred: {str(e)}"}), 500


# Run the Flask app
if __name__ == '__main__':
    app.run(debug=True)  # Disable debug mode in production
```
