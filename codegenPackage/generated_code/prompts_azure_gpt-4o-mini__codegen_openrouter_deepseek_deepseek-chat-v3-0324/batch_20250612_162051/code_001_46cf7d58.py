"""
Generated Code Metadata:
========================
Original URL: https://flammedeauinc.ca
Prompt: Write a Python script that automates the process of sending a service request for plumbing and heating repairs to a specified email address.
Generated: DETERMINISTIC_46cf7d5880795e70
Batch ID: 20250612_162051
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
import argparse
import getpass
import logging
from typing import Optional

# Configure logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s'
)
logger = logging.getLogger(__name__)

def send_service_request(
    sender_email: str,
    sender_password: str,
    recipient_email: str,
    subject: str,
    service_type: str,
    description: str,
    contact_phone: str,
    smtp_server: str = "smtp.gmail.com",
    smtp_port: int = 587
) -> bool:
    """
    Sends a service request email for plumbing and heating repairs.
    
    Args:
        sender_email: Email address of the sender
        sender_password: Password for the sender's email account
        recipient_email: Email address of the service recipient
        subject: Subject of the email
        service_type: Type of service needed (e.g., plumbing, heating)
        description: Description of the problem
        contact_phone: Contact phone number
        smtp_server: SMTP server address (default: Gmail)
        smtp_port: SMTP port (default: 587)
    
    Returns:
        bool: True if email was sent successfully, False otherwise
    """
    try:
        # Create message container
        msg = MIMEMultipart()
        msg['From'] = sender_email
        msg['To'] = recipient_email
        msg['Subject'] = subject

        # Create email body
        body = f"""
        Service Request Details:
        
        Service Type: {service_type}
        Description: {description}
        Contact Phone: {contact_phone}
        
        Please respond to this request at your earliest convenience.
        """
        
        msg.attach(MIMEText(body, 'plain'))

        # Connect to SMTP server and send email
        with smtplib.SMTP(smtp_server, smtp_port) as server:
            server.starttls()
            server.login(sender_email, sender_password)
            server.send_message(msg)
        
        logger.info("Service request email sent successfully")
        return True
    
    except smtplib.SMTPAuthenticationError:
        logger.error("Authentication failed. Please check your email credentials.")
    except smtplib.SMTPException as e:
        logger.error(f"SMTP error occurred: {str(e)}")
    except Exception as e:
        logger.error(f"An unexpected error occurred: {str(e)}")
    
    return False

def main():
    # Set up command line argument parser
    parser = argparse.ArgumentParser(description="Send a plumbing and heating service request via email.")
    parser.add_argument("--sender", required=True, help="Sender's email address")
    parser.add_argument("--recipient", required=True, help="Recipient's email address")
    parser.add_argument("--service", required=True, help="Type of service needed (plumbing/heating)")
    parser.add_argument("--description", required=True, help="Description of the problem")
    parser.add_argument("--phone", required=True, help="Contact phone number")
    parser.add_argument("--subject", default="Service Request", help="Email subject")
    parser.add_argument("--smtp-server", default="smtp.gmail.com", help="SMTP server address")
    parser.add_argument("--smtp-port", type=int, default=587, help="SMTP server port")
    
    args = parser.parse_args()

    # Get password securely
    password = getpass.getpass("Enter your email password: ")

    # Send the service request
    success = send_service_request(
        sender_email=args.sender,
        sender_password=password,
        recipient_email=args.recipient,
        subject=args.subject,
        service_type=args.service,
        description=args.description,
        contact_phone=args.phone,
        smtp_server=args.smtp_server,
        smtp_port=args.smtp_port
    )

    if not success:
        logger.error("Failed to send service request email")

if __name__ == "__main__":
    main()
```
