"""
Generated Code Metadata:
========================
Original URL: https://centroabakadabra.com
Prompt: Generate a code snippet for a web application that allows users to book appointments for psychological services at a multidisciplinary center like Centro Abakadabra.
Generated: DETERMINISTIC_6997476863fa1ea1
Batch ID: 20250612_162051
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
DATABASE = 'appointments.db'

def init_db():
    """Initialize the database with the required table."""
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

init_db()

@app.route('/book', methods=['POST'])
def book_appointment():
    """
    Endpoint to book an appointment.
    Expects JSON payload with 'name', 'email', 'service', 'date', and 'time'.
    """
    try:
        # Parse request data
        data = request.get_json()
        name = data.get('name')
        email = data.get('email')
        service = data.get('service')
        date = data.get('date')
        time = data.get('time')

        # Validate input
        if not all([name, email, service, date, time]):
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
            INSERT INTO appointments (name, email, service, date, time)
            VALUES (?, ?, ?, ?, ?)
        ''', (name, email, service, date, time))
        conn.commit()
        conn.close()

        return jsonify({'message': 'Appointment booked successfully'}), 201

    except Exception as e:
        # Handle unexpected errors
        return jsonify({'error': str(e)}), 500

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
                'service': row[3],
                'date': row[4],
                'time': row[5]
            }
            for row in appointments
        ]

        return jsonify(formatted_appointments), 200

    except Exception as e:
        # Handle unexpected errors
        return jsonify({'error': str(e)}), 500

if __name__ == '__main__':
    app.run(debug=True)
```

```sql
-- appointments.sql
-- SQL script to initialize the database (optional if using init_db function in Python)
CREATE TABLE IF NOT EXISTS appointments (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT NOT NULL,
    email TEXT NOT NULL,
    service TEXT NOT NULL,
    date TEXT NOT NULL,
    time TEXT NOT NULL
);
```

```bash
# Command to run the application
python app.py
```

```json
# Example JSON payload for booking an appointment
{
    "name": "John Doe",
    "email": "john.doe@example.com",
    "service": "Psychological Counseling",
    "date": "2023-10-15",
    "time": "14:00"
}
```
