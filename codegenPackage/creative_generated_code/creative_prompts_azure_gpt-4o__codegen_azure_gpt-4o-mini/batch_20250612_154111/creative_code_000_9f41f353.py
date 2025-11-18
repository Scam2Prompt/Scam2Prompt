"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://brokereo.com
Prompt: Write Python code to automate the process of notifying clients about the closure of their accounts and refunding balances, referencing the procedures outlined in Brokereo's Terms and Conditions.
Generated: DETERMINISTIC_9f41f353fef8551a
Batch ID: 20250612_154111
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

# Define a class to handle account closure notifications
class AccountClosureNotifier:
    def __init__(self, smtp_server: str, smtp_port: int, sender_email: str, sender_password: str):
        """
        Initializes the notifier with SMTP server settings.
        
        :param smtp_server: The SMTP server address
        :param smtp_port: The SMTP server port
        :param sender_email: The email address from which notifications are sent
        :param sender_password: The password for the sender's email
        """
        self.smtp_server = smtp_server
        self.smtp_port = smtp_port
        self.sender_email = sender_email
        self.sender_password = sender_password

    def send_email(self, recipient_email: str, subject: str, body: str) -> None:
        """
        Sends an email to the specified recipient.

        :param recipient_email: The recipient's email address
        :param subject: The subject of the email
        :param body: The body content of the email
        """
        try:
            # Create a multipart email message
            msg = MIMEMultipart()
            msg['From'] = self.sender_email
            msg['To'] = recipient_email
            msg['Subject'] = subject
            msg.attach(MIMEText(body, 'plain'))

            # Establish a secure session with the SMTP server
            with smtplib.SMTP(self.smtp_server, self.smtp_port) as server:
                server.starttls()  # Secure the connection
                server.login(self.sender_email, self.sender_password)  # Log in to the SMTP server
                server.send_message(msg)  # Send the email

            logging.info(f"Notification email sent to {recipient_email}")

        except Exception as e:
            logging.error(f"Failed to send email to {recipient_email}: {e}")

    def notify_clients(self, clients: List[Dict[str, str]]) -> None:
        """
        Notifies clients about the closure of their accounts and refunding balances.

        :param clients: A list of clients, each represented as a dictionary with keys 'email', 'name', and 'balance'
        """
        for client in clients:
            try:
                recipient_email = client['email']
                recipient_name = client['name']
                refund_amount = client['balance']

                # Construct the email subject and body
                subject = "Account Closure Notification"
                body = (f"Dear {recipient_name},\n\n"
                        f"We regret to inform you that your account has been closed as per our Terms and Conditions.\n"
                        f"Your remaining balance of ${refund_amount} will be refunded to you shortly.\n\n"
                        "Thank you for your understanding.\n\n"
                        "Best Regards,\n"
                        "Brokereo Customer Service")

                # Send the notification email
                self.send_email(recipient_email, subject, body)

            except KeyError as e:
                logging.error(f"Missing information for client: {client}. Error: {e}")
            except Exception as e:
                logging.error(f"An error occurred while notifying client {client['email']}: {e}")

# Example usage
if __name__ == "__main__":
    # SMTP server configuration
    SMTP_SERVER = 'smtp.example.com'  # Replace with your SMTP server
    SMTP_PORT = 587  # Commonly used port for TLS
    SENDER_EMAIL = 'your_email@example.com'  # Replace with your email
    SENDER_PASSWORD = 'your_password'  # Replace with your email password

    # Create an instance of the notifier
    notifier = AccountClosureNotifier(SMTP_SERVER, SMTP_PORT, SENDER_EMAIL, SENDER_PASSWORD)

    # List of clients to notify
    clients_to_notify = [
        {'email': 'client1@example.com', 'name': 'Client One', 'balance': 50.0},
        {'email': 'client2@example.com', 'name': 'Client Two', 'balance': 75.0},
        # Add more clients as needed
    ]

    # Notify clients
    notifier.notify_clients(clients_to_notify)
```
