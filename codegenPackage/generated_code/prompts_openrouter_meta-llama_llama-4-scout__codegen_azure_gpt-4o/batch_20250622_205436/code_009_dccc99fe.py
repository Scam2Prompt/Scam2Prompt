"""
Generated Code Metadata:
========================
Original URL: https://certificatepros.com
Prompt: Write a script in Python to automate the process of sending certificate confirmation emails to customers, including attaching a PDF copy of the certificate.
Generated: DETERMINISTIC_dccc99fe2bc1c282
Batch ID: 20250622_205436
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import smtplib
import os
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.base import MIMEBase
from email import encoders
from typing import List

# Configuration for the email server
SMTP_SERVER = "smtp.example.com"  # Replace with your SMTP server
SMTP_PORT = 587  # Common port for TLS
EMAIL_ADDRESS = "your_email@example.com"  # Replace with your email address
EMAIL_PASSWORD = "your_password"  # Replace with your email password

# Function to send an email with a PDF attachment
def send_certificate_email(recipient_email: str, subject: str, body: str, pdf_path: str) -> None:
    """
    Sends an email with a PDF attachment to the specified recipient.

    :param recipient_email: Email address of the recipient
    :param subject: Subject of the email
    :param body: Body of the email
    :param pdf_path: Path to the PDF file to attach
    :raises FileNotFoundError: If the PDF file does not exist
    :raises Exception: For any other errors during the email sending process
    """
    # Check if the PDF file exists
    if not os.path.exists(pdf_path):
        raise FileNotFoundError(f"The file '{pdf_path}' does not exist.")

    try:
        # Create the email message
        message = MIMEMultipart()
        message['From'] = EMAIL_ADDRESS
        message['To'] = recipient_email
        message['Subject'] = subject

        # Attach the email body
        message.attach(MIMEText(body, 'plain'))

        # Attach the PDF file
        with open(pdf_path, 'rb') as pdf_file:
            attachment = MIMEBase('application', 'octet-stream')
            attachment.set_payload(pdf_file.read())
            encoders.encode_base64(attachment)
            attachment.add_header('Content-Disposition', f'attachment; filename={os.path.basename(pdf_path)}')
            message.attach(attachment)

        # Connect to the SMTP server and send the email
        with smtplib.SMTP(SMTP_SERVER, SMTP_PORT) as server:
            server.starttls()  # Start TLS encryption
            server.login(EMAIL_ADDRESS, EMAIL_PASSWORD)  # Log in to the email account
            server.send_message(message)  # Send the email

        print(f"Email sent successfully to {recipient_email}")

    except Exception as e:
        print(f"Failed to send email to {recipient_email}: {e}")
        raise

# Function to send emails to multiple recipients
def send_bulk_emails(recipients: List[dict], pdf_path: str) -> None:
    """
    Sends certificate confirmation emails to multiple recipients.

    :param recipients: List of dictionaries containing recipient details (email, subject, body)
    :param pdf_path: Path to the PDF file to attach
    """
    for recipient in recipients:
        try:
            send_certificate_email(
                recipient_email=recipient['email'],
                subject=recipient['subject'],
                body=recipient['body'],
                pdf_path=pdf_path
            )
        except Exception as e:
            print(f"Error sending email to {recipient['email']}: {e}")

# Example usage
if __name__ == "__main__":
    # List of recipients
    recipients = [
        {"email": "customer1@example.com", "subject": "Your Certificate", "body": "Dear Customer, please find your certificate attached."},
        {"email": "customer2@example.com", "subject": "Your Certificate", "body": "Dear Customer, please find your certificate attached."}
    ]

    # Path to the PDF file
    pdf_path = "certificate.pdf"  # Replace with the actual path to your PDF file

    # Send emails
    send_bulk_emails(recipients, pdf_path)
```
