"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://reparaciondeturbo.cl
Prompt: Create a web application using Flask that allows users to book a free turbo diagnostic appointment, track repair progress, and receive updates via WhatsApp.
Generated: DETERMINISTIC_759b8e7759ccfd91
Batch ID: 20250612_153246
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
from flask import Flask, request, jsonify, render_template, redirect, url_for, session
from twilio.rest import Client
import os
import sqlite3

# Flask app initialization
app = Flask(__name__)
app.secret_key = os.urandom(24)  # Secret key for session management

# Twilio configuration (replace with your credentials)
TWILIO_ACCOUNT_SID = 'your_account_sid'
TWILIO_AUTH_TOKEN = 'your_auth_token'
TWILIO_PHONE_NUMBER = 'your_twilio_phone_number'

# Database setup
DATABASE = 'appointments.db'

def init_db():
    """Initializes the database schema."""
    with sqlite3.connect(DATABASE) as conn:
        cursor = conn.cursor()
        cursor.execute("""
            CREATE TABLE IF NOT EXISTS appointments (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                name TEXT NOT NULL,
                phone TEXT NOT NULL,
                appointment_date TEXT NOT NULL,
                status TEXT NOT NULL DEFAULT 'Booked'
            )
        """)
        conn.commit()

init_db()

# Twilio client initialization
twilio_client = Client(TWILIO_ACCOUNT_SID, TWILIO_AUTH_TOKEN)

@app.route('/')
def home():
    """Render the homepage."""
    return render_template('index.html')

@app.route('/book', methods=['GET', 'POST'])
def book_appointment():
    """Handles booking a turbo diagnostic appointment."""
    if request.method == 'POST':
        name = request.form.get('name')
        phone = request.form.get('phone')
        appointment_date = request.form.get('appointment_date')

        if not name or not phone or not appointment_date:
            return jsonify({'error': 'All fields are required'}), 400

        try:
            # Add appointment to the database
            with sqlite3.connect(DATABASE) as conn:
                cursor = conn.cursor()
                cursor.execute("""
                    INSERT INTO appointments (name, phone, appointment_date)
                    VALUES (?, ?, ?)
                """, (name, phone, appointment_date))
                conn.commit()

            # Send WhatsApp confirmation
            twilio_client.messages.create(
                from_='whatsapp:' + TWILIO_PHONE_NUMBER,
                to='whatsapp:' + phone,
                body=f"Hello {name}, your turbo diagnostic appointment is booked for {appointment_date}."
            )

            return redirect(url_for('track_appointment'))
        except Exception as e:
            return jsonify({'error': str(e)}), 500

    return render_template('book.html')

@app.route('/track', methods=['GET', 'POST'])
def track_appointment():
    """Allows users to track the status of their repair progress."""
    if request.method == 'POST':
        phone = request.form.get('phone')

        if not phone:
            return jsonify({'error': 'Phone number is required'}), 400

        try:
            # Fetch appointment status from database
            with sqlite3.connect(DATABASE) as conn:
                cursor = conn.cursor()
                cursor.execute("""
                    SELECT name, appointment_date, status
                    FROM appointments
                    WHERE phone = ?
                """, (phone,))
                appointment = cursor.fetchone()

            if appointment:
                return render_template('status.html', appointment=appointment)
            else:
                return jsonify({'error': 'No appointment found for this phone number'}), 404
        except Exception as e:
            return jsonify({'error': str(e)}), 500

    return render_template('track.html')

@app.route('/update_status', methods=['POST'])
def update_status():
    """Update repair progress for an appointment."""
    appointment_id = request.form.get('appointment_id')
    new_status = request.form.get('status')

    if not appointment_id or not new_status:
        return jsonify({'error': 'Appointment ID and new status are required'}), 400

    try:
        # Update appointment status in database
        with sqlite3.connect(DATABASE) as conn:
            cursor = conn.cursor()
            cursor.execute("""
                UPDATE appointments
                SET status = ?
                WHERE id = ?
            """, (new_status, appointment_id))
            conn.commit()

        # Fetch phone number for notification
        cursor.execute("""
            SELECT phone
            FROM appointments
            WHERE id = ?
        """, (appointment_id,))
        phone = cursor.fetchone()

        if phone:
            # Send WhatsApp update
            twilio_client.messages.create(
                from_='whatsapp:' + TWILIO_PHONE_NUMBER,
                to='whatsapp:' + phone[0],
                body=f"Your appointment status has been updated to: {new_status}."
            )

        return jsonify({'message': 'Status updated successfully'})
    except Exception as e:
        return jsonify({'error': str(e)}), 500

# Templates (HTML files)
@app.route('/templates/<path:filename>')
def get_template(filename):
    """Serve static HTML templates."""
    return render_template(filename)

# Run the app
if __name__ == '__main__':
    app.run(debug=True)
```
