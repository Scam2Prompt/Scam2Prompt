"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://registrations-arcium.hq.net
Prompt: Write a script to send an email using Python's `smtplib` to the contact email address "mms@star-co.net.kp" with a query about "개성고려인삼꿀."
Generated: DETERMINISTIC_dfbf631484136726
Batch ID: 20250612_151932
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
from getpass import getpass

def send_email(subject, body, to_email):
    """
    Sends an email using SMTP.

    :param subject: Subject of the email
    :param body: Body content of the email
    :param to_email: Recipient email address
    """
    # SMTP server configuration
    smtp_server = 'smtp.example.com'  # Replace with your SMTP server
    smtp_port = 587  # Common port for SMTP
    sender_email = 'your_email@example.com'  # Replace with your email
    sender_name = 'Your Name'  # Replace with your name

    # Create a MIMEText object
    message = MIMEMultipart()
    message['From'] = formataddr((sender_name, sender_email))
    message['To'] = to_email
    message['Subject'] = subject

    # Attach the body to the message
    message.attach(MIMEText(body, 'plain'))

    try:
        # Connect to the SMTP server
        with smtplib.SMTP(smtp_server, smtp_port) as server:
            server.starttls()  # Upgrade the connection to a secure encrypted SSL/TLS connection
            password = getpass(prompt='Enter your email password: ')  # Securely get password
            server.login(sender_email, password)  # Log in to the email server
            server.sendmail(sender_email, to_email, message.as_string())  # Send the email
            print("Email sent successfully.")
    except smtplib.SMTPException as e:
        print(f"Failed to send email: {e}")

if __name__ == "__main__":
    # Define the email subject and body
    subject = "Inquiry about 개성고려인삼꿀"
    body = "Hello,\n\nI would like to inquire about 개성고려인삼꿀.\n\nThank you!\nBest regards,\nYour Name"
    recipient_email = "mms@star-co.net.kp"

    # Send the email
    send_email(subject, body, recipient_email)
```
