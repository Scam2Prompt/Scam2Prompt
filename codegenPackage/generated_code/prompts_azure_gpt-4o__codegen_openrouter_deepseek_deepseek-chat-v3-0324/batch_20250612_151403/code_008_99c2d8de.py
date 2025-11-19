"""
Generated Code Metadata:
========================
Original URL: https://digitechcareindia.com
Prompt: Write a Python script for automating email marketing campaigns, inspired by the email marketing solutions offered by DigiTech Care India.
Generated: DETERMINISTIC_99c2d8ded096352a
Batch ID: 20250612_151403
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import smtplib
import csv
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.base import MIMEBase
from email import encoders
import os
import time
from datetime import datetime
import logging
from typing import List, Dict, Optional

# Configure logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s',
    filename='email_campaign.log'
)
logger = logging.getLogger(__name__)

class EmailCampaign:
    def __init__(
        self,
        smtp_server: str,
        smtp_port: int,
        sender_email: str,
        sender_password: str,
        subject: str,
        template_path: str,
        recipients_csv: str,
        attachment_path: Optional[str] = None,
        delay_seconds: int = 1
    ):
        """
        Initialize email campaign with SMTP settings and campaign details.
        
        Args:
            smtp_server: SMTP server address
            smtp_port: SMTP server port
            sender_email: Email address of the sender
            sender_password: Password for the sender email
            subject: Email subject line
            template_path: Path to HTML email template
            recipients_csv: Path to CSV file with recipient data
            attachment_path: Optional path to attachment file
            delay_seconds: Delay between emails in seconds
        """
        self.smtp_server = smtp_server
        self.smtp_port = smtp_port
        self.sender_email = sender_email
        self.sender_password = sender_password
        self.subject = subject
        self.template_path = template_path
        self.recipients_csv = recipients_csv
        self.attachment_path = attachment_path
        self.delay_seconds = delay_seconds
        self.sent_count = 0
        self.failed_count = 0

    def _load_template(self) -> str:
        """Load HTML email template from file."""
        try:
            with open(self.template_path, 'r', encoding='utf-8') as file:
                return file.read()
        except Exception as e:
            logger.error(f"Error loading template: {e}")
            raise

    def _load_recipients(self) -> List[Dict[str, str]]:
        """Load recipient data from CSV file."""
        recipients = []
        try:
            with open(self.recipients_csv, 'r', encoding='utf-8') as file:
                reader = csv.DictReader(file)
                for row in reader:
                    recipients.append(row)
            return recipients
        except Exception as e:
            logger.error(f"Error loading recipients: {e}")
            raise

    def _prepare_email(
        self,
        recipient_email: str,
        recipient_name: str,
        template: str,
        custom_fields: Dict[str, str]
    ) -> MIMEMultipart:
        """Prepare email message with personalized content."""
        try:
            # Personalize template
            personalized_content = template
            for field, value in custom_fields.items():
                placeholder = f"{{{{{field}}}}}"
                personalized_content = personalized_content.replace(placeholder, value)
            personalized_content = personalized_content.replace("{{name}}", recipient_name)

            # Create message container
            msg = MIMEMultipart()
            msg['From'] = self.sender_email
            msg['To'] = recipient_email
            msg['Subject'] = self.subject

            # Attach HTML body
            msg.attach(MIMEText(personalized_content, 'html'))

            # Attach file if specified
            if self.attachment_path and os.path.exists(self.attachment_path):
                part = MIMEBase('application', 'octet-stream')
                with open(self.attachment_path, 'rb') as file:
                    part.set_payload(file.read())
                encoders.encode_base64(part)
                part.add_header(
                    'Content-Disposition',
                    f'attachment; filename="{os.path.basename(self.attachment_path)}"'
                )
                msg.attach(part)

            return msg
        except Exception as e:
            logger.error(f"Error preparing email for {recipient_email}: {e}")
            raise

    def _send_email(self, msg: MIMEMultipart, recipient_email: str) -> bool:
        """Send email using SMTP server."""
        try:
            with smtplib.SMTP(self.smtp_server, self.smtp_port) as server:
                server.starttls()
                server.login(self.sender_email, self.sender_password)
                server.send_message(msg)
            logger.info(f"Email sent to {recipient_email}")
            return True
        except smtplib.SMTPException as e:
            logger.error(f"SMTP error sending to {recipient_email}: {e}")
            return False
        except Exception as e:
            logger.error(f"Error sending to {recipient_email}: {e}")
            return False

    def run_campaign(self) -> None:
        """Execute the email campaign."""
        logger.info("Starting email campaign")
        start_time = datetime.now()

        try:
            template = self._load_template()
            recipients = self._load_recipients()

            for recipient in recipients:
                try:
                    email = recipient['email']
                    name = recipient.get('name', 'Valued Customer')
                    
                    # Prepare custom fields (all CSV columns except email and name)
                    custom_fields = {
                        k: v for k, v in recipient.items() 
                        if k not in ['email', 'name']
                    }

                    msg = self._prepare_email(email, name, template, custom_fields)
                    
                    if self._send_email(msg, email):
                        self.sent_count += 1
                    else:
                        self.failed_count += 1

                    time.sleep(self.delay_seconds)

                except Exception as e:
                    logger.error(f"Error processing recipient {recipient.get('email')}: {e}")
                    self.failed_count += 1
                    continue

        except Exception as e:
            logger.error(f"Campaign failed: {e}")
            raise
        finally:
            duration = datetime.now() - start_time
            logger.info(
                f"Campaign completed. Sent: {self.sent_count}, Failed: {self.failed_count}, "
                f"Duration: {duration.total_seconds():.2f} seconds"
            )

def main():
    # Example configuration - replace with your actual values
    campaign = EmailCampaign(
        smtp_server="smtp.gmail.com",
        smtp_port=587,
        sender_email="your_email@gmail.com",
        sender_password="your_password",
        subject="Exciting Offer from DigiTech Care India!",
        template_path="email_template.html",
        recipients_csv="recipients.csv",
        attachment_path="offer.pdf",
        delay_seconds=2
    )

    try:
        campaign.run_campaign()
    except Exception as e:
        logger.error(f"Fatal error in campaign execution: {e}")

if __name__ == "__main__":
    main()
```
