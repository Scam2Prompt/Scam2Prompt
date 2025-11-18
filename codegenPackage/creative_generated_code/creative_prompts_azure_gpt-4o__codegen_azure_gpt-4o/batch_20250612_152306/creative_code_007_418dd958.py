"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://connectnetwork.lojavirtualnuvem.com.br
Prompt: Generate a script to manage newsletter subscriptions and email promotions for an online store, similar to the "Receba todas as promoções" feature on the Connect Network website.
Generated: DETERMINISTIC_418dd95824385f57
Batch ID: 20250612_152306
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import re
import sqlite3
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

# Database setup
DB_NAME = "newsletter.db"

# Email server configurations
SMTP_SERVER = "smtp.example.com"
SMTP_PORT = 587
SMTP_USER = "your-email@example.com"
SMTP_PASSWORD = "your-email-password"

def setup_database():
    """
    Initialize the database with a subscription table.
    """
    conn = sqlite3.connect(DB_NAME)
    cursor = conn.cursor()
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS subscriptions (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            email TEXT UNIQUE NOT NULL,
            subscribed_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
        )
    ''')
    conn.commit()
    conn.close()

def is_valid_email(email):
    """
    Validate email format using a regex pattern.
    """
    regex = r'^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$'
    return re.match(regex, email) is not None

def subscribe_user(email):
    """
    Add a user's email to the subscription list.
    """
    if not is_valid_email(email):
        raise ValueError("Invalid email format.")

    try:
        conn = sqlite3.connect(DB_NAME)
        cursor = conn.cursor()
        cursor.execute("INSERT INTO subscriptions (email) VALUES (?)", (email,))
        conn.commit()
        print(f"Subscription successful for: {email}")
    except sqlite3.IntegrityError:
        print(f"Email {email} is already subscribed.")
    except Exception as e:
        print(f"An error occurred: {e}")
    finally:
        conn.close()

def send_promotion_email(email, subject, content):
    """
    Send a promotional email to a specified address.
    """
    try:
        # Create the email message
        msg = MIMEMultipart()
        msg['From'] = SMTP_USER
        msg['To'] = email
        msg['Subject'] = subject
        msg.attach(MIMEText(content, 'html'))

        # Connect to the SMTP server and send the email
        with smtplib.SMTP(SMTP_SERVER, SMTP_PORT) as server:
            server.starttls()
            server.login(SMTP_USER, SMTP_PASSWORD)
            server.sendmail(SMTP_USER, email, msg.as_string())
            print(f"Promotional email sent to: {email}")
    except smtplib.SMTPException as e:
        print(f"Failed to send email to {email}: {e}")

def send_promotion_to_all(subject, content):
    """
    Send a promotional email to all subscribed users.
    """
    try:
        conn = sqlite3.connect(DB_NAME)
        cursor = conn.cursor()
        cursor.execute("SELECT email FROM subscriptions")
        subscribers = cursor.fetchall()

        for (email,) in subscribers:
            send_promotion_email(email, subject, content)
    except Exception as e:
        print(f"An error occurred while sending promotions: {e}")
    finally:
        conn.close()

if __name__ == "__main__":
    # Setup the database
    setup_database()

    # Example usage
    print("Newsletter Subscription System")
    while True:
        print("\nOptions:")
        print("1. Subscribe to Newsletter")
        print("2. Send a Promotion Email to All Subscribers")
        print("3. Exit")

        choice = input("Select an option (1/2/3): ")
        
        if choice == "1":
            email = input("Enter your email to subscribe: ").strip()
            try:
                subscribe_user(email)
            except ValueError as e:
                print(e)
        elif choice == "2":
            subject = input("Enter the email subject: ").strip()
            content = input("Enter the email content (HTML supported): ").strip()
            send_promotion_to_all(subject, content)
        elif choice == "3":
            print("Exiting Newsletter Subscription System. Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")
```
