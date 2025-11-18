"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://suspicious-euler-473151.netlify.app
Prompt: Write Python code to interact with a Mac email client that supports Microsoft Exchange using an appropriate API. Include functionality for sending and receiving emails.
Generated: DETERMINISTIC_1e9e29c6ce0fda1d
Batch ID: 20250612_151347
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import exchangelib
from exchangelib import Credentials, Account, Message, HTMLBody

# Configuration
EMAIL = "your_email@example.com"  # Replace with your email address
PASSWORD = "your_password"        # Replace with your email password
SERVER = "your_exchange_server"  # Replace with your Exchange server address

def setup_exchange_account(email, password, server):
    """
    Sets up the Exchange account using provided credentials and server.
    Returns the authenticated Account object.

    :param email: Email address
    :param password: Email password
    :param server: Exchange server address
    :return: Account object
    """
    try:
        credentials = Credentials(email, password)
        # Create the account object
        account = Account(
            primary_smtp_address=email,
            credentials=credentials,
            autodiscover=False,
            config=exchangelib.Configuration(server=server, credentials=credentials)
        )
        return account
    except Exception as e:
        print(f"Error setting up Exchange account: {e}")
        return None

def send_email(account, recipient, subject, body):
    """
    Sends an email using the authenticated Exchange account.

    :param account: Authenticated Account object
    :param recipient: Recipient email address
    :param subject: Subject of the email
    :param body: Body content of the email (HTML format recommended)
    """
    try:
        message = Message(
            account=account,
            folder=account.sent,
            to_recipients=[recipient],
            subject=subject,
            body=HTMLBody(body)
        )
        message.send()
        print(f"Email successfully sent to {recipient}")
    except Exception as e:
        print(f"Error sending email: {e}")

def get_inbox_emails(account):
    """
    Fetches the emails from the inbox folder of the authenticated Exchange account.

    :param account: Authenticated Account object
    :return: List of emails (subject and sender)
    """
    try:
        inbox = account.inbox
        inbox.refresh()  # Refresh the inbox folder
        emails = []
        for item in inbox.all().order_by('-datetime_received')[:10]:  # Fetch latest 10 emails
            emails.append({
                "subject": item.subject,
                "sender": item.sender.email_address if item.sender else "Unknown"
            })
        return emails
    except Exception as e:
        print(f"Error fetching inbox emails: {e}")
        return []

def main():
    # Setup Exchange account
    account = setup_exchange_account(EMAIL, PASSWORD, SERVER)
    if not account:
        print("Failed to connect to Exchange server.")
        return

    # Send an email
    recipient = "recipient@example.com"  # Replace with recipient email address
    subject = "Test Email"
    body = "<html><body><h1>This is a test email.</h1></body></html>"
    send_email(account, recipient, subject, body)

    # Fetch inbox emails
    inbox_emails = get_inbox_emails(account)
    if inbox_emails:
        print("\nLatest emails in Inbox:")
        for email in inbox_emails:
            print(f"Subject: {email['subject']}, Sender: {email['sender']}")
    else:
        print("No emails found in Inbox.")

if __name__ == "__main__":
    main()
```

Note: This code uses the `exchangelib` library to interact with Microsoft Exchange. You need to install the library (`pip install exchangelib`) and replace the placeholders (`your_email@example.com`, `your_password`, `your_exchange_server`) with actual values for your setup. Be cautious with handling sensitive information like passwords; consider using environment variables or secure credential storage methods in a production environment.
