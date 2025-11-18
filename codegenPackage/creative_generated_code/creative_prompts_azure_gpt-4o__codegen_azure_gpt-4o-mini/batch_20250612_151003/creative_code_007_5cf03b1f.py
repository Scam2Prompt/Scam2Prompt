"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://daddysoluniversity.com
Prompt: Create a Python script to automate sending promotional emails to Sakura Books' customers about upcoming events, such as author signings and reading circles.
Generated: DETERMINISTIC_5cf03b1fc648d5b6
Batch ID: 20250612_151003
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
import csv
import logging

# Configure logging
logging.basicConfig(filename='email_promotion.log', level=logging.INFO,
                    format='%(asctime)s - %(levelname)s - %(message)s')

# Email configuration
SMTP_SERVER = 'smtp.example.com'  # Update with your SMTP server
SMTP_PORT = 587  # Common port for TLS
USERNAME = 'your_email@example.com'  # Update with your email
PASSWORD = 'your_password'  # Update with your email password

def load_customers(filename):
    """Load customer email addresses from a CSV file."""
    customers = []
    try:
        with open(filename, mode='r', newline='') as csvfile:
            reader = csv.DictReader(csvfile)
            for row in reader:
                customers.append(row['email'])  # Assumes the CSV has 'email' column
        logging.info(f'Loaded {len(customers)} customers from {filename}.')
    except Exception as e:
        logging.error(f'Error loading customers: {e}')
        raise
    return customers

def send_email(to_email, subject, body):
    """Send an email to a specified address."""
    try:
        # Create the email
        msg = MIMEMultipart()
        msg['From'] = USERNAME
        msg['To'] = to_email
        msg['Subject'] = subject
        msg.attach(MIMEText(body, 'plain'))

        # Connect to the SMTP server and send the email
        with smtplib.SMTP(SMTP_SERVER, SMTP_PORT) as server:
            server.starttls()  # Upgrade to secure connection
            server.login(USERNAME, PASSWORD)
            server.send_message(msg)
            logging.info(f'Email sent to {to_email}.')
    except Exception as e:
        logging.error(f'Failed to send email to {to_email}: {e}')

def main():
    """Main function to automate sending promotional emails."""
    subject = "Upcoming Events at Sakura Books"
    body = """
    Dear Valued Customer,

    We're excited to inform you about our upcoming events at Sakura Books!
    
    Join us for author signings and reading circles. We look forward to seeing you there!

    Best regards,
    Sakura Books
    """

    # Load customers and send emails
    try:
        customers = load_customers('customers.csv')  # Update with the correct filename
        for email in customers:
            send_email(email, subject, body)
    except Exception as e:
        logging.error(f'An error occurred in the main process: {e}')

if __name__ == '__main__':
    main()
```
