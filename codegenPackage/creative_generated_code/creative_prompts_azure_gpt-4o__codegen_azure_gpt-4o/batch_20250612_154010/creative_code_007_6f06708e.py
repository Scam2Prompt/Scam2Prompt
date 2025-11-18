"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://vempire-opal.vercel.app
Prompt: Create an API integration to allow users to sign up for updates and receive notifications about the VEMP Hunt campaign.
Generated: DETERMINISTIC_6f06708e1378c1c4
Batch ID: 20250612_154010
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import flask
from flask import Flask, request, jsonify
import smtplib
from email.mime.text import MIMEText
import sqlite3
import re

app = Flask(__name__)

# Database initialization script
DATABASE = 'vemp_hunt.db'

def init_db():
    """Initialize the SQLite database."""
    conn = sqlite3.connect(DATABASE)
    cursor = conn.cursor()
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS subscribers (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            email TEXT NOT NULL UNIQUE,
            date_subscribed TIMESTAMP DEFAULT CURRENT_TIMESTAMP
        )
    ''')
    conn.commit()
    conn.close()

init_db()

# Utility function for email validation
def is_valid_email(email):
    """Validate email format using regex."""
    email_regex = r'^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$'
    return re.match(email_regex, email) is not None

# Utility function to send email notifications
def send_email_notification(email, campaign_name):
    """
    Send email notification to the subscriber.
    
    :param email: Subscriber's email address
    :param campaign_name: Name of the campaign
    """
    try:
        sender_email = "your_email@example.com"
        sender_password = "your_password"
        smtp_server = "smtp.example.com"
        smtp_port = 587

        subject = f"Updates on the {campaign_name} campaign"
        body = f"Hello,\n\nThank you for subscribing to updates about the {campaign_name} campaign!\nStay tuned for more information.\n\nBest regards,\nThe VEMP Hunt Team"

        message = MIMEText(body)
        message['Subject'] = subject
        message['From'] = sender_email
        message['To'] = email

        with smtplib.SMTP(smtp_server, smtp_port) as server:
            server.starttls()
            server.login(sender_email, sender_password)
            server.sendmail(sender_email, email, message.as_string())
    except Exception as e:
        print(f"Error sending email: {e}")
        raise

# API route to sign up for updates
@app.route('/api/v1/subscribe', methods=['POST'])
def subscribe():
    """
    API endpoint to subscribe for campaign updates.
    
    Request body:
        - email: Subscriber's email address
    """
    try:
        data = request.json
        email = data.get('email')
        campaign_name = "VEMP Hunt"

        # Validate email
        if not email or not is_valid_email(email):
            return jsonify({'error': 'Invalid email address'}), 400

        # Add subscriber to the database
        conn = sqlite3.connect(DATABASE)
        cursor = conn.cursor()
        try:
            cursor.execute('INSERT INTO subscribers (email) VALUES (?)', (email,))
            conn.commit()
        except sqlite3.IntegrityError:
            # Email already exists in the database
            return jsonify({'error': 'Email already subscribed'}), 409
        finally:
            conn.close()

        # Send email notification
        send_email_notification(email, campaign_name)

        return jsonify({'message': 'Successfully subscribed for updates'}), 200

    except Exception as e:
        print(f"Error in subscription process: {e}")
        return jsonify({'error': 'Internal server error'}), 500

# API route to list all subscribers (Admin functionality)
@app.route('/api/v1/subscribers', methods=['GET'])
def list_subscribers():
    """
    API endpoint to list all subscribers.
    """
    try:
        conn = sqlite3.connect(DATABASE)
        cursor = conn.cursor()
        cursor.execute('SELECT id, email, date_subscribed FROM subscribers')
        subscribers = cursor.fetchall()
        conn.close()

        return jsonify({
            'subscribers': [
                {'id': row[0], 'email': row[1], 'date_subscribed': row[2]} 
                for row in subscribers
            ]
        }), 200

    except Exception as e:
        print(f"Error retrieving subscribers: {e}")
        return jsonify({'error': 'Internal server error'}), 500

# Main application entry point
if __name__ == '__main__':
    app.run(debug=True)
```
