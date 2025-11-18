"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://lojaoficial.cloud
Prompt: Write a script to subscribe users to the Études newsletter, ensuring they receive updates on architectural articles and case studies.
Generated: DETERMINISTIC_99c6d0536c2ba0a6
Batch ID: 20250612_153225
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
import sqlite3

# Constants
DB_FILE = "subscriptions.db"      # SQLite database file
SMTP_SERVER = "smtp.example.com"  # Replace with your SMTP server
SMTP_PORT = 587                   # SMTP port (typically 587 for TLS)
EMAIL_ADDRESS = "your_email@example.com"  # Sender email address
EMAIL_PASSWORD = "your_password"         # Sender email password

def initialize_database():
    """
    Initializes the SQLite database to store subscriber information.
    Creates the 'subscribers' table if it doesn't exist.
    """
    try:
        conn = sqlite3.connect(DB_FILE)
        cursor = conn.cursor()
        cursor.execute("""
            CREATE TABLE IF NOT EXISTS subscribers (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                email TEXT NOT NULL UNIQUE,
                name TEXT NOT NULL
            )
        """)
        conn.commit()
    except sqlite3.Error as e:
        print(f"Error initializing the database: {e}")
    finally:
        conn.close()

def add_subscriber(email, name):
    """
    Adds a new subscriber to the database.
    :param email: Email address of the subscriber
    :param name: Name of the subscriber
    """
    try:
        conn = sqlite3.connect(DB_FILE)
        cursor = conn.cursor()
        cursor.execute("INSERT INTO subscribers (email, name) VALUES (?, ?)", (email, name))
        conn.commit()
        print(f"Successfully added subscriber: {name} ({email})")
    except sqlite3.IntegrityError:
        print(f"Error: The email '{email}' is already subscribed.")
    except sqlite3.Error as e:
        print(f"Error adding subscriber: {e}")
    finally:
        conn.close()

def send_subscription_email(email, name):
    """
    Sends a confirmation email to the subscriber.
    :param email: Email address of the subscriber
    :param name: Name of the subscriber
    """
    try:
        # Create the email message
        message = MIMEMultipart()
        message["From"] = EMAIL_ADDRESS
        message["To"] = email
        message["Subject"] = "Welcome to the Études Newsletter!"

        # Email body
        body = f"Hello {name},\n\nThank you for subscribing to the Études newsletter! " \
               f"You'll now receive updates on architectural articles and case studies.\n\nBest regards,\nÉtudes Team"
        message.attach(MIMEText(body, "plain"))

        # Connect to the SMTP server and send the email
        with smtplib.SMTP(SMTP_SERVER, SMTP_PORT) as server:
            server.starttls()  # Secure connection using TLS
            server.login(EMAIL_ADDRESS, EMAIL_PASSWORD)
            server.send_message(message)
        print(f"Confirmation email sent to {email}")
    except smtplib.SMTPException as e:
        print(f"Error sending email: {e}")

def main():
    """
    Main function to subscribe users to the Études newsletter.
    """
    # Initialize the database
    initialize_database()

    # Get user input
    print("Welcome to the Études Newsletter Subscription!")
    name = input("Enter your name: ").strip()
    email = input("Enter your email address: ").strip()

    # Add subscriber to the database and send confirmation email
    add_subscriber(email, name)
    send_subscription_email(email, name)

if __name__ == "__main__":
    main()
```
