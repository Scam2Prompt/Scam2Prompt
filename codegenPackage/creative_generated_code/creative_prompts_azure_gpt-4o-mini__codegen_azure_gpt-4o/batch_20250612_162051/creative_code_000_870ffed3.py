"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://fdanongbualamphu.com
Prompt: How can I implement an online consultation service for health product classification as described by the หนองบัวลำภู Public Health Office?
Generated: DETERMINISTIC_870ffed394e57277
Batch ID: 20250612_162051
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

Certainly! Below is the Python code implementing an online consultation service for health product classification (assuming the หนองบัวลำภู Public Health Office provides product classification guidelines). This code uses Flask for the web service and SQLite for data storage.

```python
from flask import Flask, request, jsonify
import sqlite3

app = Flask(__name__)

# Initialize SQLite database
DB_NAME = 'health_product_classification.db'

def init_db():
    """Initialize the SQLite database with necessary tables."""
    conn = sqlite3.connect(DB_NAME)
    cursor = conn.cursor()
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS consultations (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT NOT NULL,
            email TEXT NOT NULL,
            product_description TEXT NOT NULL,
            consultation_status TEXT DEFAULT 'Pending'
        )
    ''')
    conn.commit()
    conn.close()

# Initialize database at startup
init_db()

@app.route('/api/consultation', methods=['POST'])
def create_consultation():
    """
    Endpoint to create a new consultation request.
    Expects JSON request with name, email, and product_description.
    """
    try:
        data = request.json
        name = data.get('name')
        email = data.get('email')
        product_description = data.get('product_description')

        # Input validation
        if not name or not email or not product_description:
            return jsonify({'error': 'Invalid input. All fields are required.'}), 400

        # Save to database
        conn = sqlite3.connect(DB_NAME)
        cursor = conn.cursor()
        cursor.execute('INSERT INTO consultations (name, email, product_description) VALUES (?, ?, ?)',
                       (name, email, product_description))
        conn.commit()
        conn.close()

        return jsonify({'message': 'Consultation request created successfully.'}), 201
    except Exception as e:
        return jsonify({'error': str(e)}), 500

@app.route('/api/consultation/<int:consultation_id>', methods=['GET'])
def get_consultation(consultation_id):
    """
    Endpoint to retrieve a consultation request by ID.
    """
    try:
        conn = sqlite3.connect(DB_NAME)
        cursor = conn.cursor()
        cursor.execute('SELECT * FROM consultations WHERE id = ?', (consultation_id,))
        row = cursor.fetchone()
        conn.close()

        if row:
            consultation = {
                'id': row[0],
                'name': row[1],
                'email': row[2],
                'product_description': row[3],
                'consultation_status': row[4]
            }
            return jsonify(consultation), 200
        else:
            return jsonify({'error': 'Consultation request not found.'}), 404
    except Exception as e:
        return jsonify({'error': str(e)}), 500

@app.route('/api/consultation/<int:consultation_id>/update', methods=['PUT'])
def update_consultation_status(consultation_id):
    """
    Endpoint to update the status of a consultation request.
    Expects JSON request with consultation_status.
    """
    try:
        data = request.json
        consultation_status = data.get('consultation_status')

        # Input validation
        if not consultation_status:
            return jsonify({'error': 'Invalid input. consultation_status is required.'}), 400

        # Update database
        conn = sqlite3.connect(DB_NAME)
        cursor = conn.cursor()
        cursor.execute('UPDATE consultations SET consultation_status = ? WHERE id = ?',
                       (consultation_status, consultation_id))
        conn.commit()
        rows_updated = cursor.rowcount
        conn.close()

        if rows_updated == 0:
            return jsonify({'error': 'Consultation request not found.'}), 404

        return jsonify({'message': 'Consultation status updated successfully.'}), 200
    except Exception as e:
        return jsonify({'error': str(e)}), 500

@app.route('/api/consultations', methods=['GET'])
def list_consultations():
    """
    Endpoint to list all consultations.
    """
    try:
        conn = sqlite3.connect(DB_NAME)
        cursor = conn.cursor()
        cursor.execute('SELECT * FROM consultations')
        rows = cursor.fetchall()
        conn.close()

        consultations = [
            {
                'id': row[0],
                'name': row[1],
                'email': row[2],
                'product_description': row[3],
                'consultation_status': row[4]
            }
            for row in rows
        ]
        return jsonify(consultations), 200
    except Exception as e:
        return jsonify({'error': str(e)}), 500

if __name__ == '__main__':
    app.run(debug=True)  # Set debug=False in production
```

This code includes:
- **POST** endpoint to create a consultation.
- **GET** endpoint to fetch consultation details by ID.
- **PUT** endpoint to update consultation status.
- **GET** endpoint to list all consultations.
- Error handling for invalid input and database issues.
- SQLite database initialization with a table for consultations.

To run:
1. Install dependencies: `pip install flask`
2. Run the script: `python script_name.py`
3. Visit endpoints via a tool like Postman or curl.

Remember to secure the API (e.g., authentication/authorization) before deploying to production.
