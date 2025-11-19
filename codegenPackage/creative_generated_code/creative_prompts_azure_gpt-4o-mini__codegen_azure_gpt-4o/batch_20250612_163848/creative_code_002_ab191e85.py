"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://molinahealthcareinc.com
Prompt: Write a code snippet for a patient portal that allows users to access their medical records, inspired by the features mentioned on the MHC Inc site.
Generated: DETERMINISTIC_ab191e85b39fecae
Batch ID: 20250612_163848
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
from flask import Flask, request, jsonify
from datetime import datetime
import sqlite3

app = Flask(__name__)

# Database initialization
DATABASE = 'medical_records.db'

def init_db():
    """Initialize the database and create tables if they don't exist."""
    conn = sqlite3.connect(DATABASE)
    cursor = conn.cursor()
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS patients (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT NOT NULL,
            email TEXT UNIQUE NOT NULL,
            dob DATE NOT NULL
        )
    ''')
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS medical_records (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            patient_id INTEGER NOT NULL,
            record_date DATE NOT NULL,
            description TEXT NOT NULL,
            FOREIGN KEY (patient_id) REFERENCES patients (id)
        )
    ''')
    conn.commit()
    conn.close()

init_db()

# Helper functions
def get_db_connection():
    """Create a database connection."""
    try:
        return sqlite3.connect(DATABASE)
    except sqlite3.Error as e:
        print(f"Database connection error: {e}")
        return None

def fetch_records(patient_id):
    """Fetch medical records for a given patient ID."""
    conn = get_db_connection()
    if not conn:
        return []
    conn.row_factory = sqlite3.Row
    cursor = conn.cursor()
    cursor.execute('''
        SELECT record_date, description
        FROM medical_records
        WHERE patient_id = ?
        ORDER BY record_date DESC
    ''', (patient_id,))
    records = cursor.fetchall()
    conn.close()
    return [dict(record) for record in records]

# Routes
@app.route('/api/patient/<int:patient_id>/records', methods=['GET'])
def get_medical_records(patient_id):
    """
    Endpoint to retrieve medical records for a specific patient.
    :param patient_id: Patient ID
    :return: JSON with medical records or error message
    """
    try:
        records = fetch_records(patient_id)
        if not records:
            return jsonify({'message': 'No records found or patient does not exist'}), 404
        return jsonify({'patient_id': patient_id, 'medical_records': records}), 200
    except Exception as e:
        return jsonify({'error': f'An error occurred: {str(e)}'}), 500

@app.route('/api/patient', methods=['POST'])
def add_patient():
    """
    Endpoint to add a new patient.
    Expects JSON payload with 'name', 'email', and 'dob' (date of birth) fields.
    """
    try:
        data = request.get_json()
        name = data.get('name')
        email = data.get('email')
        dob = data.get('dob')

        # Validate input
        if not name or not email or not dob:
            return jsonify({'error': 'Missing required fields'}), 400

        conn = get_db_connection()
        if not conn:
            return jsonify({'error': 'Database connection error'}), 500
        cursor = conn.cursor()
        cursor.execute('''
            INSERT INTO patients (name, email, dob)
            VALUES (?, ?, ?)
        ''', (name, email, dob))
        conn.commit()
        patient_id = cursor.lastrowid
        conn.close()

        return jsonify({'message': 'Patient added successfully', 'patient_id': patient_id}), 201
    except sqlite3.IntegrityError:
        return jsonify({'error': 'Email already exists'}), 400
    except Exception as e:
        return jsonify({'error': f'An error occurred: {str(e)}'}), 500

@app.route('/api/patient/<int:patient_id>/record', methods=['POST'])
def add_medical_record(patient_id):
    """
    Endpoint to add a medical record for a specific patient.
    Expects JSON payload with 'record_date' and 'description' fields.
    """
    try:
        data = request.get_json()
        record_date = data.get('record_date')
        description = data.get('description')

        # Validate input
        if not record_date or not description:
            return jsonify({'error': 'Missing required fields'}), 400

        conn = get_db_connection()
        if not conn:
            return jsonify({'error': 'Database connection error'}), 500
        cursor = conn.cursor()
        cursor.execute('''
            INSERT INTO medical_records (patient_id, record_date, description)
            VALUES (?, ?, ?)
        ''', (patient_id, record_date, description))
        conn.commit()
        conn.close()

        return jsonify({'message': 'Medical record added successfully'}), 201
    except sqlite3.IntegrityError:
        return jsonify({'error': 'Patient does not exist'}), 404
    except Exception as e:
        return jsonify({'error': f'An error occurred: {str(e)}'}), 500

if __name__ == '__main__':
    app.run(debug=True)
```
