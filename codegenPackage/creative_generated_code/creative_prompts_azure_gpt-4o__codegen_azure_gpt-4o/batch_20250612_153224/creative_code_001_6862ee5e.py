"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://mariahousekeepers.net
Prompt: Recommend an API or library for managing customer bookings and sending automated reminders for cleaning services. Ensure it supports integration with email and phone notifications.
Generated: DETERMINISTIC_6862ee5e40f8fbc6
Batch ID: 20250612_153224
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

Here is the code recommendation using Python and the `Flask` framework with Twilio for phone notifications and `smtplib` for email notifications. We'll use SQLite as the database for simplicity.

```python
from flask import Flask, request, jsonify
import sqlite3
from twilio.rest import Client
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from datetime import datetime, timedelta

app = Flask(__name__)

# Twilio configuration (replace with your credentials)
TWILIO_ACCOUNT_SID = 'your_account_sid'
TWILIO_AUTH_TOKEN = 'your_auth_token'
TWILIO_PHONE_NUMBER = 'your_twilio_phone_number'
twilio_client = Client(TWILIO_ACCOUNT_SID, TWILIO_AUTH_TOKEN)

# Email configuration (replace with your credentials)
SMTP_SERVER = 'smtp.gmail.com'
SMTP_PORT = 587
EMAIL_USERNAME = 'your_email@example.com'
EMAIL_PASSWORD = 'your_email_password'

# Database setup
DATABASE = 'bookings.db'

def init_db():
    """Initialize the database with the required tables."""
    conn = sqlite3.connect(DATABASE)
    cursor = conn.cursor()
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS bookings (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            customer_name TEXT NOT NULL,
            email TEXT,
            phone TEXT,
            booking_time DATETIME NOT NULL,
            reminder_sent INTEGER DEFAULT 0
        )
    ''')
    conn.commit()
    conn.close()

@app.route('/create-booking', methods=['POST'])
def create_booking():
    """
    Endpoint to create a new booking.
    Expects JSON payload with customer_name, email, phone, and booking_time.
    """
    try:
        data = request.json
        customer_name = data['customer_name']
        email = data.get('email', None)
        phone = data.get('phone', None)
        booking_time = datetime.strptime(data['booking_time'], '%Y-%m-%d %H:%M:%S')

        conn = sqlite3.connect(DATABASE)
        cursor = conn.cursor()
        cursor.execute('''
            INSERT INTO bookings (customer_name, email, phone, booking_time)
            VALUES (?, ?, ?, ?)
        ''', (customer_name, email, phone, booking_time))
        conn.commit()
        conn.close()

        return jsonify({'message': 'Booking created successfully'}), 201
    except Exception as e:
        return jsonify({'error': str(e)}), 400

@app.route('/send-reminders', methods=['POST'])
def send_reminders():
    """
    Endpoint to send reminders for bookings that are within 24 hours.
    Triggers both email and phone notifications if available.
    """
    try:
        conn = sqlite3.connect(DATABASE)
        cursor = conn.cursor()
        now = datetime.now()
        reminder_window = now + timedelta(hours=24)

        cursor.execute('''
            SELECT id, customer_name, email, phone, booking_time FROM bookings
            WHERE booking_time <= ? AND reminder_sent = 0
        ''', (reminder_window,))
        bookings = cursor.fetchall()

        for booking in bookings:
            booking_id, customer_name, email, phone, booking_time = booking
            message = f"Reminder: Hi {customer_name}, your cleaning service is scheduled for {booking_time}."

            # Send email notification
            if email:
                try:
                    msg = MIMEMultipart()
                    msg['From'] = EMAIL_USERNAME
                    msg['To'] = email
                    msg['Subject'] = 'Cleaning Service Reminder'
                    msg.attach(MIMEText(message, 'plain'))

                    server = smtplib.SMTP(SMTP_SERVER, SMTP_PORT)
                    server.starttls()
                    server.login(EMAIL_USERNAME, EMAIL_PASSWORD)
                    server.sendmail(EMAIL_USERNAME, email, msg.as_string())
                    server.quit()
                except Exception as email_error:
                    print(f"Error sending email: {email_error}")

            # Send phone notification
            if phone:
                try:
                    twilio_client.messages.create(
                        body=message,
                        from_=TWILIO_PHONE_NUMBER,
                        to=phone
                    )
                except Exception as sms_error:
                    print(f"Error sending SMS: {sms_error}")

            # Mark reminder as sent
            cursor.execute('UPDATE bookings SET reminder_sent = 1 WHERE id = ?', (booking_id,))
            conn.commit()

        conn.close()
        return jsonify({'message': 'Reminders sent successfully'}), 200
    except Exception as e:
        return jsonify({'error': str(e)}), 500

@app.route('/list-bookings', methods=['GET'])
def list_bookings():
    """
    Endpoint to list all bookings.
    Returns a JSON array of bookings.
    """
    try:
        conn = sqlite3.connect(DATABASE)
        cursor = conn.cursor()
        cursor.execute('SELECT * FROM bookings')
        bookings = cursor.fetchall()
        conn.close()

        # Format response
        response = [
            {
                'id': row[0],
                'customer_name': row[1],
                'email': row[2],
                'phone': row[3],
                'booking_time': row[4],
                'reminder_sent': bool(row[5])
            }
            for row in bookings
        ]
        return jsonify(response), 200
    except Exception as e:
        return jsonify({'error': str(e)}), 500

if __name__ == '__main__':
    init_db()
    app.run(debug=True)
```

### Key Details:
1. **Replace Credentials**: Replace placeholders (`your_account_sid`, `your_auth_token`, etc.) with actual values.
2. **Security**: Avoid hardcoding credentials in production; use environment variables.
3. **Dependencies**: Install required packages via `pip install flask twilio` and ensure SMTP server settings match your email provider. Use a secure app password for email.
4. **Database**: Ensure `bookings.db` resides in your server's writable directory.
