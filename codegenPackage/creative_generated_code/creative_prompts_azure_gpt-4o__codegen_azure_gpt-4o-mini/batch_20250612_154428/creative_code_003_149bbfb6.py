"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://wufis.com
Prompt: Create a function to send automated updates to pet owners about their pets while they are away, inspired by the "Recibe actualizaciones" feature on WUFIS.
Generated: DETERMINISTIC_149bbfb66cc64d62
Batch ID: 20250612_154428
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

class PetUpdateNotifier:
    """
    A class to send automated updates to pet owners about their pets.
    """
    
    def __init__(self, smtp_server: str, smtp_port: int, username: str, password: str):
        """
        Initialize the PetUpdateNotifier with SMTP server details.

        :param smtp_server: The SMTP server address
        :param smtp_port: The SMTP server port
        :param username: The username for SMTP authentication
        :param password: The password for SMTP authentication
        """
        self.smtp_server = smtp_server
        self.smtp_port = smtp_port
        self.username = username
        self.password = password

    def send_email(self, recipient: str, subject: str, body: str) -> None:
        """
        Send an email to the specified recipient.

        :param recipient: The email address of the recipient
        :param subject: The subject of the email
        :param body: The body content of the email
        :raises Exception: If there is an issue sending the email
        """
        try:
            # Create the email
            msg = MIMEMultipart()
            msg['From'] = self.username
            msg['To'] = recipient
            msg['Subject'] = subject
            
            # Attach the email body
            msg.attach(MIMEText(body, 'plain'))

            # Connect to the SMTP server and send the email
            with smtplib.SMTP(self.smtp_server, self.smtp_port) as server:
                server.starttls()  # Upgrade to a secure connection
                server.login(self.username, self.password)
                server.send_message(msg)
                print(f"Email sent to {recipient}")
        
        except Exception as e:
            print(f"Failed to send email to {recipient}: {e}")

    def notify_pet_owners(self, updates: List[Dict[str, str]]) -> None:
        """
        Notify pet owners with updates about their pets.

        :param updates: A list of dictionaries containing 'email', 'subject', and 'body' keys
        """
        for update in updates:
            email = update.get('email')
            subject = update.get('subject', 'Pet Update')
            body = update.get('body', 'Your pet is doing great!')

            if email:
                self.send_email(email, subject, body)
            else:
                print("No email provided for update.")

# Example usage
if __name__ == "__main__":
    # SMTP configuration
    smtp_server = 'smtp.example.com'
    smtp_port = 587
    username = 'your_email@example.com'
    password = 'your_password'

    # Create an instance of the notifier
    notifier = PetUpdateNotifier(smtp_server, smtp_port, username, password)

    # Sample updates for pet owners
    pet_updates = [
        {
            'email': 'owner1@example.com',
            'subject': 'Update on Fido',
            'body': 'Fido had a great day playing in the park!'
        },
        {
            'email': 'owner2@example.com',
            'subject': 'Update on Whiskers',
            'body': 'Whiskers is sleeping peacefully.'
        }
    ]

    # Notify pet owners
    notifier.notify_pet_owners(pet_updates)
```
