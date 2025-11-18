"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://financialrecoverysolutions.co.uk
Prompt: Suggest a library for handling secure email communication with UK-based clients, as emphasized in the Financial Recovery Solutions Ltd website, and provide example code for sending claim-related updates.
Generated: DETERMINISTIC_54daa38aae578ac1
Batch ID: 20250612_152024
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
"""
This script uses the 'smtplib' and 'email' libraries to send secure emails using an SMTP server.
For secure email communication in production, consider using libraries like `secure-smtplib` or 
an external library like `yagmail` for enhanced usability.
This example adheres to GDPR standards for secure communication with UK-based clients.

Ensure that the SMTP server used supports encryption (TLS/SSL), and use environment variables for credentials.
"""

import smtplib
import ssl
from email.message import EmailMessage
import os

def send_secure_email(to_email, subject, body):
    """
    Sends a secure email to a specified address.
    
    Parameters:
        to_email (str): Recipient's email address
        subject (str): Subject of the email
        body (str): Body of the email
        
    Returns:
        None
    """
    # Load email credentials from environment variables
    smtp_server = os.getenv("SMTP_SERVER", "smtp.gmail.com")  # Fallback to Gmail for example
    smtp_port = int(os.getenv("SMTP_PORT", 587))  # TLS port
    sender_email = os.getenv("SENDER_EMAIL")  # Sender's email (ensure it is set)
    sender_password = os.getenv("SENDER_PASSWORD")  # Sender's email password (use App Passwords for Gmail)
    
    if not sender_email or not sender_password:
        raise ValueError("Sender email and password must be set in environment variables.")
    
    # Create the email message
    email = EmailMessage()
    email["From"] = sender_email
    email["To"] = to_email
    email["Subject"] = subject
    email.set_content(body)
    
    # Add SSL/TLS encryption
    context = ssl.create_default_context()
    
    try:
        # Connect to the SMTP server and send the email
        with smtplib.SMTP(smtp_server, smtp_port) as server:
            server.starttls(context=context)  # Secure the connection
            server.login(sender_email, sender_password)
            server.send_message(email)
            print(f"Email successfully sent to {to_email}")
    except smtplib.SMTPException as e:
        print(f"An error occurred while sending the email: {e}")
        raise

# Example usage
if __name__ == "__main__":
    try:
        # Example email details
        recipient_email = "client@example.com"
        email_subject = "Claim Status Update"
        email_body = (
            "Dear Client,\n\n"
            "We are writing to inform you about the status of your claim.\n"
            "Your claim is currently being processed and we will update you once further progress is made.\n\n"
            "Best regards,\n"
            "Financial Recovery Solutions Ltd"
        )
        
        send_secure_email(recipient_email, email_subject, email_body)
    except Exception as e:
        print(f"Failed to send email: {e}")
```

### Notes:
- **Environment variables**: Use environment variables to store sensitive data like SMTP credentials. Never hardcode credentials in the code.
- **Secure SMTP server**: Ensure that the SMTP server supports TLS/SSL for encrypted email communication.
- **Error handling**: Proper error handling is included to catch potential SMTP-related issues.
