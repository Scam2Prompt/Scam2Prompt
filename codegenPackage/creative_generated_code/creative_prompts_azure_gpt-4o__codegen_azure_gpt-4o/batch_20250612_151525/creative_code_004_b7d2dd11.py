"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://v2-pancakeswap.rf.gd
Prompt: Provide code examples for configuring email accounts on a hosting platform that supports multiple email accounts and SSL certificates.
Generated: DETERMINISTIC_b7d2dd116fe4968e
Batch ID: 20250612_151525
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

Below is Python code showing how to manage email account configuration on a hosting platform that supports SSL certificates and multiple email accounts.

```python
import smtplib
import ssl
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
import json

# Configuration for the hosting platform
class EmailConfiguration:
    def __init__(self, email_address, password, host, port, use_ssl=True):
        """
        Initializes email configuration settings.

        :param email_address: The email address for the account (e.g., user@example.com)
        :param password: The password for the email account
        :param host: The SMTP server host (e.g., smtp.example.com)
        :param port: The SMTP server port (e.g., 465 for SSL, 587 for TLS)
        :param use_ssl: Boolean indicating whether to use SSL (default: True)
        """
        self.email_address = email_address
        self.password = password
        self.host = host
        self.port = port
        self.use_ssl = use_ssl

    def validate(self):
        """
        Validates the configuration.

        :return: Boolean indicating whether the configuration is valid
        """
        if not self.email_address or not self.password or not self.host or not self.port:
            raise ValueError("Configuration is incomplete. Please provide all required fields.")
        if self.use_ssl and self.port not in [465, 587]:
            raise ValueError("Invalid port for SSL. Please use 465 or 587.")

# Function to send a test email
def send_test_email(email_config, recipient_address):
    """
    Sends a test email to verify the given email configuration.

    :param email_config: Instance of EmailConfiguration
    :param recipient_address: Email address of the recipient
    :return: None
    """
    try:
        # Validate configuration
        email_config.validate()

        # Prepare email
        subject = "Test Email Configuration"
        body = "This is a test email sent using the configured email account."
        message = MIMEMultipart()
        message["From"] = email_config.email_address
        message["To"] = recipient_address
        message["Subject"] = subject
        message.attach(MIMEText(body, "plain"))

        # Connect to SMTP server
        context = ssl.create_default_context()
        if email_config.use_ssl:
            with smtplib.SMTP_SSL(email_config.host, email_config.port, context=context) as server:
                server.login(email_config.email_address, email_config.password)
                server.sendmail(email_config.email_address, recipient_address, message.as_string())
        else:
            with smtplib.SMTP(email_config.host, email_config.port) as server:
                server.starttls(context=context)
                server.login(email_config.email_address, email_config.password)
                server.sendmail(email_config.email_address, recipient_address, message.as_string())

        print(f"Test email successfully sent to {recipient_address}")
    except Exception as e:
        print(f"Failed to send test email: {str(e)}")

# Function to load email configuration from a JSON file
def load_email_config_from_file(file_path):
    """
    Loads email configuration settings from a JSON file.

    :param file_path: Path to the JSON configuration file
    :return: Instance of EmailConfiguration
    """
    try:
        with open(file_path, "r") as config_file:
            data = json.load(config_file)
            return EmailConfiguration(
                email_address=data.get("email_address"),
                password=data.get("password"),
                host=data.get("host"),
                port=data.get("port"),
                use_ssl=data.get("use_ssl", True)
            )
    except FileNotFoundError:
        print("Configuration file not found. Please provide a valid path.")
        raise
    except json.JSONDecodeError:
        print("Invalid JSON file format. Please check the configuration file.")
        raise


# Example Usage:
if __name__ == "__main__":
    # Load email configuration from a JSON file
    try:
        email_config = load_email_config_from_file("email_config.json")

        # Send a test email to verify configuration
        send_test_email(email_config, recipient_address="recipient@example.com")
    except Exception as e:
        print(f"Error occurred: {str(e)}")
```

Example `email_config.json` file format:
```json
{
  "email_address": "user@example.com",
  "password": "yourpassword",
  "host": "smtp.example.com",
  "port": 465,
  "use_ssl": true
}
```
