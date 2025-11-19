"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://now-5000ether.paperplane.io
Prompt: What are best practices for notifying users of a permanent website shutdown in my code?
Generated: DETERMINISTIC_0d3b62554677611c
Batch ID: 20250612_160600
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
import logging

# Configure logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

def send_shutdown_notification(email_list, subject, message):
    """
    Sends an email notification to users about the permanent shutdown of the website.

    Args:
        email_list (list): List of recipient email addresses.
        subject (str): Subject of the email.
        message (str): Body of the email message.

    Raises:
        Exception: Raises an exception if sending email fails.
    """
    # Email server configuration
    smtp_server = 'smtp.example.com'
    smtp_port = 587
    sender_email = 'no-reply@example.com'
    sender_password = 'your_password_here'
    
    # Create a multipart email message
    msg = MIMEMultipart()
    msg['From'] = sender_email
    msg['Subject'] = subject
    msg.attach(MIMEText(message, 'plain'))

    try:
        # Initialize the SMTP server
        with smtplib.SMTP(smtp_server, smtp_port) as server:
            server.starttls()  # Upgrade the connection to a secure encrypted SSL/TLS connection
            server.login(sender_email, sender_password)  # Log in to the email server
            
            for recipient in email_list:
                msg['To'] = recipient  # Set recipient address
                # Send the email
                server.sendmail(sender_email, recipient, msg.as_string())
                logging.info(f'Notification sent to {recipient}')
    
    except Exception as e:
        logging.error(f'Failed to send email notification: {e}')
        raise  # Re-raise the exception after logging

if __name__ == "__main__":
    # List of user email addresses to notify
    user_emails = ['user1@example.com', 'user2@example.com']

    # Email subject and message
    shutdown_subject = "Important Notice: Website Shutdown"
    shutdown_message = (
        "Dear User,\n\n"
        "We regret to inform you that our website will be permanently shut down. "
        "We appreciate your support and understanding during our operational period.\n\n"
        "Thank you,\n"
        "The Team"
    )

    # Send shutdown notifications
    send_shutdown_notification(user_emails, shutdown_subject, shutdown_message)
```
