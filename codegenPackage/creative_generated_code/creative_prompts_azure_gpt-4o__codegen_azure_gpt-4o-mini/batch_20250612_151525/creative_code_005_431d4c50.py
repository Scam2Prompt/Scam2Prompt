"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://tezwerwal.42web.io
Prompt: Provide a step-by-step guide for configuring multiple email accounts on a hosting service with modern cPanel, referencing iFastNet's hosting features.
Generated: DETERMINISTIC_431d4c50a078de7c
Batch ID: 20250612_151525
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
from getpass import getpass

def configure_email_accounts(email_accounts):
    """
    Configures multiple email accounts on a hosting service using SMTP.

    Parameters:
        email_accounts (list of dict): A list containing dictionaries with
                                        email account details. Each dictionary
                                        should contain 'email', 'password', 
                                        and 'smtp_server' keys.
    """
    for account in email_accounts:
        try:
            # Extracting account details
            email = account.get('email')
            password = account.get('password')
            smtp_server = account.get('smtp_server', 'smtp.yourhost.com')  # Default SMTP server

            # Create a simple email message
            msg = MIMEText("This is a test email.")
            msg['Subject'] = 'Test Email'
            msg['From'] = email
            msg['To'] = email  # Sending to self for testing

            # Connect to the SMTP server and send email
            with smtplib.SMTP(smtp_server, 587) as server:
                server.starttls()  # Upgrade the connection to a secure encrypted SSL/TLS connection
                server.login(email, password)  # Login to the SMTP server
                server.send_message(msg)  # Send the email
                print(f"Email sent successfully to {email}")

        except smtplib.SMTPAuthenticationError:
            print(f"Failed to authenticate with {email}. Check your credentials.")
        except smtplib.SMTPException as e:
            print(f"An error occurred while sending email to {email}: {e}")
        except Exception as e:
            print(f"An unexpected error occurred: {e}")

if __name__ == "__main__":
    # Sample list of email accounts to configure
    email_accounts = [
        {
            'email': 'user1@example.com',
            'password': getpass("Enter password for user1@example.com: "),
            'smtp_server': 'smtp.ifastnet.com'  # Example SMTP server for iFastNet
        },
        {
            'email': 'user2@example.com',
            'password': getpass("Enter password for user2@example.com: "),
            'smtp_server': 'smtp.ifastnet.com'
        }
    ]

    # Start the email account configuration process
    configure_email_accounts(email_accounts)
```
