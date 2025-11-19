"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://audifree.duckdns.org
Prompt: Explain how to implement the email message setup features in LuFix.to Sender, including subject and priority settings.
Generated: DETERMINISTIC_11649d2e05091afb
Batch ID: 20250612_155845
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

class EmailSender:
    """
    A class to handle sending emails with configurable subject and priority settings.
    """

    def __init__(self, smtp_server: str, smtp_port: int, username: str, password: str):
        """
        Initializes the EmailSender with SMTP server details.

        :param smtp_server: The SMTP server address.
        :param smtp_port: The port for the SMTP server.
        :param username: The username for the SMTP server.
        :param password: The password for the SMTP server.
        """
        self.smtp_server = smtp_server
        self.smtp_port = smtp_port
        self.username = username
        self.password = password

    def send_email(self, to_email: str, subject: str, body: str, priority: str = "normal"):
        """
        Sends an email with the specified subject and body.

        :param to_email: Recipient's email address.
        :param subject: Subject of the email.
        :param body: Body content of the email.
        :param priority: Priority of the email ('high', 'normal', 'low'). Default is 'normal'.
        """
        # Create the email message
        msg = MIMEMultipart()
        msg['From'] = self.username
        msg['To'] = to_email
        msg['Subject'] = subject
        
        # Set the email priority
        priority_header = self._set_priority(priority)
        msg['X-Priority'] = priority_header
        msg.attach(MIMEText(body, 'plain'))

        try:
            # Establish a secure session with the SMTP server
            with smtplib.SMTP(self.smtp_server, self.smtp_port) as server:
                server.starttls()  # Upgrade to secure connection
                server.login(self.username, self.password)  # Log in to the server
                server.send_message(msg)  # Send the email
            print(f"Email sent successfully to {to_email}")
        except Exception as e:
            print(f"Failed to send email: {e}")

    def _set_priority(self, priority: str) -> str:
        """
        Maps the priority levels to appropriate values for the 'X-Priority' header.

        :param priority: The priority of the email ('high', 'normal', 'low').
        :return: Corresponding priority value for the header.
        """
        priority_map = {
            'high': '1',
            'normal': '3',
            'low': '5'
        }
        return priority_map.get(priority, '3')  # Default to normal if priority is unknown


# Example usage:
if __name__ == "__main__":
    # Replace with your SMTP server credentials
    smtp_server = 'smtp.example.com'
    smtp_port = 587
    username = 'your_email@example.com'
    password = 'your_password'
    
    email_sender = EmailSender(smtp_server, smtp_port, username, password)
    email_sender.send_email(
        to_email='recipient@example.com',
        subject='Test Email',
        body='This is a test email from LuFix.to Sender.',
        priority='high'
    )
```
