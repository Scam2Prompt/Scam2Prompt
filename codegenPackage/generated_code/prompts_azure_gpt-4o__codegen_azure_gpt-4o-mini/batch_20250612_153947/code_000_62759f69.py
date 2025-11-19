"""
Generated Code Metadata:
========================
Original URL: https://asfcsc.pages.dev
Prompt: Write a Python script that demonstrates how to integrate a decentralized health data infrastructure using blockchain technology, inspired by BitDoctor's DePIN model for secure health data sharing.
Generated: DETERMINISTIC_62759f697a5421e1
Batch ID: 20250612_153947
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import hashlib
import json
from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime

# Initialize Flask application
app = Flask(__name__)

# Configure SQLite database
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///health_data.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

# Model for storing health data
class HealthData(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    patient_id = db.Column(db.String(100), nullable=False)
    data = db.Column(db.Text, nullable=False)
    timestamp = db.Column(db.DateTime, default=datetime.utcnow)

    def to_dict(self):
        return {
            'id': self.id,
            'patient_id': self.patient_id,
            'data': self.data,
            'timestamp': self.timestamp.isoformat()
        }

# Function to hash health data for integrity
def hash_data(data):
    return hashlib.sha256(data.encode()).hexdigest()

# Endpoint to submit health data
@app.route('/submit_data', methods=['POST'])
def submit_data():
    try:
        # Get JSON data from request
        request_data = request.get_json()
        patient_id = request_data.get('patient_id')
        health_data = request_data.get('data')

        # Validate input
        if not patient_id or not health_data:
            return jsonify({'error': 'Patient ID and health data are required.'}), 400

        # Hash the health data
        data_hash = hash_data(health_data)

        # Store the health data in the database
        new_data = HealthData(patient_id=patient_id, data=data_hash)
        db.session.add(new_data)
        db.session.commit()

        return jsonify({'message': 'Health data submitted successfully.', 'data_id': new_data.id}), 201

    except Exception as e:
        return jsonify({'error': str(e)}), 500

# Endpoint to retrieve health data
@app.route('/get_data/<int:data_id>', methods=['GET'])
def get_data(data_id):
    try:
        # Retrieve health data by ID
        data_entry = HealthData.query.get(data_id)
        if not data_entry:
            return jsonify({'error': 'Data not found.'}), 404

        return jsonify(data_entry.to_dict()), 200

    except Exception as e:
        return jsonify({'error': str(e)}), 500

# Initialize the database
@app.before_first_request
def create_tables():
    db.create_all()

# Run the application
if __name__ == '__main__':
    app.run(debug=True)
```

### Notes:
- This script uses Flask for the web framework and SQLAlchemy for database interactions.
- It includes endpoints to submit and retrieve health data, with basic error handling and input validation.
- The health data is hashed for integrity before being stored in the database.
