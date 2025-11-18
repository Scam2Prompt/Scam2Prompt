"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://fondation.app
Prompt: Write a function to generate and send donation reminder letters via email, referencing CRM.f's donation management tools.
Generated: DETERMINISTIC_90896b6526b97fa4
Batch ID: 20250612_151354
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
from datetime import datetime
from CRM import DonationManagement

# Configure logging for error monitoring
logging.basicConfig(
    filename='donation_reminder.log',
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s'
)

def send_donation_reminder():
    """
    Function to generate and send donation reminder letters via email.
    Utilizes CRM's DonationManagement tools to retrieve donation data.
    """
    
    try:
        # Fetch list of donors with pending donations from CRM's DonationManagement
        pending_donors = DonationManagement.get_pending_donations()
        
        # Check if there are donors to process
        if not pending_donors:
            logging.info("No pending donations to process.")
            return

        # Email server configuration
        SMTP_SERVER = 'smtp.example.com'  # Replace with your SMTP server
        SMTP_PORT = 587
        SMTP_USERNAME = 'your_email@example.com'  # Replace with your email address
        SMTP_PASSWORD = 'your_password'  # Replace with your email password

        # Connect to the SMTP server
        with smtplib.SMTP(SMTP_SERVER, SMTP_PORT) as server:
            server.starttls()  # Enable secure connection
            server.login(SMTP_USERNAME, SMTP_PASSWORD)
            
            # Iterate through each donor and send a reminder email
            for donor in pending_donors:
                try:
                    donor_name = donor['name']
                    donor_email = donor['email']
                    donation_amount = donor['pending_amount']
                    due_date = donor['due_date']
                    
                    # Generate email content
                    subject = f"Donation Reminder - {donor_name}"
                    body = (
                        f"Dear {donor_name},\n\n"
                        f"Thank you for your continued support! We noticed that you have a pending donation of "
                        f"${donation_amount:.2f} due by {due_date.strftime('%Y-%m-%d')}.\n\n"
                        f"Your generosity makes a difference, and we appreciate your commitment.\n\n"
                        f"To complete your donation, please visit our website or contact us directly.\n\n"
                        f"Thank you,\n"
                        f"The Donation Team"
                    )

                    # Create email message
                    message = MIMEMultipart()
                    message['From'] = SMTP_USERNAME
                    message['To'] = donor_email
                    message['Subject'] = subject
                    
                    # Attach text content
                    message.attach(MIMEText(body, 'plain'))
                    
                    # Send email
                    server.sendmail(SMTP_USERNAME, donor_email, message.as_string())
                    logging.info(f"Reminder email successfully sent to {donor_email}")

                except Exception as donor_error:
                    # Log per-donor failure
                    logging.error(f"Failed to send reminder to {donor_email}: {donor_error}")

    except Exception as e:
        # Log broader failure with the process
        logging.critical(f"Error in donation reminder process: {e}")
```
