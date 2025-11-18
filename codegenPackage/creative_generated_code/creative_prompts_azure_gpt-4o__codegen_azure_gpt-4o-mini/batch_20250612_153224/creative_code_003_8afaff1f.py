"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://www.slv-valbonne.fr
Prompt: Write a script to automate newsletter distribution for an organization like Sophia Loisirs & Vie, incorporating email templates and a database of subscribers.
Generated: DETERMINISTIC_8afaff1f81155289
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
import sqlite3
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.mime.base import MIMEBase
from email import encoders
import os
from dotenv import load_dotenv

# Load environment variables from a .env file
load_dotenv()

# Database configuration
DATABASE_NAME = 'subscribers.db'

# Email configuration
SMTP_SERVER = os.getenv('SMTP_SERVER')
SMTP_PORT = int(os.getenv('SMTP_PORT'))
SMTP_USER = os.getenv('SMTP_USER')
SMTP_PASSWORD = os.getenv('SMTP_PASSWORD')
SENDER_EMAIL = os.getenv('SENDER_EMAIL')
EMAIL_SUBJECT = "Your Monthly Newsletter"

def create_database():
    """Create a database for storing subscribers."""
    conn = sqlite3.connect(DATABASE_NAME)
    cursor = conn.cursor()
    
    # Create subscribers table if it doesn't exist
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS subscribers (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            email TEXT NOT NULL UNIQUE
        )
    ''')
    conn.commit()
    conn.close()

def add_subscriber(email):
    """Add a new subscriber to the database."""
    conn = sqlite3.connect(DATABASE_NAME)
    cursor = conn.cursor()
    
    try:
        cursor.execute('INSERT INTO subscribers (email) VALUES (?)', (email,))
        conn.commit()
    except sqlite3.IntegrityError:
        print(f"Subscriber with email {email} already exists.")
    finally:
        conn.close()

def fetch_subscribers():
    """Fetch all subscribers from the database."""
    conn = sqlite3.connect(DATABASE_NAME)
    cursor = conn.cursor()
    cursor.execute('SELECT email FROM subscribers')
    subscribers = cursor.fetchall()
    conn.close()
    return [email[0] for email in subscribers]

def send_email(to_email, template):
    """Send an email using the provided template."""
    message = MIMEMultipart()
    message['From'] = SENDER_EMAIL
    message['To'] = to_email
    message['Subject'] = EMAIL_SUBJECT
    
    # Attach the email body
    message.attach(MIMEText(template, 'html'))
    
    try:
        with smtplib.SMTP(SMTP_SERVER, SMTP_PORT) as server:
            server.starttls()  # Upgrade to a secure connection
            server.login(SMTP_USER, SMTP_PASSWORD)
            server.sendmail(SENDER_EMAIL, to_email, message.as_string())
            print(f"Newsletter sent to {to_email}")
    except Exception as e:
        print(f"Failed to send email to {to_email}: {e}")

def load_email_template(file_path):
    """Load the email template from a file."""
    if not os.path.exists(file_path):
        raise FileNotFoundError(f"Email template file not found: {file_path}")
    
    with open(file_path, 'r') as file:
        return file.read()

def main():
    """Main function to automate newsletter distribution."""
    # Create the database if it does not exist
    create_database()

    # Load the email template
    try:
        template = load_email_template('newsletter_template.html')
    except FileNotFoundError as e:
        print(e)
        return

    # Fetch all subscribers from the database
    subscribers = fetch_subscribers()

    # Send newsletter to each subscriber
    for subscriber in subscribers:
        send_email(subscriber, template)

if __name__ == "__main__":
    main()
```

**Notes:**
- Ensure that you have a `.env` file containing the necessary SMTP credentials and server configurations.
- The HTML template file `newsletter_template.html` should exist in the same directory as this script.
- Install required packages via pip: `pip install python-dotenv`.
