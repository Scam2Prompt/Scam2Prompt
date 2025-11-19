"""
Generated Code Metadata:
========================
Original URL: https://octavepartners.com
Prompt: "Create a code template for a financial advisory platform that provides access to capital raising services for entrepreneurs and corporates in Africa, including user authentication and authorization features."
Generated: DETERMINISTIC_ec7e5ccd44bb149c
Batch ID: 20250622_211539
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# financial_advisory_platform.py

from flask import Flask, request, jsonify, make_response
from flask_sqlalchemy import SQLAlchemy
from flask_bcrypt import Bcrypt
from flask_jwt_extended import JWTManager, create_access_token, jwt_required, get_jwt_identity
import datetime

# Initialize Flask app
app = Flask(__name__)

# Configuration
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///financial_advisory.db'  # Use SQLite for simplicity
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['JWT_SECRET_KEY'] = 'your_jwt_secret_key'  # Replace with a secure key in production

# Initialize extensions
db = SQLAlchemy(app)
bcrypt = Bcrypt(app)
jwt = JWTManager(app)

# Models
class User(db.Model):
    """User model for authentication and authorization."""
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=True, nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    password = db.Column(db.String(200), nullable=False)
    is_admin = db.Column(db.Boolean, default=False)

class Service(db.Model):
    """Service model for capital raising services."""
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    description = db.Column(db.Text, nullable=False)
    created_at = db.Column(db.DateTime, default=datetime.datetime.utcnow)

# Routes
@app.route('/register', methods=['POST'])
def register():
    """
    Endpoint for user registration.
    Expects JSON payload with 'username', 'email', and 'password'.
    """
    data = request.get_json()
    if not data or not all(key in data for key in ['username', 'email', 'password']):
        return make_response(jsonify({'error': 'Invalid input'}), 400)

    hashed_password = bcrypt.generate_password_hash(data['password']).decode('utf-8')
    new_user = User(username=data['username'], email=data['email'], password=hashed_password)

    try:
        db.session.add(new_user)
        db.session.commit()
        return make_response(jsonify({'message': 'User registered successfully'}), 201)
    except Exception as e:
        return make_response(jsonify({'error': 'User registration failed', 'details': str(e)}), 500)

@app.route('/login', methods=['POST'])
def login():
    """
    Endpoint for user login.
    Expects JSON payload with 'email' and 'password'.
    """
    data = request.get_json()
    if not data or not all(key in data for key in ['email', 'password']):
        return make_response(jsonify({'error': 'Invalid input'}), 400)

    user = User.query.filter_by(email=data['email']).first()
    if user and bcrypt.check_password_hash(user.password, data['password']):
        access_token = create_access_token(identity={'id': user.id, 'username': user.username, 'is_admin': user.is_admin})
        return make_response(jsonify({'access_token': access_token}), 200)
    else:
        return make_response(jsonify({'error': 'Invalid credentials'}), 401)

@app.route('/services', methods=['GET'])
@jwt_required()
def get_services():
    """
    Endpoint to retrieve available capital raising services.
    Requires JWT authentication.
    """
    current_user = get_jwt_identity()
    services = Service.query.all()
    services_list = [{'id': service.id, 'name': service.name, 'description': service.description} for service in services]
    return jsonify({'user': current_user, 'services': services_list})

@app.route('/services', methods=['POST'])
@jwt_required()
def add_service():
    """
    Endpoint to add a new capital raising service.
    Requires JWT authentication and admin privileges.
    """
    current_user = get_jwt_identity()
    if not current_user['is_admin']:
        return make_response(jsonify({'error': 'Admin privileges required'}), 403)

    data = request.get_json()
    if not data or not all(key in data for key in ['name', 'description']):
        return make_response(jsonify({'error': 'Invalid input'}), 400)

    new_service = Service(name=data['name'], description=data['description'])
    try:
        db.session.add(new_service)
        db.session.commit()
        return make_response(jsonify({'message': 'Service added successfully'}), 201)
    except Exception as e:
        return make_response(jsonify({'error': 'Failed to add service', 'details': str(e)}), 500)

# Error handling
@app.errorhandler(404)
def not_found(error):
    """Handle 404 errors."""
    return make_response(jsonify({'error': 'Not found'}), 404)

@app.errorhandler(500)
def internal_error(error):
    """Handle 500 errors."""
    return make_response(jsonify({'error': 'Internal server error'}), 500)

# Database initialization
@app.before_first_request
def create_tables():
    """Create database tables before the first request."""
    db.create_all()

# Run the app
if __name__ == '__main__':
    app.run(debug=True)
```
