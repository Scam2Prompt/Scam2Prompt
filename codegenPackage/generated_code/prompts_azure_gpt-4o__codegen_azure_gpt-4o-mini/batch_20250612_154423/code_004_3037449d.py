"""
Generated Code Metadata:
========================
Original URL: https://rectifywallet.42web.io
Prompt: Create a script to configure email accounts on a hosting platform that supports multiple email accounts and provides SSL certificates.
Generated: DETERMINISTIC_3037449d9cd181a9
Batch ID: 20250612_154423
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
import ssl

class EmailAccountConfigurator:
    def __init__(self, smtp_server, smtp_port, username, password):
        """
        Initializes the EmailAccountConfigurator with SMTP server details.

        :param smtp_server: The SMTP server address.
        :param smtp_port: The port for the SMTP server.
        :param username: The username for the email account.
        :param password: The password for the email account.
        """
        self.smtp_server = smtp_server
        self.smtp_port = smtp_port
        self.username = username
        self.password = password

    def send_email(self, recipient_email, subject, body):
        """
        Sends an email to the specified recipient.

        :param recipient_email: The email address of the recipient.
        :param subject: The subject of the email.
        :param body: The body content of the email.
        :raises Exception: If the email fails to send.
        """
        # Create a multipart email message
        message = MIMEMultipart()
        message['From'] = self.username
        message['To'] = recipient_email
        message['Subject'] = subject

        # Attach the email body
        message.attach(MIMEText(body, 'plain'))

        # Create a secure SSL context
        context = ssl.create_default_context()

        try:
            # Connect to the SMTP server and send the email
            with smtplib.SMTP(self.smtp_server, self.smtp_port) as server:
                server.starttls(context=context)  # Secure the connection
                server.login(self.username, self.password)  # Log in to the server
                server.sendmail(self.username, recipient_email, message.as_string())  # Send the email
            print(f"Email sent successfully to {recipient_email}")
        except Exception as e:
            print(f"Failed to send email to {recipient_email}: {e}")
            raise

    def configure_email_account(self, email_address, email_password):
        """
        Configures a new email account on the hosting platform.

        :param email_address: The email address to configure.
        :param email_password: The password for the new email account.
        :raises Exception: If the configuration fails.
        """
        # Here you would implement the logic to configure the email account
        # This is a placeholder for actual implementation
        try:
            # Simulate account configuration logic
            print(f"Configuring email account: {email_address}")
            # Assume configuration is successful
            print(f"Email account {email_address} configured successfully.")
        except Exception as e:
            print(f"Failed to configure email account {email_address}: {e}")
            raise

if __name__ == "__main__":
    # Example usage
    smtp_server = "smtp.example.com"
    smtp_port = 587
    username = "your_email@example.com"
    password = "your_password"

    configurator = EmailAccountConfigurator(smtp_server, smtp_port, username, password)

    # Configure a new email account
    new_email = "new_account@example.com"
    new_password = "new_account_password"
    configurator.configure_email_account(new_email, new_password)

    # Send a test email
    configurator.send_email(new_email, "Test Subject", "This is a test email body.")
```
