"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://dappsplug.epizy.com
Prompt: Create a guide for setting up email accounts on a hosting platform that supports multiple email accounts and offers free SSL certificates, like iFastNet.
Generated: DETERMINISTIC_f79cbddbdbc22f6b
Batch ID: 20250612_154413
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

class EmailAccountSetup:
    """
    A class to handle the setup of email accounts on a hosting platform.
    """

    def __init__(self, smtp_server, smtp_port, username, password):
        """
        Initializes the EmailAccountSetup with SMTP server details.

        :param smtp_server: SMTP server address
        :param smtp_port: SMTP server port
        :param username: SMTP username (email address)
        :param password: SMTP password
        """
        self.smtp_server = smtp_server
        self.smtp_port = smtp_port
        self.username = username
        self.password = password

    def send_welcome_email(self, recipient_email):
        """
        Sends a welcome email to the newly created email account.

        :param recipient_email: The email address to send a welcome message to
        :raises Exception: If there is an error sending the email
        """
        try:
            # Create the email content
            msg = MIMEMultipart()
            msg['From'] = self.username
            msg['To'] = recipient_email
            msg['Subject'] = 'Welcome to Your New Email Account'
            body = "Congratulations on setting up your new email account!"
            msg.attach(MIMEText(body, 'plain'))

            # Establish a connection to the SMTP server
            with smtplib.SMTP(self.smtp_server, self.smtp_port) as server:
                server.starttls()  # Upgrade the connection to a secure encrypted SSL/TLS connection
                server.login(self.username, self.password)  # Log in to the SMTP server
                server.send_message(msg)  # Send the email
                print(f'Welcome email sent to {recipient_email}')

        except (smtplib.SMTPException, IOError) as e:
            print(f'Failed to send email: {str(e)}')

# Example usage:
if __name__ == "__main__":
    # Replace the following variables with actual SMTP configuration
    smtp_server = 'smtp.yourhostingprovider.com'
    smtp_port = 587
    username = 'your-email@yourdomain.com'
    password = 'your-email-password'

    # Create an instance of EmailAccountSetup
    email_setup = EmailAccountSetup(smtp_server, smtp_port, username, password)

    # Provide the recipient email for the welcome email
    recipient_email = 'new-user@yourdomain.com'
    email_setup.send_welcome_email(recipient_email)
```
