"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://degen-4g1.pages.dev
Prompt: Illustrate how to implement a feature for users to receive updates on upcoming drops and product releases from Highlight.
Generated: DETERMINISTIC_e43c0501be7abd0e
Batch ID: 20250612_162207
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

# Configuration for the email server
SMTP_SERVER = "smtp.example.com"
SMTP_PORT = 587
EMAIL_ADDRESS = "your-email@example.com"
EMAIL_PASSWORD = "your-email-password"

# Database file to store user subscriptions
DATABASE_FILE = "subscriptions.db"

def initialize_database():
    """
    Creates the subscriptions database if it doesn't exist.
    """
    try:
        conn = sqlite3.connect(DATABASE_FILE)
        cursor = conn.cursor()
        # Create a table to store user email subscriptions
        cursor.execute("""
        CREATE TABLE IF NOT EXISTS subscriptions (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            email TEXT NOT NULL UNIQUE
        )
        """)
        conn.commit()
    except sqlite3.Error as e:
        print(f"Error initializing the database: {e}")
    finally:
        conn.close()

def subscribe_user(email):
    """
    Adds a user's email to the subscription list.
    """
    try:
        conn = sqlite3.connect(DATABASE_FILE)
        cursor = conn.cursor()
        cursor.execute("INSERT INTO subscriptions (email) VALUES (?)", (email,))
        conn.commit()
        print(f"Subscription successful for email: {email}")
    except sqlite3.IntegrityError:
        print(f"Email already subscribed: {email}")
    except sqlite3.Error as e:
        print(f"Error subscribing user: {e}")
    finally:
        conn.close()

def send_updates(subject, message):
    """
    Sends product updates to all subscribed users via email.
    """
    try:
        conn = sqlite3.connect(DATABASE_FILE)
        cursor = conn.cursor()
        cursor.execute("SELECT email FROM subscriptions")
        subscribers = cursor.fetchall()
        
        if not subscribers:
            print("No subscribers to send updates to.")
            return
        
        for subscriber in subscribers:
            email = subscriber[0]
            
            # Compose the email
            msg = MIMEMultipart()
            msg["From"] = EMAIL_ADDRESS
            msg["To"] = email
            msg["Subject"] = subject
            msg.attach(MIMEText(message, "plain"))
            
            # Send the email
            with smtplib.SMTP(SMTP_SERVER, SMTP_PORT) as server:
                server.starttls()
                server.login(EMAIL_ADDRESS, EMAIL_PASSWORD)
                server.sendmail(EMAIL_ADDRESS, email, msg.as_string())
        
        print(f"Updates sent to {len(subscribers)} subscribers.")
    except sqlite3.Error as e:
        print(f"Error retrieving subscribers from database: {e}")
    except smtplib.SMTPException as e:
        print(f"Error sending email updates: {e}")
    finally:
        conn.close()

# Example usage
if __name__ == "__main__":
    initialize_database()
    
    # Subscribe users (this would normally come from user input in production)
    subscribe_user("user1@example.com")
    subscribe_user("user2@example.com")
    
    # Send an update
    send_updates(
        subject="Upcoming Product Releases!",
        message="Get ready for some exciting new drops from Highlight! Stay tuned!"
    )
```
