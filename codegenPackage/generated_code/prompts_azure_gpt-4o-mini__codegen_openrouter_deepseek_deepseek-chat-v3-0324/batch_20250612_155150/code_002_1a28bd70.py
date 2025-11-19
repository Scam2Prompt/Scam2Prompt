"""
Generated Code Metadata:
========================
Original URL: https://allabouthepc.com
Prompt: How can I automate notifications for account suspension events using a library in Python?
Generated: DETERMINISTIC_1a28bd705a000d59
Batch ID: 20250612_155150
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import os
import smtplib
from email.message import EmailMessage
from datetime import datetime
import logging
from typing import List, Optional

# Configure logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s',
    handlers=[
        logging.FileHandler('account_suspension_notifier.log'),
        logging.StreamHandler()
    ]
)
logger = logging.getLogger(__name__)

class AccountSuspensionNotifier:
    """
    A class to handle automated notifications for account suspension events.
    """
    
    def __init__(
        self,
        smtp_server: str,
        smtp_port: int,
        sender_email: str,
        sender_password: str,
        admin_emails: List[str]
    ):
        """
        Initialize the notifier with SMTP settings and recipient emails.
        
        Args:
            smtp_server: SMTP server address
            smtp_port: SMTP server port
            sender_email: Email address to send from
            sender_password: Password for sender email
            admin_emails: List of admin emails to notify
        """
        self.smtp_server = smtp_server
        self.smtp_port = smtp_port
        self.sender_email = sender_email
        self.sender_password = sender_password
        self.admin_emails = admin_emails
        
    def _send_email(
        self,
        subject: str,
        body: str,
        recipient_emails: List[str]
    ) -> bool:
        """
        Send an email notification.
        
        Args:
            subject: Email subject
            body: Email body content
            recipient_emails: List of recipient emails
            
        Returns:
            bool: True if email was sent successfully, False otherwise
        """
        try:
            msg = EmailMessage()
            msg['Subject'] = subject
            msg['From'] = self.sender_email
            msg['To'] = ', '.join(recipient_emails)
            msg.set_content(body)
            
            with smtplib.SMTP_SSL(self.smtp_server, self.smtp_port) as server:
                server.login(self.sender_email, self.sender_password)
                server.send_message(msg)
            
            logger.info(f"Email sent successfully to {recipient_emails}")
            return True
        except Exception as e:
            logger.error(f"Failed to send email: {str(e)}")
            return False
    
    def notify_account_suspension(
        self,
        username: str,
        account_id: str,
        suspension_reason: str,
        suspension_date: Optional[datetime] = None,
        custom_message: Optional[str] = None
    ) -> bool:
        """
        Send notification about an account suspension event.
        
        Args:
            username: The username of the suspended account
            account_id: The ID of the suspended account
            suspension_reason: Reason for suspension
            suspension_date: Date of suspension (defaults to now)
            custom_message: Optional custom message to include
            
        Returns:
            bool: True if notification was sent successfully, False otherwise
        """
        if not suspension_date:
            suspension_date = datetime.now()
            
        date_str = suspension_date.strftime("%Y-%m-%d %H:%M:%S")
        
        subject = f"Account Suspension Alert: {username}"
        
        body = f"""
        Account Suspension Notification
        
        Username: {username}
        Account ID: {account_id}
        Suspension Date: {date_str}
        Reason: {suspension_reason}
        """
        
        if custom_message:
            body += f"\nAdditional Notes: {custom_message}\n"
            
        return self._send_email(subject, body, self.admin_emails)

# Example usage
if __name__ == "__main__":
    # Load configuration from environment variables
    SMTP_SERVER = os.getenv("SMTP_SERVER", "smtp.example.com")
    SMTP_PORT = int(os.getenv("SMTP_PORT", 465))
    SENDER_EMAIL = os.getenv("SENDER_EMAIL", "noreply@example.com")
    SENDER_PASSWORD = os.getenv("SENDER_PASSWORD")
    ADMIN_EMAILS = os.getenv("ADMIN_EMAILS", "admin@example.com").split(",")
    
    if not SENDER_PASSWORD:
        raise ValueError("Sender password must be provided via SENDER_PASSWORD environment variable")
    
    notifier = AccountSuspensionNotifier(
        smtp_server=SMTP_SERVER,
        smtp_port=SMTP_PORT,
        sender_email=SENDER_EMAIL,
        sender_password=SENDER_PASSWORD,
        admin_emails=ADMIN_EMAILS
    )
    
    # Simulate an account suspension event
    notifier.notify_account_suspension(
        username="johndoe",
        account_id="12345",
        suspension_reason="Violation of terms of service",
        custom_message="Please review this account for potential reinstatement."
    )
```
