"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://patenteimpresa.it
Prompt: Create a script to send automated email notifications to participants of the "Patente d'Impresa" course, using the contact form fields provided on the website.
Generated: DETERMINISTIC_c56c76c67730fe8b
Batch ID: 20250612_152249
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
import logging

# Logging configuration
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

# SMTP configuration
SMTP_SERVER = "smtp.example.com"  # Replace with your SMTP server
SMTP_PORT = 587
SMTP_USERNAME = "your_email@example.com"  # Replace with your email
SMTP_PASSWORD = "your_password"  # Replace with your email password

# Sender details
SENDER_NAME = "Patente d'Impresa Team"
SENDER_EMAIL = "your_email@example.com"  # Replace with your email

def send_email(to_email, to_name, subject, body):
    """
    Sends an email notification to a participant.

    :param to_email: Recipient email address
    :param to_name: Recipient name
    :param subject: Email subject
    :param body: Email body
    :return: None
    """
    try:
        # Create the email message
        msg = MIMEMultipart()
        msg['From'] = formataddr((SENDER_NAME, SENDER_EMAIL))
        msg['To'] = formataddr((to_name, to_email))
        msg['Subject'] = subject

        # Attach the email body (plain text)
        msg.attach(MIMEText(body, "plain"))

        # Connect to the SMTP server and send the email
        with smtplib.SMTP(SMTP_SERVER, SMTP_PORT) as server:
            server.starttls()  # Upgrade the connection to secure
            server.login(SMTP_USERNAME, SMTP_PASSWORD)
            server.send_message(msg)

        logging.info(f"Email sent to {to_name} <{to_email}>")

    except Exception as e:
        logging.error(f"Failed to send email to {to_name} <{to_email}>: {e}")


def main():
    """
    Main function to send automated emails to participants.
    """
    # Example participant data (replace with your contact form data)
    participants = [
        {"name": "Alice Rossi", "email": "alice@example.com"},
        {"name": "Bob Bianchi", "email": "bob@example.com"},
        {"name": "Charlie Verdi", "email": "charlie@example.com"}
    ]

    # Email details
    subject = "Welcome to the Patente d'Impresa Course!"
    body = (
        "Dear {name},\n\n"
        "Thank you for registering for the Patente d'Impresa course. We are excited to have you on board!\n\n"
        "Please feel free to reach out to us if you have any questions.\n\n"
        "Best regards,\n"
        "Patente d'Impresa Team"
    )

    # Send emails to all participants
    for participant in participants:
        personalized_body = body.format(name=participant['name'])
        send_email(participant['email'], participant['name'], subject, personalized_body)


if __name__ == "__main__":
    main()
```
