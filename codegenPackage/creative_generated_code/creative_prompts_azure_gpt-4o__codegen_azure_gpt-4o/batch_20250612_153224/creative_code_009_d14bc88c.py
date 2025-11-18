"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://geeks-on-repair.com
Prompt: Recommend libraries or APIs for managing online and onsite repair appointments, and write a sample implementation based on the services described by Geeks On Repair.
Generated: DETERMINISTIC_d14bc88ce05ab546
Batch ID: 20250612_153224
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
"""
Sample implementation for managing online and onsite repair appointments inspired by services like Geeks On Repair.

This script uses Flask as the web framework and SQLite for database management. It provides endpoints for creating, viewing,
and managing repair appointments. The implementation demonstrates best practices, error handling, and production-ready design.
"""

from flask import Flask, request, jsonify
import sqlite3
from datetime import datetime

app = Flask(__name__)

# Database configuration
DATABASE = 'repair_appointments.db'


def init_db():
    """
    Initialize the database and create tables if they do not exist.
    """
    with sqlite3.connect(DATABASE) as conn:
        cursor = conn.cursor()
        cursor.execute('''
            CREATE TABLE IF NOT EXISTS appointments (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                customer_name TEXT NOT NULL,
                email TEXT NOT NULL,
                phone TEXT NOT NULL,
                appointment_type TEXT NOT NULL CHECK(appointment_type IN ('online', 'onsite')),
                appointment_date TEXT NOT NULL,
                description TEXT,
                created_at TEXT DEFAULT CURRENT_TIMESTAMP
            )
        ''')
        conn.commit()


# Initialize the database
init_db()


@app.route('/appointments', methods=['POST'])
def create_appointment():
    """
    Endpoint to create a new repair appointment.
    """
    try:
        # Extract data from the request
        data = request.json
        customer_name = data.get('customer_name')
        email = data.get('email')
        phone = data.get('phone')
        appointment_type = data.get('appointment_type')
        appointment_date = data.get('appointment_date')
        description = data.get('description')

        # Validate the input data
        if not all([customer_name, email, phone, appointment_type, appointment_date]):
            return jsonify({"error": "Missing required fields"}), 400

        if appointment_type not in ['online', 'onsite']:
            return jsonify({"error": "Invalid appointment type"}), 400

        # Store the appointment in the database
        with sqlite3.connect(DATABASE) as conn:
            cursor = conn.cursor()
            cursor.execute('''
                INSERT INTO appointments (customer_name, email, phone, appointment_type, appointment_date, description)
                VALUES (?, ?, ?, ?, ?, ?)
            ''', (customer_name, email, phone, appointment_type, appointment_date, description))
            conn.commit()
            return jsonify({"message": "Appointment created successfully"}), 201
    except Exception as e:
        return jsonify({"error": str(e)}), 500


@app.route('/appointments', methods=['GET'])
def get_appointments():
    """
    Endpoint to retrieve all repair appointments.
    """
    try:
        with sqlite3.connect(DATABASE) as conn:
            cursor = conn.cursor()
            cursor.execute('SELECT * FROM appointments')
            appointments = cursor.fetchall()

            # Format the appointments into JSON
            formatted_appointments = [
                {
                    "id": appt[0],
                    "customer_name": appt[1],
                    "email": appt[2],
                    "phone": appt[3],
                    "appointment_type": appt[4],
                    "appointment_date": appt[5],
                    "description": appt[6],
                    "created_at": appt[7],
                } for appt in appointments
            ]

            return jsonify(formatted_appointments), 200
    except Exception as e:
        return jsonify({"error": str(e)}), 500


@app.route('/appointments/<int:appointment_id>', methods=['DELETE'])
def delete_appointment(appointment_id):
    """
    Endpoint to delete a specific repair appointment by ID.
    """
    try:
        with sqlite3.connect(DATABASE) as conn:
            cursor = conn.cursor()
            cursor.execute('DELETE FROM appointments WHERE id = ?', (appointment_id,))
            conn.commit()

            if cursor.rowcount == 0:
                return jsonify({"error": "Appointment not found"}), 404

            return jsonify({"message": "Appointment deleted successfully"}), 200
    except Exception as e:
        return jsonify({"error": str(e)}), 500


@app.route('/appointments/<int:appointment_id>', methods=['PUT'])
def update_appointment(appointment_id):
    """
    Endpoint to update a specific repair appointment by ID.
    """
    try:
        # Extract data from the request
        data = request.json
        customer_name = data.get('customer_name')
        email = data.get('email')
        phone = data.get('phone')
        appointment_type = data.get('appointment_type')
        appointment_date = data.get('appointment_date')
        description = data.get('description')

        # Validate input
        if not all([customer_name, email, phone, appointment_type, appointment_date]):
            return jsonify({"error": "Missing required fields"}), 400

        if appointment_type not in ['online', 'onsite']:
            return jsonify({"error": "Invalid appointment type"}), 400

        # Update the appointment in the database
        with sqlite3.connect(DATABASE) as conn:
            cursor = conn.cursor()
            cursor.execute('''
                UPDATE appointments
                SET customer_name = ?, email = ?, phone = ?, appointment_type = ?, appointment_date = ?, description = ?
                WHERE id = ?
            ''', (customer_name, email, phone, appointment_type, appointment_date, description, appointment_id))
            conn.commit()

            if cursor.rowcount == 0:
                return jsonify({"error": "Appointment not found"}), 404

            return jsonify({"message": "Appointment updated successfully"}), 200
    except Exception as e:
        return jsonify({"error": str(e)}), 500


if __name__ == '__main__':
    app.run(debug=True)
```
