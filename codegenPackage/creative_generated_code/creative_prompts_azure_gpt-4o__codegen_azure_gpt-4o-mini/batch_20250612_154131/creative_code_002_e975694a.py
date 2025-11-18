"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://ajrobloxgfx.org
Prompt: Generate a Python script to send an email inquiry to [email protected] about customizing a "Front facing" Roblox profile picture.
Generated: DETERMINISTIC_e975694a58f3c67b
Batch ID: 20250612_154131
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
from email.mime.image import MIMEImage
import os

# Email configuration
SMTP_SERVER = 'smtp.example.com'  # Replace with your SMTP server
SMTP_PORT = 587  # Commonly used port for SMTP
SENDER_EMAIL = 'your_email@example.com'  # Replace with your email
SENDER_PASSWORD = 'your_password'  # Replace with your email password
RECIPIENT_EMAIL = 'inquiry@example.com'  # The recipient's email address

def send_email(subject: str, body: str, recipient: str):
    """
    Sends an email with the specified subject and body to the given recipient.

    Parameters:
        subject (str): The subject line of the email.
        body (str): The body content of the email.
        recipient (str): The email address of the recipient.

    Raises:
        Exception: If sending the email fails.
    """
    try:
        # Create a multipart email message
        msg = MIMEMultipart()
        msg['From'] = SENDER_EMAIL
        msg['To'] = recipient
        msg['Subject'] = subject

        # Attach the email body
        msg.attach(MIMEText(body, 'plain'))

        # Connect to the SMTP server and send the email
        with smtplib.SMTP(SMTP_SERVER, SMTP_PORT) as server:
            server.starttls()  # Upgrade the connection to a secure encrypted SSL/TLS connection
            server.login(SENDER_EMAIL, SENDER_PASSWORD)  # Log in to the email server
            server.send_message(msg)  # Send the email

        print("Email sent successfully.")
    
    except Exception as e:
        print(f"Failed to send email: {e}")

def main():
    # Email content
    subject = "Inquiry about Customizing Roblox Profile Picture"
    body = (
        "Dear Roblox Support,\n\n"
        "I am writing to inquire about the possibility of customizing a 'Front facing' profile picture "
        "for my Roblox account. I would like to know the options available and any requirements needed to proceed.\n\n"
        "Thank you for your assistance.\n\n"
        "Best regards,\n"
        "Your Name"  # Replace with your name
    )

    # Send the email
    send_email(subject, body, RECIPIENT_EMAIL)

if __name__ == '__main__':
    main()
```

**Note:** Make sure to replace the placeholders with your actual SMTP server details, email address, and password. Additionally, consider using environment variables or a configuration file to handle sensitive information like email credentials securely in production.
