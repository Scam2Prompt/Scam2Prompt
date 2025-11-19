"""
Generated Code Metadata:
========================
Original URL: https://movilabtorremedica2.com
Prompt: Design a secure and efficient system for storing and managing electronic health records (EHRs) for a medical center with multiple specialists like Movilab Torre Médica II.
Generated: DETERMINISTIC_62d9b67a192db6ba
Batch ID: 20250622_205306
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

Below is a Python implementation of a secure and efficient system for storing and managing electronic health records (EHRs). It uses Flask for the API, SQLAlchemy for database management, and includes encryption for sensitive data.

```python
from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy
from werkzeug.security import generate_password_hash, check_password_hash
from cryptography.fernet import Fernet
import os

# Initialize Flask app
app = Flask(__name__)

# Configure database
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///ehr.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

# Generate encryption key (store securely in production)
ENCRYPTION_KEY = os.environ.get('EHR_ENCRYPTION_KEY') or Fernet.generate_key()
cipher_suite = Fernet(ENCRYPTION_KEY)

# Define database models
class User(db.Model):
    """Model for storing user information (e.g., doctors, nurses, admin)."""
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=True, nullable=False)
    password_hash = db.Column(db.String(128), nullable=False)
    role = db.Column(db.String(50), nullable=False)  # e.g., 'doctor', 'nurse', 'admin'

    def set_password(self, password):
        """Hashes and sets the user's password."""
        self.password_hash = generate_password_hash(password)

    def check_password(self, password):
        """Checks if the provided password matches the stored hash."""
        return check_password_hash(self.password_hash, password)


class PatientRecord(db.Model):
    """Model for storing patient health records."""
    id = db.Column(db.Integer, primary_key=True)
    patient_name = db.Column(db.String(100), nullable=False)
    encrypted_data = db.Column(db.LargeBinary, nullable=False)  # Encrypted health data
    created_by = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)

    def encrypt_data(self, data):
        """Encrypts sensitive patient data."""
        self.encrypted_data = cipher_suite.encrypt(data.encode())

    def decrypt_data(self):
        """Decrypts sensitive patient data."""
        return cipher_suite.decrypt(self.encrypted_data).decode()


# Initialize database
@app.before_first_request
def create_tables():
    db.create_all()


# Routes
@app.route('/register', methods=['POST'])
def register_user():
    """Endpoint to register a new user."""
    data = request.json
    username = data.get('username')
    password = data.get('password')
    role = data.get('role')

    if not username or not password or not role:
        return jsonify({'error': 'Missing required fields'}), 400

    if User.query.filter_by(username=username).first():
        return jsonify({'error': 'Username already exists'}), 400

    user = User(username=username, role=role)
    user.set_password(password)
    db.session.add(user)
    db.session.commit()

    return jsonify({'message': 'User registered successfully'}), 201


@app.route('/add_record', methods=['POST'])
def add_record():
    """Endpoint to add a new patient record."""
    data = request.json
    patient_name = data.get('patient_name')
    health_data = data.get('health_data')
    created_by = data.get('created_by')  # User ID of the creator

    if not patient_name or not health_data or not created_by:
        return jsonify({'error': 'Missing required fields'}), 400

    user = User.query.get(created_by)
    if not user:
        return jsonify({'error': 'Invalid user ID'}), 400

    record = PatientRecord(patient_name=patient_name, created_by=created_by)
    record.encrypt_data(health_data)
    db.session.add(record)
    db.session.commit()

    return jsonify({'message': 'Patient record added successfully'}), 201


@app.route('/get_record/<int:record_id>', methods=['GET'])
def get_record(record_id):
    """Endpoint to retrieve a patient record."""
    record = PatientRecord.query.get(record_id)
    if not record:
        return jsonify({'error': 'Record not found'}), 404

    decrypted_data = record.decrypt_data()
    return jsonify({
        'patient_name': record.patient_name,
        'health_data': decrypted_data,
        'created_by': record.created_by
    }), 200


@app.route('/delete_record/<int:record_id>', methods=['DELETE'])
def delete_record(record_id):
    """Endpoint to delete a patient record."""
    record = PatientRecord.query.get(record_id)
    if not record:
        return jsonify({'error': 'Record not found'}), 404

    db.session.delete(record)
    db.session.commit()

    return jsonify({'message': 'Record deleted successfully'}), 200


# Error handling
@app.errorhandler(404)
def not_found_error(error):
    """Handle 404 errors."""
    return jsonify({'error': 'Resource not found'}), 404


@app.errorhandler(500)
def internal_error(error):
    """Handle 500 errors."""
    return jsonify({'error': 'Internal server error'}), 500


# Run the app
if __name__ == '__main__':
    app.run(debug=True)
```

### Notes:
- Replace `sqlite:///ehr.db` with a production-grade database URI (e.g., PostgreSQL or MySQL) for deployment.
- Store the `ENCRYPTION_KEY` securely (e.g., in environment variables or a secrets manager).
- Use HTTPS for secure communication in production.
- Implement authentication and authorization for sensitive endpoints.
