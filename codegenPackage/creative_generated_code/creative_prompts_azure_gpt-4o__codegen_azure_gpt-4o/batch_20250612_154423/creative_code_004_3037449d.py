"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://rectifywallet.42web.io
Prompt: Create a script to configure email accounts on a hosting platform that supports multiple email accounts and provides SSL certificates.
Generated: DETERMINISTIC_3037449d9cd181a9
Batch ID: 20250612_154423
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import smtplib
import ssl
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
import os

class EmailConfigError(Exception):
    """Custom exception for email configuration errors."""
    pass

def configure_email_account(email_address, password, smtp_server, smtp_port, enable_ssl=True):
    """
    Configures an email account on a hosting platform.
    
    Args:
        email_address (str): The email address to configure.
        password (str): The password for the email account.
        smtp_server (str): The SMTP server of the hosting platform.
        smtp_port (int): The SMTP server port.
        enable_ssl (bool): Whether to enable SSL for the email account. Default is True.

    Returns:
        str: Success message if configuration is successful.

    Raises:
        EmailConfigError: If configuration fails.
    """
    try:
        # Validate email address format
        if '@' not in email_address or '.' not in email_address.split('@')[1]:
            raise EmailConfigError("Invalid email address format.")

        # Validate that SMTP port is numeric and within valid range
        if not (0 < smtp_port < 65536):
            raise EmailConfigError("Invalid SMTP port number.")

        # Establish connection
        context = ssl.create_default_context() if enable_ssl else None
        connection = smtplib.SMTP(smtp_server, smtp_port)
        
        if enable_ssl:
            connection.starttls(context=context)
        
        # Authenticate
        connection.login(email_address, password)

        # Send a test email to verify configuration
        test_message = MIMEMultipart()
        test_message["From"] = email_address
        test_message["To"] = email_address
        test_message["Subject"] = "Test Email Configuration"
        body = "This is a test email to verify email configuration."
        test_message.attach(MIMEText(body, "plain"))
        connection.sendmail(email_address, email_address, test_message.as_string())
        
        # Close connection
        connection.quit()

        return f"Email account {email_address} configured successfully."
        
    except smtplib.SMTPAuthenticationError:
        raise EmailConfigError("Authentication failed. Please check your email and password.")
    except smtplib.SMTPConnectError:
        raise EmailConfigError("Failed to connect to the SMTP server. Please check server details.")
    except Exception as e:
        raise EmailConfigError(f"An error occurred during email configuration: {str(e)}")

if __name__ == "__main__":
    # Example usage of the script
    try:
        email = "user@example.com"
        password = os.environ.get("EMAIL_PASSWORD")  # Load password from environment variable for security
        smtp_server = "smtp.example.com"
        smtp_port = 587  # Common SMTP port for TLS
        enable_ssl = True
        
        result = configure_email_account(email, password, smtp_server, smtp_port, enable_ssl)
        print(result)
    except EmailConfigError as e:
        print(f"Error: {e}")
```
