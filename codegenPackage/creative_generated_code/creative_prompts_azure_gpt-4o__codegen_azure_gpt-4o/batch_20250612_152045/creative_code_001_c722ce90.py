"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://mdatechsys.com
Prompt: Generate code for a web application that includes lead tracking functionality, as described in MDA Tech Sys's services.
Generated: DETERMINISTIC_c722ce90d2330241
Batch ID: 20250612_152045
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

Certainly! Here's the code for a web application with lead tracking functionality using Python's Flask framework. It includes database integration with SQLite for simplicity.

```python
from flask import Flask, request, jsonify
import sqlite3
import os

app = Flask(__name__)

# Database file
DATABASE = 'leads.db'

# Ensure the database exists
def init_db():
    """Initialize the database and create the leads table if it does not exist."""
    if not os.path.exists(DATABASE):
        conn = sqlite3.connect(DATABASE)
        cursor = conn.cursor()
        cursor.execute('''
            CREATE TABLE leads (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                name TEXT NOT NULL,
                email TEXT NOT NULL UNIQUE,
                phone TEXT,
                message TEXT,
                created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
            )
        ''')
        conn.commit()
        conn.close()

# Initialize the database
init_db()

@app.route('/leads', methods=['POST'])
def create_lead():
    """
    Endpoint to create a new lead.
    Expects JSON payload with 'name', 'email', 'phone', and 'message'.
    Returns a success response or an error.
    """
    try:
        data = request.json
        name = data['name']
        email = data['email']
        phone = data.get('phone', None)  # Optional field
        message = data.get('message', None)  # Optional field

        # Validate required fields
        if not name or not email:
            return jsonify({'error': 'Name and email are required'}), 400

        # Insert lead into the database
        conn = sqlite3.connect(DATABASE)
        cursor = conn.cursor()
        cursor.execute('''
            INSERT INTO leads (name, email, phone, message)
            VALUES (?, ?, ?, ?)
        ''', (name, email, phone, message))
        conn.commit()
        conn.close()

        return jsonify({'message': 'Lead created successfully'}), 201
    except Exception as e:
        return jsonify({'error': str(e)}), 500

@app.route('/leads', methods=['GET'])
def get_leads():
    """
    Endpoint to retrieve all leads.
    Returns a JSON array of leads.
    """
    try:
        conn = sqlite3.connect(DATABASE)
        cursor = conn.cursor()
        cursor.execute('SELECT id, name, email, phone, message, created_at FROM leads')
        leads = cursor.fetchall()
        conn.close()

        # Convert data to list of dictionaries
        lead_list = [
            {
                'id': lead[0],
                'name': lead[1],
                'email': lead[2],
                'phone': lead[3],
                'message': lead[4],
                'created_at': lead[5]
            } for lead in leads
        ]

        return jsonify(lead_list), 200
    except Exception as e:
        return jsonify({'error': str(e)}), 500

@app.route('/leads/<int:lead_id>', methods=['GET'])
def get_lead(lead_id):
    """
    Endpoint to retrieve a specific lead by ID.
    Returns a JSON object for the requested lead.
    """
    try:
        conn = sqlite3.connect(DATABASE)
        cursor = conn.cursor()
        cursor.execute('SELECT id, name, email, phone, message, created_at FROM leads WHERE id = ?', (lead_id,))
        lead = cursor.fetchone()
        conn.close()

        if not lead:
            return jsonify({'error': 'Lead not found'}), 404

        lead_data = {
            'id': lead[0],
            'name': lead[1],
            'email': lead[2],
            'phone': lead[3],
            'message': lead[4],
            'created_at': lead[5]
        }

        return jsonify(lead_data), 200
    except Exception as e:
        return jsonify({'error': str(e)}), 500

@app.route('/leads/<int:lead_id>', methods=['DELETE'])
def delete_lead(lead_id):
    """
    Endpoint to delete a specific lead by ID.
    Returns a success response or an error.
    """
    try:
        conn = sqlite3.connect(DATABASE)
        cursor = conn.cursor()
        cursor.execute('DELETE FROM leads WHERE id = ?', (lead_id,))
        conn.commit()
        conn.close()

        if cursor.rowcount == 0:
            return jsonify({'error': 'Lead not found'}), 404

        return jsonify({'message': 'Lead deleted successfully'}), 200
    except Exception as e:
        return jsonify({'error': str(e)}), 500

# Run the application
if __name__ == '__main__':
    app.run(debug=True)
```

### Notes:
1. Install required dependencies using `pip install flask`.
2. Run the application (`python <file_name>.py`) and ensure the database initializes on first launch.
3. Use a tool like Postman or curl to interact with the endpoints.
4. Replace SQLite with a more robust database (e.g., PostgreSQL) if deploying to production.
