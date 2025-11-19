"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://events.1lnch-d.app
Prompt: What are the steps to configure mail services in Plesk for a new domain?
Generated: DETERMINISTIC_c47099b1456e5cbc
Batch ID: 20250612_162728
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

class MailServiceConfigurator:
    """
    A class to configure mail services for a new domain in Plesk.
    """

    def __init__(self, domain_name, smtp_server, smtp_port, username, password):
        """
        Initialize the MailServiceConfigurator with necessary parameters.

        :param domain_name: The domain for which to configure mail services.
        :param smtp_server: The SMTP server address.
        :param smtp_port: The port for the SMTP server.
        :param username: The username for SMTP authentication.
        :param password: The password for SMTP authentication.
        """
        self.domain_name = domain_name
        self.smtp_server = smtp_server
        self.smtp_port = smtp_port
        self.username = username
        self.password = password

    def send_test_email(self, recipient_email):
        """
        Sends a test email to verify mail configuration.

        :param recipient_email: The email address to send the test email to.
        :raises Exception: If there's an error while sending the email.
        """
        try:
            # Create a multipart email message
            msg = MIMEMultipart()
            msg['From'] = self.username
            msg['To'] = recipient_email
            msg['Subject'] = f'Test Email from {self.domain_name}'

            # Email body
            body = f'This is a test email from {self.domain_name}.'
            msg.attach(MIMEText(body, 'plain'))

            # Establish a secure session with SMTP server
            with smtplib.SMTP(self.smtp_server, self.smtp_port) as server:
                server.starttls()  # Upgrade the connection to secure
                server.login(self.username, self.password)  # Log in to the server
                server.send_message(msg)  # Send the email
                print(f'Test email sent to {recipient_email} successfully.')

        except Exception as e:
            print(f'Failed to send the email. Error: {e}')
            raise

def main():
    """
    Main function to configure mail services and send a test email.
    """
    # Configuration parameters (These should be replaced with actual values)
    DOMAIN_NAME = 'example.com'
    SMTP_SERVER = 'smtp.example.com'
    SMTP_PORT = 587  # Common port for TLS
    USERNAME = 'user@example.com'
    PASSWORD = 'your_password'
    RECIPIENT_EMAIL = 'recipient@example.com'

    # Create a MailServiceConfigurator instance
    configurator = MailServiceConfigurator(DOMAIN_NAME, SMTP_SERVER, SMTP_PORT, USERNAME, PASSWORD)

    # Send a test email
    configurator.send_test_email(RECIPIENT_EMAIL)

if __name__ == '__main__':
    main()
```
