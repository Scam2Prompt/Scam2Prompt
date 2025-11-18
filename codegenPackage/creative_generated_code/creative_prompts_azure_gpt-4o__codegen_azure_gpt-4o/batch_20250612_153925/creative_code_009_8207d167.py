"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://avabase.vercel.app
Prompt: Generate code to implement a notification system for crypto campaign updates, allowing users to sign up for alerts, similar to the "Sign up for updates" feature on AVAAI Hunt.
Generated: DETERMINISTIC_8207d167b6de63f5
Batch ID: 20250612_153925
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

# Configuration constants
SMTP_SERVER = "smtp.example.com"
SMTP_PORT = 587
EMAIL_USERNAME = "your_email@example.com"
EMAIL_PASSWORD = "your_password"
DATABASE_FILE = "notifications.db"

# Initialize the SQLite database
def initialize_database():
    """Create the database and necessary tables if they don't exist."""
    connection = sqlite3.connect(DATABASE_FILE)
    cursor = connection.cursor()
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS users (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            email TEXT NOT NULL UNIQUE
        )
    """)
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS campaign_updates (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            title TEXT NOT NULL,
            content TEXT NOT NULL
        )
    """)
    connection.commit()
    connection.close()

# Function to add a user to the notification list
def add_user(email):
    """Add a new user to the notification list."""
    try:
        connection = sqlite3.connect(DATABASE_FILE)
        cursor = connection.cursor()
        cursor.execute("INSERT INTO users (email) VALUES (?)", (email,))
        connection.commit()
        connection.close()
        print(f"User with email {email} has been added to the notification list.")
    except sqlite3.IntegrityError:
        print(f"Email {email} is already registered.")

# Function to add a new campaign update
def add_campaign_update(title, content):
    """Add a new campaign update and send notifications."""
    connection = sqlite3.connect(DATABASE_FILE)
    cursor = connection.cursor()
    cursor.execute("INSERT INTO campaign_updates (title, content) VALUES (?, ?)", (title, content))
    connection.commit()
    
    # Send email notifications to all users
    cursor.execute("SELECT email FROM users")
    users = [row[0] for row in cursor.fetchall()]
    connection.close()

    for user_email in users:
        send_email(user_email, title, content)

# Function to send an email
def send_email(to_email, subject, body):
    """Send an email notification."""
    try:
        # Construct email
        msg = MIMEMultipart()
        msg['From'] = EMAIL_USERNAME
        msg['To'] = to_email
        msg['Subject'] = subject
        msg.attach(MIMEText(body, 'plain'))
        
        # Connect to SMTP server and send email
        server = smtplib.SMTP(SMTP_SERVER, SMTP_PORT)
        server.starttls()
        server.login(EMAIL_USERNAME, EMAIL_PASSWORD)
        server.send_message(msg)
        server.quit()
        
        print(f"Email sent to {to_email}")
    except Exception as e:
        print(f"Failed to send email to {to_email}: {str(e)}")

# Main function to demonstrate functionality
if __name__ == "__main__":
    # Initialize the database
    initialize_database()

    # Example usage
    add_user("user1@example.com")
    add_user("user2@example.com")
    add_campaign_update("New Crypto Campaign Launched!", "Details about the new campaign...")
```

This code sets up a simple notification system using SQLite for storing user emails and campaign updates, and SMTP for email notifications. It ensures proper error handling and adheres to best practices. Replace the placeholders for `SMTP_SERVER`, `EMAIL_USERNAME`, and `EMAIL_PASSWORD` with the actual credentials for a production-ready implementation.
