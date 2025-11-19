"""
Generated Code Metadata:
========================
Original URL: https://linearlive.co.uk
Prompt: Write a Python script to automate sending contact form submissions to a company like Linear Live Limited, including fields for name, email, subject, and message.
Generated: DETERMINISTIC_87a689d9f8b797da
Batch ID: 20250612_150327
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
from email.utils import formataddr
import logging

# Configure logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

def send_contact_form(name, email, subject, message):
    """
    Sends an email with the contact form submission.

    Parameters:
    - name (str): The name of the person submitting the form.
    - email (str): The email address of the person submitting the form.
    - subject (str): The subject of the message.
    - message (str): The content of the message.

    Raises:
    - ValueError: If any of the fields are empty.
    - Exception: For any other errors during the email sending process.
    """
    
    # Validate input fields
    if not all([name, email, subject, message]):
        logging.error("All fields must be filled out.")
        raise ValueError("All fields must be filled out.")

    # Email configuration
    sender_email = "your_email@example.com"  # Replace with your email
    sender_name = "Your Name"  # Replace with your name
    recipient_email = "contact@linearlive.com"  # Replace with the recipient's email
    smtp_server = "smtp.example.com"  # Replace with your SMTP server
    smtp_port = 587  # Common SMTP port for TLS
    smtp_username = "your_email@example.com"  # Replace with your SMTP username
    smtp_password = "your_password"  # Replace with your SMTP password

    # Create the email message
    msg = MIMEMultipart()
    msg['From'] = formataddr((sender_name, sender_email))
    msg['To'] = recipient_email
    msg['Subject'] = subject

    # Create the email body
    body = f"Name: {name}\nEmail: {email}\n\nMessage:\n{message}"
    msg.attach(MIMEText(body, 'plain'))

    try:
        # Connect to the SMTP server and send the email
        with smtplib.SMTP(smtp_server, smtp_port) as server:
            server.starttls()  # Upgrade the connection to a secure encrypted SSL/TLS connection
            server.login(smtp_username, smtp_password)
            server.send_message(msg)
            logging.info("Email sent successfully.")
    except smtplib.SMTPException as e:
        logging.error(f"Failed to send email: {e}")
        raise Exception("An error occurred while sending the email.")

if __name__ == "__main__":
    # Example usage
    try:
        send_contact_form("John Doe", "john.doe@example.com", "Inquiry", "Hello, I would like to know more about your services.")
    except Exception as e:
        logging.error(f"Error: {e}")
```
