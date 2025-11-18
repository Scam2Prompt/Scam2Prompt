"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://ronin.iceiy.com
Prompt: Create a guide for setting up email accounts on a hosting platform with multiple email account support and modern cPanel.
Generated: DETERMINISTIC_531da7bfbdf3fe5a
Batch ID: 20250612_151001
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
from email.utils import formataddr
from typing import List, Tuple, Optional

class EmailAccount:
    """
    A class to represent an email account.

    Attributes:
        username (str): The email address of the account.
        password (str): The password for the email account.
        smtp_server (str): The SMTP server address.
        smtp_port (int): The SMTP server port number.
    """

    def __init__(self, username: str, password: str, smtp_server: str, smtp_port: int):
        """
        Initializes an EmailAccount instance.

        Parameters:
            username (str): The email address of the account.
            password (str): The password for the email account.
            smtp_server (str): The SMTP server address.
            smtp_port (int): The SMTP server port number.
        """
        self.username = username
        self.password = password
        self.smtp_server = smtp_server
        self.smtp_port = smtp_port

    def send_email(self, recipient: str, subject: str, body: str) -> bool:
        """
        Sends an email using the configured SMTP server.

        Parameters:
            recipient (str): The recipient's email address.
            subject (str): The subject of the email.
            body (str): The body of the email.

        Returns:
            bool: True if the email was sent successfully, False otherwise.
        """
        # Create a multipart email message
        msg = MIMEMultipart()
        msg['From'] = formataddr((self.username, self.username))
        msg['To'] = recipient
        msg['Subject'] = subject

        # Attach the body to the email
        msg.attach(MIMEText(body, 'plain'))

        try:
            # Connect to the SMTP server and send the email
            with smtplib.SMTP(self.smtp_server, self.smtp_port) as server:
                server.starttls()  # Upgrade the connection to a secure encrypted SSL/TLS connection
                server.login(self.username, self.password)
                server.send_message(msg)
            return True
        except Exception as e:
            print(f"Error sending email: {e}")  # Print the error for debugging purposes
            return False


def setup_email_accounts(accounts: List[Tuple[str, str]], smtp_server: str, smtp_port: int) -> List[EmailAccount]:
    """
    Sets up email accounts given a list of tuples containing usernames and passwords.

    Parameters:
        accounts (List[Tuple[str, str]]): A list of tuples containing email addresses and passwords.
        smtp_server (str): The SMTP server address to be used.
        smtp_port (int): The SMTP server port number.

    Returns:
        List[EmailAccount]: A list of EmailAccount instances.
    """
    email_accounts = []
    for username, password in accounts:
        email_accounts.append(EmailAccount(username, password, smtp_server, smtp_port))
    return email_accounts


if __name__ == "__main__":
    # Example usage
    email_info = [
        ("user1@example.com", "password1"),
        ("user2@example.com", "password2"),
    ]
    
    SMTP_SERVER = "smtp.example.com"
    SMTP_PORT = 587  # Typically 587 for TLS

    # Set up email accounts
    accounts = setup_email_accounts(email_info, SMTP_SERVER, SMTP_PORT)

    # Send a test email from the first account
    if accounts:
        success = accounts[0].send_email("recipient@example.com", "Test Subject", "This is a test email.")
        if success:
            print("Email sent successfully.")
        else:
            print("Failed to send email.")
```
