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
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
import csv
import logging
from typing import List

# Configure logging
logging.basicConfig(
    filename='email_automation.log',
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s'
)

# Constants
SMTP_SERVER = 'smtp.gmail.com'  # Replace with your SMTP server
SMTP_PORT = 587
EMAIL_USERNAME = 'your_email@example.com'  # Replace with your email address
EMAIL_PASSWORD = 'your_password'  # Replace with your email password
PROMOTIONAL_SUBJECT = "Upcoming Events at Sakura Books!"
CUSTOMER_DATA_FILE = 'customers.csv'  # CSV file containing customer details (name, email)
BATCH_SIZE = 50  # Number of emails to send per SMTP connection (optional throttling)

# Email template
EMAIL_TEMPLATE = """
Dear {name},

We are excited to invite you to our upcoming events at Sakura Books:

- Author Signings
- Reading Circles
- And much more!

Stay tuned for more updates on our website and social media.

We hope to see you soon!

Best regards,
The Sakura Books Team
"""


def read_customer_contacts(file_path: str) -> List[dict]:
    """
    Reads customer data from a CSV file.
    Assumes the CSV contains 'name' and 'email' columns.

    :param file_path: Path to the CSV file containing customer data.
    :return: A list of dictionaries with customer details.
    """
    try:
        contacts = []
        with open(file_path, mode='r', newline='', encoding='utf-8') as csvfile:
            reader = csv.DictReader(csvfile)
            for row in reader:
                if 'name' in row and 'email' in row:
                    contacts.append({'name': row['name'], 'email': row['email']})
        logging.info(f"Successfully read {len(contacts)} contacts from {file_path}.")
        return contacts
    except FileNotFoundError:
        logging.error(f"File not found: {file_path}.")
        raise
    except Exception as e:
        logging.error(f"An error occurred while reading the file: {e}.")
        raise


def send_email(to_email: str, subject: str, body: str):
    """
    Sends an email using SMTP.

    :param to_email: Recipient's email address.
    :param subject: Subject of the email.
    :param body: Body content of the email.
    """
    try:
        # Create MIME email
        message = MIMEMultipart()
        message['From'] = EMAIL_USERNAME
        message['To'] = to_email
        message['Subject'] = subject
        message.attach(MIMEText(body, 'plain'))

        # Establish SMTP connection
        with smtplib.SMTP(SMTP_SERVER, SMTP_PORT) as server:
            server.starttls()  # Upgrade the connection to secure
            server.login(EMAIL_USERNAME, EMAIL_PASSWORD)
            server.sendmail(EMAIL_USERNAME, to_email, message.as_string())
            logging.info(f"Email sent successfully to {to_email}.")
    except smtplib.SMTPException as e:
        logging.error(f"SMTP error while sending email to {to_email}: {e}")
    except Exception as e:
        logging.error(f"Unexpected error while sending email to {to_email}: {e}")


def send_promotional_emails(customers: List[dict]):
    """
    Sends promotional emails to a list of customers.

    :param customers: List of customer dictionaries, each containing 'name' and 'email'.
    """
    for index, customer in enumerate(customers):
        # Prepare email content
        email_body = EMAIL_TEMPLATE.format(name=customer['name'])
        try:
            send_email(customer['email'], PROMOTIONAL_SUBJECT, email_body)

            # Optional throttling (batching)
            if (index + 1) % BATCH_SIZE == 0:
                logging.info("Throttling... Waiting before sending the next batch.")
        except Exception as e:
            logging.error(f"Failed to send email to {customer['email']}: {e}")


if __name__ == "__main__":
    try:
        # Read customer data
        customer_contacts = read_customer_contacts(CUSTOMER_DATA_FILE)

        # Send emails
        send_promotional_emails(customer_contacts)
        logging.info("All emails processed.")
    except Exception as e:
        logging.critical(f"Email automation script failed: {e}")
```

Make sure to replace placeholder values (`your_email@example.com`, `your_password`, etc.) with real credentials or use environment variables for better security. Update the `CUSTOMER_DATA_FILE` path as needed.
