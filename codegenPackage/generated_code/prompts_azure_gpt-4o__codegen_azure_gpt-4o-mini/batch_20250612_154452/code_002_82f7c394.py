"""
Generated Code Metadata:
========================
Original URL: https://gala-games-home-f.blogspot.com
Prompt: Generate a Python script to automate email subscription for sending updates on interior design trends and exclusive materials, similar to the "Fique por Dentro" feature on the website.
Generated: DETERMINISTIC_82f7c394fdc70452
Batch ID: 20250612_154452
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
                email TEXT NOT NULL UNIQUE
            )
        ''')
        conn.commit()

def send_email(to_email):
    """Send a subscription confirmation email to the user."""
    from_email = "your_email@example.com"  # Replace with your email
    password = "your_password"  # Replace with your email password

    # Create the email content
    subject = "Subscription Confirmation"
    body = "Thank you for subscribing to our updates on interior design trends and exclusive materials!"

    # Set up the email server
    msg = MIMEMultipart()
    msg['From'] = from_email
    msg['To'] = to_email
    msg['Subject'] = subject
    msg.attach(MIMEText(body, 'plain'))

    try:
        with smtplib.SMTP('smtp.example.com', 587) as server:  # Replace with your SMTP server
            server.starttls()
            server.login(from_email, password)
            server.send_message(msg)
    except Exception as e:
        print(f"Error sending email: {e}")

@app.route('/subscribe', methods=['POST'])
def subscribe():
    """Endpoint to handle subscription requests."""
    email = request.json.get('email')

    if not email:
        return jsonify({"error": "Email is required"}), 400

    try:
        with sqlite3.connect(DATABASE) as conn:
            cursor = conn.cursor()
            cursor.execute('INSERT INTO subscriptions (email) VALUES (?)', (email,))
            conn.commit()
            send_email(email)
            return jsonify({"message": "Subscription successful!"}), 201
    except sqlite3.IntegrityError:
        return jsonify({"error": "Email already subscribed"}), 409
    except Exception as e:
        return jsonify({"error": str(e)}), 500

if __name__ == '__main__':
    init_db()  # Initialize the database
    app.run(debug=True)  # Run the Flask application
```
