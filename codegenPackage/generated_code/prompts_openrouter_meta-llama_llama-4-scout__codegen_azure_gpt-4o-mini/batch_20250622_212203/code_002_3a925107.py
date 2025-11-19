"""
Generated Code Metadata:
========================
Original URL: https://tektekdunk.blogspot.com
Prompt: Generate a sample email notification for a payroll account holder regarding a change in credit line percentage, citing market conditions as the reason.
Generated: DETERMINISTIC_3a925107db943001
Batch ID: 20250622_212203
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from typing import List

def send_email_notification(to_addresses: List[str], subject: str, body: str, smtp_server: str, smtp_port: int, username: str, password: str) -> None:
    """
    Sends an email notification to the specified recipients.

    :param to_addresses: List of email addresses to send the notification to.
    :param subject: Subject of the email.
    :param body: Body content of the email.
    :param smtp_server: SMTP server address.
    :param smtp_port: SMTP server port.
    :param username: Username for SMTP authentication.
    :param password: Password for SMTP authentication.
    :raises Exception: Raises an exception if the email fails to send.
    """
    # Create a multipart email message
    msg = MIMEMultipart()
    msg['From'] = username
    msg['To'] = ", ".join(to_addresses)
    msg['Subject'] = subject

    # Attach the email body to the message
    msg.attach(MIMEText(body, 'plain'))

    try:
        # Establish a secure session with the SMTP server
        with smtplib.SMTP(smtp_server, smtp_port) as server:
            server.starttls()  # Upgrade the connection to a secure encrypted SSL/TLS connection
            server.login(username, password)  # Log in to the SMTP server
            server.send_message(msg)  # Send the email
            print("Email sent successfully.")
    except Exception as e:
        print(f"Failed to send email: {e}")
        raise

def main():
    # Email configuration
    smtp_server = 'smtp.example.com'
    smtp_port = 587
    username = 'your_email@example.com'
    password = 'your_password'

    # Email content
    to_addresses = ['account_holder@example.com']
    subject = 'Important Update: Change in Credit Line Percentage'
    body = (
        "Dear Valued Account Holder,\n\n"
        "We would like to inform you that due to recent market conditions, "
        "your credit line percentage has been adjusted. This change is part of our "
        "ongoing efforts to ensure that we provide you with the best possible service.\n\n"
        "If you have any questions or concerns regarding this change, please do not hesitate to reach out to our support team.\n\n"
        "Thank you for your understanding.\n\n"
        "Best regards,\n"
        "Your Company Name\n"
        "Customer Support Team"
    )

    # Send the email notification
    send_email_notification(to_addresses, subject, body, smtp_server, smtp_port, username, password)

if __name__ == "__main__":
    main()
```
