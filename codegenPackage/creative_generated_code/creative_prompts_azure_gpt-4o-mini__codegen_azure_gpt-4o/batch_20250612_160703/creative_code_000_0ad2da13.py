"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://balancermt.com
Prompt: Write a code snippet to create an online booking system for a massage therapy clinic, similar to the one mentioned on balancermt.com.
Generated: DETERMINISTIC_0ad2da13f07b1adf
Batch ID: 20250612_160703
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

# Database setup
DB_FILE = 'booking_system.db'

def setup_database():
    """
    Initialize the database and create necessary tables if not present.
    """
    conn = sqlite3.connect(DB_FILE)
    cursor = conn.cursor()
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS bookings (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT NOT NULL,
            email TEXT NOT NULL,
            phone TEXT NOT NULL,
            appointment_date TEXT NOT NULL,
            appointment_time TEXT NOT NULL,
            created_at TEXT NOT NULL
        )
    ''')
    conn.commit()
    conn.close()

setup_database()

# Helper function to validate date and time formats
def validate_datetime(date_str, time_str):
    """
    Validate date and time strings for formatting.
    """
    try:
        datetime.strptime(date_str, "%Y-%m-%d")
        datetime.strptime(time_str, "%H:%M")
        return True
    except ValueError:
        return False

@app.route('/book', methods=['POST'])
def book_appointment():
    """
    Endpoint to book a massage therapy appointment.
    """
    try:
        data = request.json
        name = data.get('name')
        email = data.get('email')
        phone = data.get('phone')
        appointment_date = data.get('appointment_date')
        appointment_time = data.get('appointment_time')

        # Validate required fields
        if not all([name, email, phone, appointment_date, appointment_time]):
            return jsonify({'error': 'All fields are required'}), 400

        # Validate date and time formats
        if not validate_datetime(appointment_date, appointment_time):
            return jsonify({'error': 'Invalid date or time format'}), 400

        # Save booking to database
        conn = sqlite3.connect(DB_FILE)
        cursor = conn.cursor()
        cursor.execute('''
            INSERT INTO bookings (name, email, phone, appointment_date, appointment_time, created_at)
            VALUES (?, ?, ?, ?, ?, ?)
        ''', (name, email, phone, appointment_date, appointment_time, datetime.now().isoformat()))
        conn.commit()
        conn.close()

        return jsonify({'message': 'Appointment booked successfully'}), 201
    except Exception as e:
        return jsonify({'error': str(e)}), 500

@app.route('/appointments', methods=['GET'])
def get_appointments():
    """
    Endpoint to retrieve all appointments.
    """
    try:
        conn = sqlite3.connect(DB_FILE)
        cursor = conn.cursor()
        cursor.execute('SELECT * FROM bookings')
        appointments = [
            {
                'id': row[0],
                'name': row[1],
                'email': row[2],
                'phone': row[3],
                'appointment_date': row[4],
                'appointment_time': row[5],
                'created_at': row[6]
            }
            for row in cursor.fetchall()
        ]
        conn.close()

        return jsonify(appointments), 200
    except Exception as e:
        return jsonify({'error': str(e)}), 500

if __name__ == '__main__':
    app.run(debug=True)
```
