"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://dapps-walletconnet-validation.rf.gd
Prompt: Write code to configure email accounts for a hosting service that allows multiple email accounts and offers free SSL certificates, referencing iFastNet's features.
Generated: DETERMINISTIC_22f4bb0ff20dfb42
Batch ID: 20250612_145924
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import subprocess
import smtplib
import ssl
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

class EmailAccountManager:
    """
    Class to manage email account creation and configuration,
    including SSL certificate setup for a hosting service.
    """
    def __init__(self, domain, smtp_server, port, admin_email, admin_password):
        self.domain = domain
        self.smtp_server = smtp_server
        self.port = port
        self.admin_email = admin_email
        self.admin_password = admin_password

    def create_email_account(self, username, password):
        """
        Creates an email account on the hosting service.

        :param username: Desired username (e.g. 'user')
        :param password: Password for the email account
        :return: True if account creation is successful, False otherwise
        """
        try:
            # Here, use a hosting provider's API or system commands to create the email account.
            # For example, using a hypothetical CLI command:
            command = f"create-email --domain {self.domain} --username {username} --password {password}"
            
            # Execute the command
            result = subprocess.run(command, shell=True, check=True, text=True, capture_output=True)
            
            # Log the successful creation of the account
            print(f"Account '{username}@{self.domain}' created successfully.")
            return True
        
        except subprocess.CalledProcessError as e:
            # Handle errors in account creation
            print(f"Failed to create email account '{username}@{self.domain}'. Error: {e.stderr}")
            return False

    def send_email(self, recipient_email, subject, message_body):
        """
        Sends an email using the configured SMTP server.

        :param recipient_email: Recipient email address
        :param subject: Subject of the email
        :param message_body: Body of the email
        :return: None
        """
        try:
            # Set up the MIME structure of the email
            msg = MIMEMultipart()
            msg["From"] = self.admin_email
            msg["To"] = recipient_email
            msg["Subject"] = subject
            msg.attach(MIMEText(message_body, "plain"))

            # Establish a secure connection to the SMTP server
            context = ssl.create_default_context()
            with smtplib.SMTP_SSL(self.smtp_server, self.port, context=context) as server:
                # Log in to the server
                server.login(self.admin_email, self.admin_password)
                
                # Send the email
                server.sendmail(self.admin_email, recipient_email, msg.as_string())
                print(f"Email sent successfully to {recipient_email}.")
        
        except smtplib.SMTPException as e:
            # Handle SMTP-related errors
            print(f"Failed to send email to {recipient_email}. Error: {e}")

    def configure_ssl(self):
        """
        Configures free SSL certificates for the domain using Let's Encrypt or provider's API.

        :return: True if SSL configuration is successful, False otherwise
        """
        try:
            # Hypothetical command to generate SSL certificates using Let's Encrypt
            command = f"certbot --non-interactive --agree-tos --email {self.admin_email} --domain {self.domain} --deploy-hook 'restart-server'"
            
            # Execute the SSL configuration command
            result = subprocess.run(command, shell=True, check=True, text=True, capture_output=True)
            
            # Log the successful SSL configuration
            print(f"SSL certificate configured successfully for {self.domain}.")
            return True
        
        except subprocess.CalledProcessError as e:
            # Handle errors in SSL configuration
            print(f"Failed to configure SSL for {self.domain}. Error: {e.stderr}")
            return False


# Example usage:
if __name__ == "__main__":
    # Instantiate the manager with domain and admin credentials
    manager = EmailAccountManager(
        domain="example.com",
        smtp_server="smtp.example.com",
        port=465,
        admin_email="admin@example.com",
        admin_password="securepassword"
    )
    
    # Create a new email account
    manager.create_email_account("newuser", "newpassword123")
    
    # Send a test email
    manager.send_email("recipient@example.com", "Test Subject", "This is a test email.")
    
    # Configure free SSL certificates
    manager.configure_ssl()
```
