"""
Generated Code Metadata:
========================
Original URL: https://thatcounselingplace.com
Prompt: Generate a code snippet for a simple online appointment booking system that integrates with a therapist's website and allows clients to schedule sessions, considering the provided contact details and session cost information.
Generated: DETERMINISTIC_28bc7a8667c5837d
Batch ID: 20250622_210655
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# Import required libraries
from datetime import datetime, timedelta
import sqlite3
from flask import Flask, request, jsonify

# Create a Flask application instance
app = Flask(__name__)

# Define database connection settings
DB_NAME = 'appointment_booking.db'

# Create a database connection
def create_connection():
    conn = None
    try:
        conn = sqlite3.connect(DB_NAME)
        return conn
    except sqlite3.Error as e:
        print(e)

# Create table for therapists
def create_therapist_table(conn):
    sql = """
        CREATE TABLE IF NOT EXISTS therapists (
            id INTEGER PRIMARY KEY,
            name TEXT NOT NULL,
            email TEXT NOT NULL,
            phone TEXT NOT NULL,
            session_cost REAL NOT NULL
        )
    """
    try:
        c = conn.cursor()
        c.execute(sql)
    except sqlite3.Error as e:
        print(e)

# Create table for appointments
def create_appointment_table(conn):
    sql = """
        CREATE TABLE IF NOT EXISTS appointments (
            id INTEGER PRIMARY KEY,
            therapist_id INTEGER NOT NULL,
            client_name TEXT NOT NULL,
            client_email TEXT NOT NULL,
            client_phone TEXT NOT NULL,
            appointment_date DATE NOT NULL,
            appointment_time TIME NOT NULL,
            FOREIGN KEY (therapist_id) REFERENCES therapists (id)
        )
    """
    try:
        c = conn.cursor()
        c.execute(sql)
    except sqlite3.Error as e:
        print(e)

# Initialize database tables
def init_db():
    conn = create_connection()
    with conn:
        create_therapist_table(conn)
        create_appointment_table(conn)
    conn.close()

# Initialize database
init_db()

# API endpoint to add a therapist
@app.route('/therapist', methods=['POST'])
def add_therapist():
    try:
        data = request.json
        if not data:
            return jsonify({"message": "No data provided"}), 400
        
        therapist = (data['name'], data['email'], data['phone'], data['session_cost'])
        conn = create_connection()
        with conn:
            c = conn.cursor()
            c.execute("INSERT INTO therapists (name, email, phone, session_cost) VALUES (?, ?, ?, ?)", therapist)
            conn.commit()
            return jsonify({"message": "Therapist added successfully"}), 201
    except sqlite3.Error as e:
        return jsonify({"message": str(e)}), 500
    except Exception as e:
        return jsonify({"message": str(e)}), 400
    finally:
        if conn:
            conn.close()

# API endpoint to book an appointment
@app.route('/appointment', methods=['POST'])
def book_appointment():
    try:
        data = request.json
        if not data:
            return jsonify({"message": "No data provided"}), 400
        
        therapist_id = data['therapist_id']
        client_name = data['client_name']
        client_email = data['client_email']
        client_phone = data['client_phone']
        appointment_date = data['appointment_date']
        appointment_time = data['appointment_time']

        conn = create_connection()
        with conn:
            c = conn.cursor()
            c.execute("SELECT * FROM therapists WHERE id=?", (therapist_id,))
            therapist = c.fetchone()
            if not therapist:
                return jsonify({"message": "Therapist not found"}), 404
            
            appointment = (therapist_id, client_name, client_email, client_phone, appointment_date, appointment_time)
            c.execute("INSERT INTO appointments (therapist_id, client_name, client_email, client_phone, appointment_date, appointment_time) VALUES (?, ?, ?, ?, ?, ?)", appointment)
            conn.commit()
            return jsonify({"message": "Appointment booked successfully"}), 201
    except sqlite3.Error as e:
        return jsonify({"message": str(e)}), 500
    except Exception as e:
        return jsonify({"message": str(e)}), 400
    finally:
        if conn:
            conn.close()

# API endpoint to get all appointments for a therapist
@app.route('/therapist/<int:therapist_id>/appointments', methods=['GET'])
def get_appointments(therapist_id):
    try:
        conn = create_connection()
        with conn:
            c = conn.cursor()
            c.execute("SELECT * FROM appointments WHERE therapist_id=?", (therapist_id,))
            appointments = c.fetchall()
            return jsonify([{"id": a[0], "therapist_id": a[1], "client_name": a[2], "client_email": a[3], "client_phone": a[4], "appointment_date": a[5], "appointment_time": a[6]} for a in appointments])
    except sqlite3.Error as e:
        return jsonify({"message": str(e)}), 500
    finally:
        if conn:
            conn.close()

if __name__ == '__main__':
    app.run(debug=True)
```
