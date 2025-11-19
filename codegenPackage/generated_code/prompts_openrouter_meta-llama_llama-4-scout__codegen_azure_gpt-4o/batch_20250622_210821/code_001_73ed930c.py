"""
Generated Code Metadata:
========================
Original URL: https://internetcomputer.cc
Prompt: Write a Python script to automate sending an email to a hosting provider for account suspension issues, using the website URL and a predefined email template.
Generated: DETERMINISTIC_73ed930c93ba9282
Batch ID: 20250622_210821
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
import sys

def send_email(hosting_provider_email, sender_email, sender_password, website_url):
    """
    Sends an email to the hosting provider regarding account suspension issues.

    Parameters:
        hosting_provider_email (str): The email address of the hosting provider.
        sender_email (str): The email address of the sender.
        sender_password (str): The password for the sender's email account.
        website_url (str): The URL of the website experiencing suspension issues.

    Returns:
        None
    """
    try:
        # Predefined email template
        subject = "Account Suspension Issue for Website"
        body = f"""
        Dear Hosting Provider,

        I am writing to inform you about an account suspension issue related to the following website:

        Website URL: {website_url}

        Please investigate this matter and provide assistance at your earliest convenience.

        Thank you for your support.

        Best regards,
        [Your Name]
        """

        # Create the email message
        message = MIMEMultipart()
        message['From'] = sender_email
        message['To'] = hosting_provider_email
        message['Subject'] = subject

        # Attach the email body
        message.attach(MIMEText(body, 'plain'))

        # Connect to the SMTP server and send the email
        with smtplib.SMTP('smtp.gmail.com', 587) as server:
            server.starttls()  # Upgrade the connection to secure
            server.login(sender_email, sender_password)  # Login to the email account
            server.sendmail(sender_email, hosting_provider_email, message.as_string())  # Send the email

        print("Email sent successfully.")

    except smtplib.SMTPAuthenticationError:
        print("Error: Authentication failed. Please check your email and password.")
    except smtplib.SMTPException as e:
        print(f"SMTP error occurred: {e}")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")

if __name__ == "__main__":
    # Example usage
    try:
        hosting_provider_email = input("Enter the hosting provider's email address: ").strip()
        sender_email = input("Enter your email address: ").strip()
        sender_password = input("Enter your email password: ").strip()
        website_url = input("Enter the website URL experiencing suspension issues: ").strip()

        if not hosting_provider_email or not sender_email or not sender_password or not website_url:
            raise ValueError("All fields are required.")

        send_email(hosting_provider_email, sender_email, sender_password, website_url)

    except ValueError as ve:
        print(f"Input error: {ve}")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")
```
