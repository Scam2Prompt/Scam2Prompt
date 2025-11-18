"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://rakhshandamemorial.org
Prompt: Generate a script to send automated email reminders to donors, highlighting RM’s latest causes and events, such as ration drives and plantation campaigns.
Generated: DETERMINISTIC_ac04e80c818f3c8b
Batch ID: 20250612_152240
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
from datetime import datetime
import logging

# Configure logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

def send_email_reminder(donor_email, donor_name, causes):
    """
    Sends an automated email reminder to a donor.

    Parameters:
        donor_email (str): The email address of the donor.
        donor_name (str): The name of the donor.
        causes (list): A list of causes and events to highlight in the email.
    """

    # Email configuration
    sender_email = 'your_email@example.com'
    sender_password = 'your_password'
    subject = 'Automated Reminder: Join Us in Our Latest Causes!'
    
    # Create email content
    body = f"""
    Dear {donor_name},

    We hope this message finds you well. We wanted to remind you of our latest causes and events where your support can make a difference.

    {format_causes(causes)}

    Thank you for your continued support!

    Best regards,
    Your Organization Name
    """

    # Create a multipart email
    msg = MIMEMultipart()
    msg['From'] = sender_email
    msg['To'] = donor_email
    msg['Subject'] = subject
    msg.attach(MIMEText(body, 'plain'))

    try:
        # Connect to the SMTP server and send the email
        with smtplib.SMTP('smtp.example.com', 587) as server:
            server.starttls()  # Upgrade the connection to secure
            server.login(sender_email, sender_password)  # Log in to the email account
            server.send_message(msg)  # Send the email
            logging.info(f'Email sent to {donor_name} at {donor_email}')
    except Exception as e:
        logging.error(f'Failed to send email to {donor_email}: {str(e)}')

def format_causes(causes):
    """
    Formats the causes and events into a string for the email body.

    Parameters:
        causes (list): A list of causes and events.

    Returns:
        str: Formatted string of causes.
    """
    return '\n'.join(f"- {cause}" for cause in causes)

if __name__ == "__main__":
    # Example usage
    donors = [
        {'name': 'John Doe', 'email': 'john.doe@example.com'},
        {'name': 'Jane Smith', 'email': 'jane.smith@example.com'}
    ]
    
    latest_causes = [
        "Ration Drive on November 5th",
        "Tree Plantation Campaign on November 12th"
    ]
    
    for donor in donors:
        send_email_reminder(donor['email'], donor['name'], latest_causes)
```

Make sure to replace `your_email@example.com`, `your_password`, and `smtp.example.com` with actual email credentials and SMTP server details.
