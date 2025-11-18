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
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
import logging

# Set up logging for error handling and debugging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

# Email Configuration (Update these with your email service provider details)
SMTP_SERVER = 'smtp.gmail.com'  # Replace with your SMTP server
SMTP_PORT = 587                 # Port for TLS
EMAIL_ADDRESS = 'your_email@example.com'  # Replace with your email address
EMAIL_PASSWORD = 'your_password'          # Replace with your email's app password or credentials

# List of donors and their email addresses
donors = [
    {"name": "John Doe", "email": "john.doe@example.com"},
    {"name": "Jane Smith", "email": "jane.smith@example.com"},
    # Add more donors here
]

# Generate the email body content dynamically
def generate_email_content(donor_name):
    """
    Generate the email body content for the given donor name.
    :param donor_name: The name of the donor.
    :return: A formatted email message string.
    """
    return f"""
    Dear {donor_name},

    We hope this message finds you well.

    RM is excited to share our latest causes and upcoming events. Here's how you can contribute:
    - Ration Drives: Helping provide essential supplies to families in need.
    - Plantation Campaigns: Join us in making the planet greener for generations to come.

    Your support makes all the difference. Visit our website or reach out to us to learn more about how you can help.

    Thank you for your generosity and commitment to making a positive impact!

    Best regards,
    RM Team
    """

def send_email(to_email, donor_name):
    """
    Send an email to a specific recipient.
    :param to_email: Recipient's email address.
    :param donor_name: Recipient's name for personalization.
    """
    try:
        # Create email components
        msg = MIMEMultipart()
        msg['From'] = EMAIL_ADDRESS
        msg['To'] = to_email
        msg['Subject'] = 'RM Latest Causes and Events - Join Us!'
        
        # Attach the email content
        body = generate_email_content(donor_name)
        msg.attach(MIMEText(body, 'plain'))
        
        # Establish connection to the SMTP server
        with smtplib.SMTP(SMTP_SERVER, SMTP_PORT) as server:
            server.starttls()  # Upgrade to secure connection
            server.login(EMAIL_ADDRESS, EMAIL_PASSWORD)  # Login to email account
            server.send_message(msg)  # Send the email
            
        logging.info(f"Email sent successfully to {to_email}")
    
    except Exception as e:
        logging.error(f"Failed to send email to {to_email}: {e}")

def main():
    """
    Main function to send automated email reminders to all donors.
    """
    logging.info("Starting to send email reminders...")
    
    for donor in donors:
        send_email(donor["email"], donor["name"])
    
    logging.info("Finished sending email reminders.")

if __name__ == "__main__":
    # Entry point of the script
    main()
```
