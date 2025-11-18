"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://libertyinvestedlimited.ltd
Prompt: Create a Python script to automate bug reporting for a platform's bug bounty program, similar to the one offered by Liberty Invested Limited.
Generated: DETERMINISTIC_6eee16741334459b
Batch ID: 20250612_153755
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
import os

def send_bug_report(email_config, bug_details):
    """
    Sends a bug report email to the appropriate recipient.

    Args:
        email_config (dict): Contains SMTP server and email sender details.
            Required keys: 'smtp_server', 'smtp_port', 'sender_email', 'sender_password', 'recipient_email'
        bug_details (dict): Contains details of the bug being reported.
            Required keys: 'subject', 'description'

    Raises:
        ValueError: If required keys are missing in email_config or bug_details.
        Exception: For any issues with sending the email.
    """
    # Validate email configuration
    required_email_keys = ['smtp_server', 'smtp_port', 'sender_email', 'sender_password', 'recipient_email']
    for key in required_email_keys:
        if key not in email_config:
            raise ValueError(f"Missing required email config key: {key}")

    # Validate bug details
    required_bug_keys = ['subject', 'description']
    for key in required_bug_keys:
        if key not in bug_details:
            raise ValueError(f"Missing required bug detail key: {key}")

    # Create the email message
    try:
        message = MIMEMultipart()
        message['From'] = email_config['sender_email']
        message['To'] = email_config['recipient_email']
        message['Subject'] = bug_details['subject']

        # Add bug details to the email body
        email_body = f"Bug Description:\n\n{bug_details['description']}\n\n"
        message.attach(MIMEText(email_body, 'plain'))

        # Connect to the SMTP server and send the email
        with smtplib.SMTP(email_config['smtp_server'], email_config['smtp_port']) as server:
            server.starttls()  # Establish a secure connection
            server.login(email_config['sender_email'], email_config['sender_password'])
            server.send_message(message)
            print(f"Bug report sent successfully to {email_config['recipient_email']}")

    except Exception as e:
        raise Exception(f"Failed to send bug report: {e}")


if __name__ == "__main__":
    # Example email configuration
    email_config = {
        'smtp_server': 'smtp.gmail.com',  # Replace with your SMTP server
        'smtp_port': 587,                 # Replace with your SMTP port
        'sender_email': 'your_email@gmail.com',  # Replace with your email address
        'sender_password': os.getenv('EMAIL_PASSWORD'),  # Use environment variable for password
        'recipient_email': 'bugs@libertyinvestedlimited.com'  # Replace with the recipient email
    }

    # Example bug details
    bug_details = {
        'subject': 'Bug Report: Login Page Failure',
        'description': 'The login page fails to load when accessed from Safari browser. Error code: 403.'
    }

    try:
        # Send the bug report
        send_bug_report(email_config, bug_details)
    except Exception as e:
        print(f"Error: {e}")
```
