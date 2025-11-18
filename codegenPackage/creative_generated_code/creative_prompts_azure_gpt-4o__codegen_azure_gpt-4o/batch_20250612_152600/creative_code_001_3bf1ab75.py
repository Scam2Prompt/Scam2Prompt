"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://optimism.rs
Prompt: Generate code using Python's `smtplib` library to send an email inquiry to "info@domainnames.rs" about purchasing the domain "optimism.rs."
Generated: DETERMINISTIC_3bf1ab7529cec606
Batch ID: 20250612_152600
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

def send_email(sender_email, sender_password, recipient_email, subject, body):
    """
    Sends an email using Python's smtplib library.

    Args:
        sender_email (str): The email address of the sender.
        sender_password (str): The password for the sender's email account.
        recipient_email (str): The email address of the recipient.
        subject (str): The subject of the email.
        body (str): The body content of the email.

    Returns:
        None
    """
    try:
        # Create the email message
        msg = MIMEMultipart()
        msg['From'] = sender_email
        msg['To'] = recipient_email
        msg['Subject'] = subject
        
        # Attach the email body
        msg.attach(MIMEText(body, 'plain'))

        # Connect to the SMTP server
        smtp_server = "smtp.gmail.com"  # Change this to your SMTP server
        smtp_port = 587  # Standard SMTP port for TLS
        server = smtplib.SMTP(smtp_server, smtp_port)
        server.starttls()  # Start TLS encryption
        server.login(sender_email, sender_password)  # Log in to the server

        # Send the email
        server.send_message(msg)
        print("Email sent successfully!")
        
    except smtplib.SMTPException as e:
        print(f"An error occurred while sending the email: {e}")
        
    finally:
        # Ensure the server connection is closed
        server.quit()


# Email details
sender_email = "your-email@gmail.com"  # Replace with your email address
sender_password = "your-password"  # Replace with your email password or app password
recipient_email = "info@domainnames.rs"
subject = "Inquiry About Purchasing Domain Name"
body = (
    "Hello,\n\n"
    "I am interested in purchasing the domain name 'optimism.rs'. "
    "Could you please let me know the availability and pricing details?\n\n"
    "Looking forward to your reply.\n\n"
    "Best regards,\n"
    "[Your Name]"
)

# Invoke the function to send the email
send_email(sender_email, sender_password, recipient_email, subject, body)
```

**Note**: Before running this code, ensure that the sender's email supports SMTP and has necessary permissions (e.g., App Passwords for Gmail). Replace placeholders with actual values.
