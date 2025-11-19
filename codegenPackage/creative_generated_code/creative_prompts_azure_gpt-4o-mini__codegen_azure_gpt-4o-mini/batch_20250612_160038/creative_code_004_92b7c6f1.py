"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://shebatek.com
Prompt: Provide an example of a marketing automation script that could promote services effectively, inspired by ShebaTek's marketing solutions.
Generated: DETERMINISTIC_92b7c6f1e5e01bc3
Batch ID: 20250612_160038
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
import os

# Configure logging
logging.basicConfig(level=logging.INFO, 
                    format='%(asctime)s - %(levelname)s - %(message)s')

# Constants for email configuration
SMTP_SERVER = "smtp.example.com"  # Replace with your SMTP server
SMTP_PORT = 587  # Typical port for TLS
SENDER_EMAIL = "noreply@shebatek.com"  # Replace with your sender email address
SENDER_PASSWORD = os.getenv('EMAIL_PASSWORD')  # Use environment variable for password

def send_email(recipient_email, subject, body):
    """Send an email using SMTP."""
    try:
        # Create the email message
        msg = MIMEMultipart()
        msg['From'] = SENDER_EMAIL
        msg['To'] = recipient_email
        msg['Subject'] = subject
        
        # Attach the email body
        msg.attach(MIMEText(body, 'plain'))

        # Set up the SMTP server and send the email
        with smtplib.SMTP(SMTP_SERVER, SMTP_PORT) as server:
            server.starttls()  # Secure the connection
            server.login(SENDER_EMAIL, SENDER_PASSWORD)
            server.send_message(msg)
        
        logging.info(f'Email sent successfully to {recipient_email}')
    except Exception as e:
        logging.error(f'Failed to send email to {recipient_email}. Error: {e}')

def create_marketing_message(service_name, service_details):
    """Create a formatted marketing message."""
    return f"Hello!\n\nWe are excited to introduce our new service: {service_name}.\n\nDetails:\n{service_details}\n\nBest regards,\nShebaTek Team"

def promote_service(service_name, service_details, recipient_list):
    """Promote a service by sending emails to a list of recipients."""
    # Validate inputs
    if not isinstance(recipient_list, list) or not recipient_list:
        logging.error("Invalid recipient list provided.")
        return
    
    message_body = create_marketing_message(service_name, service_details)
    
    for recipient in recipient_list:
        send_email(recipient, f"Introducing Our New Service: {service_name}", message_body)

if __name__ == "__main__":
    # Example service details
    service = "Automated Analytics"
    details = "Get insights on your marketing performance with our new automated analytics service."
    
    # Example recipient list
    recipients = ["client1@example.com", "client2@example.com", "client3@example.com"]
    
    # Start the promotion
    promote_service(service, details, recipients)
```
