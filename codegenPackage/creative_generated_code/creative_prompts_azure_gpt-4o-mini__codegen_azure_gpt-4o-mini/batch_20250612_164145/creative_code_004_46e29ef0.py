"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://poocoinapp.rf.gd
Prompt: Provide a step-by-step guide to setting up email accounts using iFastNet Web Hosting's features.
Generated: DETERMINISTIC_46e29ef0cbf0c864
Batch ID: 20250612_164145
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
    A class to handle the setup and configuration of email accounts using iFastNet Web Hosting.
    """

    def __init__(self, smtp_server, port):
        """
        Initializes the EmailAccountSetup with SMTP server details.

        Args:
            smtp_server (str): The SMTP server address.
            port (int): The port number for the SMTP server.
        """
        self.smtp_server = smtp_server
        self.port = port

    def create_email_account(self, username, password):
        """
        Simulates the creation of an email account.

        Args:
            username (str): The email account username.
            password (str): The email account password.

        Raises:
            Exception: If the email account creation fails.
        """
        try:
            # Simulate account creation logic (mocked for this example)
            print(f"Creating email account: {username}@yourdomain.com")
            # Here you would implement actual API calls to iFastNet to create the account
            print(f"Account {username}@yourdomain.com created successfully.")
        except Exception as e:
            raise Exception(f"Failed to create email account: {str(e)}")

    def send_test_email(self, from_email, to_email, subject, body):
        """
        Sends a test email to verify the setup.

        Args:
            from_email (str): The sender's email address.
            to_email (str): The recipient's email address.
            subject (str): The subject of the email.
            body (str): The body of the email.

        Raises:
            Exception: If sending the email fails.
        """
        try:
            # Setup the email
            msg = MIMEMultipart()
            msg['From'] = from_email
            msg['To'] = to_email
            msg['Subject'] = subject

            msg.attach(MIMEText(body, 'plain'))

            # Connect to the SMTP server and send the email
            with smtplib.SMTP(self.smtp_server, self.port) as server:
                server.starttls()  # Upgrade the connection to a secure encrypted SSL/TLS
                server.login(from_email, getpass("Enter your email password: "))
                server.send_message(msg)

            print("Test email sent successfully.")
        except Exception as e:
            raise Exception(f"Failed to send test email: {str(e)}")

if __name__ == "__main__":
    # Configuration for iFastNet SMTP server (example values, replace with actual)
    SMTP_SERVER = 'smtp.yourdomain.com'
    PORT = 587

    setup = EmailAccountSetup(SMTP_SERVER, PORT)

    # Step 1: Create an email account
    username = input("Enter the desired email username (without domain): ")
    password = getpass("Enter the desired email password: ")
    setup.create_email_account(username, password)

    # Step 2: Send a test email
    from_email = f"{username}@yourdomain.com"
    to_email = input("Enter the recipient's email address: ")
    subject = "Test Email from iFastNet"
    body = "This is a test email to verify your email account setup."
    
    setup.send_test_email(from_email, to_email, subject, body)
```
