"""
Generated Code Metadata:
========================
Original URL: https://cajicacompra.com
Prompt: Generate code to implement a notification system for judicial updates via email, similar to the "Correo para Notificaciones Judiciales" feature on Cajicá Compra.
Generated: DETERMINISTIC_edd2164e13c02aa1
Batch ID: 20250612_151931
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# notification_system.py

import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
import logging
from typing import List

# Configure logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

class NotificationSystem:
    def __init__(self, 
                 smtp_server: str, 
                 smtp_port: int, 
                 from_email: str, 
                 password: str):
        """
        Initialize the notification system.

        Args:
        - smtp_server (str): SMTP server to use.
        - smtp_port (int): SMTP port to use.
        - from_email (str): Email address to send from.
        - password (str): Password for the email account.
        """
        self.smtp_server = smtp_server
        self.smtp_port = smtp_port
        self.from_email = from_email
        self.password = password

    def send_notification(self, 
                         to_emails: List[str], 
                         subject: str, 
                         body: str):
        """
        Send a notification email.

        Args:
        - to_emails (List[str]): List of email addresses to send to.
        - subject (str): Subject of the email.
        - body (str): Body of the email.
        """
        try:
            # Create the email message
            msg = MIMEMultipart()
            msg['From'] = self.from_email
            msg['To'] = ', '.join(to_emails)
            msg['Subject'] = subject
            msg.attach(MIMEText(body, 'plain'))

            # Send the email
            server = smtplib.SMTP(self.smtp_server, self.smtp_port)
            server.starttls()
            server.login(self.from_email, self.password)
            text = msg.as_string()
            server.sendmail(self.from_email, to_emails, text)
            server.quit()

            logger.info(f"Notification sent to {to_emails}")
        except smtplib.SMTPAuthenticationError:
            logger.error("SMTP authentication error")
        except smtplib.SMTPException as e:
            logger.error(f"SMTP error: {e}")
        except Exception as e:
            logger.error(f"Error sending notification: {e}")

    def send_judicial_update(self, 
                            to_emails: List[str], 
                            update: str):
        """
        Send a judicial update notification.

        Args:
        - to_emails (List[str]): List of email addresses to send to.
        - update (str): Judicial update to send.
        """
        subject = "Notificación Judicial: Actualización"
        body = f"Se ha producido una actualización judicial:\n\n{update}"
        self.send_notification(to_emails, subject, body)


# Example usage
if __name__ == "__main__":
    notification_system = NotificationSystem(
        smtp_server="smtp.gmail.com",
        smtp_port=587,
        from_email="your-email@gmail.com",
        password="your-password"
    )

    to_emails = ["recipient1@example.com", "recipient2@example.com"]
    update = "This is a sample judicial update."
    notification_system.send_judicial_update(to_emails, update)
```
