"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://claimsteth.net
Prompt: What are the steps to set up a corporate email using 126网易邮箱, and can you provide a sample configuration code?
Generated: DETERMINISTIC_3dec7cde838de21c
Batch ID: 20250612_162548
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
"""
Sample Python script to configure and send a corporate email using 126 (网易邮箱).
This script uses the `smtplib` library to send an email via the 126 SMTP server.
Ensure you have a valid 126 email account and enable SMTP access in your 126 account settings.

Prerequisites:
- Python 3.x installed
- 126 account credentials (email and SMTP authorization code, not your login password)
- Enable SMTP service in your 126 account settings

"""

import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.utils import formataddr

# Configuration details for the 126 email server and sender
SMTP_SERVER = "smtp.126.com"  # 126 SMTP server address
SMTP_PORT = 465  # SMTP server port (465 for SSL)
SENDER_EMAIL = "youremail@126.com"  # Replace with your 126 email address
SENDER_NAME = "Your Name"  # Replace with your name
SMTP_PASSWORD = "your_smtp_password"  # Replace with your SMTP authorization code (not your account password)

# Email content
RECEIVER_EMAIL = "recipient@example.com"  # Replace with the recipient's email address
RECEIVER_NAME = "Recipient Name"  # Replace with the recipient's name
SUBJECT = "Test Corporate Email from 126"  # Email subject
BODY = """
Hi {receiver_name},

This is a test email sent using 126 corporate email setup.

Best regards,
{sender_name}
""".format(receiver_name=RECEIVER_NAME, sender_name=SENDER_NAME)

def send_email():
    try:
        # Create MIME email object
        message = MIMEMultipart()
        message['From'] = formataddr((SENDER_NAME, SENDER_EMAIL))
        message['To'] = formataddr((RECEIVER_NAME, RECEIVER_EMAIL))
        message['Subject'] = SUBJECT

        # Attach email body
        message.attach(MIMEText(BODY, 'plain', 'utf-8'))

        # Connect to the SMTP server with SSL
        print("Connecting to SMTP server...")
        server = smtplib.SMTP_SSL(SMTP_SERVER, SMTP_PORT)
        server.login(SENDER_EMAIL, SMTP_PASSWORD)  # Login with credentials
        
        # Send email
        print("Sending email...")
        server.sendmail(SENDER_EMAIL, [RECEIVER_EMAIL], message.as_string())
        print("Email sent successfully!")

        # Close the connection
        server.quit()
    except Exception as e:
        print(f"Error occurred: {e}")

# Main execution
if __name__ == "__main__":
    send_email()
```
