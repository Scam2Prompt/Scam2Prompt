"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://airdrophunter.pages.dev
Prompt: Suggest tools or libraries to integrate email-based notifications into a cryptocurrency airdrop platform, as described on the website.
Generated: DETERMINISTIC_c68d56b7a67ffed2
Batch ID: 20250612_152358
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

class EmailNotifier:
    def __init__(self, smtp_server: str, smtp_port: int, username: str, password: str):
        """
        Initializes the EmailNotifier with SMTP server details.

        Args:
            smtp_server (str): The SMTP server address.
            smtp_port (int): The SMTP server port.
            username (str): The username for SMTP authentication.
            password (str): The password for SMTP authentication.
        """
        self.smtp_server = smtp_server
        self.smtp_port = smtp_port
        self.username = username
        self.password = password

    def send_email(self, recipients: List[str], subject: str, body: str) -> None:
        """
        Sends an email to the specified recipients.

        Args:
            recipients (List[str]): A list of recipient email addresses.
            subject (str): The subject of the email.
            body (str): The body content of the email.
        
        Raises:
            Exception: Raises an exception if sending the email fails.
        """
        try:
            # Create a multipart email message
            msg = MIMEMultipart()
            msg['From'] = self.username
            msg['To'] = ', '.join(recipients)
            msg['Subject'] = subject
            
            # Attach the body to the email
            msg.attach(MIMEText(body, 'plain'))

            # Connect to the SMTP server and send the email
            with smtplib.SMTP(self.smtp_server, self.smtp_port) as server:
                server.starttls()  # Upgrade the connection to a secure encrypted SSL/TLS connection
                server.login(self.username, self.password)  # Log in to the SMTP server
                server.send_message(msg)  # Send the email
            print(f"Email sent successfully to: {', '.join(recipients)}")
        except Exception as e:
            print(f"Failed to send email: {str(e)}")
            raise

def main():
    # Example usage of the EmailNotifier class
    smtp_details = {
        'smtp_server': 'smtp.example.com',
        'smtp_port': 587,
        'username': 'your_email@example.com',
        'password': 'your_password'
    }

    email_notifier = EmailNotifier(**smtp_details)
    
    # Define recipients, subject, and body for the email notification
    recipients = ['user1@example.com', 'user2@example.com']
    subject = 'Crypto Airdrop Notification'
    body = 'Congratulations! You have received tokens in our recent airdrop.'

    # Send the email notification
    email_notifier.send_email(recipients, subject, body)

if __name__ == '__main__':
    main()
```
