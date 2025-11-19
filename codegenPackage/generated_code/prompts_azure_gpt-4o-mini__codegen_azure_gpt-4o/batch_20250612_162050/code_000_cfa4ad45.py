"""
Generated Code Metadata:
========================
Original URL: https://depilarmg.com.br
Prompt: Generate a code snippet for a web application that allows users to book a waxing appointment at a salon specializing in painless waxing services.
Generated: DETERMINISTIC_cfa4ad458e52ce58
Batch ID: 20250612_162050
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# app.py

from flask import Flask, request, jsonify
from datetime import datetime
import sqlite3

app = Flask(__name__)

# Database setup
DATABASE = 'salon.db'

def init_db():
    """Initialize the database and create tables if they don't exist."""
    conn = sqlite3.connect(DATABASE)
    cursor = conn.cursor()
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS appointments (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT NOT NULL,
            email TEXT NOT NULL,
            phone TEXT NOT NULL,
            date TEXT NOT NULL,
            time TEXT NOT NULL
        )
    ''')
    conn.commit()
    conn.close()

init_db()

@app.route('/book', methods=['POST'])
def book_appointment():
    """
    Endpoint to book a waxing appointment.
    Expects JSON payload with name, email, phone, date, and time.
    """
    try:
        # Parse request data
        data = request.get_json()
        name = data.get('name')
        email = data.get('email')
        phone = data.get('phone')
        date = data.get('date')
        time = data.get('time')

        # Validate input
        if not all([name, email, phone, date, time]):
            return jsonify({'error': 'All fields are required'}), 400

        # Validate date and time format
        try:
            datetime.strptime(date, '%Y-%m-%d')
            datetime.strptime(time, '%H:%M')
        except ValueError:
            return jsonify({'error': 'Invalid date or time format'}), 400

        # Save appointment to database
        conn = sqlite3.connect(DATABASE)
        cursor = conn.cursor()
        cursor.execute('''
            INSERT INTO appointments (name, email, phone, date, time)
            VALUES (?, ?, ?, ?, ?)
        ''', (name, email, phone, date, time))
        conn.commit()
        conn.close()

        return jsonify({'message': 'Appointment booked successfully'}), 201

    except Exception as e:
        # Handle unexpected errors
        return jsonify({'error': 'An error occurred', 'details': str(e)}), 500

@app.route('/appointments', methods=['GET'])
def get_appointments():
    """
    Endpoint to retrieve all booked appointments.
    """
    try:
        conn = sqlite3.connect(DATABASE)
        cursor = conn.cursor()
        cursor.execute('SELECT * FROM appointments')
        appointments = cursor.fetchall()
        conn.close()

        # Format appointments as a list of dictionaries
        formatted_appointments = [
            {
                'id': row[0],
                'name': row[1],
                'email': row[2],
                'phone': row[3],
                'date': row[4],
                'time': row[5]
            }
            for row in appointments
        ]

        return jsonify(formatted_appointments), 200

    except Exception as e:
        # Handle unexpected errors
        return jsonify({'error': 'An error occurred', 'details': str(e)}), 500

if __name__ == '__main__':
    app.run(debug=True)
```

```sql
-- salon.sql

-- Run this script to initialize the database manually if needed
CREATE TABLE IF NOT EXISTS appointments (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT NOT NULL,
    email TEXT NOT NULL,
    phone TEXT NOT NULL,
    date TEXT NOT NULL,
    time TEXT NOT NULL
);
```

### Instructions:
1. Install Flask: `pip install flask`.
2. Run the Python script: `python app.py`.
3. Use a tool like Postman or cURL to test the `/book` and `/appointments` endpoints.
4. Ensure the SQLite database (`salon.db`) is created in the same directory as the script.
