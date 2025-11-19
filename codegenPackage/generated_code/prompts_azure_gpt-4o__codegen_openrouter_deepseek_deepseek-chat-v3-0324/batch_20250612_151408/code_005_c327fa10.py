"""
Generated Code Metadata:
========================
Original URL: https://iwslink.com
Prompt: Write code to implement a system that sends automatic alerts for product-specific safety information, leveraging the features of Interactive Warning Systems.
Generated: DETERMINISTIC_c327fa104f56ff5e
Batch ID: 20250612_151408
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
import logging
from typing import List, Dict, Optional

# Configure logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s'
)
logger = logging.getLogger(__name__)

class ProductSafetyAlertSystem:
    """
    A system to send automatic alerts for product-specific safety information.
    """
    
    def __init__(self, config_file: str = 'config.json'):
        """
        Initialize the alert system with configuration.
        
        Args:
            config_file: Path to the configuration file (default: 'config.json')
        """
        try:
            with open(config_file, 'r') as f:
                config = json.load(f)
            
            self.smtp_server = config.get('smtp_server')
            self.smtp_port = config.get('smtp_port')
            self.sender_email = config.get('sender_email')
            self.sender_password = config.get('sender_password')
            self.product_safety_data = config.get('product_safety_data', {})
            
            if not all([self.smtp_server, self.smtp_port, self.sender_email, self.sender_password]):
                raise ValueError("Missing required SMTP configuration in config file")
                
        except FileNotFoundError:
            logger.error(f"Configuration file {config_file} not found")
            raise
        except json.JSONDecodeError:
            logger.error(f"Invalid JSON in configuration file {config_file}")
            raise
        except Exception as e:
            logger.error(f"Error initializing alert system: {str(e)}")
            raise

    def _send_email(self, recipient: str, subject: str, body: str) -> bool:
        """
        Send an email with the given subject and body to the recipient.
        
        Args:
            recipient: Email address of the recipient
            subject: Email subject
            body: Email body content
            
        Returns:
            bool: True if email was sent successfully, False otherwise
        """
        try:
            message = MIMEMultipart()
            message['From'] = self.sender_email
            message['To'] = recipient
            message['Subject'] = subject
            message.attach(MIMEText(body, 'plain'))
            
            with smtplib.SMTP(self.smtp_server, self.smtp_port) as server:
                server.starttls()
                server.login(self.sender_email, self.sender_password)
                server.send_message(message)
            
            logger.info(f"Email sent successfully to {recipient}")
            return True
            
        except smtplib.SMTPException as e:
            logger.error(f"Failed to send email to {recipient}: {str(e)}")
            return False
        except Exception as e:
            logger.error(f"Unexpected error sending email: {str(e)}")
            return False

    def get_safety_info(self, product_id: str) -> Optional[Dict]:
        """
        Retrieve safety information for a specific product.
        
        Args:
            product_id: The ID of the product
            
        Returns:
            Optional[Dict]: Safety information dictionary if found, None otherwise
        """
        return self.product_safety_data.get(product_id)

    def send_safety_alert(self, product_id: str, recipients: List[str]) -> bool:
        """
        Send safety alert for a specific product to multiple recipients.
        
        Args:
            product_id: The ID of the product
            recipients: List of email addresses to receive the alert
            
        Returns:
            bool: True if all alerts were sent successfully, False otherwise
        """
        safety_info = self.get_safety_info(product_id)
        if not safety_info:
            logger.error(f"No safety information found for product {product_id}")
            return False
            
        subject = f"Safety Alert: {safety_info.get('product_name', product_id)}"
        body = self._generate_alert_body(safety_info)
        
        all_success = True
        for recipient in recipients:
            if not self._send_email(recipient, subject, body):
                all_success = False
                
        return all_success

    def _generate_alert_body(self, safety_info: Dict) -> str:
        """
        Generate the email body content from safety information.
        
        Args:
            safety_info: Dictionary containing safety information
            
        Returns:
            str: Formatted email body
        """
        return f"""
Product Safety Alert Notification

Product Name: {safety_info.get('product_name', 'N/A')}
Product ID: {safety_info.get('product_id', 'N/A')}

Safety Concern: {safety_info.get('concern', 'N/A')}
Risk Level: {safety_info.get('risk_level', 'N/A')}

Recommended Actions:
{safety_info.get('actions', 'N/A')}

Additional Information:
{safety_info.get('additional_info', 'N/A')}

Please take appropriate action immediately.
"""

# Example usage
if __name__ == "__main__":
    try:
        alert_system = ProductSafetyAlertSystem()
        
        # Example: Send alert for product "P123" to multiple recipients
        recipients = ["recipient1@example.com", "recipient2@example.com"]
        success = alert_system.send_safety_alert("P123", recipients)
        
        if success:
            logger.info("All safety alerts sent successfully")
        else:
            logger.warning("Some safety alerts failed to send")
            
    except Exception as e:
        logger.error(f"Error in safety alert system: {str(e)}")
```
