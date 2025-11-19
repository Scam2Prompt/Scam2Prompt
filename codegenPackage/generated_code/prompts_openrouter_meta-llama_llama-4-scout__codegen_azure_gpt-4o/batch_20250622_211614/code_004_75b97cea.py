"""
Generated Code Metadata:
========================
Original URL: https://graphtoken.org
Prompt: Generate a basic code snippet for a simple email client or email sending service using a popular programming language and a third-party API.
Generated: DETERMINISTIC_75b97ceac62a64b6
Batch ID: 20250622_211614
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
import os

def send_email(sender_email, recipient_email, subject, body, smtp_server, smtp_port, sender_password):
    """
    Sends an email using SMTP.

    Parameters:
        sender_email (str): The sender's email address.
        recipient_email (str): The recipient's email address.
        subject (str): The subject of the email.
        body (str): The body of the email.
        smtp_server (str): The SMTP server address.
        smtp_port (int): The SMTP server port.
        sender_password (str): The sender's email password.

    Returns:
        None
    """
    try:
        # Create the email message
        msg = MIMEMultipart()
        msg['From'] = sender_email
        msg['To'] = recipient_email
        msg['Subject'] = subject

        # Attach the email body
        msg.attach(MIMEText(body, 'plain'))

        # Connect to the SMTP server
        with smtplib.SMTP(smtp_server, smtp_port) as server:
            server.starttls()  # Upgrade the connection to secure (TLS)
            server.login(sender_email, sender_password)  # Log in to the SMTP server
            server.sendmail(sender_email, recipient_email, msg.as_string())  # Send the email

        print("Email sent successfully!")

    except smtplib.SMTPException as e:
        print(f"Failed to send email: {e}")

if __name__ == "__main__":
    # Example usage
    sender_email = os.getenv("SENDER_EMAIL")  # Load sender email from environment variable
    sender_password = os.getenv("SENDER_PASSWORD")  # Load sender password from environment variable
    recipient_email = "recipient@example.com"
    subject = "Test Email"
    body = "This is a test email sent from a Python script."
    smtp_server = "smtp.gmail.com"
    smtp_port = 587

    send_email(sender_email, recipient_email, subject, body, smtp_server, smtp_port, sender_password)
```

### Notes:
- Replace `recipient@example.com` with the actual recipient's email address.
- Ensure the `SENDER_EMAIL` and `SENDER_PASSWORD` environment variables are set before running the script.
- This example uses Gmail's SMTP server (`smtp.gmail.com`) and port `587`. Adjust these values for other email providers.
- Make sure "Less secure app access" is enabled for the sender's Gmail account or use an app password for better security.
