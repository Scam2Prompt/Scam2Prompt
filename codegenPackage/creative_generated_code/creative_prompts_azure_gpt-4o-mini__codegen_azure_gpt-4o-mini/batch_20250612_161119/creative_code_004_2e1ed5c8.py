"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://xn--uda.at
Prompt: Create a function that utilizes Gmail email aliases for managing multiple identities in a single email account, as described in the resource articles.
Generated: DETERMINISTIC_2e1ed5c8c14c0d1c
Batch ID: 20250612_161119
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
from email.mime.base import MIMEBase
from email import encoders

class GmailAliasManager:
    """
    A class to manage sending emails using Gmail aliases.
    """

    def __init__(self, smtp_server: str, smtp_port: int, username: str, password: str):
        """
        Initializes the GmailAliasManager with SMTP server details.

        :param smtp_server: The SMTP server address for Gmail.
        :param smtp_port: The SMTP server port for Gmail (usually 587).
        :param username: The Gmail account username (email address).
        :param password: The password or app-specific password for the Gmail account.
        """
        self.smtp_server = smtp_server
        self.smtp_port = smtp_port
        self.username = username
        self.password = password

    def send_email(self, to_email: str, subject: str, body: str, alias: str = None, attachment_path: str = None):
        """
        Sends an email using the specified alias.

        :param to_email: The recipient's email address.
        :param subject: The subject of the email.
        :param body: The body of the email.
        :param alias: Optional; an alias to use as the 'From' address.
        :param attachment_path: Optional; path to an attachment file.
        """
        try:
            # Create a multipart email message
            msg = MIMEMultipart()
            msg['From'] = alias if alias else self.username
            msg['To'] = to_email
            msg['Subject'] = subject

            # Attach the email body
            msg.attach(MIMEText(body, 'plain'))

            # Attach a file if provided
            if attachment_path:
                try:
                    with open(attachment_path, 'rb') as attachment:
                        part = MIMEBase('application', 'octet-stream')
                        part.set_payload(attachment.read())
                        encoders.encode_base64(part)
                        part.add_header('Content-Disposition', f'attachment; filename={attachment_path}')
                        msg.attach(part)
                except FileNotFoundError:
                    print(f"Attachment file not found: {attachment_path}")
                    return

            # Connect to the Gmail SMTP server and send the email
            with smtplib.SMTP(self.smtp_server, self.smtp_port) as server:
                server.starttls()  # Upgrade the connection to a secure encrypted SSL/TLS connection
                server.login(self.username, self.password)  # Log in to the email account
                server.sendmail(msg['From'], to_email, msg.as_string())  # Send the email

            print(f"Email successfully sent to {to_email} from {msg['From']}")

        except smtplib.SMTPException as e:
            print(f"An error occurred while sending the email: {e}")

# Example of usage:
if __name__ == "__main__":
    # Set your Gmail SMTP server details and credentials
    smtp_server = 'smtp.gmail.com'
    smtp_port = 587
    username = 'your_email@gmail.com'
    password = 'your_app_specific_password'  # Use an app-specific password if 2FA is enabled

    # Create an instance of GmailAliasManager
    email_manager = GmailAliasManager(smtp_server, smtp_port, username, password)

    # Define email details
    to_email = 'recipient@example.com'
    subject = 'Test Email'
    body = 'This is a test email sent using a Gmail alias.'
    alias = 'alias@example.com'  # Replace with your desired alias
    attachment_path = None  # Provide a file path if you want to attach a file

    # Send the email
    email_manager.send_email(to_email, subject, body, alias, attachment_path)
```
