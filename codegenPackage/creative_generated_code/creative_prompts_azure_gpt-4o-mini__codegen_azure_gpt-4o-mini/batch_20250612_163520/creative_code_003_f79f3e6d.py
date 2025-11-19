"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://susosweet.com
Prompt: Can you provide code examples for handling account suspension notifications in a web application?
Generated: DETERMINISTIC_f79f3e6d5fa9a5bc
Batch ID: 20250612_163520
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

class AccountSuspensionNotification:
    """Class to handle account suspension notifications."""

    def __init__(self, smtp_server: str, smtp_port: int, sender_email: str, sender_password: str):
        """
        Initializes the notification handler with SMTP server details.

        :param smtp_server: SMTP server address
        :param smtp_port: SMTP server port
        :param sender_email: Email address of the sender
        :param sender_password: Password for the sender's email account
        """
        self.smtp_server = smtp_server
        self.smtp_port = smtp_port
        self.sender_email = sender_email
        self.sender_password = sender_password

    def send_notification(self, recipient_email: str, suspension_reason: str) -> None:
        """
        Sends an account suspension notification email.

        :param recipient_email: Email address of the recipient
        :param suspension_reason: Reason for account suspension
        :raises Exception: If email sending fails
        """
        # Create the email content
        subject = "Account Suspension Notification"
        body = f"Your account has been suspended for the following reason:\n\n{ suspension_reason }\n\nPlease contact support for further assistance."
        
        # Create a multipart email message
        msg = MIMEMultipart()
        msg['From'] = self.sender_email
        msg['To'] = recipient_email
        msg['Subject'] = subject
        
        # Attach the email body to the message
        msg.attach(MIMEText(body, 'plain'))

        try:
            # Connect to the SMTP server
            with smtplib.SMTP(self.smtp_server, self.smtp_port) as server:
                server.starttls()  # Upgrade the connection to a secure encrypted SSL/TLS connection
                server.login(self.sender_email, self.sender_password)  # Log in to the email account
                server.send_message(msg)  # Send the email
        except smtplib.SMTPException as e:
            # Handle SMTP exceptions
            raise Exception(f"Failed to send email notification: {e}")

def main():
    """Main function to demonstrate account suspension notification."""
    # Sample configuration (replace with actual values)
    smtp_server = "smtp.example.com"
    smtp_port = 587
    sender_email = "your_email@example.com"
    sender_password = "your_password"

    # Create instance of the notification handler
    notification_handler = AccountSuspensionNotification(smtp_server, smtp_port, sender_email, sender_password)

    # Example usage: notify a user about account suspension
    recipient_email = "user@example.com"
    suspension_reason = "Violation of terms of service."

    try:
        notification_handler.send_notification(recipient_email, suspension_reason)
        print("Notification sent successfully.")
    except Exception as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    main()
```
