"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://vip-token2049.vercel.app
Prompt: Generate code for subscribing users to a newsletter and sending event updates, as described in the TOKEN2049 website content.
Generated: DETERMINISTIC_b2d6dc277c305c68
Batch ID: 20250612_150013
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
from typing import List

# Define a class to handle newsletter subscriptions and event updates
class NewsletterManager:
    def __init__(self, smtp_server: str, smtp_port: int, email_user: str, email_password: str):
        """
        Initialize the Newsletter Manager with SMTP server credentials.

        :param smtp_server: SMTP server address
        :param smtp_port: SMTP server port
        :param email_user: Email username for authentication
        :param email_password: Email password for authentication
        """
        self.smtp_server = smtp_server
        self.smtp_port = smtp_port
        self.email_user = email_user
        self.email_password = email_password
        self.subscribers = set()  # Use a set to avoid duplicate email addresses

    def subscribe_user(self, email: str) -> str:
        """
        Subscribe a user to the newsletter.

        :param email: The email address to subscribe
        :return: Success message
        """
        if email in self.subscribers:
            return f"{email} is already subscribed."
        self.subscribers.add(email)
        return f"{email} has been successfully subscribed."

    def send_event_update(self, subject: str, message: str, attachments: List[str] = None) -> None:
        """
        Send an event update to all subscribed users.

        :param subject: Email subject
        :param message: Email body content
        :param attachments: List of file paths for attachments (optional)
        """
        if not self.subscribers:
            print("No subscribers to send updates to.")
            return

        try:
            # Establish connection to the SMTP server
            with smtplib.SMTP(self.smtp_server, self.smtp_port) as server:
                server.starttls()  # Secure the connection
                server.login(self.email_user, self.email_password)

                # Send email to each subscriber
                for subscriber in self.subscribers:
                    email_msg = MIMEMultipart()
                    email_msg['From'] = self.email_user
                    email_msg['To'] = subscriber
                    email_msg['Subject'] = subject

                    # Attach the message body
                    email_msg.attach(MIMEText(message, 'plain'))

                    # Attach files if provided
                    if attachments:
                        for file_path in attachments:
                            try:
                                with open(file_path, 'rb') as f:
                                    attachment = MIMEText(f.read(), 'base64')
                                    attachment.add_header('Content-Disposition', f'attachment; filename="{file_path.split("/")[-1]}"')
                                    email_msg.attach(attachment)
                            except FileNotFoundError:
                                print(f"Attachment not found: {file_path}")
                                continue

                    # Send the email
                    server.sendmail(self.email_user, subscriber, email_msg.as_string())

                print("Event updates sent successfully.")

        except smtplib.SMTPException as e:
            print(f"Failed to send email: {e}")

# Example usage
if __name__ == "__main__":
    # Replace with actual SMTP server details and credentials
    smtp_server = "smtp.example.com"
    smtp_port = 587
    email_user = "your_email@example.com"
    email_password = "your_password"

    # Create an instance of NewsletterManager
    manager = NewsletterManager(smtp_server, smtp_port, email_user, email_password)

    # Subscribe users to the newsletter
    print(manager.subscribe_user("user1@example.com"))
    print(manager.subscribe_user("user2@example.com"))
    print(manager.subscribe_user("user1@example.com"))  # Test duplicate subscription

    # Send an event update
    subject = "TOKEN2049 Event Updates"
    message = "Join us for the latest TOKEN2049 event. Don't miss out!"
    manager.send_event_update(subject, message)
```
