"""
Generated Code Metadata:
========================
Original URL: https://solutechsystem.com.ng
Prompt: Write Python code to automate email marketing campaigns for a business website, incorporating the targeted communication strategies outlined by Solutech System's email marketing services.
Generated: DETERMINISTIC_f651ee2e8a997ad8
Batch ID: 20250612_154601
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import smtplib
import ssl
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.base import MIMEBase
from email import encoders
import csv
import os
from datetime import datetime
import logging
from typing import List, Dict, Optional

# Configure logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s',
    handlers=[
        logging.FileHandler('email_campaign.log'),
        logging.StreamHandler()
    ]
)

class EmailCampaign:
    """
    A class to automate email marketing campaigns with targeted communication strategies.
    """
    
    def __init__(self, smtp_server: str, smtp_port: int, sender_email: str, password: str):
        """
        Initialize the EmailCampaign with SMTP server details.
        
        Args:
            smtp_server (str): SMTP server address
            smtp_port (int): SMTP server port
            sender_email (str): Email address of the sender
            password (str): Password for the sender email
        """
        self.smtp_server = smtp_server
        self.smtp_port = smtp_port
        self.sender_email = sender_email
        self.password = password
        self.context = ssl.create_default_context()
        
    def _connect_to_smtp(self) -> smtplib.SMTP:
        """
        Establish a secure connection to the SMTP server.
        
        Returns:
            smtplib.SMTP: SMTP connection object
            
        Raises:
            Exception: If connection fails
        """
        try:
            server = smtplib.SMTP(self.smtp_server, self.smtp_port)
            server.starttls(context=self.context)
            server.login(self.sender_email, self.password)
            return server
        except Exception as e:
            logging.error(f"Failed to connect to SMTP server: {e}")
            raise

    def _create_email(
        self,
        recipient: str,
        subject: str,
        body: str,
        html_body: Optional[str] = None,
        attachments: Optional[List[str]] = None
    ) -> MIMEMultipart:
        """
        Create an email message with optional HTML content and attachments.
        
        Args:
            recipient (str): Recipient email address
            subject (str): Email subject
            body (str): Plain text email body
            html_body (str, optional): HTML version of email body
            attachments (List[str], optional): List of file paths to attach
            
        Returns:
            MIMEMultipart: Constructed email message
        """
        message = MIMEMultipart('alternative')
        message['From'] = self.sender_email
        message['To'] = recipient
        message['Subject'] = subject
        
        # Add plain text body
        message.attach(MIMEText(body, 'plain'))
        
        # Add HTML body if provided
        if html_body:
            message.attach(MIMEText(html_body, 'html'))
        
        # Add attachments if provided
        if attachments:
            for file_path in attachments:
                try:
                    with open(file_path, 'rb') as attachment:
                        part = MIMEBase('application', 'octet-stream')
                        part.set_payload(attachment.read())
                    encoders.encode_base64(part)
                    part.add_header(
                        'Content-Disposition',
                        f'attachment; filename="{os.path.basename(file_path)}"'
                    )
                    message.attach(part)
                except Exception as e:
                    logging.warning(f"Failed to attach {file_path}: {e}")
        
        return message

    def send_email(
        self,
        recipient: str,
        subject: str,
        body: str,
        html_body: Optional[str] = None,
        attachments: Optional[List[str]] = None
    ) -> bool:
        """
        Send an email to a single recipient.
        
        Args:
            recipient (str): Recipient email address
            subject (str): Email subject
            body (str): Plain text email body
            html_body (str, optional): HTML version of email body
            attachments (List[str], optional): List of file paths to attach
            
        Returns:
            bool: True if email was sent successfully, False otherwise
        """
        try:
            server = self._connect_to_smtp()
            message = self._create_email(recipient, subject, body, html_body, attachments)
            server.sendmail(self.sender_email, recipient, message.as_string())
            server.quit()
            logging.info(f"Email sent successfully to {recipient}")
            return True
        except Exception as e:
            logging.error(f"Failed to send email to {recipient}: {e}")
            return False

    def send_bulk_emails(
        self,
        recipients: List[Dict[str, str]],
        subject_template: str,
        body_template: str,
        html_body_template: Optional[str] = None,
        attachments: Optional[List[str]] = None,
        batch_size: int = 50,
        delay: int = 10
    ) -> Dict[str, int]:
        """
        Send personalized emails to multiple recipients in batches.
        
        Args:
            recipients (List[Dict[str, str]]): List of recipient dictionaries with email and personalization fields
            subject_template (str): Email subject template with placeholders
            body_template (str): Plain text body template with placeholders
            html_body_template (str, optional): HTML body template with placeholders
            attachments (List[str], optional): List of file paths to attach
            batch_size (int, optional): Number of emails to send in each batch
            delay (int, optional): Delay in seconds between batches
            
        Returns:
            Dict[str, int]: Statistics of the campaign (success_count, failure_count)
        """
        stats = {'success': 0, 'failure': 0}
        
        try:
            server = self._connect_to_smtp()
            
            for i, recipient_data in enumerate(recipients):
                try:
                    # Personalize email content
                    email = recipient_data['email']
                    subject = subject_template.format(**recipient_data)
                    body = body_template.format(**recipient_data)
                    html_body = html_body_template.format(**recipient_data) if html_body_template else None
                    
                    message = self._create_email(email, subject, body, html_body, attachments)
                    server.sendmail(self.sender_email, email, message.as_string())
                    stats['success'] += 1
                    logging.info(f"Sent email to {email} ({i+1}/{len(recipients)})")
                    
                    # Implement batch processing
                    if (i + 1) % batch_size == 0:
                        logging.info(f"Sent {i+1} emails. Pausing for {delay} seconds...")
                        time.sleep(delay)
                        
                except Exception as e:
                    stats['failure'] += 1
                    logging.error(f"Failed to send email to {recipient_data.get('email', 'unknown')}: {e}")
                    
            server.quit()
            logging.info(f"Campaign completed. Success: {stats['success']}, Failure: {stats['failure']}")
            
        except Exception as e:
            logging.error(f"Bulk email campaign failed: {e}")
            stats['failure'] = len(recipients) - stats['success']
            
        return stats

    def load_recipients_from_csv(self, file_path: str) -> List[Dict[str, str]]:
        """
        Load recipient data from a CSV file.
        
        Args:
            file_path (str): Path to the CSV file
            
        Returns:
            List[Dict[str, str]]: List of recipient dictionaries
            
        Raises:
            FileNotFoundError: If the CSV file doesn't exist
            Exception: For other CSV parsing errors
        """
        recipients = []
        try:
            with open(file_path, mode='r', encoding='utf-8') as file:
                reader = csv.DictReader(file)
                for row in reader:
                    recipients.append(dict(row))
            logging.info(f"Loaded {len(recipients)} recipients from {file_path}")
            return recipients
        except FileNotFoundError:
            logging.error(f"CSV file not found: {file_path}")
            raise
        except Exception as e:
            logging.error(f"Error reading CSV file: {e}")
            raise

    def save_campaign_report(self, stats: Dict[str, int], output_dir: str = 'reports') -> str:
        """
        Save campaign statistics to a report file.
        
        Args:
            stats (Dict[str, int]): Campaign statistics
            output_dir (str, optional): Directory to save the report
            
        Returns:
            str: Path to the saved report file
        """
        os.makedirs(output_dir, exist_ok=True)
        timestamp = datetime.now().strftime('%Y%m%d_%H%M%S')
        report_path = os.path.join(output_dir, f'campaign_report_{timestamp}.txt')
        
        with open(report_path, 'w') as file:
            file.write(f"Email Campaign Report - {timestamp}\n")
            file.write("=" * 40 + "\n")
            file.write(f"Successful emails: {stats['success']}\
