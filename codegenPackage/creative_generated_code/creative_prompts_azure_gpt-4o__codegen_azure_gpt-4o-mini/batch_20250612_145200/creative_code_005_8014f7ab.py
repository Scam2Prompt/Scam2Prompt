"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://wombat-exchange.rf.gd
Prompt: Create a guide for setting up email accounts on iFastNet hosting and integrating them with a web application.
Generated: DETERMINISTIC_8014f7ab75d1078d
Batch ID: 20250612_145200
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

class EmailSetup:
    """
    A class to handle setting up and sending emails through iFastNet hosting.
    """

    def __init__(self, smtp_server, port, username, password):
        """
        Initializes the EmailSetup with SMTP server details and user credentials.

        :param smtp_server: SMTP server address
        :param port: SMTP server port
        :param username: Email account username
        :param password: Email account password
        """
        self.smtp_server = smtp_server
        self.port = port
        self.username = username
        self.password = password

    def send_email(self, recipient_email, subject, body):
        """
        Sends an email to the specified recipient.

        :param recipient_email: The recipient's email address
        :param subject: The subject of the email
        :param body: The body text of the email
        :raises Exception: If there is an error sending the email
        """
        try:
            # Create the email content
            msg = MIMEMultipart()
            msg['From'] = self.username
            msg['To'] = recipient_email
            msg['Subject'] = subject
            msg.attach(MIMEText(body, 'plain'))

            # Establish a secured connection with the server
            with smtplib.SMTP(self.smtp_server, self.port) as server:
                server.starttls()  # Upgrade the connection to a secure encrypted SSL/TLS
                server.login(self.username, self.password)  # Log in to the server
                server.send_message(msg)  # Send the email

            print(f"Email sent successfully to {recipient_email}")

        except smtplib.SMTPException as e:
            raise Exception(f"Failed to send email: {e}")

# Example usage
if __name__ == "__main__":
    # SMTP settings for iFastNet hosting
    SMTP_SERVER = "smtp.ifastnet.com"  # Replace with actual iFastNet SMTP server
    SMTP_PORT = 587  # Commonly used port for TLS
    USERNAME = "your_email@ifastnet.com"  # Your iFastNet email
    PASSWORD = "your_password"  # Your iFastNet password

    # Create an instance of EmailSetup
    email_client = EmailSetup(SMTP_SERVER, SMTP_PORT, USERNAME, PASSWORD)

    # Define email parameters
    recipient = "recipient@example.com"  # Recipient's email address
    subject = "Test Email from iFastNet"
    body = "This is a test email sent using iFastNet hosting."

    # Send the email
    email_client.send_email(recipient, subject, body)
```
