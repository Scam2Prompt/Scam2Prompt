"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://naikreatif.com
Prompt: Generate a code snippet for a digital marketing campaign that could be used by a branding agency like Naikreatif in Jakarta.
Generated: DETERMINISTIC_d2e18f5289a8b439
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
import logging
from datetime import datetime

# Configure logging for error handling and monitoring
logging.basicConfig(
    filename='campaign.log', 
    level=logging.INFO, 
    format='%(asctime)s - %(levelname)s - %(message)s'
)

def send_email_notification(recipient_email, subject, message_body):
    """
    Sends an email notification for the digital marketing campaign.
    
    Parameters:
        recipient_email (str): The email of the recipient.
        subject (str): The subject of the email.
        message_body (str): The body text of the email.
    
    Returns:
        None
    """
    try:
        # Email sender details
        sender_email = "your_email@example.com"
        sender_password = "your_password"  # Use environment variables for sensitive data
        
        # Create the email message
        msg = MIMEMultipart()
        msg['From'] = sender_email
        msg['To'] = recipient_email
        msg['Subject'] = subject
        msg.attach(MIMEText(message_body, 'plain'))
        
        # Connect to the SMTP server and send email
        with smtplib.SMTP('smtp.example.com', 587) as server:
            server.starttls()  # Secure the connection
            server.login(sender_email, sender_password)
            server.sendmail(sender_email, recipient_email, msg.as_string())
        
        logging.info(f"Email sent successfully to {recipient_email}")
    
    except Exception as e:
        logging.error(f"Failed to send email: {e}")
        raise

def create_campaign():
    """
    Creates and launches a digital marketing campaign.
    
    Returns:
        None
    """
    try:
        # Example campaign data
        campaign_name = "Jakarta Branding Campaign - Naikreatif"
        campaign_message = ("Hello, \n\nWe are excited to introduce our latest branding solutions tailored for businesses in Jakarta. "
                            "Take your brand to the next level with Naikreatif!\n\nBest regards,\nNaikreatif Team")
        recipients = ["client1@example.com", "client2@example.com"]
        
        # Log campaign creation
        logging.info(f"Launching campaign: {campaign_name}")
        
        # Send notifications to each recipient
        for recipient in recipients:
            send_email_notification(
                recipient_email=recipient,
                subject=campaign_name,
                message_body=campaign_message
            )
        
        logging.info("Campaign successfully launched.")

    except Exception as e:
        logging.error(f"Campaign creation failed: {e}")
        raise

if __name__ == "__main__":
    try:
        # Entry point for the program
        logging.info("Starting the digital marketing campaign script.")
        create_campaign()
    except Exception as e:
        logging.critical(f"Unhandled exception occurred: {e}")
    finally:
        logging.info("Campaign script execution completed.")
```
