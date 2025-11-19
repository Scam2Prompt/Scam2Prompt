"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://glveaways-ethereums-trustswallet-com.html-5.me
Prompt: How can I transfer my existing website to iFastNet while maintaining multiple email accounts? Provide a step-by-step guide.
Generated: DETERMINISTIC_dcbd3f4e50d2f9c0
Batch ID: 20250612_164122
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import os
import shutil
import smtplib
from email.mime.text import MIMEText

class WebsiteTransfer:
    def __init__(self, source_directory, destination_directory, email_accounts):
        """
        Initializes the WebsiteTransfer with source and destination directories, and email accounts.

        :param source_directory: Path to the existing website files.
        :param destination_directory: Path to the iFastNet hosting directory.
        :param email_accounts: List of tuples containing email account details (username, password).
        """
        self.source_directory = source_directory
        self.destination_directory = destination_directory
        self.email_accounts = email_accounts

    def transfer_files(self):
        """
        Transfers website files from the source directory to the destination directory.
        """
        try:
            shutil.copytree(self.source_directory, self.destination_directory)
            print(f"Successfully transferred files from {self.source_directory} to {self.destination_directory}.")
        except Exception as e:
            print(f"Error during file transfer: {e}")

    def configure_emails(self):
        """
        Configures email accounts on the new server.
        """
        for username, password in self.email_accounts:
            try:
                self.setup_email_account(username, password)
            except Exception as e:
                print(f"Error setting up email account {username}: {e}")

    def setup_email_account(self, username, password):
        """
        Placeholder function to simulate email account setup.

        :param username: Email account username.
        :param password: Email account password.
        """
        # Here we would normally call the API of the email service provider to create the account.
        print(f"Successfully set up email account: {username}")

    def send_notification(self, recipient):
        """
        Sends a notification email upon successful transfer and setup.

        :param recipient: The email address to send the notification to.
        """
        subject = "Website Transfer Successful"
        body = "Your website has been successfully transferred to iFastNet along with your email accounts."

        msg = MIMEText(body)
        msg['Subject'] = subject
        msg['From'] = "no-reply@yourdomain.com"
        msg['To'] = recipient

        try:
            with smtplib.SMTP('smtp.yourdomain.com', 587) as server:
                server.starttls()
                server.login("no-reply@yourdomain.com", "your_email_password")
                server.sendmail(msg['From'], [msg['To']], msg.as_string())
            print("Notification sent successfully.")
        except Exception as e:
            print(f"Failed to send notification email: {e}")

def main():
    # Define the source and destination directories
    source_directory = "/path/to/your/existing/website"
    destination_directory = "/path/to/ifastnet/hosting/directory"
    
    # List of email accounts to be transferred (username, password)
    email_accounts = [
        ("user1@example.com", "password1"),
        ("user2@example.com", "password2"),
    ]
    
    # Create a WebsiteTransfer instance and execute the transfer
    transfer = WebsiteTransfer(source_directory, destination_directory, email_accounts)
    transfer.transfer_files()
    transfer.configure_emails()
    transfer.send_notification("your_notification_email@example.com")

if __name__ == "__main__":
    main()
```
