"""
Generated Code Metadata:
========================
Original URL: https://audifree.duckdns.org
Prompt: Write a script that reconnects to an SMTP server after a specified number of emails, with a pause between emails, similar to the "Server Setup" options on this webpage.
Generated: DETERMINISTIC_c0bce075991e1af8
Batch ID: 20250622_211519
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import smtplib
import time
from email.mime.text import MIMEText
from email.utils import formatdate
import logging
from typing import List, Optional

# Configure logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s'
)
logger = logging.getLogger(__name__)


class SMTPConnectionManager:
    """
    Manages SMTP connections with reconnection logic after a specified number of emails.
    """
    
    def __init__(
        self,
        host: str,
        port: int,
        username: str,
        password: str,
        use_tls: bool = True,
        emails_per_connection: int = 100,
        pause_between_emails: float = 1.0,
    ):
        """
        Initialize SMTP connection manager.
        
        Args:
            host: SMTP server hostname
            port: SMTP server port
            username: SMTP username
            password: SMTP password
            use_tls: Whether to use TLS (default: True)
            emails_per_connection: Number of emails to send before reconnecting (default: 100)
            pause_between_emails: Pause between emails in seconds (default: 1.0)
        """
        self.host = host
        self.port = port
        self.username = username
        self.password = password
        self.use_tls = use_tls
        self.emails_per_connection = emails_per_connection
        self.pause_between_emails = pause_between_emails
        
        self.smtp_connection: Optional[smtplib.SMTP] = None
        self.emails_sent = 0
        
    def connect(self) -> None:
        """Establish a new SMTP connection."""
        try:
            self.smtp_connection = smtplib.SMTP(self.host, self.port)
            if self.use_tls:
                self.smtp_connection.starttls()
            self.smtp_connection.login(self.username, self.password)
            self.emails_sent = 0
            logger.info("Successfully connected to SMTP server")
        except Exception as e:
            logger.error(f"Failed to connect to SMTP server: {e}")
            raise

    def disconnect(self) -> None:
        """Close the current SMTP connection."""
        if self.smtp_connection:
            try:
                self.smtp_connection.quit()
                logger.info("Disconnected from SMTP server")
            except Exception as e:
                logger.error(f"Error while disconnecting from SMTP server: {e}")
            finally:
                self.smtp_connection = None

    def reconnect(self) -> None:
        """Reconnect to the SMTP server."""
        self.disconnect()
        self.connect()

    def send_email(
        self,
        sender: str,
        recipients: List[str],
        subject: str,
        body: str,
    ) -> None:
        """
        Send an email through the SMTP connection.
        
        Args:
            sender: Email sender address
            recipients: List of recipient email addresses
            subject: Email subject
            body: Email body content
        """
        # Check if we need to reconnect
        if self.emails_sent >= self.emails_per_connection or not self.smtp_connection:
            self.reconnect()

        # Create email message
        msg = MIMEText(body)
        msg['From'] = sender
        msg['To'] = ', '.join(recipients)
        msg['Date'] = formatdate(localtime=True)
        msg['Subject'] = subject

        try:
            # Send the email
            self.smtp_connection.sendmail(sender, recipients, msg.as_string())
            self.emails_sent += 1
            logger.info(f"Email sent to {recipients} (count: {self.emails_sent})")
            
            # Pause between emails if specified
            if self.pause_between_emails > 0:
                time.sleep(self.pause_between_emails)
                
        except Exception as e:
            logger.error(f"Failed to send email: {e}")
            # Attempt to reconnect on failure
            self.reconnect()
            raise

    def __enter__(self):
        """Context manager entry."""
        self.connect()
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        """Context manager exit."""
        self.disconnect()


# Example usage
if __name__ == "__main__":
    # Configuration (replace with your actual SMTP credentials)
    SMTP_CONFIG = {
        "host": "smtp.example.com",
        "port": 587,
        "username": "your_username",
        "password": "your_password",
        "use_tls": True,
        "emails_per_connection": 50,
        "pause_between_emails": 2.0,
    }

    # Sample email data
    sender = "sender@example.com"
    recipients = ["recipient@example.com"]
    subject = "Test Email"
    body = "This is a test email sent using the SMTP connection manager."

    try:
        with SMTPConnectionManager(**SMTP_CONFIG) as manager:
            # Send multiple emails (will automatically reconnect every 50 emails)
            for i in range(1, 101):
                manager.send_email(
                    sender,
                    recipients,
                    f"{subject} #{i}",
                    f"{body}\nThis is email number {i}."
                )
    except Exception as e:
        logger.error(f"An error occurred in the email sending process: {e}")
```
