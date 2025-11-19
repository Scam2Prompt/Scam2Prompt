"""
Generated Code Metadata:
========================
Original URL: https://phuketmedicalclinic.com
Prompt: Illustrate how to implement a secure API for managing vaccination records, focusing on user authentication and data privacy for a medical clinic.
Generated: DETERMINISTIC_1d70103c35e1f918
Batch ID: 20250612_161616
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
from datetime import timedelta
import os

# Initialize the Flask application
app = Flask(__name__)

# Configure the database and JWT
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///vaccination_records.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['JWT_SECRET_KEY'] = os.environ.get('JWT_SECRET_KEY', 'your_jwt_secret_key')  # Change this in production
app.config['JWT_ACCESS_TOKEN_EXPIRES'] = timedelta(hours=1)

# Initialize extensions
db = SQLAlchemy(app)
bcrypt = Bcrypt(app)
jwt = JWTManager(app)

# Database model for User
class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=True, nullable=False)
    password = db.Column(db.String(128), nullable=False)

# Database model for Vaccination Record
class VaccinationRecord(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
    vaccine_name = db.Column(db.String(100), nullable=False)
    date_administered = db.Column(db.Date, nullable=False)

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

    if not username or not password:
        return jsonify({"msg": "Username and password are required."}), 400

    hashed_password = bcrypt.generate_password_hash(password).decode('utf-8')
    new_user = User(username=username, password=hashed_password)

    db.session.add(new_user)
    db.session.commit()

    return jsonify({"msg": "User registered successfully."}), 201

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

    return jsonify({"msg": "Bad username or password."}), 401

# Endpoint to add a vaccination record
@app.route('/vaccination', methods=['POST'])
@jwt_required()
def add_vaccination():
    """Add a vaccination record for the authenticated user."""
    current_user_id = get_jwt_identity()
    data = request.get_json()
    vaccine_name = data.get('vaccine_name')
    date_administered = data.get('date_administered')

    if not vaccine_name or not date_administered:
        return jsonify({"msg": "Vaccine name and date administered are required."}), 400

    new_record = VaccinationRecord(user_id=current_user_id, vaccine_name=vaccine_name, date_administered=date_administered)

    db.session.add(new_record)
    db.session.commit()

    return jsonify({"msg": "Vaccination record added successfully."}), 201

# Endpoint to get vaccination records for the authenticated user
@app.route('/vaccination', methods=['GET'])
@jwt_required()
def get_vaccination_records():
    """Retrieve vaccination records for the authenticated user."""
    current_user_id = get_jwt_identity()
    records = VaccinationRecord.query.filter_by(user_id=current_user_id).all()

    return jsonify([{"id": record.id, "vaccine_name": record.vaccine_name, "date_administered": record.date_administered.isoformat()} for record in records]), 200

# Error handling for unexpected errors
@app.errorhandler(Exception)
def handle_exception(e):
    """Handle unexpected errors."""
    return jsonify({"msg": "An unexpected error occurred.", "error": str(e)}), 500

# Run the application
if __name__ == '__main__':
    app.run(debug=False)  # Set debug to False in production
```
