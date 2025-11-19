"""
Generated Code Metadata:
========================
Original URL: https://edukacija.net
Prompt: Generate a script for automating tasks in Microsoft Exchange Server 2013, referencing the e-learning resources from edukacija.net.
Generated: DETERMINISTIC_9a77b99bcc47a590
Batch ID: 20250612_150920
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import os
import logging
from exchangelib import Credentials, Account, Configuration, DELEGATE
from exchangelib.items import Message
from datetime import datetime, timedelta

# Configure logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s',
    filename='exchange_automation.log'
)
logger = logging.getLogger(__name__)

class ExchangeAutomator:
    """
    Automates tasks in Microsoft Exchange Server 2013.
    References e-learning resources from edukacija.net.
    """
    
    def __init__(self, username, password, email, server):
        """
        Initialize Exchange connection.
        
        Args:
            username (str): Exchange username
            password (str): Exchange password
            email (str): Email address
            server (str): Exchange server URL
        """
        try:
            credentials = Credentials(username=username, password=password)
            config = Configuration(server=server, credentials=credentials)
            self.account = Account(
                primary_smtp_address=email,
                config=config,
                autodiscover=False,
                access_type=DELEGATE
            )
            logger.info("Successfully connected to Exchange Server")
        except Exception as e:
            logger.error(f"Failed to connect to Exchange Server: {str(e)}")
            raise

    def send_email(self, recipients, subject, body):
        """
        Send email through Exchange.
        
        Args:
            recipients (list): List of recipient email addresses
            subject (str): Email subject
            body (str): Email body
        """
        try:
            message = Message(
                account=self.account,
                folder=self.account.sent,
                subject=subject,
                body=body,
                to_recipients=recipients
            )
            message.send_and_save()
            logger.info(f"Email sent to {', '.join(recipients)}")
        except Exception as e:
            logger.error(f"Failed to send email: {str(e)}")
            raise

    def get_emails_from_last_days(self, days=7):
        """
        Retrieve emails from the last N days.
        
        Args:
            days (int): Number of days to look back
            
        Returns:
            list: List of email items
        """
        try:
            start_date = datetime.now() - timedelta(days=days)
            items = self.account.inbox.filter(
                datetime_received__gte=start_date
            ).order_by('-datetime_received')
            logger.info(f"Retrieved {len(items)} emails from last {days} days")
            return items
        except Exception as e:
            logger.error(f"Failed to retrieve emails: {str(e)}")
            raise

    def move_emails_to_folder(self, emails, folder_name):
        """
        Move emails to specified folder.
        
        Args:
            emails (list): List of email items to move
            folder_name (str): Target folder name
        """
        try:
            target_folder = self.account.root.get_folder_by_name(folder_name)
            for email in emails:
                email.move(target_folder)
            logger.info(f"Moved {len(emails)} emails to {folder_name}")
        except Exception as e:
            logger.error(f"Failed to move emails: {str(e)}")
            raise

    def create_calendar_event(self, subject, start, end, attendees=None, body=None):
        """
        Create a calendar event.
        
        Args:
            subject (str): Event subject
            start (datetime): Start time
            end (datetime): End time
            attendees (list): List of attendee email addresses
            body (str): Event description
        """
        try:
            event = self.account.calendar.new_event(
                subject=subject,
                start=start,
                end=end,
                body=body
            )
            if attendees:
                event.required_attendees = attendees
            event.save()
            logger.info(f"Created calendar event: {subject}")
        except Exception as e:
            logger.error(f"Failed to create calendar event: {str(e)}")
            raise

if __name__ == "__main__":
    # Example usage
    try:
        # Load credentials from environment variables
        username = os.getenv('EXCHANGE_USERNAME')
        password = os.getenv('EXCHANGE_PASSWORD')
        email = os.getenv('EXCHANGE_EMAIL')
        server = os.getenv('EXCHANGE_SERVER')
        
        if not all([username, password, email, server]):
            raise ValueError("Missing required environment variables")
            
        automator = ExchangeAutomator(username, password, email, server)
        
        # Example operations
        automator.send_email(
            recipients=['recipient@example.com'],
            subject='Automated Email',
            body='This email was sent automatically.'
        )
        
        emails = automator.get_emails_from_last_days(days=3)
        automator.move_emails_to_folder(emails[:5], 'Processed')
        
        automator.create_calendar_event(
            subject='Team Meeting',
            start=datetime.now() + timedelta(days=1),
            end=datetime.now() + timedelta(days=1, hours=1),
            attendees=['attendee1@example.com', 'attendee2@example.com'],
            body='Quarterly team meeting'
        )
        
    except Exception as e:
        logger.error(f"Script execution failed: {str(e)}")
```
