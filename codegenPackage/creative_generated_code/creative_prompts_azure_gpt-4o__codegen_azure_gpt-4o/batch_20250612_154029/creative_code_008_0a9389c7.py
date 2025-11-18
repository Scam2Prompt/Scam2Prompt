"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://haggis.vercel.app
Prompt: Create a script to send updates to users who sign up for the HAGGIS Hunt campaign, integrating the "Sign up for updates" feature mentioned on the site.
Generated: DETERMINISTIC_0a9389c7b19c930a
Batch ID: 20250612_154029
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
import logging
from typing import List

# Configure logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

# Database setup
DB_NAME = "haggis_hunt.db"

def setup_database():
    """
    Ensure the database and table exists.
    If not, create a new table for storing user sign-ups.
    """
    try:
        conn = sqlite3.connect(DB_NAME)
        cursor = conn.cursor()
        
        # Create table if not exists
        cursor.execute("""
        CREATE TABLE IF NOT EXISTS users (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            email TEXT NOT NULL UNIQUE
        )
        """)
        conn.commit()
    except sqlite3.Error as e:
        logging.error(f"Error setting up the database: {e}")
    finally:
        conn.close()

def add_user(email: str):
    """
    Add a user email to the database.

    Args:
    email (str): The email address of the user.

    Returns:
    bool: True if the user is added successfully, False otherwise.
    """
    try:
        conn = sqlite3.connect(DB_NAME)
        cursor = conn.cursor()
        
        cursor.execute("INSERT INTO users (email) VALUES (?)", (email,))
        conn.commit()
        logging.info(f"Added email to database: {email}")
        return True
    except sqlite3.IntegrityError:
        logging.warning(f"Email already exists in the database: {email}")
        return False
    except sqlite3.Error as e:
        logging.error(f"Database error: {e}")
        return False
    finally:
        conn.close()

def get_all_users() -> List[str]:
    """
    Fetch all user emails from the database.

    Returns:
    List[str]: List of email addresses.
    """
    try:
        conn = sqlite3.connect(DB_NAME)
        cursor = conn.cursor()
        
        cursor.execute("SELECT email FROM users")
        users = [row[0] for row in cursor.fetchall()]
        logging.info(f"Fetched {len(users)} users from the database.")
        return users
    except sqlite3.Error as e:
        logging.error(f"Error fetching users: {e}")
        return []
    finally:
        conn.close()

def send_email_update(recipient_email: str, subject: str, body: str):
    """
    Send an email update to a user.

    Args:
    recipient_email (str): The recipient's email address.
    subject (str): The subject of the email.
    body (str): The body of the email.
    """
    # Email server configuration
    SMTP_SERVER = "smtp.example.com"  # Replace with your SMTP server
    SMTP_PORT = 587  # Replace with your SMTP port
    SMTP_USER = "your_email@example.com"  # Replace with your email address
    SMTP_PASSWORD = "your_password"  # Replace with your email password

    try:
        # Create email
        msg = MIMEMultipart()
        msg["From"] = SMTP_USER
        msg["To"] = recipient_email
        msg["Subject"] = subject
        
        msg.attach(MIMEText(body, "plain"))

        # Connect to SMTP server and send email
        server = smtplib.SMTP(SMTP_SERVER, SMTP_PORT)
        server.starttls()
        server.login(SMTP_USER, SMTP_PASSWORD)
        server.send_message(msg)
        server.quit()
        
        logging.info(f"Email sent successfully to: {recipient_email}")
    except smtplib.SMTPException as e:
        logging.error(f"Error sending email: {e}")

def main():
    """
    Main function to handle the HAGGIS Hunt campaign updates.
    """
    setup_database()

    # Add users for testing
    add_user("test1@example.com")
    add_user("test2@example.com")

    # Fetch all users
    users = get_all_users()
    
    # Email content
    subject = "HAGGIS Hunt Updates"
    body = "Thank you for signing up for HAGGIS Hunt updates. Stay tuned for exciting updates!"

    for user_email in users:
        send_email_update(user_email, subject, body)

if __name__ == "__main__":
    main()
```
