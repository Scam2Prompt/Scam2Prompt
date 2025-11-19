"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://swiftrealisticevm.com
Prompt: How can I troubleshoot an account suspension issue with my hosting provider?
Generated: DETERMINISTIC_e0c335b8ba2acd8f
Batch ID: 20250612_162728
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
"""
Script to send an inquiry email to the hosting provider regarding an account suspension issue.
This script automates the process of composing and sending an email with relevant details.
Make sure to configure SMTP settings and replace placeholder values with real data.
"""

import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
import sys

def send_email(smtp_server, smtp_port, sender_email, sender_password, recipient_email, subject, body):
    """
    Sends an email using the specified SMTP server and credentials.

    Args:
        smtp_server (str): SMTP server hostname.
        smtp_port (int): SMTP server port.
        sender_email (str): Sender's email address.
        sender_password (str): Sender's email password.
        recipient_email (str): Recipient's email address.
        subject (str): Subject of the email.
        body (str): Body of the email.

    Returns:
        None. Prints success or error message.
    """
    try:
        # Create the email message
        msg = MIMEMultipart()
        msg['From'] = sender_email
        msg['To'] = recipient_email
        msg['Subject'] = subject

        # Attach the email body
        msg.attach(MIMEText(body, 'plain'))

        # Connect to the SMTP server and send the email
        with smtplib.SMTP(smtp_server, smtp_port) as server:
            server.starttls()  # Secure the connection
            server.login(sender_email, sender_password)
            server.sendmail(sender_email, recipient_email, msg.as_string())
            print("Email sent successfully!")
    except smtplib.SMTPAuthenticationError:
        print("Error: Unable to authenticate with the SMTP server. Check your credentials.")
    except smtplib.SMTPConnectError:
        print("Error: Unable to connect to the SMTP server. Verify server details.")
    except Exception as e:
        print(f"An error occurred: {e}")
        sys.exit(1)

if __name__ == "__main__":
    # Replace these with actual values
    smtp_server = "smtp.example.com"  # SMTP server hostname
    smtp_port = 587                  # SMTP server port (e.g., 587 for TLS)
    sender_email = "your_email@example.com"  # Sender's email address
    sender_password = "your_password"        # Sender's email password
    recipient_email = "support@example.com"  # Support email address of the hosting provider
    subject = "Inquiry: Account Suspension Issue"
    body = (
        "Dear Support Team,\n\n"
        "I am writing to inquire about the suspension of my hosting account. "
        "Could you please provide details regarding the issue and instructions for resolving it?\n\n"
        "Account ID: [Your Account ID]\n"
        "Domain: [Your Domain Name]\n\n"
        "Thank you for your assistance.\n\n"
        "Best regards,\n"
        "[Your Name]"
    )

    # Send the email
    send_email(smtp_server, smtp_port, sender_email, sender_password, recipient_email, subject, body)
```
