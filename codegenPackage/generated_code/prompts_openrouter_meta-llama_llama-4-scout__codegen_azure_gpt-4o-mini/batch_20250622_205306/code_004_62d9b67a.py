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

```python
import os
import json
import hashlib
from cryptography.fernet import Fernet
from flask import Flask, request, jsonify, abort
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.exc import IntegrityError

# Initialize Flask application
app = Flask(__name__)

# Configure the SQLite database
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///ehr.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

# Generate a key for encryption
def generate_key():
    return Fernet.generate_key()

# Load the encryption key from environment variable or generate a new one
encryption_key = os.environ.get('EHR_ENCRYPTION_KEY', generate_key())
cipher = Fernet(encryption_key)

# Define the EHR model
class EHR(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    patient_id = db.Column(db.String(80), unique=True, nullable=False)
    record_data = db.Column(db.LargeBinary, nullable=False)

    def __repr__(self):
        return f'<EHR {self.patient_id}>'

# Initialize the database
with app.app_context():
    db.create_all()

# Function to encrypt data
def encrypt_data(data):
    return cipher.encrypt(data.encode())

# Function to decrypt data
def decrypt_data(encrypted_data):
    return cipher.decrypt(encrypted_data).decode()

@app.route('/ehr', methods=['POST'])
def create_ehr():
    """Create a new electronic health record."""
    data = request.json
    if not data or 'patient_id' not in data or 'record_data' not in data:
        abort(400, 'Invalid input data')

    patient_id = data['patient_id']
    record_data = data['record_data']

    # Encrypt the record data
    encrypted_record_data = encrypt_data(record_data)

    new_ehr = EHR(patient_id=patient_id, record_data=encrypted_record_data)

    try:
        db.session.add(new_ehr)
        db.session.commit()
    except IntegrityError:
        db.session.rollback()
        abort(400, 'EHR for this patient already exists')

    return jsonify({'message': 'EHR created successfully'}), 201

@app.route('/ehr/<patient_id>', methods=['GET'])
def get_ehr(patient_id):
    """Retrieve an electronic health record by patient ID."""
    ehr = EHR.query.filter_by(patient_id=patient_id).first()
    if ehr is None:
        abort(404, 'EHR not found')

    # Decrypt the record data
    decrypted_record_data = decrypt_data(ehr.record_data)
    return jsonify({'patient_id': ehr.patient_id, 'record_data': decrypted_record_data})

@app.route('/ehr/<patient_id>', methods=['PUT'])
def update_ehr(patient_id):
    """Update an existing electronic health record."""
    data = request.json
    if not data or 'record_data' not in data:
        abort(400, 'Invalid input data')

    ehr = EHR.query.filter_by(patient_id=patient_id).first()
    if ehr is None:
        abort(404, 'EHR not found')

    # Encrypt the new record data
    encrypted_record_data = encrypt_data(data['record_data'])
    ehr.record_data = encrypted_record_data

    db.session.commit()
    return jsonify({'message': 'EHR updated successfully'})

@app.route('/ehr/<patient_id>', methods=['DELETE'])
def delete_ehr(patient_id):
    """Delete an electronic health record."""
    ehr = EHR.query.filter_by(patient_id=patient_id).first()
    if ehr is None:
        abort(404, 'EHR not found')

    db.session.delete(ehr)
    db.session.commit()
    return jsonify({'message': 'EHR deleted successfully'})

if __name__ == '__main__':
    app.run(debug=False)
```

### Notes:
- Ensure to set the `EHR_ENCRYPTION_KEY` environment variable for production use.
- This code uses Flask and SQLAlchemy for web service and database management.
- The `cryptography` library is used for data encryption.
- Error handling is implemented for various scenarios, including input validation and database integrity.
