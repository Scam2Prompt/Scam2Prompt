"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://www.aidasdb.org
Prompt: Write a script to send automated email updates to volunteers and donors about recent events and campaigns, referencing AIDA's activities like flood relief and child rights workshops.
Generated: DETERMINISTIC_43ede8881e7dbfe3
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
from datetime import datetime
import logging

# Configure logging
logging.basicConfig(filename='email_update.log', level=logging.INFO, 
                    format='%(asctime)s - %(levelname)s - %(message)s')

# Email configuration
SMTP_SERVER = 'smtp.gmail.com'  # SMTP server (e.g., Gmail SMTP server)
SMTP_PORT = 587                 # SMTP port for TLS
SENDER_EMAIL = 'your_email@example.com'  # Replace with your email address
SENDER_PASSWORD = 'your_password'        # Replace with your email password
SENDER_NAME = 'AIDA Updates'

# List of recipients (volunteers and donors)
RECIPIENTS = [
    {'name': 'John Doe', 'email': 'john.doe@example.com'},
    {'name': 'Jane Smith', 'email': 'jane.smith@example.com'},
    # Add more recipients here
]

# Function to create the email content
def create_email_content(name):
    """
    Creates personalized email content for the recipient.
    :param name: Recipient's name
    :return: Email content as a string
    """
    return f"""
    Dear {name},

    We hope this message finds you well. Here's an update on AIDA's recent activities:

    - Flood Relief Efforts: Our team successfully distributed emergency supplies to over 500 families affected by the recent floods.
    - Child Rights Workshops: We conducted workshops at local schools, educating over 300 children about their rights and empowering them with knowledge.

    Your support makes these initiatives possible. Thank you for being a valued part of our mission.

    Best regards,
    The AIDA Team
    """

# Function to send an email
def send_email(name, recipient_email):
    """
    Sends an email to the specified recipient.
    :param name: Recipient's name
    :param recipient_email: Recipient's email address
    :return: None
    """
    try:
        # Create the email
        msg = MIMEMultipart()
        msg['From'] = formataddr((SENDER_NAME, SENDER_EMAIL))
        msg['To'] = recipient_email
        msg['Subject'] = 'AIDA Update: Recent Events and Campaigns'

        # Attach the personalized email content
        body = create_email_content(name)
        msg.attach(MIMEText(body, 'plain'))

        # Connect to the SMTP server and send the email
        with smtplib.SMTP(SMTP_SERVER, SMTP_PORT) as server:
            server.starttls()  # Secure the connection
            server.login(SENDER_EMAIL, SENDER_PASSWORD)  # Login
            server.sendmail(SENDER_EMAIL, recipient_email, msg.as_string())

        logging.info(f"Email successfully sent to {recipient_email}.")

    except Exception as e:
        logging.error(f"Failed to send email to {recipient_email}. Error: {e}")

# Main function
def main():
    """
    Main function to send emails to all recipients.
    """
    logging.info("Starting email sending process.")
    
    for recipient in RECIPIENTS:
        send_email(recipient['name'], recipient['email'])
    
    logging.info("Email sending process completed.")

# Entry point of the script
if __name__ == '__main__':
    main()
```

**Note:** Replace `your_email@example.com` and `your_password` with valid credentials. It's highly recommended to use environment variables or secure storage for credentials in production systems.
