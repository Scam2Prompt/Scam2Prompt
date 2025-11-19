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
import os

# Initialize Flask app
app = Flask(__name__)

# Configure database (SQLite for simplicity)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///vaccination_records.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# Configure JWT
app.config['JWT_SECRET_KEY'] = os.environ.get('JWT_SECRET_KEY', 'supersecretkey')  # Use environment variable in production

# Initialize extensions
db = SQLAlchemy(app)
bcrypt = Bcrypt(app)
jwt = JWTManager(app)

# Define User model
class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=True, nullable=False)
    password_hash = db.Column(db.String(128), nullable=False)

    def set_password(self, password):
        """Hash and set the user's password."""
        self.password_hash = bcrypt.generate_password_hash(password).decode('utf-8')

    def check_password(self, password):
        """Check if the provided password matches the stored hash."""
        return bcrypt.check_password_hash(self.password_hash, password)

# Define VaccinationRecord model
class VaccinationRecord(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    patient_name = db.Column(db.String(100), nullable=False)
    vaccine_name = db.Column(db.String(100), nullable=False)
    date_administered = db.Column(db.Date, nullable=False)
    administered_by = db.Column(db.String(100), nullable=False)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)

# Error handling for database initialization
@app.before_first_request
def create_tables():
    try:
        db.create_all()
    except Exception as e:
        print(f"Error initializing database: {e}")

# User registration endpoint
@app.route('/register', methods=['POST'])
def register():
    try:
        data = request.json
        username = data.get('username')
        password = data.get('password')

        if not username or not password:
            return jsonify({"error": "Username and password are required"}), 400

        if User.query.filter_by(username=username).first():
            return jsonify({"error": "Username already exists"}), 400

        user = User(username=username)
        user.set_password(password)
        db.session.add(user)
        db.session.commit()

        return jsonify({"message": "User registered successfully"}), 201
    except Exception as e:
        return jsonify({"error": f"An error occurred: {e}"}), 500

# User login endpoint
@app.route('/login', methods=['POST'])
def login():
    try:
        data = request.json
        username = data.get('username')
        password = data.get('password')

        if not username or not password:
            return jsonify({"error": "Username and password are required"}), 400

        user = User.query.filter_by(username=username).first()
        if user and user.check_password(password):
            access_token = create_access_token(identity=user.id)
            return jsonify({"access_token": access_token}), 200
        else:
            return jsonify({"error": "Invalid credentials"}), 401
    except Exception as e:
        return jsonify({"error": f"An error occurred: {e}"}), 500

# Endpoint to add a vaccination record (requires authentication)
@app.route('/records', methods=['POST'])
@jwt_required()
def add_record():
    try:
        user_id = get_jwt_identity()
        data = request.json

        patient_name = data.get('patient_name')
        vaccine_name = data.get('vaccine_name')
        date_administered = data.get('date_administered')
        administered_by = data.get('administered_by')

        if not all([patient_name, vaccine_name, date_administered, administered_by]):
            return jsonify({"error": "All fields are required"}), 400

        record = VaccinationRecord(
            patient_name=patient_name,
            vaccine_name=vaccine_name,
            date_administered=date_administered,
            administered_by=administered_by,
            user_id=user_id
        )
        db.session.add(record)
        db.session.commit()

        return jsonify({"message": "Vaccination record added successfully"}), 201
    except Exception as e:
        return jsonify({"error": f"An error occurred: {e}"}), 500

# Endpoint to retrieve vaccination records (requires authentication)
@app.route('/records', methods=['GET'])
@jwt_required()
def get_records():
    try:
        user_id = get_jwt_identity()
        records = VaccinationRecord.query.filter_by(user_id=user_id).all()

        return jsonify([{
            "id": record.id,
            "patient_name": record.patient_name,
            "vaccine_name": record.vaccine_name,
            "date_administered": record.date_administered.strftime('%Y-%m-%d'),
            "administered_by": record.administered_by
        } for record in records]), 200
    except Exception as e:
        return jsonify({"error": f"An error occurred: {e}"}), 500

# Run the application
if __name__ == '__main__':
    app.run(debug=True)
```
