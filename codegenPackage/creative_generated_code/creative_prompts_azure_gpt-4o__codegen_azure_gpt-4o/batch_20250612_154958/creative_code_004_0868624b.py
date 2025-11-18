"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://openseaaward-program.epizy.com
Prompt: Write code to configure multiple email accounts on a hosting service that supports unlimited disk space and bandwidth, using iFastNet hosting as an example.
Generated: DETERMINISTIC_0868624b6475b24d
Batch ID: 20250612_154958
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

# Configuration for email accounts
email_accounts = [
    {
        "email": "user1@example.com",
        "password": "password1",
        "smtp_server": "mail.example.com",
        "smtp_port": 587
    },
    {
        "email": "user2@example.com",
        "password": "password2",
        "smtp_server": "mail.example.com",
        "smtp_port": 587
    },
    # Add more accounts as needed
]

def send_test_email(account):
    """
    Send a test email using the given email account configuration.
    Args:
        account (dict): Email account configuration with keys:
            - email: Email address
            - password: Password for the email account
            - smtp_server: SMTP server address
            - smtp_port: SMTP server port
    """
    try:
        # Create a connection to the SMTP server
        server = smtplib.SMTP(account['smtp_server'], account['smtp_port'])
        server.starttls()  # Use TLS encryption
        server.login(account['email'], account['password'])  # Log in to the email account
        
        # Create the email
        message = MIMEMultipart()
        message['From'] = account['email']
        message['To'] = account['email']  # Sending the test email to self
        message['Subject'] = "Test Email from Hosting Service"
        body = "This is a test email to confirm the configuration of your email account."
        message.attach(MIMEText(body, 'plain'))
        
        # Send the email
        server.send_message(message)
        print(f"Test email sent successfully from {account['email']}")
    except Exception as e:
        print(f"Failed to send email from {account['email']}: {e}")
    finally:
        # Ensure the connection to the server is closed
        server.quit()

# Configure each email account and send a test email
for email_account in email_accounts:
    send_test_email(email_account)
```
