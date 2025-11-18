"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://connectdappweb.rf.gd
Prompt: Provide code examples for setting up email accounts on a hosting service that supports multiple email accounts and modern cPanel, similar to iFastNet's offerings.
Generated: DETERMINISTIC_031ccfde7e02e34a
Batch ID: 20250612_151119
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

class EmailAccountManager:
    """A class to manage email account creation and configuration on a hosting service."""

    def __init__(self, smtp_server, smtp_port, admin_email, admin_password):
        """
        Initializes the EmailAccountManager with SMTP server details.

        Parameters:
        smtp_server (str): The SMTP server address.
        smtp_port (int): The SMTP server port.
        admin_email (str): The email address of the admin.
        admin_password (str): The password for the admin email account.
        """
        self.smtp_server = smtp_server
        self.smtp_port = smtp_port
        self.admin_email = admin_email
        self.admin_password = admin_password

    def send_email(self, recipient_email, subject, body):
        """
        Sends an email to the specified recipient.

        Parameters:
        recipient_email (str): The recipient's email address.
        subject (str): The subject of the email.
        body (str): The body content of the email.

        Raises:
        Exception: If sending the email fails.
        """
        try:
            # Create the email message
            msg = MIMEMultipart()
            msg['From'] = self.admin_email
            msg['To'] = recipient_email
            msg['Subject'] = subject
            msg.attach(MIMEText(body, 'plain'))

            # Connect to the SMTP server and send the email
            with smtplib.SMTP(self.smtp_server, self.smtp_port) as server:
                server.starttls()  # Secure the connection
                server.login(self.admin_email, self.admin_password)
                server.send_message(msg)

            print(f"Email sent successfully to {recipient_email}.")

        except smtplib.SMTPException as e:
            print(f"Error occurred while sending email: {e}")
            raise

    def create_email_account(self, new_email, new_password):
        """
        Placeholder method for creating a new email account.
        In an actual implementation, this would interface with the hosting provider's API.

        Parameters:
        new_email (str): The new email account to create.
        new_password (str): The password for the new email account.

        Raises:
        NotImplementedError: This method needs to be implemented.
        """
        raise NotImplementedError("This method should interface with the hosting service API.")

# Example usage
if __name__ == "__main__":
    # Define SMTP server details (example for illustrative purposes)
    SMTP_SERVER = "smtp.example.com"
    SMTP_PORT = 587
    ADMIN_EMAIL = "admin@example.com"
    ADMIN_PASSWORD = "your_admin_password"

    # Create an instance of EmailAccountManager
    email_manager = EmailAccountManager(SMTP_SERVER, SMTP_PORT, ADMIN_EMAIL, ADMIN_PASSWORD)

    # Example of sending an email
    try:
        email_manager.send_email("user@example.com", "Welcome!", "Your email account has been set up.")
    except Exception as e:
        print(f"Failed to send email: {e}")

    # Example of creating an email account
    try:
        # email_manager.create_email_account("user@example.com", "user_password")  # Uncomment when implemented
        pass
    except NotImplementedError as e:
        print(e)
```
