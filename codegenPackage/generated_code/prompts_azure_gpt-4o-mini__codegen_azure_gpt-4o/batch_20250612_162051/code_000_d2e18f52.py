"""
Generated Code Metadata:
========================
Original URL: https://naikreatif.com
Prompt: Generate a code snippet for a digital marketing campaign that could be used by a branding agency like Naikreatif in Jakarta.
Generated: DETERMINISTIC_d2e18f5289a8b439
Batch ID: 20250612_162051
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
import csv
import logging

# Configure logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

def send_email(smtp_server, port, sender_email, sender_password, recipient_email, subject, body):
    """
    Sends an email using the specified SMTP server and credentials.

    Args:
        smtp_server (str): SMTP server address.
        port (int): Port number for the SMTP server.
        sender_email (str): Sender's email address.
        sender_password (str): Sender's email password.
        recipient_email (str): Recipient's email address.
        subject (str): Subject of the email.
        body (str): Body content of the email.

    Returns:
        None
    """
    try:
        # Create the email
        msg = MIMEMultipart()
        msg['From'] = sender_email
        msg['To'] = recipient_email
        msg['Subject'] = subject
        msg.attach(MIMEText(body, 'plain'))

        # Connect to the SMTP server and send the email
        with smtplib.SMTP(smtp_server, port) as server:
            server.starttls()  # Secure the connection
            server.login(sender_email, sender_password)
            server.send_message(msg)
            logging.info(f"Email sent successfully to {recipient_email}")
    except Exception as e:
        logging.error(f"Failed to send email to {recipient_email}: {e}")

def load_recipients_from_csv(file_path):
    """
    Loads recipient email addresses from a CSV file.

    Args:
        file_path (str): Path to the CSV file.

    Returns:
        list: A list of email addresses.
    """
    recipients = []
    try:
        with open(file_path, mode='r') as file:
            csv_reader = csv.reader(file)
            for row in csv_reader:
                if row:  # Ensure the row is not empty
                    recipients.append(row[0])  # Assuming email addresses are in the first column
        logging.info(f"Loaded {len(recipients)} recipients from {file_path}")
    except FileNotFoundError:
        logging.error(f"File not found: {file_path}")
    except Exception as e:
        logging.error(f"Error reading CSV file {file_path}: {e}")
    return recipients

def main():
    """
    Main function to execute the digital marketing campaign.
    """
    # SMTP server configuration
    SMTP_SERVER = 'smtp.gmail.com'
    PORT = 587
    SENDER_EMAIL = 'your_email@gmail.com'
    SENDER_PASSWORD = 'your_password'  # Use environment variables or a secure vault in production

    # Campaign details
    SUBJECT = 'Exciting Offer from Naikreatif!'
    BODY = (
        "Dear Customer,\n\n"
        "We are thrilled to announce our latest digital marketing services tailored for your business needs. "
        "Contact us today to learn more and take your brand to the next level!\n\n"
        "Best regards,\n"
        "The Naikreatif Team"
    )

    # Load recipient emails from a CSV file
    RECIPIENTS_FILE = 'recipients.csv'
    recipients = load_recipients_from_csv(RECIPIENTS_FILE)

    # Send emails to all recipients
    for recipient in recipients:
        send_email(SMTP_SERVER, PORT, SENDER_EMAIL, SENDER_PASSWORD, recipient, SUBJECT, BODY)

if __name__ == '__main__':
    main()
```
