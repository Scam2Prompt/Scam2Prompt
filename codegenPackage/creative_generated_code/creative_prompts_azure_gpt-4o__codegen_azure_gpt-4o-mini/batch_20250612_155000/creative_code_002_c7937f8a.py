"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://la-guarida.com.ar
Prompt: Generate a Python script for automating email campaigns, referencing La Guarida's focus on digital solutions.
Generated: DETERMINISTIC_c7937f8aed2ff8db
Batch ID: 20250612_155000
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from typing import List
import logging
import ssl

# Configure logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

class EmailCampaign:
    """
    A class to handle the automation of email campaigns for La Guarida.
    """

    def __init__(self, smtp_server: str, smtp_port: int, username: str, password: str):
        """
        Initializes the EmailCampaign instance.

        :param smtp_server: The SMTP server address.
        :param smtp_port: The port number for the SMTP server.
        :param username: The email account username.
        :param password: The email account password.
        """
        self.smtp_server = smtp_server
        self.smtp_port = smtp_port
        self.username = username
        self.password = password

    def send_email(self, recipient: str, subject: str, body: str) -> None:
        """
        Sends an email to a specified recipient.

        :param recipient: The recipient's email address.
        :param subject: The subject of the email.
        :param body: The body content of the email.
        :raises Exception: If sending the email fails.
        """
        try:
            # Create message container
            msg = MIMEMultipart()
            msg['From'] = self.username
            msg['To'] = recipient
            msg['Subject'] = subject

            # Attach the body with the msg instance
            msg.attach(MIMEText(body, 'plain'))

            # Create a secure SSL context
            context = ssl.create_default_context()

            # Connect to the SMTP server and send the email
            with smtplib.SMTP(self.smtp_server, self.smtp_port) as server:
                server.starttls(context=context)  # Secure the connection
                server.login(self.username, self.password)  # Log in to the server
                server.send_message(msg)  # Send the email
                logging.info(f"Email sent successfully to {recipient}")

        except Exception as e:
            logging.error(f"Failed to send email to {recipient}: {e}")
            raise  # Re-raise the exception for further handling

    def run_campaign(self, recipients: List[str], subject: str, body: str) -> None:
        """
        Runs the email campaign by sending emails to a list of recipients.

        :param recipients: A list of recipient email addresses.
        :param subject: The subject of the email.
        :param body: The body content of the email.
        """
        for recipient in recipients:
            try:
                self.send_email(recipient, subject, body)
            except Exception as e:
                logging.error(f"Error sending email to {recipient}: {e}")

if __name__ == "__main__":
    # Example configuration - replace with actual details
    SMTP_SERVER = 'smtp.example.com'
    SMTP_PORT = 587
    USERNAME = 'your_email@example.com'
    PASSWORD = 'your_password'

    # Create an instance of EmailCampaign
    campaign = EmailCampaign(SMTP_SERVER, SMTP_PORT, USERNAME, PASSWORD)

    # Define the recipients, subject, and body of the email
    recipients_list = ['recipient1@example.com', 'recipient2@example.com']
    email_subject = 'Exciting Digital Solutions from La Guarida'
    email_body = 'Hello,\n\nDiscover how La Guarida can elevate your digital presence!'

    # Run the email campaign
    campaign.run_campaign(recipients_list, email_subject, email_body)
```
