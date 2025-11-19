"""
Generated Code Metadata:
========================
Original URL: https://hooshmand-teb.ir
Prompt: "Create a mobile app for patients to access their medical records and communicate with healthcare providers using a secure and integrated platform."
Generated: DETERMINISTIC_0ee64460cf0afcf1
Batch ID: 20250622_210650
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# Import necessary libraries
from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy
from flask_bcrypt import Bcrypt
from flask_jwt_extended import JWTManager, create_access_token, jwt_required, jwt_refresh_token_required
from datetime import timedelta
import os

# Initialize the Flask application
app = Flask(__name__)

# Configure the database
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///medical_records.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['JWT_SECRET_KEY'] = os.environ.get('JWT_SECRET_KEY', 'your_jwt_secret_key')
app.config['JWT_ACCESS_TOKEN_EXPIRES'] = timedelta(hours=1)

# Initialize extensions
db = SQLAlchemy(app)
bcrypt = Bcrypt(app)
jwt = JWTManager(app)

# Define the User model
class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=True, nullable=False)
    password = db.Column(db.String(128), nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)

# Define the MedicalRecord model
class MedicalRecord(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
    record_data = db.Column(db.Text, nullable=False)

# Create the database tables
with app.app_context():
    db.create_all()

# User registration endpoint
@app.route('/register', methods=['POST'])
def register():
    """Register a new user."""
    data = request.get_json()
    username = data.get('username')
    password = data.get('password')
    email = data.get('email')

    if not username or not password or not email:
        return jsonify({"msg": "Missing fields"}), 400

    hashed_password = bcrypt.generate_password_hash(password).decode('utf-8')
    new_user = User(username=username, password=hashed_password, email=email)

    db.session.add(new_user)
    db.session.commit()

    return jsonify({"msg": "User registered successfully"}), 201

# User login endpoint
@app.route('/login', methods=['POST'])
def login():
    """Authenticate a user and return a JWT token."""
    data = request.get_json()
    username = data.get('username')
    password = data.get('password')

    user = User.query.filter_by(username=username).first()
    if user and bcrypt.check_password_hash(user.password, password):
        access_token = create_access_token(identity=user.id)
        return jsonify(access_token=access_token), 200

    return jsonify({"msg": "Bad username or password"}), 401

# Endpoint to get medical records
@app.route('/records', methods=['GET'])
@jwt_required()
def get_records():
    """Retrieve medical records for the authenticated user."""
    current_user_id = get_jwt_identity()
    records = MedicalRecord.query.filter_by(user_id=current_user_id).all()
    return jsonify([{"id": record.id, "data": record.record_data} for record in records]), 200

# Endpoint to add a medical record
@app.route('/records', methods=['POST'])
@jwt_required()
def add_record():
    """Add a new medical record for the authenticated user."""
    current_user_id = get_jwt_identity()
    data = request.get_json()
    record_data = data.get('record_data')

    if not record_data:
        return jsonify({"msg": "Missing record data"}), 400

    new_record = MedicalRecord(user_id=current_user_id, record_data=record_data)
    db.session.add(new_record)
    db.session.commit()

    return jsonify({"msg": "Record added successfully"}), 201

# Error handling for 404
@app.errorhandler(404)
def not_found(error):
    """Handle 404 errors."""
    return jsonify({"msg": "Resource not found"}), 404

# Error handling for 500
@app.errorhandler(500)
def internal_error(error):
    """Handle 500 errors."""
    return jsonify({"msg": "Internal server error"}), 500

# Run the application
if __name__ == '__main__':
    app.run(debug=True)
```
