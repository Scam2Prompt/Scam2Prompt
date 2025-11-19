"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://sembradordevidaac.org
Prompt: How can I write a Python script to send an email to join the Sembrador de Vida community?
Generated: DETERMINISTIC_375e42266a0bc3be
Batch ID: 20250612_135557
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
import os

def send_email(sender_email, sender_name, recipient_email, subject, message_body, smtp_server, smtp_port, login_user, login_password):
    """
    Function to send an email using SMTP.

    Args:
        sender_email (str): The email address of the sender.
        sender_name (str): The display name of the sender.
        recipient_email (str): The email address of the recipient.
        subject (str): The subject of the email.
        message_body (str): The body of the email.
        smtp_server (str): SMTP server address.
        smtp_port (int): SMTP server port.
        login_user (str): Username for SMTP authentication.
        login_password (str): Password for SMTP authentication.

    Returns:
        None
    """
    try:
        # Construct the email
        msg = MIMEMultipart()
        msg['From'] = formataddr((sender_name, sender_email))
        msg['To'] = recipient_email
        msg['Subject'] = subject

        # Attach the message body
        msg.attach(MIMEText(message_body, 'plain'))

        # Connect to the SMTP server
        with smtplib.SMTP(smtp_server, smtp_port) as server:
            server.starttls()  # Upgrade the connection to secure (TLS)
            server.login(login_user, login_password)  # Authenticate
            server.sendmail(sender_email, recipient_email, msg.as_string())  # Send the email
            print("Email sent successfully")
    except Exception as e:
        print(f"An error occurred while sending email: {e}")

if __name__ == "__main__":
    # Configuration values (replace these with actual details)
    SENDER_EMAIL = "your_email@example.com"
    SENDER_NAME = "Your Name"
    RECIPIENT_EMAIL = "recipient_email@example.com"
    SUBJECT = "Join Sembrador de Vida Community"
    MESSAGE_BODY = (
        "Hello,\n\n"
        "We would like to invite you to join the Sembrador de Vida community.\n"
        "Together, we can make a difference in the world by fostering growth, "
        "positivity, and sustainability.\n\n"
        "Best regards,\n"
        "Sembrador de Vida Team"
    )
    SMTP_SERVER = "smtp.example.com"  # Replace with your SMTP server (e.g., smtp.gmail.com)
    SMTP_PORT = 587  # Common SMTP port for TLS
    LOGIN_USER = "your_email@example.com"
    LOGIN_PASSWORD = os.getenv("EMAIL_PASSWORD")  # Use environment variables for sensitive data

    # Send the email
    send_email(SENDER_EMAIL, SENDER_NAME, RECIPIENT_EMAIL, SUBJECT, MESSAGE_BODY, SMTP_SERVER, SMTP_PORT, LOGIN_USER, LOGIN_PASSWORD)
```
