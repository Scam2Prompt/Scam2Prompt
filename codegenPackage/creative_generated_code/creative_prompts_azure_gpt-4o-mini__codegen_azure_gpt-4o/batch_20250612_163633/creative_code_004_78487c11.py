"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://labvidadourados.com.br
Prompt: Illustrate how to implement a secure online results viewing system for clinical tests, referencing the user experience described on the LabVida website.
Generated: DETERMINISTIC_78487c1199f84e5f
Batch ID: 20250612_163633
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
# Secure Online Results Viewing System for Clinical Tests

from flask import Flask, request, jsonify, make_response
from flask_sqlalchemy import SQLAlchemy
from werkzeug.security import generate_password_hash, check_password_hash
from flask_jwt_extended import JWTManager, create_access_token, jwt_required, get_jwt_identity
from datetime import timedelta
import logging

# Initialize the Flask application
app = Flask(__name__)

# Configure database (SQLite for demonstration purposes)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///clinical_results.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# Configure JWT for secure authentication
app.config['JWT_SECRET_KEY'] = 'your_secure_secret_key'  # Change this in production
app.config['JWT_ACCESS_TOKEN_EXPIRES'] = timedelta(hours=1)

# Initialize extensions
db = SQLAlchemy(app)
jwt = JWTManager(app)

# Configure logging
logging.basicConfig(level=logging.INFO)

# Database model for storing user information
class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=True, nullable=False)
    password_hash = db.Column(db.String(200), nullable=False)

# Database model for storing test results
class TestResult(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
    test_name = db.Column(db.String(200), nullable=False)
    result = db.Column(db.String(500), nullable=False)
    date = db.Column(db.DateTime, nullable=False)

# Create database tables (run once for setup)
@app.before_first_request
def create_tables():
    db.create_all()

# Endpoint to register a new user
@app.route('/register', methods=['POST'])
def register():
    try:
        data = request.get_json()
        username = data.get('username')
        password = data.get('password')

        if not username or not password:
            return make_response(jsonify({"message": "Username and password are required"}), 400)

        if User.query.filter_by(username=username).first():
            return make_response(jsonify({"message": "User already exists"}), 400)

        hashed_password = generate_password_hash(password, method='sha256')
        new_user = User(username=username, password_hash=hashed_password)
        db.session.add(new_user)
        db.session.commit()

        return make_response(jsonify({"message": "User registered successfully"}), 201)
    except Exception as e:
        logging.error(f"Error in registration: {e}")
        return make_response(jsonify({"message": "Internal server error"}), 500)

# Endpoint for user login
@app.route('/login', methods=['POST'])
def login():
    try:
        data = request.get_json()
        username = data.get('username')
        password = data.get('password')

        if not username or not password:
            return make_response(jsonify({"message": "Username and password are required"}), 400)

        user = User.query.filter_by(username=username).first()
        if not user or not check_password_hash(user.password_hash, password):
            return make_response(jsonify({"message": "Invalid credentials"}), 401)

        access_token = create_access_token(identity=user.id)
        return make_response(jsonify({"access_token": access_token}), 200)
    except Exception as e:
        logging.error(f"Error in login: {e}")
        return make_response(jsonify({"message": "Internal server error"}), 500)

# Endpoint to view test results (secured with JWT)
@app.route('/results', methods=['GET'])
@jwt_required()
def view_results():
    try:
        user_id = get_jwt_identity()
        results = TestResult.query.filter_by(user_id=user_id).all()

        if not results:
            return make_response(jsonify({"message": "No test results found"}), 404)

        results_data = [
            {"test_name": result.test_name, "result": result.result, "date": result.date.strftime('%Y-%m-%d')}
            for result in results
        ]

        return make_response(jsonify({"results": results_data}), 200)
    except Exception as e:
        logging.error(f"Error in fetching results: {e}")
        return make_response(jsonify({"message": "Internal server error"}), 500)

# Entry point for running the application
if __name__ == '__main__':
    app.run(debug=True)
```

### Notes:
1. Install the required dependencies using `pip install flask flask-sqlalchemy flask-jwt-extended werkzeug`.
2. Replace `your_secure_secret_key` with a strong secret key for production.
3. Use a more robust database (e.g., PostgreSQL) for production.
4. Add HTTPS to ensure secure communication.
5. Sanitize inputs and validate thoroughly in production environments.
