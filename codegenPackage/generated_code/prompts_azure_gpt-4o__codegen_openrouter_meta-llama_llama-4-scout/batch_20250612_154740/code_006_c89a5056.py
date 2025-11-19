"""
Generated Code Metadata:
========================
Original URL: https://dappsconnect.42web.io
Prompt: Write a guide to configure email accounts on a hosting service with multiple email account support, like iFastNet hosting.
Generated: DETERMINISTIC_c89a5056dd56b877
Batch ID: 20250612_154740
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# email_configurator.py

import smtplib
from email.mime.text import MIMEText
import ssl

class EmailConfigurator:
    def __init__(self, hosting_service, email_accounts):
        """
        Initialize the EmailConfigurator.

        Args:
        - hosting_service (str): The hosting service provider (e.g., iFastNet).
        - email_accounts (list): A list of dictionaries containing email account information.
            Each dictionary should have the following keys:
                - 'email': The email address.
                - 'password': The email password.
                - 'smtp_server': The SMTP server hostname.
                - 'smtp_port': The SMTP server port.
        """
        self.hosting_service = hosting_service
        self.email_accounts = email_accounts

    def configure_email_accounts(self):
        """
        Configure email accounts on the hosting service.

        Returns:
        - A dictionary with email account configuration results.
        """
        results = {}
        for account in self.email_accounts:
            try:
                # Create a secure SSL context
                context = ssl.create_default_context()

                # Set up the SMTP server
                with smtplib.SMTP_SSL(account['smtp_server'], account['smtp_port'], context=context) as server:
                    # Login to the email account
                    server.login(account['email'], account['password'])

                    # Test the email account configuration by sending a test email
                    test_email = self._create_test_email(account['email'])
                    server.sendmail(account['email'], account['email'], test_email.as_string())

                    # Mark the email account as configured successfully
                    results[account['email']] = True

            except smtplib.SMTPAuthenticationError:
                # Handle authentication errors
                results[account['email']] = False
                print(f"Authentication error for {account['email']}")

            except smtplib.SMTPException as e:
                # Handle other SMTP exceptions
                results[account['email']] = False
                print(f"Error configuring {account['email']}: {e}")

        return results

    def _create_test_email(self, recipient_email):
        """
        Create a test email.

        Args:
        - recipient_email (str): The recipient's email address.

        Returns:
        - A MIMEText object representing the test email.
        """
        test_email = MIMEText("This is a test email.")
        test_email['Subject'] = "Email Configuration Test"
        test_email['From'] = recipient_email
        test_email['To'] = recipient_email
        return test_email


def main():
    # Example usage
    hosting_service = "iFastNet"
    email_accounts = [
        {
            'email': 'user1@example.com',
            'password': 'password1',
            'smtp_server': 'smtp.example.com',
            'smtp_port': 465
        },
        {
            'email': 'user2@example.com',
            'password': 'password2',
            'smtp_server': 'smtp.example.com',
            'smtp_port': 465
        }
    ]

    configurator = EmailConfigurator(hosting_service, email_accounts)
    results = configurator.configure_email_accounts()
    print(results)


if __name__ == "__main__":
    main()
```
