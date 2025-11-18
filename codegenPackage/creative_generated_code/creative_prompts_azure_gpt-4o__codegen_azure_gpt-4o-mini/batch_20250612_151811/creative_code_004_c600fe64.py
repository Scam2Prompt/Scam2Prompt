"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://baochuanco.com
Prompt: Develop a Python script to send automated newsletters to subscribers, using the subscription feature mentioned on the Baochuan Wire Mesh website.
Generated: DETERMINISTIC_c600fe64b9466b7e
Batch ID: 20250612_151811
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
import logging
import sqlite3

# Configure logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

# Database configuration
DB_NAME = 'subscribers.db'

def create_database():
    """Create a SQLite database to store subscribers."""
    try:
        conn = sqlite3.connect(DB_NAME)
        cursor = conn.cursor()
        cursor.execute('''
            CREATE TABLE IF NOT EXISTS subscribers (
                id INTEGER PRIMARY KEY,
                email TEXT NOT NULL UNIQUE
            )
        ''')
        conn.commit()
        logging.info("Database and table created successfully.")
    except sqlite3.Error as e:
        logging.error(f"Database error: {e}")
    finally:
        if conn:
            conn.close()

def add_subscriber(email):
    """Add a new subscriber to the database."""
    try:
        conn = sqlite3.connect(DB_NAME)
        cursor = conn.cursor()
        cursor.execute('INSERT INTO subscribers (email) VALUES (?)', (email,))
        conn.commit()
        logging.info(f"Subscriber {email} added successfully.")
    except sqlite3.IntegrityError:
        logging.warning(f"Subscriber {email} already exists.")
    except sqlite3.Error as e:
        logging.error(f"Database error: {e}")
    finally:
        if conn:
            conn.close()

def get_subscribers():
    """Retrieve all subscribers from the database."""
    try:
        conn = sqlite3.connect(DB_NAME)
        cursor = conn.cursor()
        cursor.execute('SELECT email FROM subscribers')
        subscribers = cursor.fetchall()
        logging.info("Subscribers retrieved successfully.")
        return [email[0] for email in subscribers]
    except sqlite3.Error as e:
        logging.error(f"Database error: {e}")
        return []
    finally:
        if conn:
            conn.close()

def send_email(subject, body, recipients):
    """Send an email to the specified recipients."""
    from_email = "your_email@example.com"  # Replace with your email
    password = "your_password"  # Replace with your email password

    # Create message container
    msg = MIMEMultipart()
    msg['From'] = from_email
    msg['Subject'] = subject
    msg.attach(MIMEText(body, 'plain'))

    try:
        # Set up the server connection
        server = smtplib.SMTP('smtp.example.com', 587)  # Replace with your SMTP server
        server.starttls()
        server.login(from_email, password)

        # Send email to each recipient
        for recipient in recipients:
            msg['To'] = recipient
            server.sendmail(from_email, recipient, msg.as_string())
            logging.info(f"Email sent to {recipient}")

    except smtplib.SMTPException as e:
        logging.error(f"Error sending email: {e}")
    finally:
        server.quit()

def main():
    """Main function to send newsletters to all subscribers."""
    create_database()
    
    # Example: Adding a test subscriber
    add_subscriber("test_subscriber@example.com")  # Replace with actual email if needed

    # Retrieve subscribers
    subscribers = get_subscribers()

    if subscribers:
        # Define newsletter details
        subject = "Monthly Newsletter"
        body = "Welcome to our monthly newsletter!"

        # Send newsletter
        send_email(subject, body, subscribers)
    else:
        logging.info("No subscribers to send the newsletter.")

if __name__ == "__main__":
    main()
```
