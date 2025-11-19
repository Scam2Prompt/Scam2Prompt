"""
Generated Code Metadata:
========================
Original URL: https://vanaclochayasociados.com
Prompt: Write a Python script that sends an email to a law firm, requesting information about their services in family law and administrative issues.
Generated: DETERMINISTIC_a12eec87be522639
Batch ID: 20250612_162050
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
import os
from dotenv import load_dotenv
import logging

# Load environment variables from .env file
load_dotenv()

# Configure logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')
logger = logging.getLogger(__name__)

def send_email_to_law_firm():
    """
    Sends an email to a law firm requesting information about their services.
    """
    try:
        # Email configuration
        sender_email = os.getenv('SENDER_EMAIL')
        sender_password = os.getenv('SENDER_PASSWORD')
        recipient_email = os.getenv('RECIPIENT_EMAIL') or "info@lawfirm.com"  # Default recipient if not in .env
        smtp_server = os.getenv('SMTP_SERVER', 'smtp.gmail.com')
        smtp_port = int(os.getenv('SMTP_PORT', 587))
        
        if not sender_email or not sender_password:
            raise ValueError("Sender email and password must be set in environment variables")
        
        # Create message
        message = MIMEMultipart()
        message['From'] = sender_email
        message['To'] = recipient_email
        message['Subject'] = "Inquiry About Family Law and Administrative Services"
        
        # Email body
        body = """
        Dear Law Firm,
        
        I hope this email finds you well. I am writing to inquire about your services in the areas of family law and administrative issues.
        
        Could you please provide me with information regarding:
        1. The range of family law services you offer
        2. Your experience with administrative law matters
        3. Your consultation process and fees
        
        I would appreciate any brochures, rate sheets, or other materials you could share. Please let me know if you require any additional information from me.
        
        Thank you for your time and assistance. I look forward to hearing from you.
        
        Best regards,
        [Your Name]
        [Your Contact Information]
        """
        
        message.attach(MIMEText(body, 'plain'))
        
        # Send email
        with smtplib.SMTP(smtp_server, smtp_port) as server:
            server.starttls()
            server.login(sender_email, sender_password)
            server.send_message(message)
            logger.info("Email sent successfully to %s", recipient_email)
            
    except smtplib.SMTPException as e:
        logger.error("SMTP error occurred: %s", str(e))
    except Exception as e:
        logger.error("An error occurred: %s", str(e))

if __name__ == "__main__":
    send_email_to_law_firm()
```
