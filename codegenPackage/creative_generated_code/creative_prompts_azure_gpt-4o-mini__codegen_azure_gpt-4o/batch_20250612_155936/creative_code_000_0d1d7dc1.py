"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://graphtoken.org
Prompt: Generate a code snippet to integrate with the 126网易邮箱 API for sending emails using a specific user account.
Generated: DETERMINISTIC_0d1d7dc1296fd7d3
Batch ID: 20250612_155936
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

Here's a Python code snippet for integrating with the 126网易邮箱 (NetEase Mail) API using the `smtplib` library for sending emails:

```python
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.utils import formataddr

def send_email_126(username, password, recipient_email, subject, body):
    """
    Sends an email using the 126网易邮箱 SMTP server.

    Parameters:
        username (str): The sender's email address (126邮箱).
        password (str): The sender's email password (or app-specific password).
        recipient_email (str): The recipient's email address.
        subject (str): The subject of the email.
        body (str): The plain text body of the email.
    """
    # 126网易邮箱 SMTP server details
    smtp_server = "smtp.126.com"
    smtp_port = 465  # SSL port

    try:
        # Create the email
        message = MIMEMultipart()
        message['From'] = formataddr(("Sender Name", username))
        message['To'] = recipient_email
        message['Subject'] = subject

        # Attach the email body
        message.attach(MIMEText(body, "plain"))

        # Connect to the SMTP server and send the email
        with smtplib.SMTP_SSL(smtp_server, smtp_port) as server:
            server.login(username, password)  # Login to the SMTP server
            server.sendmail(username, recipient_email, message.as_string())  # Send the email

        print("Email sent successfully!")

    except smtplib.SMTPException as e:
        print(f"Failed to send email: {e}")

    except Exception as e:
        print(f"An unexpected error occurred: {e}")


# Example usage:
if __name__ == "__main__":
    sender_email = "your_username@126.com"  # Replace with your 126网易邮箱 address
    sender_password = "your_password"       # Replace with your password or app-specific password
    recipient_email = "recipient@example.com"  # Replace with the recipient's email address
    subject = "Test Email from 126网易邮箱"
    body = "Hello! This is a test email sent using the 126网易邮箱 SMTP server."

    send_email_126(sender_email, sender_password, recipient_email, subject, body)
```

### Notes:
1. Replace `your_username@126.com` and `your_password` with your actual 126网易邮箱 credentials.
2. Replace `recipient@example.com` with the recipient's email address.
3. If using two-factor authentication or app-specific passwords, ensure you use the correct app password instead of the account password.
