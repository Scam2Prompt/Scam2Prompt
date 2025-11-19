"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://futuretowerlight.com
Prompt: How do I set up automated email notifications for account status changes on a Bluehost-hosted site?
Generated: DETERMINISTIC_b8556f464c7148ee
Batch ID: 20250612_162051
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
import json
import logging

# Set up logging for error handling
logging.basicConfig(filename='email_notifications.log', level=logging.INFO, 
                    format='%(asctime)s:%(levelname)s:%(message)s')

# Email configuration
SMTP_SERVER = 'smtp.your-email-provider.com'  # Update with your SMTP server
SMTP_PORT = 587  # Change as necessary
EMAIL_ADDRESS = 'your-email@example.com'  # Update with your email address
EMAIL_PASSWORD = 'your-email-password'  # Update with your email password

def send_email(to_address, subject, body):
    """
    Sends an email with the specified subject and body to the given address.

    Parameters:
        to_address (str): The recipient's email address.
        subject (str): The subject of the email.
        body (str): The body text of the email.

    Returns:
        bool: True if email sent successfully, False otherwise.
    """
    try:
        # Create email message
        msg = MIMEMultipart()
        msg['From'] = EMAIL_ADDRESS
        msg['To'] = to_address
        msg['Subject'] = subject

        # Attach body to email
        msg.attach(MIMEText(body, 'plain'))

        # Set up the server
        server = smtplib.SMTP(SMTP_SERVER, SMTP_PORT)
        server.starttls()  # Use TLS for security
        server.login(EMAIL_ADDRESS, EMAIL_PASSWORD)

        # Send the email
        server.send_message(msg)
        server.quit()
        logging.info(f'Email sent to {to_address} with subject: "{subject}"')
        return True

    except Exception as e:
        logging.error(f'Failed to send email to {to_address}. Error: {e}')
        return False

def notify_account_status_change(user_email, new_status):
    """
    Notifies the user of a change in account status via email.

    Parameters:
        user_email (str): The user's email address.
        new_status (str): The new status of the account.
    """
    subject = 'Account Status Update'
    body = f'Dear User,\n\nYour account status has been changed to: {new_status}.\n\nThank you.'

    # Attempt to send the email notification
    if not send_email(user_email, subject, body):
        logging.error('Email notification failed.')

# Example usage (this would typically be triggered by an event in your application)
if __name__ == "__main__":
    user_data = json.loads('{"email": "user@example.com", "status": "active"}')  # Example JSON user data

    # Notify user about account status change
    notify_account_status_change(user_data['email'], user_data['status'])
```
