"""
Generated Code Metadata:
========================
Original URL: https://harinderfarms.com
Prompt: Write a script to automate the process of sending timely updates and notifications to farmers about their orders and deliveries, similar to Harinder Farms' delivery services.
Generated: DETERMINISTIC_d86a228ae80c2a16
Batch ID: 20250622_210655
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
import schedule
import time
from datetime import datetime, timedelta
import logging

# Configure logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

# Email configuration
SMTP_SERVER = 'smtp.example.com'  # Replace with your SMTP server
SMTP_PORT = 587  # Replace with your SMTP port
USERNAME = 'your_email@example.com'  # Replace with your email
PASSWORD = 'your_password'  # Replace with your email password

# Farmer class to hold order and delivery information
class Farmer:
    def __init__(self, name, email, order_details):
        self.name = name
        self.email = email
        self.order_details = order_details

# List of farmers (this would typically come from a database)
farmers = [
    Farmer('John Doe', 'john@example.com', 'Order #123: 50kg of apples'),
    Farmer('Jane Smith', 'jane@example.com', 'Order #124: 30kg of oranges'),
]

def send_email(to_email, subject, body):
    """Send an email notification to the specified recipient."""
    try:
        msg = MIMEMultipart()
        msg['From'] = USERNAME
        msg['To'] = to_email
        msg['Subject'] = subject

        msg.attach(MIMEText(body, 'plain'))

        with smtplib.SMTP(SMTP_SERVER, SMTP_PORT) as server:
            server.starttls()  # Upgrade the connection to a secure encrypted SSL/TLS connection
            server.login(USERNAME, PASSWORD)
            server.send_message(msg)
            logging.info(f'Email sent to {to_email}')
    except Exception as e:
        logging.error(f'Failed to send email to {to_email}: {e}')

def notify_farmers():
    """Notify all farmers about their orders and deliveries."""
    for farmer in farmers:
        subject = f'Order Update for {farmer.name}'
        body = f'Dear {farmer.name},\n\nYour order details are as follows:\n{farmer.order_details}\n\nThank you for your business!'
        send_email(farmer.email, subject, body)

def schedule_notifications():
    """Schedule notifications to be sent daily at a specific time."""
    schedule.every().day.at("09:00").do(notify_farmers)  # Set the time for notifications

    logging.info('Notification scheduling started. Notifications will be sent daily at 09:00.')

    while True:
        schedule.run_pending()
        time.sleep(60)  # Wait for one minute before checking again

if __name__ == '__main__':
    try:
        schedule_notifications()
    except KeyboardInterrupt:
        logging.info('Notification scheduling stopped by user.')
    except Exception as e:
        logging.error(f'An error occurred: {e}')
```
