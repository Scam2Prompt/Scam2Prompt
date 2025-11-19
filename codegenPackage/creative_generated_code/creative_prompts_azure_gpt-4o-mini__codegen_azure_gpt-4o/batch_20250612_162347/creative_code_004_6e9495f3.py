"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://codyalt.com
Prompt: Suggest a code snippet for implementing a subscription model for a newsletter like The Infinite Game, aimed at self-improvement and entrepreneurship.
Generated: DETERMINISTIC_6e9495f3cbe3c5b4
Batch ID: 20250612_162347
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
# newsletter_subscription.py

import sqlite3
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

# Database setup (SQLite for simplicity)
DB_PATH = "subscriptions.db"

def initialize_database():
    """
    Initialize the database and create the subscriptions table if it doesn't exist.
    """
    try:
        conn = sqlite3.connect(DB_PATH)
        cursor = conn.cursor()
        cursor.execute("""
            CREATE TABLE IF NOT EXISTS subscriptions (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                email TEXT NOT NULL UNIQUE,
                name TEXT NOT NULL
            )
        """)
        conn.commit()
    except sqlite3.Error as e:
        print(f"Error initializing database: {e}")
    finally:
        conn.close()

def add_subscription(email, name):
    """
    Add a new subscription to the database.
    
    Args:
        email (str): Subscriber's email.
        name (str): Subscriber's name.

    Returns:
        str: Success or error message.
    """
    try:
        conn = sqlite3.connect(DB_PATH)
        cursor = conn.cursor()
        cursor.execute("INSERT INTO subscriptions (email, name) VALUES (?, ?)", (email, name))
        conn.commit()
        return "Subscription added successfully."
    except sqlite3.IntegrityError:
        return "Error: Email already subscribed."
    except sqlite3.Error as e:
        return f"Error adding subscription: {e}"
    finally:
        conn.close()

def send_welcome_email(email, name):
    """
    Send a welcome email to the subscriber.
    
    Args:
        email (str): Subscriber's email.
        name (str): Subscriber's name.
    """
    try:
        # SMTP server configuration
        smtp_server = "smtp.gmail.com"
        smtp_port = 587
        sender_email = "your_email@example.com"
        sender_password = "your_email_password"

        # Create email content
        subject = "Welcome to The Infinite Game Newsletter!"
        body = f"Hi {name},\n\nWelcome to The Infinite Game Newsletter! We're excited to have you on board.\n\nBest regards,\nThe Infinite Game Team"

        msg = MIMEMultipart()
        msg["From"] = sender_email
        msg["To"] = email
        msg["Subject"] = subject
        msg.attach(MIMEText(body, "plain"))

        # Send email
        with smtplib.SMTP(smtp_server, smtp_port) as server:
            server.starttls()  # Secure the connection
            server.login(sender_email, sender_password)
            server.sendmail(sender_email, email, msg.as_string())
        print(f"Welcome email sent to {email}.")
    except Exception as e:
        print(f"Error sending email: {e}")

def subscribe_user():
    """
    Interactive function to subscribe a new user.
    """
    print("Subscribe to The Infinite Game Newsletter")
    email = input("Enter your email: ").strip()
    name = input("Enter your name: ").strip()
    
    if not email or not name:
        print("Error: Email and name cannot be empty.")
        return
    
    status = add_subscription(email, name)
    print(status)
    if "successfully" in status:
        send_welcome_email(email, name)

if __name__ == "__main__":
    # Initialize the database
    initialize_database()
    
    # Subscribe a user
    subscribe_user()
```

### Notes:
- Before running, replace `your_email@example.com` and `your_email_password` with valid credentials for sending emails via SMTP.
- Consider using environment variables or a secrets manager for storing sensitive data like email credentials.
- For production usage, upgrade to a more robust database and email service.
