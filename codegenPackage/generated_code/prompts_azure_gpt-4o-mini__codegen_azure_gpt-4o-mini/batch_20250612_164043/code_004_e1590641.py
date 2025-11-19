"""
Generated Code Metadata:
========================
Original URL: https://atualcontabilidade.com
Prompt: Outline a library recommendation for integrating email communication within an accounting software, considering the emphasis on client availability highlighted by Atual Contabilidade.
Generated: DETERMINISTIC_e1590641903d1df7
Batch ID: 20250612_164043
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
from typing import List, Dict

class EmailClient:
    """
    A class to handle email communication for accounting software.
    """

    def __init__(self, smtp_server: str, smtp_port: int, username: str, password: str):
        """
        Initializes the EmailClient with SMTP server details.

        :param smtp_server: The SMTP server address.
        :param smtp_port: The port for the SMTP server.
        :param username: The username for the email account.
        :param password: The password for the email account.
        """
        self.smtp_server = smtp_server
        self.smtp_port = smtp_port
        self.username = username
        self.password = password

    def send_email(self, recipient: str, subject: str, body: str) -> bool:
        """
        Sends an email to the specified recipient.

        :param recipient: The email address of the recipient.
        :param subject: The subject of the email.
        :param body: The body content of the email.
        :return: True if the email was sent successfully, False otherwise.
        """
        try:
            # Create a multipart email message
            msg = MIMEMultipart()
            msg['From'] = self.username
            msg['To'] = recipient
            msg['Subject'] = subject

            # Attach the email body
            msg.attach(MIMEText(body, 'plain'))

            # Connect to the SMTP server and send the email
            with smtplib.SMTP(self.smtp_server, self.smtp_port) as server:
                server.starttls()  # Upgrade the connection to a secure encrypted SSL/TLS connection
                server.login(self.username, self.password)
                server.send_message(msg)

            return True
        except smtplib.SMTPException as e:
            print(f"Error sending email: {e}")
            return False

    def send_bulk_emails(self, recipients: List[str], subject: str, body: str) -> Dict[str, bool]:
        """
        Sends emails to multiple recipients.

        :param recipients: A list of email addresses to send the email to.
        :param subject: The subject of the email.
        :param body: The body content of the email.
        :return: A dictionary with recipient email addresses as keys and success status as values.
        """
        results = {}
        for recipient in recipients:
            results[recipient] = self.send_email(recipient, subject, body)
        return results

# Example usage
if __name__ == "__main__":
    # Initialize the EmailClient with SMTP server details
    email_client = EmailClient(smtp_server='smtp.example.com', smtp_port=587, 
                               username='your_email@example.com', password='your_password')

    # Define the email subject and body
    subject = "Client Availability Reminder"
    body = "Dear Client,\n\nThis is a reminder to check your availability for our upcoming meeting.\n\nBest regards,\nAtual Contabilidade"

    # Send a single email
    email_client.send_email('client@example.com', subject, body)

    # Send bulk emails
    recipients = ['client1@example.com', 'client2@example.com', 'client3@example.com']
    results = email_client.send_bulk_emails(recipients, subject, body)
    print(results)
```
