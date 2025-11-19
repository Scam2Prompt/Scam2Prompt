"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://audifree.duckdns.org
Prompt: Generate a code snippet that demonstrates how to use LuFix.to Sender to create a message with dynamic email user and domain variables.
Generated: DETERMINISTIC_8a8056d6e817ef24
Batch ID: 20250612_155845
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
# Required Libraries
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

def send_email(user, domain, recipient_email, subject, message_body):
    """
    Sends an email dynamically using the given user and domain variables.
    
    Parameters:
        user (str): The email username (e.g., 'john.doe').
        domain (str): The email domain (e.g., 'example.com').
        recipient_email (str): The receiver's email address.
        subject (str): The subject of the email.
        message_body (str): The body content of the email.
    
    Returns:
        None
        
    Raises:
        Exception: If the email fails to send.
    """
    try:
        # Construct sender email dynamically
        sender_email = f"{user}@{domain}"

        # SMTP server configuration (assuming standard Gmail SMTP here)
        smtp_server = "smtp.gmail.com"
        smtp_port = 587

        # Create the email object
        msg = MIMEMultipart()
        msg['From'] = sender_email
        msg['To'] = recipient_email
        msg['Subject'] = subject

        # Attach message body
        msg.attach(MIMEText(message_body, 'plain'))

        # Prompt for sender's email credentials
        print(f"Connecting to SMTP server for {sender_email}...")
        sender_password = input(f"Enter password for {sender_email}: ")

        # Establish connection to SMTP server
        with smtplib.SMTP(smtp_server, smtp_port) as server:
            server.starttls()  # Enable secure connection
            server.login(sender_email, sender_password)  # Login using sender's credentials
            server.sendmail(sender_email, recipient_email, msg.as_string())  # Send email

        print(f"Email successfully sent from {sender_email} to {recipient_email}.")

    except Exception as e:
        print(f"Error occurred while sending email: {e}")
        raise  # Raise exception to ensure proper error handling in production use

# Example usage:
if __name__ == "__main__":
    # Dynamic variables
    email_user = "john.doe"  # Replace with the actual user
    email_domain = "example.com"  # Replace with the actual domain
    recipient = "recipient@example.com"  # Replace with recipient's email
    email_subject = "Dynamic Email Test"
    email_body = "Hello! This is a dynamically generated email."

    # Send the email
    send_email(email_user, email_domain, recipient, email_subject, email_body)
```
