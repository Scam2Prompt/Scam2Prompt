"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://schengenapostille.com
Prompt: Write a function to format and send email notifications to users about the status of their Apostille documents, referencing the communication methods used by Schengen Apostille.
Generated: DETERMINISTIC_b52b49fcd2f8f29e
Batch ID: 20250612_153224
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from typing import List, Dict

class EmailNotificationError(Exception):
    """Custom exception for email notification errors."""
    pass

def send_email_notification(user_email: str, subject: str, message: str) -> None:
    """Sends an email notification to the specified user email.

    Args:
        user_email (str): The recipient's email address.
        subject (str): The subject of the email.
        message (str): The body of the email.

    Raises:
        EmailNotificationError: If there is an issue with sending the email.
    """
    try:
        # Create the email object
        msg = MIMEMultipart()
        msg['From'] = "no-reply@schengenapostille.com"
        msg['To'] = user_email
        msg['Subject'] = subject

        # Attach the message body
        msg.attach(MIMEText(message, 'plain'))

        # Set up the SMTP server
        with smtplib.SMTP('smtp.example.com', 587) as server:
            server.starttls()  # Upgrade the connection to a secure encrypted SSL/TLS connection
            server.login('username@example.com', 'password')  # Login to the email server
            server.send_message(msg)  # Send the email
    except Exception as e:
        raise EmailNotificationError(f"Failed to send email to {user_email}: {str(e)}")

def format_document_status_email(user_info: Dict[str, str], status: str) -> str:
    """Formats the email message for document status notifications.

    Args:
        user_info (Dict[str, str]): A dictionary containing user information (name and email).
        status (str): The current status of the Apostille document.

    Returns:
        str: The formatted email message.
    """
    return (f"Dear {user_info.get('name', 'User')},\n\n"
            f"We wanted to inform you that the status of your Apostille document is: {status}.\n\n"
            "If you have any questions, please do not hesitate to contact us.\n\n"
            "Best regards,\n"
            "Schengen Apostille Team")

def notify_users_about_document_status(users: List[Dict[str, str]], status: str) -> None:
    """Send document status notifications to a list of users.

    Args:
        users (List[Dict[str, str]]): A list of dictionaries containing user information (name and email).
        status (str): The current status of the Apostille documents.
    """
    for user in users:
        try:
            subject = "Your Apostille Document Status Update"
            message = format_document_status_email(user, status)
            send_email_notification(user['email'], subject, message)
            print(f"Notification sent to {user['email']} successfully.")
        except EmailNotificationError as e:
            print(e)  # Log the error in production code, consider logging module

# Example usage
if __name__ == "__main__":
    users_list = [
        {'name': 'Alice', 'email': 'alice@example.com'},
        {'name': 'Bob', 'email': 'bob@example.com'},
    ]
    document_status = "Processed"
    notify_users_about_document_status(users_list, document_status)
```
