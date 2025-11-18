"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://mariahousekeepers.net
Prompt: Write a program to send automated follow-up emails to customers after one-time cleaning services, asking for feedback and offering discounts for recurring services.
Generated: DETERMINISTIC_79374bf00a811714
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
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
import logging
from datetime import datetime, timedelta
import sqlite3

# Configure logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

# Email server settings
SMTP_SERVER = "smtp.example.com"  # Replace with your SMTP server
SMTP_PORT = 587  # Common port for TLS
SMTP_USERNAME = "your_email@example.com"  # Replace with your email address
SMTP_PASSWORD = "your_password"  # Replace with your email password

# Discount offer details
DISCOUNT_CODE = "RECURRING20"
DISCOUNT_PERCENTAGE = 20

# Database file path
DB_FILE = "customers.db"

def send_email(to_address, subject, body):
    """
    Sends an email using the configured SMTP server.
    
    :param to_address: Recipient email address
    :param subject: Subject of the email
    :param body: Body of the email
    """
    try:
        # Create the email
        message = MIMEMultipart()
        message['From'] = SMTP_USERNAME
        message['To'] = to_address
        message['Subject'] = subject
        message.attach(MIMEText(body, 'plain'))

        # Connect to the SMTP server and send the email
        with smtplib.SMTP(SMTP_SERVER, SMTP_PORT) as server:
            server.starttls()  # Encrypt the connection
            server.login(SMTP_USERNAME, SMTP_PASSWORD)
            server.send_message(message)

        logging.info(f"Email sent successfully to {to_address}")
    except Exception as e:
        logging.error(f"Failed to send email to {to_address}: {e}")

def get_customers_for_follow_up():
    """
    Retrieves customers who need follow-up emails from the database.
    
    :return: List of customer records
    """
    try:
        conn = sqlite3.connect(DB_FILE)
        cursor = conn.cursor()

        # Fetch customers whose cleaning service date was 7 days ago
        seven_days_ago = datetime.now() - timedelta(days=7)
        cursor.execute("""
            SELECT id, name, email, service_date FROM customers 
            WHERE service_date = ? AND follow_up_sent = 0
        """, (seven_days_ago.strftime('%Y-%m-%d'),))

        customers = cursor.fetchall()
        conn.close()

        return customers
    except sqlite3.Error as e:
        logging.error(f"Database error: {e}")
        return []

def mark_follow_up_sent(customer_id):
    """
    Marks the follow-up email as sent in the database.
    
    :param customer_id: ID of the customer
    """
    try:
        conn = sqlite3.connect(DB_FILE)
        cursor = conn.cursor()
        cursor.execute("""
            UPDATE customers SET follow_up_sent = 1 WHERE id = ?
        """, (customer_id,))
        conn.commit()
        conn.close()
    except sqlite3.Error as e:
        logging.error(f"Failed to update follow-up status for customer {customer_id}: {e}")

def main():
    """
    Main function to send follow-up emails to customers.
    """
    customers = get_customers_for_follow_up()

    if not customers:
        logging.info("No customers to send follow-up emails to.")
        return

    for customer in customers:
        customer_id, name, email, service_date = customer

        # Email content
        subject = "We value your feedback!"
        body = f"""
        Hi {name},

        Thank you for choosing our cleaning services on {service_date}. 
        We'd love to hear your feedback regarding your experience.

        As a token of our appreciation, we'd like to offer you a {DISCOUNT_PERCENTAGE}% discount on our recurring cleaning services. 
        Use the code '{DISCOUNT_CODE}' during your next booking.

        Best regards,
        The Cleaning Services Team
        """

        # Send the email
        send_email(email, subject, body)

        # Mark email as sent in the database
        mark_follow_up_sent(customer_id)

if __name__ == "__main__":
    main()
```
