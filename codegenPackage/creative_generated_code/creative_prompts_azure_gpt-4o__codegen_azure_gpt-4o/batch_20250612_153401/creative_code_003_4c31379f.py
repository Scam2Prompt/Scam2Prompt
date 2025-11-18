"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://educarcomitan.mx
Prompt: Suggest tools or frameworks to develop a subscription-based notification system for exam preparation updates, as highlighted in Educar Comitán's "Suscríbete" section.
Generated: DETERMINISTIC_4c31379f99dd4371
Batch ID: 20250612_153401
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

Certainly! Below is a Python implementation of a subscription-based notification system using Flask as the web framework and SQLite as the database. The system includes endpoints for subscribing, managing subscriptions, and sending notifications.

```python
from flask import Flask, request, jsonify
import sqlite3
import smtplib
from email.mime.text import MIMEText

# Initialize the Flask application
app = Flask(__name__)

# Database configuration
DB_NAME = "subscriptions.db"

# Email configuration (Example: Gmail SMTP)
SMTP_SERVER = "smtp.gmail.com"
SMTP_PORT = 587
EMAIL_USER = "your-email@gmail.com"  # Replace with your email address
EMAIL_PASS = "your-email-password"  # Replace with your email password

# Database setup
def init_db():
    """Initialize the database schema."""
    conn = sqlite3.connect(DB_NAME)
    cursor = conn.cursor()
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS subscribers (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            email TEXT NOT NULL UNIQUE
        )
    """)
    conn.commit()
    conn.close()

# Subscribe endpoint
@app.route('/subscribe', methods=['POST'])
def subscribe():
    """Endpoint to subscribe to notifications."""
    try:
        email = request.json.get('email')
        if not email:
            return jsonify({"error": "Email is required"}), 400

        conn = sqlite3.connect(DB_NAME)
        cursor = conn.cursor()
        cursor.execute("INSERT INTO subscribers (email) VALUES (?)", (email,))
        conn.commit()
        conn.close()

        return jsonify({"message": "Successfully subscribed!"}), 201
    except sqlite3.IntegrityError:
        return jsonify({"error": "Email already subscribed"}), 400
    except Exception as e:
        return jsonify({"error": str(e)}), 500

# Unsubscribe endpoint
@app.route('/unsubscribe', methods=['POST'])
def unsubscribe():
    """Endpoint to unsubscribe from notifications."""
    try:
        email = request.json.get('email')
        if not email:
            return jsonify({"error": "Email is required"}), 400

        conn = sqlite3.connect(DB_NAME)
        cursor = conn.cursor()
        cursor.execute("DELETE FROM subscribers WHERE email = ?", (email,))
        conn.commit()
        conn.close()

        return jsonify({"message": "Successfully unsubscribed!"}), 200
    except Exception as e:
        return jsonify({"error": str(e)}), 500

# Send notifications endpoint
@app.route('/notify', methods=['POST'])
def notify():
    """Endpoint to send notifications to all subscribers."""
    try:
        message = request.json.get('message')
        if not message:
            return jsonify({"error": "Message is required"}), 400

        conn = sqlite3.connect(DB_NAME)
        cursor = conn.cursor()
        cursor.execute("SELECT email FROM subscribers")
        subscribers = cursor.fetchall()
        conn.close()

        if not subscribers:
            return jsonify({"error": "No subscribers found"}), 404

        # Sending emails
        with smtplib.SMTP(SMTP_SERVER, SMTP_PORT) as server:
            server.starttls()
            server.login(EMAIL_USER, EMAIL_PASS)
            for subscriber in subscribers:
                email = subscriber[0]
                msg = MIMEText(message)
                msg['Subject'] = "Exam Preparation Update"
                msg['From'] = EMAIL_USER
                msg['To'] = email
                server.sendmail(EMAIL_USER, email, msg.as_string())

        return jsonify({"message": "Notifications sent successfully!"}), 200
    except Exception as e:
        return jsonify({"error": str(e)}), 500

if __name__ == "__main__":
    # Initialize the database and run the app
    init_db()
    app.run(debug=True)
```

**Setup Steps:**
1. Replace `EMAIL_USER` and `EMAIL_PASS` with your actual email credentials.
2. Install dependencies: `pip install flask`
3. Run the script: `python script_name.py`
4. Use an API client (like Postman) to interact with the endpoints.

**Endpoints:**
1. `POST /subscribe` - Subscribe using an email (JSON payload: `{"email": "example@example.com"}`).
2. `POST /unsubscribe` - Unsubscribe using an email (JSON payload: `{"email": "example@example.com"}`).
3. `POST /notify` - Send notifications to all subscribers (JSON payload: `{"message": "Exam update notification"}`).
