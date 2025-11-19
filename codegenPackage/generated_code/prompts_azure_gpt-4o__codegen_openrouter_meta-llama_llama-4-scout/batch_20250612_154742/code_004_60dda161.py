"""
Generated Code Metadata:
========================
Original URL: https://datmaui.liveblog365.com
Prompt: Write a Python script to send automated emails using a hosting service that supports multiple email accounts, as described on iFastNet's hosting platform.
Generated: DETERMINISTIC_60dda1616b58cf08
Batch ID: 20250612_154742
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# Import required libraries
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
import ssl
import logging

# Set up logging configuration
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

class EmailService:
    def __init__(self, host, port, username, password):
        """
        Initialize the EmailService class.

        Args:
        - host (str): The hostname or IP address of the SMTP server.
        - port (int): The port number of the SMTP server.
        - username (str): The username of the email account.
        - password (str): The password of the email account.
        """
        self.host = host
        self.port = port
        self.username = username
        self.password = password

    def send_email(self, recipient, subject, body):
        """
        Send an email to a recipient.

        Args:
        - recipient (str): The email address of the recipient.
        - subject (str): The subject of the email.
        - body (str): The body of the email.

        Returns:
        - bool: True if the email is sent successfully, False otherwise.
        """
        try:
            # Create a secure SSL context
            context = ssl.create_default_context()

            # Set up the SMTP server
            with smtplib.SMTP_SSL(self.host, self.port, context=context) as server:
                # Log in to the email account
                server.login(self.username, self.password)

                # Create a multipart message
                message = MIMEMultipart()
                message['From'] = self.username
                message['To'] = recipient
                message['Subject'] = subject

                # Attach the email body
                message.attach(MIMEText(body, 'plain'))

                # Send the email
                server.sendmail(self.username, recipient, message.as_string())

                logging.info(f'Email sent to {recipient} successfully.')
                return True

        except smtplib.SMTPAuthenticationError:
            logging.error('Authentication error: Invalid username or password.')
        except smtplib.SMTPException as e:
            logging.error(f'SMTP error: {e}')
        except Exception as e:
            logging.error(f'An error occurred: {e}')

        return False


def main():
    # iFastNet's hosting platform SMTP settings
    host = 'smtp.yourhostingservice.com'
    port = 465
    username = 'your_email_username'
    password = 'your_email_password'

    # Create an instance of the EmailService class
    email_service = EmailService(host, port, username, password)

    # Email settings
    recipient = 'recipient@example.com'
    subject = 'Test Email from Python Script'
    body = 'This is a test email sent from a Python script.'

    # Send the email
    email_sent = email_service.send_email(recipient, subject, body)

    if not email_sent:
        logging.error('Failed to send email.')


if __name__ == '__main__':
    main()
```
