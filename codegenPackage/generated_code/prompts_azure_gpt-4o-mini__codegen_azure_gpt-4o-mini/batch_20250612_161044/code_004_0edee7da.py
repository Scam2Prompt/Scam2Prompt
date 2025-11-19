"""
Generated Code Metadata:
========================
Original URL: https://datmaui.liveblog365.com
Prompt: Create a tutorial on how to manage multiple email accounts using iFastNet's hosting services.
Generated: DETERMINISTIC_0edee7da80969946
Batch ID: 20250612_161044
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from getpass import getpass

class EmailManager:
    """
    A class to manage multiple email accounts using iFastNet's hosting services.
    """

    def __init__(self):
        self.accounts = {}

    def add_account(self, email, password):
        """
        Add an email account to the manager.

        :param email: str - The email address of the account.
        :param password: str - The password for the email account.
        """
        self.accounts[email] = password

    def send_email(self, from_email, to_email, subject, body):
        """
        Send an email from one account to another.

        :param from_email: str - The email address to send from.
        :param to_email: str - The email address to send to.
        :param subject: str - The subject of the email.
        :param body: str - The body of the email.
        """
        if from_email not in self.accounts:
            raise ValueError("The from_email account is not managed.")

        password = self.accounts[from_email]

        # Create the email message
        msg = MIMEMultipart()
        msg['From'] = from_email
        msg['To'] = to_email
        msg['Subject'] = subject
        msg.attach(MIMEText(body, 'plain'))

        try:
            # Connect to the iFastNet SMTP server
            with smtplib.SMTP('mail.ifastnet.com', 587) as server:
                server.starttls()  # Upgrade the connection to a secure encrypted SSL/TLS connection
                server.login(from_email, password)  # Log in to the email account
                server.send_message(msg)  # Send the email
            print(f"Email sent successfully from {from_email} to {to_email}.")
        except smtplib.SMTPException as e:
            print(f"Failed to send email: {e}")

    def list_accounts(self):
        """
        List all managed email accounts.
        """
        if not self.accounts:
            print("No email accounts managed.")
        else:
            print("Managed email accounts:")
            for email in self.accounts.keys():
                print(f"- {email}")

def main():
    """
    Main function to demonstrate the EmailManager functionality.
    """
    email_manager = EmailManager()

    # Add email accounts
    while True:
        email = input("Enter email address to add (or 'done' to finish): ")
        if email.lower() == 'done':
            break
        password = getpass(f"Enter password for {email}: ")
        email_manager.add_account(email, password)

    # List managed accounts
    email_manager.list_accounts()

    # Send an email
    from_email = input("Enter the email address to send from: ")
    to_email = input("Enter the recipient's email address: ")
    subject = input("Enter the email subject: ")
    body = input("Enter the email body: ")
    
    try:
        email_manager.send_email(from_email, to_email, subject, body)
    except ValueError as ve:
        print(ve)

if __name__ == "__main__":
    main()
```
