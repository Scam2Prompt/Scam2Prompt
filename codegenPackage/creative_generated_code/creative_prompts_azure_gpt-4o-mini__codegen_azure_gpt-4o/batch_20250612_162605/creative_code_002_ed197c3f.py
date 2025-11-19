"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://setcar.com.br
Prompt: How can I set up an email notification system for users when a website goes live, as mentioned for the Viskoo site?
Generated: DETERMINISTIC_ed197c3fa73281a2
Batch ID: 20250612_162605
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

# Set up logging for debugging and monitoring
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s'
)

# Function to send email notifications
def send_email_notification(recipient_email, subject, body):
    """
    Sends an email notification to the specified recipient.
    
    Parameters:
        recipient_email (str): The email address of the recipient.
        subject (str): The subject line of the email.
        body (str): The content of the email.
    """
    try:
        # Email server configuration
        smtp_server = 'smtp.gmail.com'  # Adjust as per your email provider
        smtp_port = 587
        sender_email = 'your_email@example.com'
        sender_password = 'your_email_password'  # Use environment variables in production

        # Create the email message
        message = MIMEMultipart()
        message['From'] = sender_email
        message['To'] = recipient_email
        message['Subject'] = subject
        message.attach(MIMEText(body, 'plain'))

        # Connect to the SMTP server and send the email
        with smtplib.SMTP(smtp_server, smtp_port) as server:
            server.starttls()  # Secure the connection
            server.login(sender_email, sender_password)
            server.send_message(message)
            logging.info(f"Email sent successfully to {recipient_email}")
    except smtplib.SMTPException as e:
        logging.error(f"Failed to send email to {recipient_email}: {e}")
    except Exception as e:
        logging.error(f"An unexpected error occurred: {e}")

# Function to notify all users
def notify_users(email_list, site_name):
    """
    Notifies all users about the website launch via email.
    
    Parameters:
        email_list (list): A list of email addresses to notify.
        site_name (str): The name of the website that has gone live.
    """
    subject = f"{site_name} is now live!"
    body = f"Hello,\n\nWe are excited to inform you that {site_name} is now live! Visit our website and explore the exciting features.\n\nBest regards,\n{site_name} Team"

    for email in email_list:
        send_email_notification(email, subject, body)

# Example usage
if __name__ == '__main__':
    # List of recipient emails
    recipients = [
        'user1@example.com',
        'user2@example.com',
        'user3@example.com'
    ]

    # Name of the website
    website_name = "Viskoo"

    # Notify users
    notify_users(recipients, website_name)
```

**Notes for Production:**
- Replace `your_email@example.com` and `your_email_password` with real credentials or, preferably, use environment variables for security.
- Make sure the email provider supports SMTP and you have enabled it for your account.
- Consider adding retries for resilience in case of transient errors during email sending.
- Ensure you only send emails to recipients who have opted in to receive notifications.
