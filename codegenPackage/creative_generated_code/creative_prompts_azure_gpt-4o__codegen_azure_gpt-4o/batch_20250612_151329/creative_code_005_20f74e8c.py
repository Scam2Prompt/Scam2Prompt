"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://hamptons-uk.com
Prompt: Develop a marketing automation workflow in Python for increasing hotel sales, using the principles from Hampton's Hotel Institute's International Tourism & Hospitality Management course.
Generated: DETERMINISTIC_20f74e8c8465bdf1
Batch ID: 20250612_151329
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
import logging
import sqlite3
from datetime import datetime, timedelta

# Configure logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

# Database setup to store customer data and email history
DB_FILE = "hotel_marketing.db"


def setup_database():
    """Sets up the database schema for the marketing workflow."""
    conn = sqlite3.connect(DB_FILE)
    cursor = conn.cursor()
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS customers (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT NOT NULL,
            email TEXT NOT NULL UNIQUE,
            last_booking_date DATE
        )
    """)
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS email_history (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            customer_id INTEGER NOT NULL,
            email_subject TEXT NOT NULL,
            email_body TEXT NOT NULL,
            sent_date DATE NOT NULL,
            FOREIGN KEY (customer_id) REFERENCES customers (id)
        )
    """)
    conn.commit()
    conn.close()


def send_email(smtp_server, port, username, password, recipient_email, subject, body):
    """
    Sends an email using SMTP server.
    
    Args:
        smtp_server (str): SMTP server address.
        port (int): SMTP server port.
        username (str): Sender email username.
        password (str): Sender email password.
        recipient_email (str): Recipient email address.
        subject (str): Email subject.
        body (str): Email body content.
    
    Returns:
        bool: True if email sent successfully, False otherwise.
    """
    try:
        # Create the email message
        message = MIMEMultipart()
        message['From'] = username
        message['To'] = recipient_email
        message['Subject'] = subject
        message.attach(MIMEText(body, 'plain'))
        
        # Connect to the SMTP server and send email
        with smtplib.SMTP(smtp_server, port) as server:
            server.starttls()  # Secure the connection
            server.login(username, password)
            server.send_message(message)
            
        logging.info(f"Email sent successfully to {recipient_email}")
        return True
    except Exception as e:
        logging.error(f"Failed to send email to {recipient_email}: {str(e)}")
        return False


def generate_email_content(customer_name, days_since_last_booking):
    """
    Generates email content based on the customer's profile and activity.
    
    Args:
        customer_name (str): Name of the customer.
        days_since_last_booking (int): Days since the customer's last booking.
    
    Returns:
        tuple: Email subject and email body.
    """
    subject = "Exclusive Offer Just For You!"
    body = f"""
    Hi {customer_name},
    
    We noticed it’s been {days_since_last_booking} days since your last booking with us!
    As a valued customer, we’d love to welcome you back with an exclusive 20% discount on your next stay.
    
    Book now to take advantage of this limited-time offer. We look forward to seeing you again!
    
    Best regards,
    The Hotel Team
    """
    return subject, body


def run_marketing_workflow():
    """
    Executes the marketing automation workflow.
    """
    smtp_server = "smtp.example.com"
    port = 587
    email_username = "your-email@example.com"
    email_password = "your-email-password"
    
    conn = sqlite3.connect(DB_FILE)
    cursor = conn.cursor()
    
    # Fetch customers who haven't booked in the last 30 days
    thirty_days_ago = datetime.now() - timedelta(days=30)
    cursor.execute("SELECT id, name, email, last_booking_date FROM customers WHERE last_booking_date < ?", (thirty_days_ago,))
    customers_to_email = cursor.fetchall()
    
    for customer in customers_to_email:
        customer_id, name, email, last_booking_date = customer
        days_since_last_booking = (datetime.now() - datetime.strptime(last_booking_date, "%Y-%m-%d")).days
        
        # Generate email content
        subject, body = generate_email_content(name, days_since_last_booking)
        
        # Send email
        if send_email(smtp_server, port, email_username, email_password, email, subject, body):
            # Record email history
            cursor.execute("""
                INSERT INTO email_history (customer_id, email_subject, email_body, sent_date)
                VALUES (?, ?, ?, ?)
            """, (customer_id, subject, body, datetime.now().strftime("%Y-%m-%d")))
            conn.commit()
    
    conn.close()


if __name__ == "__main__":
    # Ensure database is set up
    setup_database()
    
    # Run the marketing workflow
    run_marketing_workflow()
```
