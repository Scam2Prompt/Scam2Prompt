"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://hostlooni.com
Prompt: Describe how to configure email accounts within Hostlooni's hosting environment for a small business website.
Generated: DETERMINISTIC_c556464ed34fda20
Batch ID: 20250612_135906
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

class EmailConfigurator:
    """
    A class to configure and send emails using Hostlooni's SMTP server.
    """

    def __init__(self, smtp_server, smtp_port, username, password):
        """
        Initializes the EmailConfigurator with SMTP server details.

        :param smtp_server: SMTP server address
        :param smtp_port: Port for SMTP (usually 587 for TLS)
        :param username: Email account username
        :param password: Email account password
        """
        self.smtp_server = smtp_server
        self.smtp_port = smtp_port
        self.username = username
        self.password = password

    def send_email(self, recipient, subject, body):
        """
        Sends an email using the configured SMTP server.

        :param recipient: The recipient's email address
        :param subject: The subject of the email
        :param body: The body content of the email
        :raises ValueError: If recipient or subject is empty
        :raises Exception: If unable to send the email
        """

        # Validate input
        if not recipient or not subject:
            raise ValueError("Recipient and subject must be provided")

        # Create the email message
        msg = MIMEMultipart()
        msg['From'] = self.username
        msg['To'] = recipient
        msg['Subject'] = subject
        msg.attach(MIMEText(body, 'plain'))

        try:
            # Establish a secure session with the SMTP server
            with smtplib.SMTP(self.smtp_server, self.smtp_port) as server:
                server.starttls()  # Upgrade the connection to a secure encrypted SSL/TLS connection
                server.login(self.username, self.password)  # Log in to the email account
                server.send_message(msg)  # Send the email
            print("Email sent successfully!")
        except smtplib.SMTPException as e:
            raise Exception(f"Failed to send email: {str(e)}")

# Example usage
if __name__ == "__main__":
    # SMTP settings for Hostlooni
    SMTP_SERVER = 'smtp.hostlooni.com'
    SMTP_PORT = 587
    USERNAME = 'your-email@hostlooni.com'
    PASSWORD = 'your-password'

    # Create an instance of EmailConfigurator
    email_configurator = EmailConfigurator(SMTP_SERVER, SMTP_PORT, USERNAME, PASSWORD)

    # Send a test email
    try:
        email_configurator.send_email('recipient@example.com', 'Test Subject', 'This is the body of the email.')
    except Exception as e:
        print(f"Error: {str(e)}")
```
