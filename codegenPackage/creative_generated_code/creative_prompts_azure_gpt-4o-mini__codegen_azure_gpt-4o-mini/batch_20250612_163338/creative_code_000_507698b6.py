"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://markandecastro.com
Prompt: Write a Python script that handles account suspension notifications for a web application.
Generated: DETERMINISTIC_507698b6f38e2ec8
Batch ID: 20250612_163338
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


class AccountSuspensionNotifier:
    """
    A class to handle account suspension notifications.
    """

    def __init__(self, smtp_server: str, smtp_port: int, sender_email: str, sender_password: str):
        """
        Initializes the notifier with SMTP server details.

        :param smtp_server: SMTP server address
        :param smtp_port: SMTP server port
        :param sender_email: Email address of the sender
        :param sender_password: Password for the sender's email
        """
        self.smtp_server = smtp_server
        self.smtp_port = smtp_port
        self.sender_email = sender_email
        self.sender_password = sender_password

    def send_notification(self, recipient_email: str, account_details: Dict[str, str]) -> None:
        """
        Sends an account suspension notification email.

        :param recipient_email: The recipient's email address
        :param account_details: A dictionary with account information
        :raises ValueError: If recipient_email is invalid or account_details are insufficient
        """
        if not self._is_valid_email(recipient_email):
            raise ValueError("Invalid recipient email address.")

        if 'username' not in account_details or 'reason' not in account_details:
            raise ValueError("Account details must include 'username' and 'reason'.")

        subject = "Account Suspension Notification"
        body = self._compose_email_body(account_details)

        try:
            self._send_email(recipient_email, subject, body)
            print(f"Notification sent to {recipient_email}.")
        except Exception as e:
            print(f"Failed to send notification to {recipient_email}: {e}")

    def _compose_email_body(self, account_details: Dict[str, str]) -> str:
        """
        Composes the email body for the notification.

        :param account_details: A dictionary with account information
        :return: A formatted email body string
        """
        return f"""
        Dear {account_details['username']},

        We regret to inform you that your account has been suspended due to the following reason:
        {account_details['reason']}

        If you believe this to be an error, please contact support.

        Sincerely,
        The Support Team
        """

    def _send_email(self, recipient_email: str, subject: str, body: str) -> None:
        """
        Sends an email using SMTP.

        :param recipient_email: The recipient's email address
        :param subject: The subject of the email
        :param body: The body of the email
        :raises Exception: If sending the email fails
        """
        msg = MIMEMultipart()
        msg['From'] = self.sender_email
        msg['To'] = recipient_email
        msg['Subject'] = subject

        msg.attach(MIMEText(body, 'plain'))

        with smtplib.SMTP(self.smtp_server, self.smtp_port) as server:
            server.starttls()  # Upgrade the connection to a secure encrypted SSL/TLS connection
            server.login(self.sender_email, self.sender_password)
            server.sendmail(self.sender_email, recipient_email, msg.as_string())

    @staticmethod
    def _is_valid_email(email: str) -> bool:
        """
        Validates the format of an email address.

        :param email: The email address to validate
        :return: True if valid, False otherwise
        """
        import re
        email_regex = r'^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$'
        return re.match(email_regex, email) is not None


# Example usage (commented out for production):
# if __name__ == "__main__":
#     notifier = AccountSuspensionNotifier(
#         smtp_server='smtp.example.com',
#         smtp_port=587,
#         sender_email='your_email@example.com',
#         sender_password='your_password'
#     )
#     try:
#         notifier.send_notification(
#             recipient_email='user@example.com',
#             account_details={'username': 'user123', 'reason': 'Violation of terms of service'}
#         )
#     except Exception as e:
#         print(f"Error: {e}")
```
