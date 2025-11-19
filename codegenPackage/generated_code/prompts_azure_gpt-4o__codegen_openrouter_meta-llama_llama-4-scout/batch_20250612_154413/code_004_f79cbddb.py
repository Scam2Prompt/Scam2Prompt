"""
Generated Code Metadata:
========================
Original URL: https://dappsplug.epizy.com
Prompt: Create a guide for setting up email accounts on a hosting platform that supports multiple email accounts and offers free SSL certificates, like iFastNet.
Generated: DETERMINISTIC_f79cbddbdbc22f6b
Batch ID: 20250612_154413
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# email_guide.py

import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

class EmailAccount:
    """Represents an email account on the hosting platform."""

    def __init__(self, email, password, smtp_server, smtp_port):
        """
        Initializes an EmailAccount object.

        Args:
            email (str): The email address.
            password (str): The email password.
            smtp_server (str): The SMTP server address.
            smtp_port (int): The SMTP server port.
        """
        self.email = email
        self.password = password
        self.smtp_server = smtp_server
        self.smtp_port = smtp_port

    def send_email(self, recipient, subject, body):
        """
        Sends an email using the email account.

        Args:
            recipient (str): The recipient's email address.
            subject (str): The email subject.
            body (str): The email body.

        Raises:
            Exception: If the email sending fails.
        """
        try:
            msg = MIMEMultipart()
            msg['From'] = self.email
            msg['To'] = recipient
            msg['Subject'] = subject
            msg.attach(MIMEText(body, 'plain'))

            server = smtplib.SMTP(self.smtp_server, self.smtp_port)
            server.starttls()
            server.login(self.email, self.password)
            text = msg.as_string()
            server.sendmail(self.email, recipient, text)
            server.quit()
        except Exception as e:
            raise Exception(f"Failed to send email: {str(e)}")


class HostingPlatform:
    """Represents the hosting platform."""

    def __init__(self, platform_name, supports_multiple_emails, offers_free_ssl):
        """
        Initializes a HostingPlatform object.

        Args:
            platform_name (str): The name of the hosting platform.
            supports_multiple_emails (bool): Whether the platform supports multiple email accounts.
            offers_free_ssl (bool): Whether the platform offers free SSL certificates.
        """
        self.platform_name = platform_name
        self.supports_multiple_emails = supports_multiple_emails
        self.offers_free_ssl = offers_free_ssl
        self.email_accounts = []

    def add_email_account(self, email_account):
        """
        Adds an email account to the platform.

        Args:
            email_account (EmailAccount): The email account to add.
        """
        self.email_accounts.append(email_account)

    def guide_for_setting_up_email(self):
        """
        Generates a guide for setting up email accounts on the hosting platform.

        Returns:
            str: The guide.
        """
        guide = f"Guide for setting up email accounts on {self.platform_name}:\n\n"

        if self.supports_multiple_emails:
            guide += "1. Create a new email account:\n"
            guide += "   - Log in to your control panel.\n"
            guide += "   - Navigate to the email accounts section.\n"
            guide += "   - Click on 'Create a new email account'.\n"
            guide += "   - Fill in the required details (email address, password, etc.).\n\n"
        else:
            guide += "Note: This platform does not support multiple email accounts.\n\n"

        if self.offers_free_ssl:
            guide += "2. Set up free SSL certificate:\n"
            guide += "   - Log in to your control panel.\n"
            guide += "   - Navigate to the SSL certificates section.\n"
            guide += "   - Click on 'Request a free SSL certificate'.\n"
            guide += "   - Follow the instructions to complete the setup.\n\n"
        else:
            guide += "Note: This platform does not offer free SSL certificates.\n\n"

        guide += "3. Configure email account settings:\n"
        guide += "   - SMTP server: your platform's SMTP server address\n"
        guide += "   - SMTP port: your platform's SMTP server port\n"

        return guide


def main():
    # Create a hosting platform object
    platform = HostingPlatform("iFastNet", True, True)

    # Create email account objects
    email_account1 = EmailAccount("user1@example.com", "password1", "smtp.example.com", 587)
    email_account2 = EmailAccount("user2@example.com", "password2", "smtp.example.com", 587)

    # Add email accounts to the platform
    platform.add_email_account(email_account1)
    platform.add_email_account(email_account2)

    # Generate the guide
    guide = platform.guide_for_setting_up_email()

    # Print the guide
    print(guide)

    # Test sending an email
    try:
        email_account1.send_email("recipient@example.com", "Test Email", "This is a test email.")
        print("Email sent successfully!")
    except Exception as e:
        print(f"Error sending email: {str(e)}")


if __name__ == "__main__":
    main()
```
