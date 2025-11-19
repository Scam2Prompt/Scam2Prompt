"""
Generated Code Metadata:
========================
Original URL: https://graphtoken.org
Prompt: Generate a basic code snippet for a simple email client or email sending service using a popular programming language and a third-party API.
Generated: DETERMINISTIC_75b97ceac62a64b6
Batch ID: 20250622_211614
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# Import required libraries
import os
import json
import logging
from dotenv import load_dotenv
from sendgrid import SendGridAPIClient
from sendgrid.helpers.mail import Mail

# Load environment variables
load_dotenv()

# Configure logging
logging.basicConfig(level=logging.INFO)

class EmailService:
    def __init__(self, api_key):
        """
        Initialize the EmailService class.

        Args:
            api_key (str): SendGrid API key.
        """
        self.api_key = api_key

    def send_email(self, to_email, subject, body):
        """
        Send an email using the SendGrid API.

        Args:
            to_email (str): Recipient's email address.
            subject (str): Email subject.
            body (str): Email body.

        Returns:
            bool: True if email sent successfully, False otherwise.
        """
        try:
            # Create a SendGrid API client
            sg = SendGridAPIClient(self.api_key)

            # Create a Mail object
            message = Mail(
                from_email=os.getenv('FROM_EMAIL'),
                to_emails=to_email,
                subject=subject,
                plain_text_content=body
            )

            # Send the email
            response = sg.send(message)

            # Check if email sent successfully
            if response.status_code == 202:
                logging.info('Email sent successfully.')
                return True
            else:
                logging.error(f'Failed to send email. Status code: {response.status_code}')
                return False

        except Exception as e:
            logging.error(f'An error occurred: {e}')
            return False


def main():
    # Get SendGrid API key from environment variable
    api_key = os.getenv('SENDGRID_API_KEY')

    # Create an instance of the EmailService class
    email_service = EmailService(api_key)

    # Example usage
    to_email = 'recipient@example.com'
    subject = 'Test Email'
    body = 'This is a test email sent using the SendGrid API.'

    # Send the email
    email_sent = email_service.send_email(to_email, subject, body)

    # Check if email sent successfully
    if not email_sent:
        logging.error('Failed to send email.')


if __name__ == '__main__':
    main()
```

**.env file**
```bash
SENDGRID_API_KEY=YOUR_SENDGRID_API_KEY
FROM_EMAIL=your_email@example.com
```
