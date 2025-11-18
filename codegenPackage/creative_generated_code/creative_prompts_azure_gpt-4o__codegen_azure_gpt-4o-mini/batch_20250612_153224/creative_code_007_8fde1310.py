"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://corfucoastalcollection.com
Prompt: Develop a script to send automated follow-up emails to clients who inquire about plots or villas, based on the contact form structure provided by Corfu Coastal Collection.
Generated: DETERMINISTIC_8fde13102169cca8
Batch ID: 20250612_153224
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
from email.utils import formataddr
import logging
import os

# Set up logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

# Email configuration
SMTP_SERVER = 'smtp.your-email-provider.com'
SMTP_PORT = 587
USERNAME = os.getenv('EMAIL_USER')  # Email user from environment variable
PASSWORD = os.getenv('EMAIL_PASSWORD')  # Email password from environment variable
FROM_EMAIL = 'info@corfucoastalcollection.com'
FROM_NAME = 'Corfu Coastal Collection'

# Function to send follow-up email
def send_follow_up_email(to_email, client_name):
    """Sends a follow-up email to the client."""
    try:
        # Create the email content
        subject = 'Thank You for Your Inquiry!'
        body = f"Dear {client_name},\n\nThank you for your interest in our plots and villas. We are excited to assist you further.\n\nBest regards,\nCorfu Coastal Collection"
        
        # Set up the email
        msg = MIMEMultipart()
        msg['From'] = formataddr((FROM_NAME, FROM_EMAIL))
        msg['To'] = to_email
        msg['Subject'] = subject
        msg.attach(MIMEText(body, 'plain'))
        
        # Connect to the SMTP server and send the email
        with smtplib.SMTP(SMTP_SERVER, SMTP_PORT) as server:
            server.starttls()  # Upgrade the connection to a secure encrypted SSL/TLS connection
            server.login(USERNAME, PASSWORD)  # Authenticate with the email server
            server.send_message(msg)  # Send the email
            
        logging.info(f'Successfully sent follow-up email to {client_name} at {to_email}')
        
    except smtplib.SMTPException as e:
        logging.error(f'Failed to send email to {to_email}. Error: {str(e)}')
    except Exception as e:
        logging.error(f'An unexpected error occurred while sending email to {to_email}. Error: {str(e)}')

# Example usage
if __name__ == '__main__':
    # Sample client data (to be replaced with actual data from the contact form)
    clients = [
        {'name': 'John Doe', 'email': 'john.doe@example.com'},
        {'name': 'Jane Smith', 'email': 'jane.smith@example.com'},
    ]
    
    # Sending follow-up emails to clients
    for client in clients:
        send_follow_up_email(client['email'], client['name'])
```

**Note**: Make sure to replace `smtp.your-email-provider.com` and other email configurations with actual values. The script expects the email user and password to be set as environment variables. Adjust the client data as necessary to match your contact form structure.
