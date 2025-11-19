"""
Generated Code Metadata:
========================
Original URL: https://airdropbtc.epizy.com
Prompt: Create a Python script to configure email accounts on a hosting platform that supports multiple email accounts and provides free SSL, similar to iFastNet's hosting services.
Generated: DETERMINISTIC_9216bdd2f0a1fc0c
Batch ID: 20250612_151301
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# email_configurator.py

import ssl
import smtplib
from email.utils import formatdate
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

class EmailConfigurator:
    def __init__(self, hosting_platform_api):
        """
        Initialize the EmailConfigurator with a hosting platform API.

        Args:
            hosting_platform_api (object): The API object for the hosting platform.
        """
        self.hosting_platform_api = hosting_platform_api

    def create_email_account(self, email_address, password, mailbox_size):
        """
        Create a new email account on the hosting platform.

        Args:
            email_address (str): The email address to create.
            password (str): The password for the email account.
            mailbox_size (int): The mailbox size in MB.

        Returns:
            bool: True if the email account was created successfully, False otherwise.
        """
        try:
            # Create the email account using the hosting platform API
            response = self.hosting_platform_api.create_email_account(email_address, password, mailbox_size)
            return response['success']
        except Exception as e:
            # Handle any exceptions that occur during email account creation
            print(f"Error creating email account: {e}")
            return False

    def configure_email_account(self, email_address, smtp_server, smtp_port, imap_server, imap_port):
        """
        Configure an existing email account on the hosting platform.

        Args:
            email_address (str): The email address to configure.
            smtp_server (str): The SMTP server hostname.
            smtp_port (int): The SMTP server port.
            imap_server (str): The IMAP server hostname.
            imap_port (int): The IMAP server port.

        Returns:
            bool: True if the email account was configured successfully, False otherwise.
        """
        try:
            # Configure the email account using the hosting platform API
            response = self.hosting_platform_api.configure_email_account(email_address, smtp_server, smtp_port, imap_server, imap_port)
            return response['success']
        except Exception as e:
            # Handle any exceptions that occur during email account configuration
            print(f"Error configuring email account: {e}")
            return False

    def enable_ssl(self, email_address):
        """
        Enable free SSL for an email account on the hosting platform.

        Args:
            email_address (str): The email address to enable SSL for.

        Returns:
            bool: True if SSL was enabled successfully, False otherwise.
        """
        try:
            # Enable SSL using the hosting platform API
            response = self.hosting_platform_api.enable_ssl(email_address)
            return response['success']
        except Exception as e:
            # Handle any exceptions that occur during SSL enablement
            print(f"Error enabling SSL: {e}")
            return False

    def test_email_account(self, email_address, password):
        """
        Test an email account by sending a test email.

        Args:
            email_address (str): The email address to test.
            password (str): The password for the email account.

        Returns:
            bool: True if the email account test was successful, False otherwise.
        """
        try:
            # Create a test email message
            msg = MIMEMultipart()
            msg['From'] = email_address
            msg['To'] = email_address
            msg['Date'] = formatdate(localtime=True)
            msg['Subject'] = 'Test Email'
            msg.attach(MIMEText('This is a test email.', 'plain'))

            # Send the test email using SMTP
            server = smtplib.SMTP('smtp.example.com', 587)
            server.starttls()
            server.login(email_address, password)
            server.sendmail(email_address, email_address, msg.as_string())
            server.quit()
            return True
        except Exception as e:
            # Handle any exceptions that occur during email account testing
            print(f"Error testing email account: {e}")
            return False


class HostingPlatformAPI:
    def create_email_account(self, email_address, password, mailbox_size):
        # Simulate creating an email account
        return {'success': True}

    def configure_email_account(self, email_address, smtp_server, smtp_port, imap_server, imap_port):
        # Simulate configuring an email account
        return {'success': True}

    def enable_ssl(self, email_address):
        # Simulate enabling SSL
        return {'success': True}


if __name__ == '__main__':
    # Create a hosting platform API object
    hosting_platform_api = HostingPlatformAPI()

    # Create an email configurator object
    email_configurator = EmailConfigurator(hosting_platform_api)

    # Create a new email account
    email_address = 'example@example.com'
    password = 'password123'
    mailbox_size = 1000
    if email_configurator.create_email_account(email_address, password, mailbox_size):
        print(f"Email account {email_address} created successfully.")

    # Configure the email account
    smtp_server = 'smtp.example.com'
    smtp_port = 587
    imap_server = 'imap.example.com'
    imap_port = 993
    if email_configurator.configure_email_account(email_address, smtp_server, smtp_port, imap_server, imap_port):
        print(f"Email account {email_address} configured successfully.")

    # Enable SSL for the email account
    if email_configurator.enable_ssl(email_address):
        print(f"SSL enabled for email account {email_address}.")

    # Test the email account
    if email_configurator.test_email_account(email_address, password):
        print(f"Email account {email_address} test successful.")
```
