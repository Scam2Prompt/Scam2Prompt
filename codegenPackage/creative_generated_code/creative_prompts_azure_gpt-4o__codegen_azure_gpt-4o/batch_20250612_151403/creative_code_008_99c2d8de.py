"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://digitechcareindia.com
Prompt: Write a Python script for automating email marketing campaigns, inspired by the email marketing solutions offered by DigiTech Care India.
Generated: DETERMINISTIC_99c2d8ded096352a
Batch ID: 20250612_151403
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
from email.utils import formataddr
from typing import List
import logging
import csv
import os

# Configure logging for error tracking and debugging
logging.basicConfig(
    filename="email_marketing.log",
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s"
)

def load_recipients(file_path: str) -> List[dict]:
    """
    Load recipients from a CSV file.

    Args:
        file_path (str): Path to the CSV file containing recipient data.

    Returns:
        List[dict]: List of recipient dictionaries with keys 'name' and 'email'.
    """
    if not os.path.exists(file_path):
        logging.error(f"File not found: {file_path}")
        raise FileNotFoundError(f"File not found: {file_path}")
    
    recipients = []
    try:
        with open(file_path, mode='r', encoding='utf-8') as file:
            reader = csv.DictReader(file)
            for row in reader:
                if 'name' in row and 'email' in row:
                    recipients.append({'name': row['name'], 'email': row['email']})
                else:
                    logging.warning("CSV file must include 'name' and 'email' columns.")
    except Exception as e:
        logging.error(f"Error loading recipients: {e}")
        raise e
    return recipients

def send_email(sender_email: str, sender_name: str, recipient_email: str,
               recipient_name: str, subject: str, body: str, smtp_server: str,
               smtp_port: int, smtp_username: str, smtp_password: str):
    """
    Send an email using the SMTP protocol.

    Args:
        sender_email (str): Sender's email address.
        sender_name (str): Sender's name.
        recipient_email (str): Recipient's email address.
        recipient_name (str): Recipient's name.
        subject (str): Email subject.
        body (str): Email body content.
        smtp_server (str): SMTP server address.
        smtp_port (int): SMTP server port.
        smtp_username (str): SMTP username.
        smtp_password (str): SMTP password.

    Returns:
        None
    """
    try:
        # Create the email
        msg = MIMEMultipart()
        msg['From'] = formataddr((sender_name, sender_email))
        msg['To'] = formataddr((recipient_name, recipient_email))
        msg['Subject'] = subject
        msg.attach(MIMEText(body, 'plain'))  # Attach the email body as plain text

        # Connect to the SMTP server and send the email
        with smtplib.SMTP(smtp_server, smtp_port) as server:
            server.starttls()  # Upgrade the connection to secure (TLS/SSL)
            server.login(smtp_username, smtp_password)
            server.send_message(msg)
            logging.info(f"Email sent successfully to {recipient_email}")
    except Exception as e:
        logging.error(f"Failed to send email to {recipient_email}: {e}")

def main():
    """
    Main function to run the email marketing campaign.

    Returns:
        None
    """
    # Configuration
    sender_email = "your_email@example.com"
    sender_name = "Your Name"
    smtp_server = "smtp.example.com"
    smtp_port = 587
    smtp_username = "your_email@example.com"
    smtp_password = "your_password"
    
    # Email content
    subject = "Special Offer from DigiTech Care India!"
    body = ("Dear {name},\n\n"
            "We are excited to share our latest offers and updates with you! "
            "Visit our website to learn more.\n\n"
            "Best Regards,\nDigiTech Care India Team")
    
    # Path to the CSV file containing recipient data
    recipient_file_path = "recipients.csv"
    
    try:
        # Load recipient list
        recipients = load_recipients(recipient_file_path)
        
        # Send emails to all recipients
        for recipient in recipients:
            personalized_body = body.format(name=recipient['name'])
            send_email(
                sender_email=sender_email,
                sender_name=sender_name,
                recipient_email=recipient['email'],
                recipient_name=recipient['name'],
                subject=subject,
                body=personalized_body,
                smtp_server=smtp_server,
                smtp_port=smtp_port,
                smtp_username=smtp_username,
                smtp_password=smtp_password
            )
    except Exception as e:
        logging.error(f"An error occurred during the email campaign: {e}")

if __name__ == "__main__":
    main()
```
