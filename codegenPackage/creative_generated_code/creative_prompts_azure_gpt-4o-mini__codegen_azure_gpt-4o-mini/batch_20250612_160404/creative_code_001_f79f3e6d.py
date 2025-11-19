"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://project-database.com
Prompt: Can you provide code examples for handling account suspension notifications in a web application?
Generated: DETERMINISTIC_f79f3e6d5fa9a5bc
Batch ID: 20250612_160404
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
from typing import List

class AccountSuspensionNotifier:
    """
    A class to handle account suspension notifications via email.
    """

    def __init__(self, smtp_server: str, smtp_port: int, username: str, password: str):
        """
        Initializes the notifier with SMTP server details.

        :param smtp_server: The SMTP server address.
        :param smtp_port: The port for the SMTP server.
        :param username: SMTP server username for authentication.
        :param password: SMTP server password for authentication.
        """
        self.smtp_server = smtp_server
        self.smtp_port = smtp_port
        self.username = username
        self.password = password

    def send_notification(self, recipient_email: str, user_name: str) -> None:
        """
        Sends an account suspension notification email.

        :param recipient_email: The email address of the user.
        :param user_name: The name of the user for personalized notification.
        :raises Exception: If unable to send the email.
        """
        subject = "Account Suspension Notification"
        body = f"Dear {user_name},\n\nYour account has been suspended due to policy violations.\n\nBest regards,\nSupport Team"

        # Create the email message
        msg = MIMEText(body)
        msg['Subject'] = subject
        msg['From'] = self.username
        msg['To'] = recipient_email

        try:
            # Establish a secure session with the SMTP server
            with smtplib.SMTP(self.smtp_server, self.smtp_port) as server:
                server.starttls()  # Upgrade to a secure connection
                server.login(self.username, self.password)  # Log in to the SMTP server
                server.send_message(msg)  # Send the email
            print(f"Notification sent to {recipient_email}")
        except smtplib.SMTPException as e:
            print(f"Error sending email to {recipient_email}: {e}")
            raise  # Re-raise the exception for further handling if necessary

def main():
    """
    Main function to demonstrate account suspension notification.
    """
    # Configuration for the SMTP server
    SMTP_SERVER = "smtp.example.com"
    SMTP_PORT = 587
    USERNAME = "your_email@example.com"
    PASSWORD = "your_password"

    # Create an instance of the notifier
    notifier = AccountSuspensionNotifier(SMTP_SERVER, SMTP_PORT, USERNAME, PASSWORD)

    # List of suspended accounts (for demonstration purposes)
    suspended_accounts = [
        {"email": "user1@example.com", "name": "User One"},
        {"email": "user2@example.com", "name": "User Two"},
    ]

    # Send notifications for each suspended account
    for account in suspended_accounts:
        try:
            notifier.send_notification(account["email"], account["name"])
        except Exception as e:
            print(f"Failed to notify {account['name']} ({account['email']}): {e}")

if __name__ == "__main__":
    main()
```
