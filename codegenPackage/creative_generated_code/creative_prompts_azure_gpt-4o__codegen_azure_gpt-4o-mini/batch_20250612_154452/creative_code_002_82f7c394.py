"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://gala-games-home-f.blogspot.com
Prompt: Generate a Python script to automate email subscription for sending updates on interior design trends and exclusive materials, similar to the "Fique por Dentro" feature on the website.
Generated: DETERMINISTIC_82f7c394fdc70452
Batch ID: 20250612_154452
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from flask import Flask, request, jsonify
import sqlite3

app = Flask(__name__)

# Database setup for subscription storage
def init_db():
    conn = sqlite3.connect('subscriptions.db')
    cursor = conn.cursor()
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS subscribers (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            email TEXT UNIQUE NOT NULL
        )
    ''')
    conn.commit()
    conn.close()

# Function to send email notification
def send_email(subscriber_email):
    # Email configuration
    sender_email = "your_email@example.com"
    sender_password = "your_password"
    subject = "Welcome to Fique por Dentro!"
    body = "Thank you for subscribing! Stay tuned for updates on interior design trends and exclusive materials."

    # Prepare the email
    msg = MIMEMultipart()
    msg['From'] = sender_email
    msg['To'] = subscriber_email
    msg['Subject'] = subject
    msg.attach(MIMEText(body, 'plain'))

    # Send the email
    try:
        with smtplib.SMTP('smtp.example.com', 587) as server:
            server.starttls()  # Upgrade the connection
            server.login(sender_email, sender_password)
            server.send_message(msg)
            print(f"Email sent to {subscriber_email}")
    except Exception as e:
        print(f"Failed to send email to {subscriber_email}: {e}")

# API endpoint for email subscription
@app.route('/subscribe', methods=['POST'])
def subscribe():
    data = request.get_json()
    email = data.get('email')

    # Validate email format
    if not email or '@' not in email:
        return jsonify({"error": "Invalid email address"}), 400

    # Add subscriber to the database
    try:
        conn = sqlite3.connect('subscriptions.db')
        cursor = conn.cursor()
        cursor.execute('INSERT INTO subscribers (email) VALUES (?)', (email,))
        conn.commit()
        conn.close()
        
        # Send welcome email
        send_email(email)
        
        return jsonify({"message": "Subscription successful!"}), 201
    except sqlite3.IntegrityError:
        return jsonify({"error": "Email already subscribed"}), 409
    except Exception as e:
        return jsonify({"error": str(e)}), 500

if __name__ == '__main__':
    init_db()  # Initialize the database
    app.run(debug=True)  # Run the Flask app
```

Make sure to replace `"your_email@example.com"`, `"your_password"`, and `"smtp.example.com"` with your actual email credentials and SMTP server details before running the script.
