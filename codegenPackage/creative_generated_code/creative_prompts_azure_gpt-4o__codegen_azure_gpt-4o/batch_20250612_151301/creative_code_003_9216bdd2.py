"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://airdropbtc.epizy.com
Prompt: Create a Python script to configure email accounts on a hosting platform that supports multiple email accounts and provides free SSL, similar to iFastNet's hosting services.
Generated: DETERMINISTIC_9216bdd2f0a1fc0c
Batch ID: 20250612_151301
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import os
import re
import smtplib
import ssl
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

def validate_email(email):
    """
    Validate an email address using regex.
    :param email: str - Email address to validate.
    :return: bool - True if valid, False otherwise.
    """
    email_regex = r'^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$'
    return re.match(email_regex, email) is not None

def create_email_account(email, password, hosting_provider):
    """
    Simulate the creation of an email account on a hosting platform.
    :param email: str - The email address to create.
    :param password: str - Password for the email account.
    :param hosting_provider: str - Hosting platform name.
    :return: bool - True if account created successfully, False otherwise.
    """
    try:
        # Validate email
        if not validate_email(email):
            print(f"Error: '{email}' is not a valid email address.")
            return False
        
        # Validate password strength
        if len(password) < 8:
            print("Error: Password must be at least 8 characters long.")
            return False

        # Simulate account creation (replace with actual API calls if available)
        print(f"Creating email account '{email}' on hosting provider '{hosting_provider}'...")
        # Example: Call hosting platform's API to create the email account
        # Hosting API integration code would go here

        print("Account created successfully!")
        return True
    except Exception as e:
        print(f"An error occurred while creating the email account: {e}")
        return False

def send_welcome_email(email, smtp_server, smtp_port, sender_email, sender_password):
    """
    Send a welcome email to the newly created email account.
    :param email: str - Recipient email address.
    :param smtp_server: str - SMTP server address.
    :param smtp_port: int - SMTP server port.
    :param sender_email: str - Sender email address.
    :param sender_password: str - Sender email password.
    :return: bool - True if email sent successfully, False otherwise.
    """
    try:
        # Create the email message
        message = MIMEMultipart("alternative")
        message["Subject"] = "Welcome to Your New Email Account"
        message["From"] = sender_email
        message["To"] = email

        # Email body
        text = f"Hello,\n\nYour email account '{email}' has been successfully created.\nEnjoy our services!\n\nBest regards,\nYour Hosting Provider"
        html = f"""
        <html>
            <body>
                <p>Hello,<br><br>
                Your email account <b>{email}</b> has been successfully created.<br>
                Enjoy our services!<br><br>
                Best regards,<br>
                Your Hosting Provider
                </p>
            </body>
        </html>
        """
        # Attach both plain text and HTML versions
        message.attach(MIMEText(text, "plain"))
        message.attach(MIMEText(html, "html"))

        # Send the email
        context = ssl.create_default_context()
        with smtplib.SMTP_SSL(smtp_server, smtp_port, context=context) as server:
            server.login(sender_email, sender_password)
            server.sendmail(sender_email, email, message.as_string())
        
        print(f"Welcome email sent successfully to '{email}'.")
        return True
    except Exception as e:
        print(f"Error sending welcome email to '{email}': {e}")
        return False

if __name__ == "__main__":
    # Configuration (replace with real credentials in production)
    hosting_provider = "ExampleHosting"
    smtp_server = "smtp.example.com"
    smtp_port = 465
    sender_email = "admin@example.com"
    sender_password = os.getenv("SENDER_EMAIL_PASSWORD", "password123")  # Fetch from environment variables for security

    # Input email setup details
    new_email = input("Enter the new email address to create: ")
    new_password = input("Enter a password for the new email account: ")

    # Create the email account
    if create_email_account(new_email, new_password, hosting_provider):
        # Send a welcome email
        send_welcome_email(new_email, smtp_server, smtp_port, sender_email, sender_password)
```

Note: Make sure to replace placeholder values (e.g., hosting provider name, SMTP server settings, sender email credentials) with actual data for your production environment. Also, secure sensitive information like passwords using environment variables or secure vaults.
