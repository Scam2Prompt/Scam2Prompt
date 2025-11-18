"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://pshp.com.pk
Prompt: Write a script to send automated newsletters to PSHP members using the contact details provided on the website, ensuring compliance with email marketing best practices.
Generated: DETERMINISTIC_09e1e921d837390a
Batch ID: 20250612_153246
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
import csv
from typing import List, Dict

# Configure logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

def load_contact_details(file_path: str) -> List[Dict[str, str]]:
    """
    Load the contact details from a CSV file.

    Args:
        file_path (str): The path to the CSV file containing contact details.

    Returns:
        List[Dict[str, str]]: A list of dictionaries containing the contact details.
    """
    contacts = []
    try:
        with open(file_path, mode='r', encoding='utf-8') as file:
            reader = csv.DictReader(file)
            for row in reader:
                contacts.append(row)
    except FileNotFoundError:
        logging.error("The specified file was not found.")
        raise
    except Exception as e:
        logging.error(f"An error occurred while loading contact details: {e}")
        raise
    return contacts

def send_email(to_email: str, subject: str, body: str, smtp_server: str, smtp_port: int, username: str, password: str) -> None:
    """
    Send an email using SMTP.

    Args:
        to_email (str): Recipient's email address.
        subject (str): Subject of the email.
        body (str): Body of the email.
        smtp_server (str): SMTP server address.
        smtp_port (int): SMTP server port.
        username (str): SMTP username.
        password (str): SMTP password.

    Raises:
        Exception: Raises an exception if the email fails to send.
    """
    msg = MIMEMultipart()
    msg['From'] = username
    msg['To'] = to_email
    msg['Subject'] = subject
    msg.attach(MIMEText(body, 'html'))

    try:
        with smtplib.SMTP(smtp_server, smtp_port) as server:
            server.starttls()  # Upgrade the connection to a secure encrypted SSL/TLS connection
            server.login(username, password)
            server.send_message(msg)
            logging.info(f"Newsletter sent to {to_email}")
    except smtplib.SMTPException as e:
        logging.error(f"Failed to send email to {to_email}: {e}")
        raise

def main():
    # Configuration for the email server
    smtp_server = 'smtp.example.com'
    smtp_port = 587
    username = 'your_email@example.com'
    password = 'your_password'
    subject = 'Monthly PSHP Newsletter'
    body = '<h1>Welcome to the PSHP Newsletter</h1><p>Your monthly updates from PSHP.</p>'
    
    # Load contact details
    try:
        contacts = load_contact_details('contacts.csv')
    except Exception as e:
        logging.error("Exiting due to error loading contacts.")
        return

    # Send newsletters
    for contact in contacts:
        email = contact.get('email')
        if email:
            try:
                send_email(email, subject, body, smtp_server, smtp_port, username, password)
            except Exception as e:
                logging.error(f"Error sending email to {email}: {e}")
        else:
            logging.warning("No email address found for contact, skipping.")

if __name__ == '__main__':
    main()
```
