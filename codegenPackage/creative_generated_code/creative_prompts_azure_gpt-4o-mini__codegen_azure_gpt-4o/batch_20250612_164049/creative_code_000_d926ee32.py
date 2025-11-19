"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://www.tubellaesteticaduepuntozero.it
Prompt: Generate a booking API integration for a beauty center that allows users to schedule appointments online, similar to TuBella Estetica 2.0 in Mestre.
Generated: DETERMINISTIC_d926ee32165bd3a2
Batch ID: 20250612_164049
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
DATABASE = 'beauty_center.db'

def initialize_database():
    """Initialize the SQLite database."""
    conn = sqlite3.connect(DATABASE)
    cursor = conn.cursor()
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS appointments (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT NOT NULL,
            email TEXT NOT NULL,
            service TEXT NOT NULL,
            date TEXT NOT NULL,
            time TEXT NOT NULL
        )
    ''')
    conn.commit()
    conn.close()

initialize_database()

@app.route('/book_appointment', methods=['POST'])
def book_appointment():
    """
    Endpoint to book an appointment.
    Request JSON should contain the following fields:
    - name: Customer's name
    - email: Customer's email
    - service: Service name
    - date: Appointment date (format: YYYY-MM-DD)
    - time: Appointment time (format: HH:MM)
    """
    try:
        # Retrieve data from request
        data = request.get_json()
        name = data.get('name')
        email = data.get('email')
        service = data.get('service')
        date = data.get('date')
        time = data.get('time')

        # Validate input
        if not all([name, email, service, date, time]):
            return jsonify({'error': 'All fields (name, email, service, date, time) are required.'}), 400

        # Validate date and time format
        try:
            datetime.strptime(date, '%Y-%m-%d')
            datetime.strptime(time, '%H:%M')
        except ValueError:
            return jsonify({'error': 'Invalid date or time format. Use YYYY-MM-DD for date and HH:MM for time.'}), 400

        # Save appointment to database
        conn = sqlite3.connect(DATABASE)
        cursor = conn.cursor()
        cursor.execute('''
            INSERT INTO appointments (name, email, service, date, time)
            VALUES (?, ?, ?, ?, ?)
        ''', (name, email, service, date, time))
        conn.commit()
        conn.close()

        return jsonify({'message': 'Appointment booked successfully!'}), 201

    except Exception as e:
        return jsonify({'error': 'An error occurred while booking the appointment.', 'details': str(e)}), 500

@app.route('/get_appointments', methods=['GET'])
def get_appointments():
    """
    Endpoint to retrieve all appointments.
    Returns a list of appointments with the following fields:
    - id: Appointment ID
    - name: Customer's name
    - email: Customer's email
    - service: Service name
    - date: Appointment date
    - time: Appointment time
    """
    try:
        conn = sqlite3.connect(DATABASE)
        cursor = conn.cursor()
        cursor.execute('SELECT id, name, email, service, date, time FROM appointments')
        rows = cursor.fetchall()
        conn.close()

        appointments = [
            {
                'id': row[0],
                'name': row[1],
                'email': row[2],
                'service': row[3],
                'date': row[4],
                'time': row[5]
            }
            for row in rows
        ]

        return jsonify({'appointments': appointments}), 200

    except Exception as e:
        return jsonify({'error': 'An error occurred while retrieving appointments.', 'details': str(e)}), 500

@app.route('/cancel_appointment/<int:appointment_id>', methods=['DELETE'])
def cancel_appointment(appointment_id):
    """
    Endpoint to cancel an appointment.
    Requires the appointment ID in the URL.
    """
    try:
        conn = sqlite3.connect(DATABASE)
        cursor = conn.cursor()
        cursor.execute('DELETE FROM appointments WHERE id = ?', (appointment_id,))
        changes = conn.total_changes
        conn.commit()
        conn.close()

        if changes == 0:
            return jsonify({'error': 'Appointment not found.'}), 404

        return jsonify({'message': 'Appointment canceled successfully!'}), 200

    except Exception as e:
        return jsonify({'error': 'An error occurred while canceling the appointment.', 'details': str(e)}), 500

if __name__ == '__main__':
    app.run(debug=True)
```
