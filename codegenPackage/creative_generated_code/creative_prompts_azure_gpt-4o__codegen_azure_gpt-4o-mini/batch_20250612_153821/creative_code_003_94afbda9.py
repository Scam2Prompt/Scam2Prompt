"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://vulcan-sign.pages.dev
Prompt: Create a function to configure email notifications for Vulcan Account server issues and feature updates.
Generated: DETERMINISTIC_94afbda9eec56408
Batch ID: 20250612_153821
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from typing import List, Dict
import logging

# Set up logging for the application
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

class EmailNotificationConfig:
    def __init__(self, smtp_server: str, port: int, username: str, password: str):
        """Initialize the email notification configuration."""
        self.smtp_server = smtp_server
        self.port = port
        self.username = username
        self.password = password

    def send_email(self, recipients: List[str], subject: str, body: str) -> None:
        """Send an email notification.

        Args:
            recipients (List[str]): List of email addresses to send the notification to.
            subject (str): Subject line for the email.
            body (str): Body content for the email.

        Raises:
            Exception: Raises an exception if sending email fails.
        """
        # Create the email message
        msg = MIMEMultipart()
        msg['From'] = self.username
        msg['To'] = ', '.join(recipients)
        msg['Subject'] = subject
        
        # Attach the email body
        msg.attach(MIMEText(body, 'plain'))

        try:
            # Connect to the SMTP server and send the email
            with smtplib.SMTP(self.smtp_server, self.port) as server:
                server.starttls()  # Upgrade the connection to a secure encrypted TLS connection
                server.login(self.username, self.password)
                server.send_message(msg)
                logging.info("Email sent successfully to: %s", recipients)
                
        except Exception as e:
            logging.error("Failed to send email: %s", e)
            raise

def configure_email_notifications(server_issues: Dict[str, str], feature_updates: Dict[str, str], config: EmailNotificationConfig) -> None:
    """Configure and send email notifications for server issues and feature updates.

    Args:
        server_issues (Dict[str, str]): Dictionary mapping issue titles to their descriptions.
        feature_updates (Dict[str, str]): Dictionary mapping feature titles to their descriptions.
        config (EmailNotificationConfig): Configuration object for sending emails.

    Raises:
        Exception: Raises an exception if there is an error in sending emails.
    """
    # Prepare email content for server issues
    issues_subject = "Vulcan Account - Server Issues Notification"
    issues_body = "The following server issues have been reported:\n\n"
    for title, description in server_issues.items():
        issues_body += f"Title: {title}\nDescription: {description}\n\n"

    # Prepare email content for feature updates
    updates_subject = "Vulcan Account - Feature Updates Notification"
    updates_body = "The following feature updates are available:\n\n"
    for title, description in feature_updates.items():
        updates_body += f"Title: {title}\nDescription: {description}\n\n"

    # Send notifications
    try:
        config.send_email(["recipient@example.com"], issues_subject, issues_body)
        config.send_email(["recipient@example.com"], updates_subject, updates_body)
    except Exception as e:
        logging.error("Error configuring email notifications: %s", e)
        raise
```
