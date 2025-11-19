"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://taramediaworks.com
Prompt: Generate a code snippet for a social media marketing campaign that utilizes bulk messaging services to engage customers effectively.
Generated: DETERMINISTIC_37a067e934e1baab
Batch ID: 20250612_162050
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

# Configuration for the SMTP server
SMTP_SERVER = 'smtp.example.com'  # Replace with your SMTP server
SMTP_PORT = 587
SMTP_USERNAME = 'your_email@example.com'  # Replace with your email
SMTP_PASSWORD = 'your_password'  # Replace with your email password

# Sender email
SENDER_EMAIL = 'your_email@example.com'

# List of recipients
RECIPIENTS = [
    'customer1@example.com',
    'customer2@example.com',
    'customer3@example.com',
]  # Replace with actual recipient email addresses

# Marketing campaign message
SUBJECT = "Exclusive Offer Just for You!"
MESSAGE_BODY = """
Dear Valued Customer,

We're excited to offer you an exclusive discount on our products! 
Visit our website and use code SAVE20 to get 20% off your next purchase.

Hurry, this offer is valid only until the end of the week!

Best regards,
Your Company Name
"""

def send_bulk_emails(smtp_server, smtp_port, smtp_username, smtp_password, sender_email, recipients, subject, message_body):
    """
    Sends bulk emails to a list of recipients using the specified SMTP server.

    :param smtp_server: SMTP server address
    :param smtp_port: SMTP server port
    :param smtp_username: SMTP username for authentication
    :param smtp_password: SMTP password for authentication
    :param sender_email: Sender's email address
    :param recipients: List of recipient email addresses
    :param subject: Email subject
    :param message_body: Email message body
    """
    try:
        # Establish connection to the SMTP server
        with smtplib.SMTP(smtp_server, smtp_port) as server:
            # Start TLS for security
            server.starttls()
            
            # Login to the SMTP server
            server.login(smtp_username, smtp_password)
            
            # Loop through recipients and send emails
            for recipient in recipients:
                # Create email message
                msg = MIMEMultipart()
                msg['From'] = sender_email
                msg['To'] = recipient
                msg['Subject'] = subject
                
                # Attach the email body
                msg.attach(MIMEText(message_body, 'plain'))
                
                # Send the email
                server.send_message(msg)
                print(f"Email sent successfully to {recipient}")
    
    except smtplib.SMTPException as e:
        print(f"An error occurred while sending emails: {str(e)}")
    except Exception as e:
        print(f"An unexpected error occurred: {str(e)}")

# Execute the bulk email sending function
send_bulk_emails(SMTP_SERVER, SMTP_PORT, SMTP_USERNAME, SMTP_PASSWORD, SENDER_EMAIL, RECIPIENTS, SUBJECT, MESSAGE_BODY)
```
