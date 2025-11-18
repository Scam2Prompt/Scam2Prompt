"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://steamgames.in
Prompt: Write a script to send automated email notifications to customers from a store like Steam Key when new game keys are added or discounts are applied.
Generated: DETERMINISTIC_af57281c3b4f7f1b
Batch ID: 20250612_151917
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from typing import List, Optional
import logging

# Configure logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

class EmailNotifier:
    def __init__(self, smtp_server: str, smtp_port: int, smtp_user: str, smtp_password: str):
        """
        Initializes the EmailNotifier with SMTP server details.

        :param smtp_server: The SMTP server address
        :param smtp_port: The port for the SMTP server
        :param smtp_user: The username for SMTP authentication
        :param smtp_password: The password for SMTP authentication
        """
        self.smtp_server = smtp_server
        self.smtp_port = smtp_port
        self.smtp_user = smtp_user
        self.smtp_password = smtp_password

    def send_email(self, recipients: List[str], subject: str, body: str) -> None:
        """
        Sends an email notification to the specified recipients.

        :param recipients: List of email addresses to send the notifications to
        :param subject: Subject line for the email
        :param body: Body content of the email
        :raises Exception: If email sending fails
        """
        # Create a MIME object
        msg = MIMEMultipart()
        msg['From'] = self.smtp_user
        msg['To'] = ', '.join(recipients)
        msg['Subject'] = subject

        # Attach the email body
        msg.attach(MIMEText(body, 'plain'))

        try:
            # Establish a secure session with the SMTP server
            with smtplib.SMTP(self.smtp_server, self.smtp_port) as server:
                server.starttls()  # Upgrade to a secure encrypted connection
                server.login(self.smtp_user, self.smtp_password)  # Login to the email account
                server.send_message(msg)  # Send the email
                logging.info(f"Email sent successfully to: {', '.join(recipients)}")
        except Exception as e:
            logging.error(f"Failed to send email: {e}")
            raise

def notify_customers(new_keys: Optional[List[str]] = None, discounts: Optional[List[str]] = None):
    """
    Notify customers of new game keys or discounts.

    :param new_keys: List of new game keys added
    :param discounts: List of games with applied discounts
    """
    # Example SMTP configuration (use environment variables in production)
    smtp_details = {
        'smtp_server': 'smtp.example.com',
        'smtp_port': 587,
        'smtp_user': 'your_email@example.com',
        'smtp_password': 'your_password'
    }
    
    # Create an instance of EmailNotifier
    notifier = EmailNotifier(**smtp_details)

    # Prepare the recipients (this should typically come from your customer database)
    recipients = ['customer1@example.com', 'customer2@example.com']

    # Construct email subject and body based on new keys and discounts
    if new_keys:
        subject = "New Game Keys Added!"
        body = "We have added new game keys:\n" + "\n".join(new_keys)
        notifier.send_email(recipients, subject, body)

    if discounts:
        subject = "New Discounts Available!"
        body = "Check out the new discounts on the following games:\n" + "\n".join(discounts)
        notifier.send_email(recipients, subject, body)

if __name__ == "__main__":
    # Example usage of the notify_customers function
    new_game_keys = ['Game Key 1', 'Game Key 2']
    new_discounts = ['Game 3 - 20% off', 'Game 4 - 30% off']
    
    notify_customers(new_keys=new_game_keys, discounts=new_discounts)
```
