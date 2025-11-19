"""
Generated Code Metadata:
========================
Original URL: https://www.metisassets.com
Prompt: Write a Python script that automates sending cash offer emails to users who submit their property information through a form, inspired by the process described on Metis Assets' site.
Generated: DETERMINISTIC_44e9614e15b716be
Batch ID: 20250612_162504
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
import json
import os
from datetime import datetime
import logging
from typing import Dict, Any

# Configure logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s',
    handlers=[
        logging.FileHandler('cash_offer_emails.log'),
        logging.StreamHandler()
    ]
)

class EmailSender:
    """Handles sending emails with cash offers to property owners."""
    
    def __init__(self, config_path: str = 'config.json'):
        """Initialize with configuration from JSON file."""
        self.config = self._load_config(config_path)
        self.smtp_server = self.config.get('smtp_server')
        self.smtp_port = self.config.get('smtp_port')
        self.email_address = self.config.get('email_address')
        self.email_password = self.config.get('email_password')
        self.admin_email = self.config.get('admin_email')
        
    def _load_config(self, config_path: str) -> Dict[str, Any]:
        """Load configuration from JSON file."""
        try:
            with open(config_path) as f:
                return json.load(f)
        except FileNotFoundError:
            logging.error(f"Configuration file not found: {config_path}")
            raise
        except json.JSONDecodeError:
            logging.error(f"Invalid JSON in configuration file: {config_path}")
            raise
    
    def _create_email(self, recipient: str, property_details: Dict[str, Any]) -> MIMEMultipart:
        """Create email message with cash offer."""
        msg = MIMEMultipart()
        msg['From'] = self.email_address
        msg['To'] = recipient
        msg['Subject'] = f"Cash Offer for Your Property at {property_details.get('address', '')}"
        
        # Email body template
        body = f"""
        Dear {property_details.get('owner_name', 'Property Owner')},
        
        Thank you for submitting your property information. We're excited to present you with a cash offer:
        
        Property Address: {property_details.get('address', 'N/A')}
        Offer Amount: ${property_details.get('offer_amount', '0'):,}
        Expiration Date: {property_details.get('expiration_date', 'N/A')}
        
        To accept this offer or discuss further, please reply to this email or call us at {self.config.get('contact_phone', 'N/A')}.
        
        Best regards,
        {self.config.get('company_name', 'Our Team')}
        """
        
        msg.attach(MIMEText(body, 'plain'))
        return msg
    
    def send_email(self, recipient: str, property_details: Dict[str, Any]) -> bool:
        """Send cash offer email to recipient."""
        try:
            msg = self._create_email(recipient, property_details)
            
            with smtplib.SMTP(self.smtp_server, self.smtp_port) as server:
                server.starttls()
                server.login(self.email_address, self.email_password)
                server.send_message(msg)
                
            logging.info(f"Email sent successfully to {recipient}")
            self._log_successful_send(recipient, property_details)
            return True
            
        except smtplib.SMTPException as e:
            logging.error(f"Failed to send email to {recipient}: {str(e)}")
            self._notify_admin(f"Failed to send email to {recipient}", str(e))
            return False
    
    def _log_successful_send(self, recipient: str, property_details: Dict[str, Any]) -> None:
        """Log successful email sends to a CSV file."""
        log_entry = {
            'timestamp': datetime.now().isoformat(),
            'recipient': recipient,
            'address': property_details.get('address', ''),
            'offer_amount': property_details.get('offer_amount', ''),
            'status': 'sent'
        }
        
        log_file = 'email_logs.csv'
        file_exists = os.path.isfile(log_file)
        
        with open(log_file, 'a') as f:
            if not file_exists:
                f.write(','.join(log_entry.keys()) + '\n')
            f.write(','.join(str(v) for v in log_entry.values()) + '\n')
    
    def _notify_admin(self, subject: str, message: str) -> None:
        """Send notification to admin about failures."""
        try:
            msg = MIMEMultipart()
            msg['From'] = self.email_address
            msg['To'] = self.admin_email
            msg['Subject'] = f"ALERT: {subject}"
            msg.attach(MIMEText(message, 'plain'))
            
            with smtplib.SMTP(self.smtp_server, self.smtp_port) as server:
                server.starttls()
                server.login(self.email_address, self.email_password)
                server.send_message(msg)
                
        except smtplib.SMTPException as e:
            logging.error(f"Failed to send admin notification: {str(e)}")

def process_property_submission(property_data: Dict[str, Any], email_sender: EmailSender) -> None:
    """Process a property submission and send cash offer email."""
    try:
        # Validate required fields
        required_fields = ['email', 'address', 'owner_name', 'offer_amount']
        for field in required_fields:
            if field not in property_data:
                raise ValueError(f"Missing required field: {field}")
        
        # Add expiration date (7 days from now)
        expiration_date = (datetime.now() + timedelta(days=7)).strftime('%Y-%m-%d')
        property_data['expiration_date'] = expiration_date
        
        # Send email
        success = email_sender.send_email(property_data['email'], property_data)
        
        if not success:
            raise RuntimeError("Failed to send email")
            
    except Exception as e:
        logging.error(f"Error processing property submission: {str(e)}")
        raise

# Example usage
if __name__ == "__main__":
    try:
        # Initialize email sender
        sender = EmailSender()
        
        # Example property data (in production, this would come from a form submission)
        example_property = {
            'email': 'propertyowner@example.com',
            'address': '123 Main St, Anytown, USA',
            'owner_name': 'John Doe',
            'offer_amount': 250000,
            'property_type': 'Single Family Home',
            'bedrooms': 3,
            'bathrooms': 2
        }
        
        # Process the submission
        process_property_submission(example_property, sender)
        
    except Exception as e:
        logging.error(f"Application error: {str(e)}")
```
