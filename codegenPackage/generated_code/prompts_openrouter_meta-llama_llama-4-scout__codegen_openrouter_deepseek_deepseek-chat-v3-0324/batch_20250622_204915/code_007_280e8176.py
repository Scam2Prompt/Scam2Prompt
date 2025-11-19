"""
Generated Code Metadata:
========================
Original URL: https://foolz.sellpass.io
Prompt: Develop a Sellpass plugin to automate the process of sending promo codes and coupons to customers.
Generated: DETERMINISTIC_280e8176a4760d3c
Batch ID: 20250622_204915
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import os
import json
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from typing import List, Dict, Optional
import logging
from datetime import datetime

# Configure logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s'
)
logger = logging.getLogger(__name__)

class SellpassPromoCodeSender:
    """
    A Sellpass plugin to automate sending promo codes and coupons to customers.
    """
    
    def __init__(self, config_path: str = "config.json"):
        """
        Initialize the plugin with configuration.
        
        Args:
            config_path (str): Path to the configuration file.
        """
        self.config = self._load_config(config_path)
        self.smtp_connection = None
        
    def _load_config(self, config_path: str) -> Dict:
        """
        Load configuration from JSON file.
        
        Args:
            config_path (str): Path to the configuration file.
            
        Returns:
            Dict: Configuration dictionary.
            
        Raises:
            FileNotFoundError: If config file doesn't exist.
            json.JSONDecodeError: If config file is not valid JSON.
        """
        try:
            with open(config_path, 'r') as f:
                return json.load(f)
        except FileNotFoundError:
            logger.error(f"Config file not found at {config_path}")
            raise
        except json.JSONDecodeError as e:
            logger.error(f"Invalid JSON in config file: {e}")
            raise
    
    def _connect_smtp(self) -> None:
        """
        Establish SMTP connection using configuration.
        
        Raises:
            smtplib.SMTPException: If connection fails.
        """
        try:
            self.smtp_connection = smtplib.SMTP(
                self.config['smtp']['host'],
                self.config['smtp']['port']
            )
            if self.config['smtp'].get('tls', False):
                self.smtp_connection.starttls()
            self.smtp_connection.login(
                self.config['smtp']['username'],
                self.config['smtp']['password']
            )
            logger.info("SMTP connection established successfully")
        except smtplib.SMTPException as e:
            logger.error(f"Failed to connect to SMTP server: {e}")
            raise
    
    def _disconnect_smtp(self) -> None:
        """
        Close SMTP connection if it exists.
        """
        if self.smtp_connection:
            try:
                self.smtp_connection.quit()
                logger.info("SMTP connection closed")
            except smtplib.SMTPException as e:
                logger.warning(f"Error while disconnecting SMTP: {e}")
    
    def _render_email_template(self, template_name: str, context: Dict) -> str:
        """
        Render email template with provided context.
        
        Args:
            template_name (str): Name of the template to use.
            context (Dict): Context variables for template.
            
        Returns:
            str: Rendered email content.
            
        Raises:
            FileNotFoundError: If template file doesn't exist.
        """
        template_path = os.path.join(
            self.config['templates_dir'],
            f"{template_name}.html"
        )
        
        try:
            with open(template_path, 'r') as f:
                template = f.read()
                return template.format(**context)
        except FileNotFoundError:
            logger.error(f"Template file not found: {template_path}")
            raise
    
    def _send_email(self, recipient: str, subject: str, html_content: str) -> bool:
        """
        Send an email to the recipient.
        
        Args:
            recipient (str): Email address of recipient.
            subject (str): Email subject.
            html_content (str): HTML content of the email.
            
        Returns:
            bool: True if email was sent successfully, False otherwise.
        """
        if not self.smtp_connection:
            try:
                self._connect_smtp()
            except smtplib.SMTPException:
                return False
        
        try:
            msg = MIMEMultipart()
            msg['From'] = self.config['email']['from']
            msg['To'] = recipient
            msg['Subject'] = subject
            
            msg.attach(MIMEText(html_content, 'html'))
            
            self.smtp_connection.send_message(msg)
            logger.info(f"Email sent to {recipient}")
            return True
        except smtplib.SMTPException as e:
            logger.error(f"Failed to send email to {recipient}: {e}")
            return False
    
    def send_promo_codes(
        self,
        customers: List[Dict],
        promo_code: str,
        template_name: str = "default",
        subject: Optional[str] = None
    ) -> Dict[str, List[str]]:
        """
        Send promo codes to multiple customers.
        
        Args:
            customers (List[Dict]): List of customer dictionaries containing at least 'email'.
            promo_code (str): The promo code to send.
            template_name (str): Name of the template to use.
            subject (str, optional): Email subject. Defaults to config value.
            
        Returns:
            Dict[str, List[str]]: Dictionary with 'success' and 'failed' lists of emails.
        """
        if not subject:
            subject = self.config['email'].get('default_subject', 'Your Promo Code')
        
        results = {
            'success': [],
            'failed': []
        }
        
        for customer in customers:
            email = customer.get('email')
            if not email:
                logger.warning("Customer missing email, skipping")
                continue
            
            context = {
                'customer': customer,
                'promo_code': promo_code,
                'date': datetime.now().strftime('%Y-%m-%d')
            }
            
            try:
                html_content = self._render_email_template(template_name, context)
            except FileNotFoundError:
                results['failed'].append(email)
                continue
            
            if self._send_email(email, subject, html_content):
                results['success'].append(email)
            else:
                results['failed'].append(email)
        
        self._disconnect_smtp()
        return results

# Example usage
if __name__ == "__main__":
    try:
        # Initialize the plugin
        sender = SellpassPromoCodeSender()
        
        # Example customers data
        customers = [
            {"email": "customer1@example.com", "name": "John Doe"},
            {"email": "customer2@example.com", "name": "Jane Smith"}
        ]
        
        # Send promo codes
        promo_code = "SUMMER2023"
        results = sender.send_promo_codes(customers, promo_code)
        
        logger.info(f"Results: {results}")
    except Exception as e:
        logger.error(f"Error in main execution: {e}")
```
