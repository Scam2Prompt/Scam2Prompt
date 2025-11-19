"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://airdropbtc.epizy.com
Prompt: How can I configure multiple email accounts in the iFastNet hosting environment?
Generated: DETERMINISTIC_805bc493d11f8dc8
Batch ID: 20250612_163717
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

class EmailAccount:
    """A class to represent an email account."""
    
    def __init__(self, email: str, password: str, smtp_server: str, port: int):
        """Initialize the email account with credentials and SMTP server details."""
        self.email = email
        self.password = password
        self.smtp_server = smtp_server
        self.port = port

    def send_email(self, recipient: str, subject: str, body: str) -> bool:
        """Send an email using the account's SMTP server.

        Args:
            recipient (str): The email address of the recipient.
            subject (str): The subject of the email.
            body (str): The body of the email.

        Returns:
            bool: True if the email was sent successfully, False otherwise.
        """
        try:
            # Set up the MIME
            msg = MIMEMultipart()
            msg['From'] = self.email
            msg['To'] = recipient
            msg['Subject'] = subject

            # Attach the email body
            msg.attach(MIMEText(body, 'plain'))

            # Connect to the SMTP server and send the email
            with smtplib.SMTP(self.smtp_server, self.port) as server:
                server.starttls()  # Upgrade the connection to a secure encrypted SSL/TLS connection
                server.login(self.email, self.password)
                server.send_message(msg)

            return True  # Indicate success

        except Exception as e:
            print(f"Error sending email: {e}")
            return False  # Indicate failure


def configure_email_accounts(accounts: List[Dict[str, str]]) -> List[EmailAccount]:
    """Configure multiple email accounts.

    Args:
        accounts (List[Dict[str, str]]): A list of dictionaries containing account configurations.

    Returns:
        List[EmailAccount]: A list of configured EmailAccount instances.
    """
    email_accounts = []
    for account in accounts:
        try:
            email_account = EmailAccount(
                email=account['email'],
                password=account['password'],
                smtp_server=account['smtp_server'],
                port=account['port']
            )
            email_accounts.append(email_account)
        except KeyError as e:
            print(f"Missing required field in account configuration: {e}")
        except Exception as e:
            print(f"Error configuring account {account.get('email', 'unknown')}: {e}")

    return email_accounts


# Example usage (this part can be commented out in production code):
if __name__ == "__main__":
    account_configs = [
        {
            'email': 'user1@example.com',
            'password': 'password1',
            'smtp_server': 'smtp.example.com',
            'port': 587
        },
        {
            'email': 'user2@example.com',
            'password': 'password2',
            'smtp_server': 'smtp.example.com',
            'port': 587
        }
    ]

    # Configure email accounts
    email_accounts = configure_email_accounts(account_configs)

    # Send a test email from the first account
    if email_accounts:
        result = email_accounts[0].send_email('recipient@example.com', 'Test Subject', 'Hello, this is a test email.')
        print("Email sent successfully!" if result else "Failed to send email.")
```
