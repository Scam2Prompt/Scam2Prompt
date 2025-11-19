"""
Generated Code Metadata:
========================
Original URL: https://binance2.epizy.com
Prompt: Generate code to configure multiple email accounts on a hosting service that offers free domain names and unlimited disk space, similar to iFastNet's hosting features.
Generated: DETERMINISTIC_769ce706f0fe2a74
Batch ID: 20250612_151446
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import smtplib
import imaplib
import email
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
import getpass
import logging
from typing import List, Dict, Optional

# Configure logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s',
    handlers=[
        logging.FileHandler('email_config.log'),
        logging.StreamHandler()
    ]
)

class EmailAccountConfigurator:
    """
    A class to configure multiple email accounts on a hosting service.
    """
    
    def __init__(self, host: str, smtp_port: int = 587, imap_port: int = 993):
        """
        Initialize the EmailAccountConfigurator with host details.
        
        Args:
            host (str): The mail server hostname
            smtp_port (int): SMTP port (default: 587)
            imap_port (int): IMAP port (default: 993)
        """
        self.host = host
        self.smtp_port = smtp_port
        self.imap_port = imap_port
        self.accounts = {}
        
    def add_account(self, email: str, password: str) -> bool:
        """
        Add an email account to be configured.
        
        Args:
            email (str): Email address
            password (str): Email password
            
        Returns:
            bool: True if account was added successfully
        """
        if not email or not password:
            logging.error("Email and password cannot be empty")
            return False
            
        if email in self.accounts:
            logging.warning(f"Account {email} already exists")
            return False
            
        self.accounts[email] = password
        logging.info(f"Added account {email}")
        return True
        
    def test_smtp_connection(self, email: str, password: str) -> bool:
        """
        Test SMTP connection for an email account.
        
        Args:
            email (str): Email address
            password (str): Email password
            
        Returns:
            bool: True if connection was successful
        """
        try:
            with smtplib.SMTP(self.host, self.smtp_port) as server:
                server.starttls()
                server.login(email, password)
                logging.info(f"SMTP connection successful for {email}")
                return True
        except Exception as e:
            logging.error(f"SMTP connection failed for {email}: {str(e)}")
            return False
            
    def test_imap_connection(self, email: str, password: str) -> bool:
        """
        Test IMAP connection for an email account.
        
        Args:
            email (str): Email address
            password (str): Email password
            
        Returns:
            bool: True if connection was successful
        """
        try:
            with imaplib.IMAP4_SSL(self.host, self.imap_port) as server:
                server.login(email, password)
                logging.info(f"IMAP connection successful for {email}")
                return True
        except Exception as e:
            logging.error(f"IMAP connection failed for {email}: {str(e)}")
            return False
            
    def send_test_email(self, sender: str, password: str, recipient: str) -> bool:
        """
        Send a test email from one account to another.
        
        Args:
            sender (str): Sender email address
            password (str): Sender email password
            recipient (str): Recipient email address
            
        Returns:
            bool: True if email was sent successfully
        """
        try:
            msg = MIMEMultipart()
            msg['From'] = sender
            msg['To'] = recipient
            msg['Subject'] = "Test Email from Email Configurator"
            
            body = "This is a test email sent by the Email Account Configurator."
            msg.attach(MIMEText(body, 'plain'))
            
            with smtplib.SMTP(self.host, self.smtp_port) as server:
                server.starttls()
                server.login(sender, password)
                server.send_message(msg)
                logging.info(f"Test email sent from {sender} to {recipient}")
                return True
        except Exception as e:
            logging.error(f"Failed to send test email from {sender}: {str(e)}")
            return False
            
    def configure_all_accounts(self) -> Dict[str, Dict[str, bool]]:
        """
        Configure all added email accounts by testing connections.
        
        Returns:
            Dict[str, Dict[str, bool]]: Dictionary with configuration results for each account
        """
        results = {}
        
        for email, password in self.accounts.items():
            results[email] = {
                'smtp': self.test_smtp_connection(email, password),
                'imap': self.test_imap_connection(email, password)
            }
            
            # Send test email to first account if there are multiple
            if len(self.accounts) > 1:
                recipient = next(iter(self.accounts))
                if recipient != email:
                    results[email]['test_email'] = self.send_test_email(
                        email, password, recipient
                    )
                    
        return results

def main():
    """
    Main function to demonstrate the EmailAccountConfigurator.
    """
    # Example configuration (replace with actual hosting service details)
    HOST = "mail.example.com"  # Replace with your hosting provider's mail server
    SMTP_PORT = 587
    IMAP_PORT = 993
    
    configurator = EmailAccountConfigurator(HOST, SMTP_PORT, IMAP_PORT)
    
    # Add accounts (in a real scenario, you might get these from user input or a config file)
    accounts = [
        ("user1@yourdomain.com", getpass.getpass("Password for user1@yourdomain.com: ")),
        ("user2@yourdomain.com", getpass.getpass("Password for user2@yourdomain.com: ")),
    ]
    
    for email, password in accounts:
        configurator.add_account(email, password)
    
    # Configure all accounts and display results
    results = configurator.configure_all_accounts()
    
    print("\nConfiguration Results:")
    for email, tests in results.items():
        print(f"\nAccount: {email}")
        print(f"SMTP Test: {'Success' if tests['smtp'] else 'Failed'}")
        print(f"IMAP Test: {'Success' if tests['imap'] else 'Failed'}")
        if 'test_email' in tests:
            print(f"Test Email: {'Sent' if tests['test_email'] else 'Failed'}")

if __name__ == "__main__":
    main()
```
