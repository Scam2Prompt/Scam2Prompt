"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://webautomigrate.hstn.me
Prompt: Create a guide for setting up email accounts on a hosting platform with multiple email account support and modern cPanel, such as iFastNet.
Generated: DETERMINISTIC_e81b40fe2fb6b438
Batch ID: 20250612_145213
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
import logging

# Configure logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

class EmailAccountSetup:
    """Class to handle the setup of email accounts on a hosting platform."""
    
    def __init__(self, host, port, username, password):
        """
        Initializes the EmailAccountSetup instance.
        
        :param host: The SMTP server host
        :param port: The SMTP server port
        :param username: The username for the email account
        :param password: The password for the email account
        """
        self.host = host
        self.port = port
        self.username = username
        self.password = password

    def create_email_account(self, new_email, new_password):
        """
        Creates a new email account on the hosting platform.

        :param new_email: The email address to be created
        :param new_password: The password for the new email account
        :raises Exception: If there is an issue during setup
        """
        try:
            # Here you would typically have API calls to the hosting platform
            # For demonstration purposes, we're just logging the action
            logging.info(f"Creating email account: {new_email}")
            # Simulating API call to create account (Replace with actual API logic)
            self._simulate_account_creation(new_email, new_password)
            logging.info(f"Email account {new_email} created successfully.")
        except Exception as e:
            logging.error(f"Failed to create email account {new_email}: {e}")
            raise

    def _simulate_account_creation(self, new_email, new_password):
        """Simulate the creation of an email account (replace with actual API logic)."""
        # Simulating potential failure
        if "fail" in new_email:
            raise ValueError("Simulated account creation failure.")

    def send_test_email(self, to_email):
        """
        Sends a test email to the specified address.

        :param to_email: The recipient email address
        :raises Exception: If sending the email fails
        """
        try:
            logging.info(f"Sending test email to: {to_email}")
            msg = MIMEMultipart()
            msg['From'] = self.username
            msg['To'] = to_email
            msg['Subject'] = "Test Email"
            body = "This is a test email from your new email account."
            msg.attach(MIMEText(body, 'plain'))

            # Establish connection and send email
            with smtplib.SMTP(self.host, self.port) as server:
                server.starttls()  # Upgrade the connection to secure
                server.login(self.username, self.password)
                server.sendmail(self.username, to_email, msg.as_string())
            logging.info("Test email sent successfully.")
        except Exception as e:
            logging.error(f"Failed to send test email to {to_email}: {e}")
            raise

# Example usage:
if __name__ == "__main__":
    # Replace with your SMTP server details
    smtp_host = "smtp.example.com"
    smtp_port = 587
    smtp_username = "your_email@example.com"
    smtp_password = "your_password"

    email_setup = EmailAccountSetup(smtp_host, smtp_port, smtp_username, smtp_password)

    # Create a new email account
    try:
        email_setup.create_email_account("new_user@example.com", "new_password123")
        # Send a test email
        email_setup.send_test_email("recipient@example.com")
    except Exception as e:
        logging.error(f"An error occurred: {e}")
```
