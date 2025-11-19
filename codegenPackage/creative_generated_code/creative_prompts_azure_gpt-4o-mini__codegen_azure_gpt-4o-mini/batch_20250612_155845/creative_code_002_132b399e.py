"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://audifree.duckdns.org
Prompt: What are the steps to configure the SMTP settings in LuFix.to Sender for sending emails securely?
Generated: DETERMINISTIC_132b399e054af4a3
Batch ID: 20250612_155845
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

Here's a sample Python script demonstrating how to configure SMTP settings for sending emails securely using the `smtplib` library. This code uses environment variables for sensitive information and includes proper error handling.

```python
import os
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

def send_email(subject, body, recipient_email):
    """
    Send an email using SMTP settings configured via environment variables.

    Parameters:
        subject (str): The subject of the email.
        body (str): The body content of the email.
        recipient_email (str): The recipient's email address.

    Raises:
        Exception: If there is an error during the SMTP process.
    """
    # Load SMTP settings from environment variables
    smtp_server = os.getenv('SMTP_SERVER')
    smtp_port = int(os.getenv('SMTP_PORT', 587))
    sender_email = os.getenv('SENDER_EMAIL')
    sender_password = os.getenv('SENDER_PASSWORD')

    # Create a multipart email
    msg = MIMEMultipart()
    msg['From'] = sender_email
    msg['To'] = recipient_email
    msg['Subject'] = subject

    # Attach the email body to the message
    msg.attach(MIMEText(body, 'plain'))

    try:
        # Establish a secure session with the SMTP server
        with smtplib.SMTP(smtp_server, smtp_port) as server:
            server.starttls()  # Upgrade to a secure connection
            server.login(sender_email, sender_password)  # Log in to the SMTP server
            server.send_message(msg)  # Send the email

        print("Email sent successfully.")

    except smtplib.SMTPException as e:
        # Handle SMTP exceptions
        print(f"Failed to send email: {e}")
        raise  # Re-raise the exception for further handling if needed

if __name__ == "__main__":
    # Example usage
    subject = "Test Email"
    body = "This is a test email sent securely."
    recipient_email = "recipient@example.com"

    # Send the email
    send_email(subject, body, recipient_email)
```

**Note**: Before running this code, make sure to set the required environment variables (`SMTP_SERVER`, `SMTP_PORT`, `SENDER_EMAIL`, `SENDER_PASSWORD`) with your SMTP server details and credentials.
