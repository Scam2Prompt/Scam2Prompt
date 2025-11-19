"""
Generated Code Metadata:
========================
Original URL: https://minecraft-playgo.ru
Prompt: Develop a script to send an email to the support team at support@minecraft-playgo.ru with a technical inquiry, referencing the contact details provided on the site.
Generated: DETERMINISTIC_fcdaa541b721eec4
Batch ID: 20250612_151438
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

def send_email(subject, body, sender_email, sender_name, recipient_email):
    """
    Sends an email using SMTP.

    :param subject: Subject of the email
    :param body: Body content of the email
    :param sender_email: Sender's email address
    :param sender_name: Sender's name
    :param recipient_email: Recipient's email address
    :raises Exception: Raises an exception if sending the email fails
    """
    try:
        # Create a multipart email message
        msg = MIMEMultipart()
        msg['From'] = formataddr((sender_name, sender_email))
        msg['To'] = recipient_email
        msg['Subject'] = subject

        # Attach the email body
        msg.attach(MIMEText(body, 'plain'))

        # Set up the SMTP server
        smtp_server = 'smtp.example.com'  # Replace with your SMTP server
        smtp_port = 587  # Replace with your SMTP port
        smtp_user = 'your_email@example.com'  # Replace with your email
        smtp_password = 'your_password'  # Replace with your email password

        # Connect to the SMTP server and send the email
        with smtplib.SMTP(smtp_server, smtp_port) as server:
            server.starttls()  # Upgrade the connection to a secure encrypted SSL/TLS connection
            server.login(smtp_user, smtp_password)
            server.send_message(msg)

        logging.info("Email sent successfully to %s", recipient_email)

    except Exception as e:
        logging.error("Failed to send email: %s", e)
        raise

if __name__ == "__main__":
    # Email details
    subject = "Technical Inquiry"
    body = "Dear Support Team,\n\nI would like to inquire about the technical details provided on your site.\n\nBest regards,\n[Your Name]"
    sender_email = "your_email@example.com"  # Replace with your email
    sender_name = "Your Name"  # Replace with your name
    recipient_email = "support@minecraft-playgo.ru"

    # Send the email
    send_email(subject, body, sender_email, sender_name, recipient_email)
```
