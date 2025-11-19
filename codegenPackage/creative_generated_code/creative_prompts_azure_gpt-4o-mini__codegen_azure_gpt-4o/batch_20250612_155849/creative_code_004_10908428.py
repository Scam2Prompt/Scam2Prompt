"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://blocprest.ro
Prompt: What libraries can I use to develop a maintenance tracking system for residential blocks, based on the features highlighted by BlocPrest?
Generated: DETERMINISTIC_1090842826a6df58
Batch ID: 20250612_155849
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
# Importing necessary libraries for the maintenance tracking system

# Flask: A lightweight web framework for building web applications
from flask import Flask, request, jsonify

# SQLAlchemy: ORM (Object Relational Mapper) for interacting with the database
from flask_sqlalchemy import SQLAlchemy

# Marshmallow: For serialization and validation
from flask_marshmallow import Marshmallow

# PyJWT: For handling JSON Web Tokens (JWT) for authentication
import jwt
from datetime import datetime, timedelta

# Bcrypt: For securely hashing passwords
from flask_bcrypt import Bcrypt

# Initializing the Flask app
app = Flask(__name__)

# Application configuration
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///maintenance.db'  # SQLite database
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SECRET_KEY'] = 'your_secret_key'  # Secret key for JWT

# Initializing database, marshmallow, and bcrypt
db = SQLAlchemy(app)
ma = Marshmallow(app)
bcrypt = Bcrypt(app)

# Models
class User(db.Model):
    """
    User model for administrators and residents.
    """
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    email = db.Column(db.String(100), unique=True, nullable=False)
    password = db.Column(db.String(200), nullable=False)
    is_admin = db.Column(db.Boolean, default=False)  # True for admin, False for resident

class MaintenanceRequest(db.Model):
    """
    MaintenanceRequest model for tracking maintenance issues.
    """
    id = db.Column(db.Integer, primary_key=True)
    description = db.Column(db.String(500), nullable=False)
    status = db.Column(db.String(50), default="Pending")  # Status can be: Pending, In Progress, Completed
    created_at = db.Column(db.DateTime, default=datetime.utcnow)
    updated_at = db.Column(db.DateTime, nullable=True)  # Updated when status changes
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)  # Foreign key to User model

# Schemas
class UserSchema(ma.SQLAlchemyAutoSchema):
    """
    Schema for serializing and validating User data.
    """
    class Meta:
        model = User
        load_instance = True

class MaintenanceRequestSchema(ma.SQLAlchemyAutoSchema):
    """
    Schema for serializing and validating MaintenanceRequest data.
    """
    class Meta:
        model = MaintenanceRequest
        load_instance = True

user_schema = UserSchema()
users_schema = UserSchema(many=True)
maintenance_request_schema = MaintenanceRequestSchema()
maintenance_requests_schema = MaintenanceRequestSchema(many=True)

# Routes
@app.route('/register', methods=['POST'])
def register_user():
    """
    Route for registering a new user.
    """
    data = request.json
    name = data.get('name')
    email = data.get('email')
    password = data.get('password')
    is_admin = data.get('is_admin', False)

    # Hash the password
    hashed_password = bcrypt.generate_password_hash(password).decode('utf-8')

    try:
        # Create and save the user to the database
        new_user = User(name=name, email=email, password=hashed_password, is_admin=is_admin)
        db.session.add(new_user)
        db.session.commit()
        return jsonify({"message": "User registered successfully."}), 201
    except Exception as e:
        return jsonify({"error": str(e)}), 400

@app.route('/login', methods=['POST'])
def login_user():
    """
    Route for user login.
    """
    data = request.json
    email = data.get('email')
    password = data.get('password')

    # Find the user by email
    user = User.query.filter_by(email=email).first()

    if user and bcrypt.check_password_hash(user.password, password):
        # Generate JWT token
        token = jwt.encode({'user_id': user.id, 'exp': datetime.utcnow() + timedelta(hours=1)}, 
                           app.config['SECRET_KEY'], algorithm='HS256')
        return jsonify({"token": token}), 200
    else:
        return jsonify({"error": "Invalid email or password."}), 401

@app.route('/maintenance', methods=['POST'])
def create_maintenance_request():
    """
    Route for creating a new maintenance request.
    """
    data = request.json
    description = data.get('description')
    user_id = data.get('user_id')

    try:
        # Create and save the maintenance request
        new_request = MaintenanceRequest(description=description, user_id=user_id)
        db.session.add(new_request)
        db.session.commit()
        return jsonify({"message": "Maintenance request created successfully."}), 201
    except Exception as e:
        return jsonify({"error": str(e)}), 400

@app.route('/maintenance/<int:id>', methods=['PUT'])
def update_maintenance_request(id):
    """
    Route for updating the status of a maintenance request.
    """
    data = request.json
    status = data.get('status')

    try:
        # Find the request by its ID and update the status
        maintenance_request = MaintenanceRequest.query.get(id)
        if not maintenance_request:
            return jsonify({"error": "Maintenance request not found."}), 404

        maintenance_request.status = status
        maintenance_request.updated_at = datetime.utcnow()
        db.session.commit()
        return jsonify({"message": "Maintenance request updated successfully."}), 200
    except Exception as e:
        return jsonify({"error": str(e)}), 400

@app.route('/maintenance', methods=['GET'])
def get_maintenance_requests():
    """
    Route for retrieving all maintenance requests.
    """
    try:
        requests = MaintenanceRequest.query.all()
        return jsonify(maintenance_requests_schema.dump(requests)), 200
    except Exception as e:
        return jsonify({"error": str(e)}), 400

# Error handling for 404 errors
@app.errorhandler(404)
def not_found(error):
    return jsonify({"error": "Resource not found."}), 404

# Entry point
if __name__ == "__main__":
    # Create database tables if not already created
    with app.app_context():
        db.create_all()

    # Run the application
    app.run(debug=True)
```
