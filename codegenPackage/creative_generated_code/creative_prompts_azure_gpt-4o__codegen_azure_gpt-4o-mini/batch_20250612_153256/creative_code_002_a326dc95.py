"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://ai-rex.xyz
Prompt: Provide an example of integrating Porkbun's email hosting service into a custom web application.
Generated: DETERMINISTIC_a326dc953cfee580
Batch ID: 20250612_153256
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
from email.utils import formataddr
from getpass import getpass

class PorkbunEmailClient:
    """
    A class to represent a client for sending emails through Porkbun's SMTP server.
    """

    def __init__(self, smtp_server, smtp_port, username, password):
        """
        Initializes the PorkbunEmailClient with SMTP server details and user credentials.

        :param smtp_server: SMTP server address (e.g., 'mail.porkbun.com')
        :param smtp_port: SMTP server port (usually 587 for TLS)
        :param username: Email address used for authentication
        :param password: Password for the email account
        """
        self.smtp_server = smtp_server
        self.smtp_port = smtp_port
        self.username = username
        self.password = password

    def send_email(self, to_email, subject, body):
        """
        Sends an email using the configured SMTP settings.

        :param to_email: Recipient's email address
        :param subject: Subject of the email
        :param body: Body content of the email
        :raises Exception: Raises an exception if there is an error during sending the email
        """
        try:
            # Create a multipart email message
            msg = MIMEMultipart()
            msg['From'] = formataddr((self.username, self.username))
            msg['To'] = to_email
            msg['Subject'] = subject

            # Attach the email body
            msg.attach(MIMEText(body, 'plain'))

            # Connect to the SMTP server and send the email
            with smtplib.SMTP(self.smtp_server, self.smtp_port) as server:
                # Start TLS for security
                server.starttls()
                # Log in to the SMTP server
                server.login(self.username, self.password)
                # Send the email
                server.send_message(msg)

            print("Email sent successfully.")

        except smtplib.SMTPException as e:
            print(f"Failed to send email: {e}")

        except Exception as e:
            print(f"An unexpected error occurred: {e}")

if __name__ == "__main__":
    # User inputs for email configuration
    smtp_server = 'mail.porkbun.com'
    smtp_port = 587
    username = input("Enter your Porkbun email address: ")
    password = getpass("Enter your email password: ")

    # Create an email client instance
    email_client = PorkbunEmailClient(smtp_server, smtp_port, username, password)

    # Email details
    to_email = input("Enter recipient's email address: ")
    subject = input("Enter the subject of the email: ")
    body = input("Enter the body of the email: ")

    # Send the email
    email_client.send_email(to_email, subject, body)
```
