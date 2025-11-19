"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://smartconnects.org
Prompt: Provide an example of using Smart Connect to manage client interactions effectively.
Generated: DETERMINISTIC_7889653fce0bd77c
Batch ID: 20250612_164040
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
from typing import List, Dict

class SmartConnect:
    """
    A class to manage client interactions effectively by sending personalized emails.
    """

    def __init__(self, smtp_server: str, smtp_port: int, username: str, password: str):
        """
        Initialize the SmartConnect instance with SMTP server details.

        :param smtp_server: SMTP server address
        :param smtp_port: SMTP server port
        :param username: Username for SMTP authentication
        :param password: Password for SMTP authentication
        """
        self.smtp_server = smtp_server
        self.smtp_port = smtp_port
        self.username = username
        self.password = password

    def send_email(self, recipient: str, subject: str, body: str) -> None:
        """
        Send an email to the specified recipient.

        :param recipient: Email address of the recipient
        :param subject: Subject of the email
        :param body: Body content of the email
        :raises Exception: Raises an exception if there is an error while sending the email
        """
        # Create a multipart email message
        msg = MIMEMultipart()
        msg['From'] = self.username
        msg['To'] = recipient
        msg['Subject'] = subject

        # Attach the email body to the message
        msg.attach(MIMEText(body, 'plain'))

        try:
            # Connect to the SMTP server and send the email
            with smtplib.SMTP(self.smtp_server, self.smtp_port) as server:
                server.starttls()  # Upgrade the connection to a secure encrypted SSL/TLS connection
                server.login(self.username, self.password)  # Log in to the server
                server.send_message(msg)  # Send the email
            print(f"Email sent successfully to {recipient}")
        except Exception as e:
            print(f"Failed to send email to {recipient}: {str(e)}")

    def send_bulk_emails(self, clients: List[Dict[str, str]]) -> None:
        """
        Send personalized emails to a list of clients.

        :param clients: A list of dictionaries containing client details (name and email)
        """
        for client in clients:
            name = client.get('name')
            email = client.get('email')
            subject = f"Hello {name}, Welcome to Our Service!"
            body = f"Dear {name},\n\nThank you for joining us! We are excited to have you.\n\nBest regards,\nYour Company"
            self.send_email(email, subject, body)

# Example usage:
if __name__ == "__main__":
    smtp_server = 'smtp.example.com'
    smtp_port = 587
    username = 'your_email@example.com'
    password = 'your_password'

    # Create an instance of SmartConnect
    smart_connect = SmartConnect(smtp_server, smtp_port, username, password)

    # List of clients to send emails to
    clients = [
        {'name': 'Alice', 'email': 'alice@example.com'},
        {'name': 'Bob', 'email': 'bob@example.com'},
        {'name': 'Charlie', 'email': 'charlie@example.com'}
    ]

    # Send bulk emails to clients
    smart_connect.send_bulk_emails(clients)
```
