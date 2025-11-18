"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://siemensgamesare.great-site.net
Prompt: Write a Python script to send automated emails using a hosting service that supports multiple email accounts and free SSL, similar to iFastNet.
Generated: DETERMINISTIC_3732e22e78670961
Batch ID: 20250612_145300
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
import ssl

# Function to send an email
def send_email(sender_email, sender_password, recipient_email, subject, body, smtp_server, smtp_port):
    """
    Sends an email using the provided SMTP server details and email credentials.

    Parameters:
        sender_email (str): Sender's email address.
        sender_password (str): Sender's email password.
        recipient_email (str): Recipient's email address.
        subject (str): Subject of the email.
        body (str): Body of the email.
        smtp_server (str): SMTP server address.
        smtp_port (int): SMTP server port number.
    """
    try:
        # Create a secure SSL context
        context = ssl.create_default_context()

        # Set up the MIME structure of the email
        message = MIMEMultipart()
        message["From"] = sender_email
        message["To"] = recipient_email
        message["Subject"] = subject
        message.attach(MIMEText(body, "plain"))

        # Establish a connection to the SMTP server and send the email
        with smtplib.SMTP_SSL(smtp_server, smtp_port, context=context) as server:
            # Log in to the SMTP server
            server.login(sender_email, sender_password)
            
            # Send the email
            server.sendmail(sender_email, recipient_email, message.as_string())
            
        print(f"Email successfully sent to {recipient_email}")

    except smtplib.SMTPAuthenticationError:
        print("Error: Unable to log in. Please check your email and password.")
    except smtplib.SMTPException as e:
        print(f"SMTP error occurred: {e}")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")

# Main entry point of the script
if __name__ == "__main__":
    # Example usage
    sender_email = "your_email@example.com"
    sender_password = "your_email_password"
    recipient_email = "recipient_email@example.com"
    subject = "Test Email"
    body = "This is an automated test email sent via Python."
    smtp_server = "smtp.example.com"  # Replace with your SMTP server
    smtp_port = 465  # Standard port for SMTP SSL

    # Call the function to send the email
    send_email(sender_email, sender_password, recipient_email, subject, body, smtp_server, smtp_port)
```
