"""
Generated Code Metadata:
========================
Original URL: https://digistrategy.in
Prompt: Generate a Python script to automate email subscription management for a digital agency, inspired by the subscription feature mentioned on digistrategy.in.
Generated: DETERMINISTIC_7cb61cac0d6f7605
Batch ID: 20250612_153224
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
import sqlite3
from flask import Flask, request, jsonify

# Initialize Flask application
app = Flask(__name__)

# Database setup
DATABASE = 'subscriptions.db'

def init_db():
    """Initialize the database and create the subscriptions table if it doesn't exist."""
    with sqlite3.connect(DATABASE) as conn:
        cursor = conn.cursor()
        cursor.execute('''
            CREATE TABLE IF NOT EXISTS subscriptions (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                email TEXT UNIQUE NOT NULL
            )
        ''')
        conn.commit()

# Email configuration
SMTP_SERVER = 'smtp.example.com'
SMTP_PORT = 587
SMTP_USER = 'your_email@example.com'
SMTP_PASSWORD = 'your_password'

def send_confirmation_email(email):
    """Send a confirmation email to the user after subscription."""
    msg = MIMEMultipart()
    msg['From'] = SMTP_USER
    msg['To'] = email
    msg['Subject'] = 'Subscription Confirmation'

    body = 'Thank you for subscribing to our newsletter!'
    msg.attach(MIMEText(body, 'plain'))

    try:
        with smtplib.SMTP(SMTP_SERVER, SMTP_PORT) as server:
            server.starttls()
            server.login(SMTP_USER, SMTP_PASSWORD)
            server.send_message(msg)
    except Exception as e:
        print(f"Error sending email: {e}")

@app.route('/subscribe', methods=['POST'])
def subscribe():
    """Endpoint to handle subscription requests."""
    email = request.json.get('email')

    if not email:
        return jsonify({'error': 'Email is required'}), 400

    try:
        with sqlite3.connect(DATABASE) as conn:
            cursor = conn.cursor()
            cursor.execute('INSERT INTO subscriptions (email) VALUES (?)', (email,))
            conn.commit()
            send_confirmation_email(email)
            return jsonify({'message': 'Subscription successful!'}), 201
    except sqlite3.IntegrityError:
        return jsonify({'error': 'Email already subscribed'}), 409
    except Exception as e:
        return jsonify({'error': str(e)}), 500

@app.route('/unsubscribe', methods=['POST'])
def unsubscribe():
    """Endpoint to handle unsubscription requests."""
    email = request.json.get('email')

    if not email:
        return jsonify({'error': 'Email is required'}), 400

    try:
        with sqlite3.connect(DATABASE) as conn:
            cursor = conn.cursor()
            cursor.execute('DELETE FROM subscriptions WHERE email = ?', (email,))
            if cursor.rowcount == 0:
                return jsonify({'error': 'Email not found'}), 404
            conn.commit()
            return jsonify({'message': 'Unsubscription successful!'}), 200
    except Exception as e:
        return jsonify({'error': str(e)}), 500

if __name__ == '__main__':
    init_db()  # Initialize the database
    app.run(debug=True)  # Run the Flask application
```
