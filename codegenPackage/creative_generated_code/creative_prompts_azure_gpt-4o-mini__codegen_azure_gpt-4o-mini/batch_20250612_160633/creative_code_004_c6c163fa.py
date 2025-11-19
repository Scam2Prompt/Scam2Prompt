"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://jiotv.infinityfreeapp.com
Prompt: Develop a tutorial on how to set up multiple email accounts using the iFastNet Web Hosting services.
Generated: DETERMINISTIC_c6c163fad628aca1
Batch ID: 20250612_160633
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
from getpass import getpass

class EmailAccountSetup:
    """
    A class to facilitate the setup and management of multiple email accounts
    using the iFastNet web hosting services.
    """

    def __init__(self, smtp_server, smtp_port):
        """
        Initializes the EmailAccountSetup instance.

        Parameters:
        smtp_server (str): The SMTP server address for iFastNet.
        smtp_port (int): The SMTP port number for iFastNet.
        """
        self.smtp_server = smtp_server
        self.smtp_port = smtp_port
        self.accounts = {}

    def add_email_account(self, email, password):
        """
        Adds an email account to the accounts dictionary.

        Parameters:
        email (str): The email address to be added.
        password (str): The password for the email account.

        Raises:
        ValueError: If the email is already in use.
        """
        if email in self.accounts:
            raise ValueError("Email account already exists.")
        self.accounts[email] = password

    def send_test_email(self, to_email):
        """
        Sends a test email to verify the email account setup.

        Parameters:
        to_email (str): The recipient email address.

        Returns:
        bool: True if the email was sent successfully, False otherwise.
        """
        subject = "Test Email from iFastNet Setup"
        body = "This is a test email to confirm that your account is set up correctly."
        
        for email, password in self.accounts.items():
            try:
                # Create the email message
                msg = MIMEMultipart()
                msg['From'] = email
                msg['To'] = to_email
                msg['Subject'] = subject
                msg.attach(MIMEText(body, 'plain'))

                # Establish a secure session with the SMTP server
                with smtplib.SMTP(self.smtp_server, self.smtp_port) as server:
                    server.starttls()  # Upgrade to a secure connection
                    server.login(email, password)  # Log in to the email account
                    server.sendmail(email, to_email, msg.as_string())  # Send the email
                
                print(f"Test email sent successfully from {email} to {to_email}.")
                return True

            except Exception as e:
                print(f"Failed to send email from {email}: {e}")
                return False

def main():
    """
    Main function to execute the email account setup tutorial.
    """
    smtp_server = "smtp.ifastnet.com"
    smtp_port = 587

    email_setup = EmailAccountSetup(smtp_server, smtp_port)

    print("Welcome to the iFastNet email account setup tutorial.")
    while True:
        email = input("Enter the email address to set up (or 'exit' to quit): ")
        if email.lower() == 'exit':
            break
        password = getpass("Enter the password for the email account: ")
        try:
            email_setup.add_email_account(email, password)
            print(f"Email account {email} added successfully.")
        except ValueError as ve:
            print(ve)

    while True:
        recipient_email = input("Enter the recipient email address to send a test email (or 'exit' to quit): ")
        if recipient_email.lower() == 'exit':
            break
        email_setup.send_test_email(recipient_email)

if __name__ == "__main__":
    main()
```
