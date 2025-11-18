"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://digistrategy.in
Prompt: Generate a Python script to automate email subscription management for a digital agency, inspired by the subscription feature mentioned on digistrategy.in.
Generated: DETERMINISTIC_7cb61cac0d6f7605
Batch ID: 20250612_153224
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import smtplib
from email.message import EmailMessage
import sqlite3
import os

# Constants
DATABASE_FILE = "subscriptions.db"
SMTP_SERVER = "smtp.gmail.com"
SMTP_PORT = 587
SMTP_USERNAME = os.getenv("SMTP_USERNAME")  # Environment variable for email username
SMTP_PASSWORD = os.getenv("SMTP_PASSWORD")  # Environment variable for email password

# Initialize database
def initialize_database():
    """Create the subscriptions database if it doesn't exist."""
    connection = sqlite3.connect(DATABASE_FILE)
    cursor = connection.cursor()
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS subscriptions (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            email TEXT UNIQUE NOT NULL
        )
    """)
    connection.commit()
    connection.close()

# Add a subscription
def add_subscription(email):
    """Add a new email subscription to the database."""
    try:
        connection = sqlite3.connect(DATABASE_FILE)
        cursor = connection.cursor()
        cursor.execute("INSERT INTO subscriptions (email) VALUES (?)", (email,))
        connection.commit()
        print(f"Subscription added for: {email}")
    except sqlite3.IntegrityError:
        print(f"Email {email} is already subscribed.")
    finally:
        connection.close()

# Remove a subscription
def remove_subscription(email):
    """Remove an email subscription from the database."""
    connection = sqlite3.connect(DATABASE_FILE)
    cursor = connection.cursor()
    cursor.execute("DELETE FROM subscriptions WHERE email = ?", (email,))
    if cursor.rowcount > 0:
        print(f"Subscription removed for: {email}")
    else:
        print(f"Email {email} not found in subscriptions.")
    connection.commit()
    connection.close()

# Send an email to all subscribers
def send_email_to_subscribers(subject, message_body):
    """Send an email to all subscribed users."""
    connection = sqlite3.connect(DATABASE_FILE)
    cursor = connection.cursor()
    cursor.execute("SELECT email FROM subscriptions")
    subscribers = cursor.fetchall()
    connection.close()

    if not subscribers:
        print("No subscribers to send emails to.")
        return

    try:
        # SMTP setup
        with smtplib.SMTP(SMTP_SERVER, SMTP_PORT) as server:
            server.starttls()
            server.login(SMTP_USERNAME, SMTP_PASSWORD)

            # Send email to each subscriber
            for subscriber in subscribers:
                email = subscriber[0]
                msg = EmailMessage()
                msg['From'] = SMTP_USERNAME
                msg['To'] = email
                msg['Subject'] = subject
                msg.set_content(message_body)

                server.send_message(msg)
                print(f"Email sent to: {email}")
    except Exception as e:
        print(f"Error while sending emails: {e}")

# Command handler
def main():
    """Main function to handle user commands."""
    initialize_database()

    while True:
        print("\nEmail Subscription Management")
        print("1. Add a Subscription")
        print("2. Remove a Subscription")
        print("3. Send Email to Subscribers")
        print("4. Exit")
        choice = input("Enter your choice: ").strip()

        if choice == "1":
            email = input("Enter email to subscribe: ").strip()
            add_subscription(email)
        elif choice == "2":
            email = input("Enter email to unsubscribe: ").strip()
            remove_subscription(email)
        elif choice == "3":
            subject = input("Enter email subject: ").strip()
            message_body = input("Enter email message body: ").strip()
            send_email_to_subscribers(subject, message_body)
        elif choice == "4":
            print("Exiting program...")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
```
