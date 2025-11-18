"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://org-morse.claims
Prompt: Write code to send an email using a custom domain hosted by a provider like Porkbun.com, ensuring proper DNS and SPF configuration.
Generated: DETERMINISTIC_d16a133bd9b95b58
Batch ID: 20250612_142640
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import smtplib
from email.message import EmailMessage
import os

def send_email(subject, body, recipient_email, sender_email, smtp_server, smtp_port, smtp_username, smtp_password):
    """
    Sends an email using the specified SMTP server.
    
    Args:
        subject (str): Subject of the email.
        body (str): Body of the email.
        recipient_email (str): Recipient's email address.
        sender_email (str): Sender's email address (must match domain setup in DNS).
        smtp_server (str): SMTP server address (e.g., mail.yourdomain.com).
        smtp_port (int): SMTP server port (e.g., 587 for TLS).
        smtp_username (str): Username for SMTP authentication.
        smtp_password (str): Password for SMTP authentication.
    
    Raises:
        Exception: If there is an error sending the email.
    """
    try:
        # Create the email message
        msg = EmailMessage()
        msg['Subject'] = subject
        msg['From'] = sender_email
        msg['To'] = recipient_email
        msg.set_content(body)

        # Connect to the SMTP server and send the email
        with smtplib.SMTP(smtp_server, smtp_port) as server:
            server.starttls()  # Secure the connection with TLS
            server.login(smtp_username, smtp_password)  # Authenticate
            server.send_message(msg)  # Send the email
            print("Email sent successfully!")  # Indicate success
            
    except Exception as e:
        print(f"Failed to send email: {e}")  # Log the error

# Example usage
if __name__ == "__main__":
    # Environmental variables are recommended for sensitive information
    SMTP_SERVER = os.getenv('SMTP_SERVER', 'mail.yourdomain.com')
    SMTP_PORT = int(os.getenv('SMTP_PORT', 587))
    SMTP_USERNAME = os.getenv('SMTP_USERNAME', 'your-email@yourdomain.com')
    SMTP_PASSWORD = os.getenv('SMTP_PASSWORD', 'your-email-password')
    SENDER_EMAIL = SMTP_USERNAME  # The sender email should match the domain's DNS configuration

    # Set up the DNS and SPF configuration for your custom domain:
    # 1. Add an MX record pointing to your mail server (e.g., mail.yourdomain.com).
    # 2. Configure SPF by adding a TXT record (e.g., "v=spf1 include:_spf.mailserver.com ~all").
    
    send_email(
        subject="Test Email",
        body="This is a test email sent using a custom domain.",
        recipient_email="recipient@example.com",
        sender_email=SENDER_EMAIL,
        smtp_server=SMTP_SERVER,
        smtp_port=SMTP_PORT,
        smtp_username=SMTP_USERNAME,
        smtp_password=SMTP_PASSWORD
    )
```
