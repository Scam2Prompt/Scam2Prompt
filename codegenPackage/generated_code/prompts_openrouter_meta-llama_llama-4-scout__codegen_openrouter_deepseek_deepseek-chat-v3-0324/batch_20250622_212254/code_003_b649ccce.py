"""
Generated Code Metadata:
========================
Original URL: https://khaleeji.com
Prompt: How can I use a library like Python's `smtplib` to handle email inquiries for a domain sale listing, similar to the contact information provided for khaleeji.com?
Generated: DETERMINISTIC_b649ccce22c99d2b
Batch ID: 20250622_212254
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
from email.utils import formatdate
import os
from dotenv import load_dotenv
import logging

# Load environment variables
load_dotenv()

# Configure logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s'
)
logger = logging.getLogger(__name__)

class DomainSaleEmailHandler:
    def __init__(self):
        self.smtp_server = os.getenv('SMTP_SERVER')
        self.smtp_port = int(os.getenv('SMTP_PORT', 587))
        self.smtp_username = os.getenv('SMTP_USERNAME')
        self.smtp_password = os.getenv('SMTP_PASSWORD')
        self.sender_email = os.getenv('SENDER_EMAIL')
        self.admin_email = os.getenv('ADMIN_EMAIL')
        self.domain_name = os.getenv('DOMAIN_NAME', 'khaleeji.com')

    def send_email(self, recipient_email, subject, body):
        """
        Send an email using SMTP with TLS encryption.
        
        Args:
            recipient_email (str): Email address of the recipient
            subject (str): Subject of the email
            body (str): Body content of the email
        """
        try:
            # Create message container
            msg = MIMEMultipart()
            msg['From'] = self.sender_email
            msg['To'] = recipient_email
            msg['Date'] = formatdate(localtime=True)
            msg['Subject'] = subject

            # Attach the body to the message
            msg.attach(MIMEText(body, 'plain'))

            # Connect to SMTP server and send email
            with smtplib.SMTP(self.smtp_server, self.smtp_port) as server:
                server.starttls()
                server.login(self.smtp_username, self.smtp_password)
                server.send_message(msg)
            
            logger.info(f"Email sent successfully to {recipient_email}")
            return True
        except smtplib.SMTPException as e:
            logger.error(f"SMTP error occurred: {str(e)}")
            return False
        except Exception as e:
            logger.error(f"Unexpected error occurred: {str(e)}")
            return False

    def handle_inquiry(self, name, email, message):
        """
        Handle domain sale inquiry by sending emails to both admin and customer.
        
        Args:
            name (str): Name of the inquirer
            email (str): Email of the inquirer
            message (str): Inquiry message
        """
        try:
            # Email to admin
            admin_subject = f"New Inquiry for {self.domain_name}"
            admin_body = (
                f"You have received a new inquiry for {self.domain_name}:\n\n"
                f"Name: {name}\n"
                f"Email: {email}\n"
                f"Message: {message}\n\n"
                "Please respond promptly."
            )
            
            # Email to customer
            customer_subject = f"Thank you for your interest in {self.domain_name}"
            customer_body = (
                f"Dear {name},\n\n"
                f"Thank you for your interest in {self.domain_name}. "
                "We have received your inquiry and will get back to you shortly.\n\n"
                "Best regards,\n"
                f"The {self.domain_name} Team"
            )
            
            # Send both emails
            admin_success = self.send_email(self.admin_email, admin_subject, admin_body)
            customer_success = self.send_email(email, customer_subject, customer_body)
            
            return admin_success and customer_success
        except Exception as e:
            logger.error(f"Error handling inquiry: {str(e)}")
            return False

# Example usage (would typically be called from a web form handler)
if __name__ == "__main__":
    email_handler = DomainSaleEmailHandler()
    
    # Simulate form submission
    inquiry_data = {
        'name': 'John Doe',
        'email': 'john@example.com',
        'message': 'I am interested in purchasing this domain. What is your asking price?'
    }
    
    success = email_handler.handle_inquiry(**inquiry_data)
    if success:
        print("Inquiry processed successfully")
    else:
        print("Failed to process inquiry")
```
