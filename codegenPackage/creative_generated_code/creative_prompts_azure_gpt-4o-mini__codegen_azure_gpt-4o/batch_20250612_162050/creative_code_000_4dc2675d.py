"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://getupenergy.co.uk
Prompt: Generate a code snippet for a web application that integrates Tibi's massage therapy services, focusing on user appointment scheduling and stress management features.
Generated: DETERMINISTIC_4dc2675d55701d78
Batch ID: 20250612_162050
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

# Initialize and set up SQLite database
DATABASE = 'tibis_massage_therapy.db'


def init_db():
    """Initialize the SQLite database."""
    conn = sqlite3.connect(DATABASE)
    cursor = conn.cursor()
    # Create appointments table
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS appointments (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT NOT NULL,
            email TEXT NOT NULL,
            phone TEXT NOT NULL,
            service TEXT NOT NULL,
            appointment_date TEXT NOT NULL,
            created_at TEXT NOT NULL
        )
    ''')
    conn.commit()
    conn.close()


# Run database initialization
init_db()


# Routes
@app.route('/schedule', methods=['POST'])
def schedule_appointment():
    """
    Endpoint to schedule an appointment.
    Accepts JSON payload with name, email, phone, service, and appointment_date.
    """
    try:
        data = request.json

        # Input validation
        required_fields = ['name', 'email', 'phone', 'service', 'appointment_date']
        for field in required_fields:
            if field not in data or not data[field]:
                return jsonify({'error': f'{field} is required'}), 400

        # Parse and validate appointment date
        try:
            appointment_date = datetime.strptime(data['appointment_date'], '%Y-%m-%d %H:%M:%S')
        except ValueError:
            return jsonify({'error': 'Invalid appointment_date format. Use YYYY-MM-DD HH:MM:SS'}), 400

        # Save the appointment to the database
        conn = sqlite3.connect(DATABASE)
        cursor = conn.cursor()
        cursor.execute('''
            INSERT INTO appointments (name, email, phone, service, appointment_date, created_at)
            VALUES (?, ?, ?, ?, ?, ?)
        ''', (
            data['name'],
            data['email'],
            data['phone'],
            data['service'],
            appointment_date.strftime('%Y-%m-%d %H:%M:%S'),
            datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        ))
        conn.commit()
        conn.close()

        return jsonify({'message': 'Appointment scheduled successfully!'}), 201

    except Exception as e:
        # Catch any unexpected errors
        return jsonify({'error': str(e)}), 500


@app.route('/appointments', methods=['GET'])
def list_appointments():
    """
    Endpoint to retrieve all scheduled appointments.
    """
    try:
        conn = sqlite3.connect(DATABASE)
        cursor = conn.cursor()
        cursor.execute('SELECT * FROM appointments')
        appointments = cursor.fetchall()
        conn.close()

        # Format appointments data
        result = []
        for appointment in appointments:
            result.append({
                'id': appointment[0],
                'name': appointment[1],
                'email': appointment[2],
                'phone': appointment[3],
                'service': appointment[4],
                'appointment_date': appointment[5],
                'created_at': appointment[6],
            })

        return jsonify({'appointments': result}), 200

    except Exception as e:
        # Handle unexpected errors
        return jsonify({'error': str(e)}), 500


@app.route('/stress-management', methods=['GET'])
def stress_management_tips():
    """
    Endpoint to provide stress management tips.
    """
    tips = [
        "Practice deep breathing exercises.",
        "Engage in regular physical activity.",
        "Try mindful meditation.",
        "Get a massage to relax tense muscles.",
        "Maintain a healthy diet and stay hydrated.",
        "Connect with loved ones for emotional support."
    ]
    return jsonify({'tips': tips}), 200


# Start the Flask application
if __name__ == '__main__':
    app.run(debug=True)
```
