"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://btc5000.epizy.com
Prompt: Recommend an API or library for managing email accounts on a hosting service that supports multiple email accounts, such as iFastNet.
Generated: DETERMINISTIC_0d171d65468a1ca3
Batch ID: 20250612_154302
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

Based on your request, here's Python code using the `IMAPClient` library for managing email accounts on a hosting service that supports IMAP (e.g., iFastNet). The code demonstrates connecting to an email account, retrieving messages, and error handling:

```python
# Import necessary libraries
import imapclient
import imaplib
from backports.ssl_match_hostname import match_hostname
from imapclient.exceptions import IMAPClientError

# Class to manage email accounts via IMAP
class EmailManager:
    def __init__(self, host: str, username: str, password: str, port: int = 993):
        """
        Initialize the EmailManager with connection details.
        
        :param host: The IMAP server hostname (e.g., 'mail.ifastnet.com')
        :param username: The email username.
        :param password: The email account password.
        :param port: The IMAP port (default is 993 for SSL).
        """
        self.host = host
        self.username = username
        self.password = password
        self.port = port
        self.connection = None

    def connect(self):
        """
        Establish a connection to the IMAP server.
        """
        try:
            # Create an IMAP client instance
            self.connection = imapclient.IMAPClient(self.host, port=self.port, ssl=True)
            # Login to the server
            self.connection.login(self.username, self.password)
            print("Successfully connected to the server.")
        except IMAPClientError as e:
            print(f"Error connecting to the server: {e}")
            self.connection = None
        except imaplib.IMAP4.error as e:
            print(f"Authentication error: {e}")
            self.connection = None

    def list_mailboxes(self):
        """
        List all mailboxes for the email account.
        """
        if not self.connection:
            print("Not connected to the server.")
            return
        try:
            mailboxes = self.connection.list_folders()
            print("Mailboxes:")
            for mailbox in mailboxes:
                print(mailbox)
        except IMAPClientError as e:
            print(f"Error retrieving mailboxes: {e}")

    def fetch_emails(self, mailbox: str = "INBOX"):
        """
        Fetch all emails from the specified mailbox.
        
        :param mailbox: The name of the mailbox to fetch emails from (default is 'INBOX').
        """
        if not self.connection:
            print("Not connected to the server.")
            return
        try:
            # Select the mailbox
            self.connection.select_folder(mailbox)
            # Search for all emails
            emails = self.connection.search()
            print(f"Found {len(emails)} emails in {mailbox}.")
            for email_id in emails:
                email_data = self.connection.fetch(email_id, ['ENVELOPE'])
                print(f"Email ID: {email_id}, Subject: {email_data[email_id][b'ENVELOPE'].subject.decode()}")
        except IMAPClientError as e:
            print(f"Error fetching emails: {e}")

    def disconnect(self):
        """
        Disconnect from the IMAP server.
        """
        if self.connection:
            self.connection.logout()
            print("Disconnected from the server.")
        else:
            print("No connection to disconnect.")

# Example usage
if __name__ == "__main__":
    # Replace with your actual email account details
    HOST = "mail.ifastnet.com"
    USERNAME = "your_email@ifastnet.com"
    PASSWORD = "your_password"

    # Initialize the EmailManager
    email_manager = EmailManager(host=HOST, username=USERNAME, password=PASSWORD)
    
    # Connect to the server
    email_manager.connect()
    
    # List mailboxes
    email_manager.list_mailboxes()
    
    # Fetch emails from the INBOX
    email_manager.fetch_emails(mailbox="INBOX")
    
    # Disconnect from the server
    email_manager.disconnect()
```

### Notes:
- Replace `HOST`, `USERNAME`, and `PASSWORD` with your actual email server details.
- Ensure that the `IMAPClient` library is installed (`pip install imapclient`).
- The code handles common errors, such as authentication and connection failures, and gracefully disconnects from the server.

Let me know if you need further assistance!
