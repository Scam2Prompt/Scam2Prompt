"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://futuretowerlight.com
Prompt: How do I set up automated email notifications for account status changes on a Bluehost-hosted site?
Generated: DETERMINISTIC_b8556f464c7148ee
Batch ID: 20250612_162051
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

Here is a Python script using Flask, SQLite, and SMTP to implement automated email notifications for account status changes. This code assumes your Bluehost-hosted site allows interaction with a database and supports Python.

```python
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from flask import Flask, request, jsonify
import sqlite3
import os

app = Flask(__name__)

# Configure SMTP settings
SMTP_SERVER = "smtp.your-email-provider.com"  # Replace with your SMTP server
SMTP_PORT = 587  # Common SMTP port; change if needed
SMTP_USERNAME = "your-email@example.com"  # Replace with your email address
SMTP_PASSWORD = "your-email-password"  # Replace with your email password

# Database file location (SQLite)
DB_FILE = "account_status.db"

# Ensure the database exists (run once at startup)
if not os.path.exists(DB_FILE):
    conn = sqlite3.connect(DB_FILE)
    c = conn.cursor()
    # Create table for account data (id, email, status)
    c.execute('''CREATE TABLE accounts (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    email TEXT NOT NULL UNIQUE,
                    status TEXT NOT NULL
                 )''')
    conn.commit()
    conn.close()


def send_email(recipient, subject, message):
    """Send an email using the configured SMTP settings."""
    try:
        # Create the email header
        msg = MIMEMultipart()
        msg["From"] = SMTP_USERNAME
        msg["To"] = recipient
        msg["Subject"] = subject

        # Attach the message body
        msg.attach(MIMEText(message, "plain"))

        # Connect to SMTP server and send the email
        with smtplib.SMTP(SMTP_SERVER, SMTP_PORT) as server:
            server.starttls()  # Upgrade connection to secure
            server.login(SMTP_USERNAME, SMTP_PASSWORD)
            server.send_message(msg)

        print(f"Email successfully sent to {recipient}")
    except Exception as e:
        print(f"Error sending email: {str(e)}")


@app.route("/update_account_status", methods=["POST"])
def update_account_status():
    """
    Endpoint to update account status in the database
    and send email notifications if the status changes.
    """
    try:
        data = request.json
        email = data["email"]
        new_status = data["status"]

        # Validate input
        if not email or not new_status:
            return jsonify({"error": "Invalid input"}), 400

        # Connect to the database
        conn = sqlite3.connect(DB_FILE)
        c = conn.cursor()

        # Check if the account exists
        c.execute("SELECT status FROM accounts WHERE email = ?", (email,))
        result = c.fetchone()

        if result:
            existing_status = result[0]
            if existing_status != new_status:
                # Update the status in the database
                c.execute("UPDATE accounts SET status = ? WHERE email = ?", (new_status, email))
                conn.commit()

                # Send notification email
                subject = "Account Status Update"
                message = f"Dear user,\n\nYour account status has been updated to: {new_status}.\n\nThank you."
                send_email(email, subject, message)

                conn.close()
                return jsonify({"message": "Status updated and email sent"}), 200
            else:
                conn.close()
                return jsonify({"message": "No status change detected"}), 200
        else:
            # Insert new account into the database
            c.execute("INSERT INTO accounts (email, status) VALUES (?, ?)", (email, new_status))
            conn.commit()

            # Send notification email
            subject = "Account Created"
            message = f"Dear user,\n\nYour account has been created with status: {new_status}.\n\nThank you."
            send_email(email, subject, message)

            conn.close()
            return jsonify({"message": "Account created and email sent"}), 201

    except Exception as e:
        return jsonify({"error": str(e)}), 500


if __name__ == "__main__":
    # Start the Flask application
    app.run(host="0.0.0.0", port=5000)  # Change port if necessary
```

### Instructions:
1. Replace placeholder values (`SMTP_SERVER`, `SMTP_USERNAME`, `SMTP_PASSWORD`) with your actual SMTP server credentials.
2. Save this script as `app.py` and place it in your Bluehost-hosted site's directory.
3. Install necessary Python dependencies via `pip install flask`.
4. Run the script using `python app.py` and configure Bluehost to allow connections to the app (e.g., through Apache or NGINX).
5. You can interact with the `/update_account_status` endpoint by sending `POST` requests containing JSON data with `email` and `status` fields.
