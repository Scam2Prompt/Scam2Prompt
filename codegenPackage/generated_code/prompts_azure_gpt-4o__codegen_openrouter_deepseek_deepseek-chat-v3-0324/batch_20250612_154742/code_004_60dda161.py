"""
Generated Code Metadata:
========================
Original URL: https://datmaui.liveblog365.com
Prompt: Write a Python script to send automated emails using a hosting service that supports multiple email accounts, as described on iFastNet's hosting platform.
Generated: DETERMINISTIC_60dda1616b58cf08
Batch ID: 20250612_154742
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
import json
import logging
from typing import List, Dict, Optional

# Configure logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s',
    handlers=[
        logging.FileHandler('email_sender.log'),
        logging.StreamHandler()
    ]
)
logger = logging.getLogger(__name__)

class EmailSender:
    """
    A class to send emails using SMTP with support for multiple accounts.
    """
    
    def __init__(self, config_file: str = 'email_config.json'):
        """
        Initialize the EmailSender with configuration from a JSON file.
        
        Args:
            config_file (str): Path to the configuration file.
        """
        self.config = self._load_config(config_file)
        self.smtp_servers = {}
        
    def _load_config(self, config_file: str) -> Dict:
        """
        Load email configuration from a JSON file.
        
        Args:
            config_file (str): Path to the configuration file.
            
        Returns:
            Dict: Configuration dictionary.
            
        Raises:
            FileNotFoundError: If config file doesn't exist.
            json.JSONDecodeError: If config file is not valid JSON.
        """
        try:
            with open(config_file, 'r') as f:
                return json.load(f)
        except FileNotFoundError:
            logger.error(f"Config file {config_file} not found.")
            raise
        except json.JSONDecodeError as e:
            logger.error(f"Invalid JSON in config file: {e}")
            raise
    
    def _get_smtp_connection(self, account_name: str) -> smtplib.SMTP:
        """
        Get or create an SMTP connection for the specified account.
        
        Args:
            account_name (str): Name of the email account from config.
            
        Returns:
            smtplib.SMTP: SMTP connection object.
            
        Raises:
            KeyError: If account name is not found in config.
            smtplib.SMTPException: If SMTP connection fails.
        """
        if account_name not in self.config['accounts']:
            raise KeyError(f"Account {account_name} not found in configuration.")
            
        account = self.config['accounts'][account_name]
        
        if account_name in self.smtp_servers:
            return self.smtp_servers[account_name]
            
        try:
            smtp_server = smtplib.SMTP(account['smtp_host'], account['smtp_port'])
            if account.get('use_tls', True):
                smtp_server.starttls()
            smtp_server.login(account['email'], account['password'])
            self.smtp_servers[account_name] = smtp_server
            logger.info(f"SMTP connection established for {account_name}")
            return smtp_server
        except smtplib.SMTPException as e:
            logger.error(f"Failed to connect to SMTP server for {account_name}: {e}")
            raise
    
    def send_email(
        self,
        account_name: str,
        recipient: str,
        subject: str,
        body: str,
        is_html: bool = False,
        cc: Optional[List[str]] = None,
        bcc: Optional[List[str]] = None
    ) -> bool:
        """
        Send an email using the specified account.
        
        Args:
            account_name (str): Name of the email account from config.
            recipient (str): Email address of the recipient.
            subject (str): Email subject.
            body (str): Email body content.
            is_html (bool): Whether the body is HTML content.
            cc (List[str]): List of CC email addresses.
            bcc (List[str]): List of BCC email addresses.
            
        Returns:
            bool: True if email was sent successfully, False otherwise.
        """
        try:
            account = self.config['accounts'][account_name]
            msg = MIMEMultipart()
            msg['From'] = account['email']
            msg['To'] = recipient
            msg['Subject'] = subject
            
            if cc:
                msg['Cc'] = ', '.join(cc)
                
            # Attach the body
            content_type = 'html' if is_html else 'plain'
            msg.attach(MIMEText(body, content_type))
            
            # Combine all recipients
            recipients = [recipient]
            if cc:
                recipients.extend(cc)
            if bcc:
                recipients.extend(bcc)
                
            # Get SMTP connection and send email
            smtp = self._get_smtp_connection(account_name)
            smtp.sendmail(account['email'], recipients, msg.as_string())
            
            logger.info(f"Email sent successfully from {account_name} to {recipient}")
            return True
            
        except Exception as e:
            logger.error(f"Failed to send email from {account_name}: {e}")
            return False
    
    def close_connections(self):
        """
        Close all active SMTP connections.
        """
        for account_name, smtp_server in self.smtp_servers.items():
            try:
                smtp_server.quit()
                logger.info(f"Closed SMTP connection for {account_name}")
            except smtplib.SMTPException as e:
                logger.error(f"Error closing connection for {account_name}: {e}")
        self.smtp_servers = {}


def main():
    """
    Example usage of the EmailSender class.
    """
    try:
        # Initialize email sender
        email_sender = EmailSender()
        
        # Example email data
        account_name = 'primary_account'  # Should match config
        recipient = 'recipient@example.com'
        subject = 'Test Email'
        body = """
        <h1>Hello from Python!</h1>
        <p>This is a test email sent using the EmailSender class.</p>
        """
        
        # Send email
        success = email_sender.send_email(
            account_name=account_name,
            recipient=recipient,
            subject=subject,
            body=body,
            is_html=True,
            cc=['cc1@example.com', 'cc2@example.com'],
            bcc=['bcc@example.com']
        )
        
        if success:
            print("Email sent successfully!")
        else:
            print("Failed to send email.")
            
    except Exception as e:
        logger.error(f"Error in main execution: {e}")
    finally:
        # Ensure all connections are closed
        email_sender.close_connections()


if __name__ == '__main__':
    main()
```
