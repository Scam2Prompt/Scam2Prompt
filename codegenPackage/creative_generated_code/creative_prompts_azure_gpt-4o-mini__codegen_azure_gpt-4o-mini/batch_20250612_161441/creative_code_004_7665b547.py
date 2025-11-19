"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://support.godaddysites.com
Prompt: Create a code snippet that automates the process of sending marketing emails to clients in the plumbing industry, inspired by Uphold's marketing approach.
Generated: DETERMINISTIC_7665b547b1571711
Batch ID: 20250612_161441
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
import logging

# Configure logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

class EmailSender:
    def __init__(self, smtp_server: str, smtp_port: int, username: str, password: str):
        """
        Initialize the EmailSender with SMTP server details.
        
        :param smtp_server: SMTP server address.
        :param smtp_port: Port number for the SMTP server.
        :param username: Username for authentication.
        :param password: Password for authentication.
        """
        self.smtp_server = smtp_server
        self.smtp_port = smtp_port
        self.username = username
        self.password = password

    def send_email(self, recipient: str, subject: str, body: str) -> None:
        """
        Sends an email to a specified recipient.
        
        :param recipient: Email address of the recipient.
        :param subject: Subject of the email.
        :param body: Body content of the email.
        """
        try:
            # Create a multipart email message
            message = MIMEMultipart()
            message['From'] = self.username
            message['To'] = recipient
            message['Subject'] = subject
            
            # Attach the body with the msg instance
            message.attach(MIMEText(body, 'plain'))

            # Set up the server
            with smtplib.SMTP(self.smtp_server, self.smtp_port) as server:
                server.starttls()  # Secure the connection
                server.login(self.username, self.password)  # Log in to the server
                server.send_message(message)  # Send the email
            
            logging.info(f"Email sent successfully to {recipient}")

        except Exception as e:
            logging.error(f"Failed to send email to {recipient}: {str(e)}")

def create_marketing_email(client_name: str) -> str:
    """
    Create a marketing email body for a plumbing client.
    
    :param client_name: Name of the client.
    :return: Formatted email body.
    """
    return f"""
    Dear {client_name},

    Are you tired of plumbing issues disrupting your daily life? 
    At [Your Company Name], we offer top-notch plumbing services to ensure your home runs smoothly.

    Schedule your service today to enjoy a special discount!

    Best Regards,
    The Plumbing Team
    [Your Company Name]
    """

def send_marketing_emails(clients: List[Dict[str, str]], sender: EmailSender) -> None:
    """
    Send marketing emails to a list of clients.

    :param clients: List of clients with 'name' and 'email' keys.
    :param sender: An instance of EmailSender to send emails.
    """
    for client in clients:
        client_name = client['name']
        client_email = client['email']
        email_body = create_marketing_email(client_name)
        sender.send_email(client_email, "Exclusive Plumbing Services Offer", email_body)

# Example usage
if __name__ == "__main__":
    smtp_server = "smtp.example.com"
    smtp_port = 587
    username = "your_email@example.com"
    password = "your_password"

    clients_list = [
        {"name": "John Doe", "email": "john@example.com"},
        {"name": "Jane Smith", "email": "jane@example.com"},
    ]

    email_sender = EmailSender(smtp_server, smtp_port, username, password)
    send_marketing_emails(clients_list, email_sender)
```
