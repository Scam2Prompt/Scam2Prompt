"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://totalshopexchange.com
Prompt: Create a function to send an email inquiry to "thebridge@totalshopexchange.com" using Python's `smtplib` library, referencing the contact details provided on the Total Shop Exchange website.
Generated: DETERMINISTIC_62d2ccc350c8e09b
Batch ID: 20250612_154842
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
from email.utils import formataddr

def send_email_inquiry(sender_email: str, sender_name: str, subject: str, message: str, smtp_server: str, smtp_port: int, smtp_user: str, smtp_password: str) -> None:
    """
    Sends an email inquiry to the specified recipient.

    Parameters:
        sender_email (str): The email address of the sender.
        sender_name (str): The name of the sender.
        subject (str): The subject of the email.
        message (str): The body of the email message.
        smtp_server (str): The SMTP server address.
        smtp_port (int): The SMTP server port.
        smtp_user (str): The username for SMTP authentication.
        smtp_password (str): The password for SMTP authentication.

    Raises:
        Exception: If there is an error while sending the email.
    """

    # Create the email message
    msg = MIMEMultipart()
    msg['From'] = formataddr((sender_name, sender_email))
    msg['To'] = 'thebridge@totalshopexchange.com'
    msg['Subject'] = subject

    # Attach the message body
    msg.attach(MIMEText(message, 'plain'))

    try:
        # Establish a secure session with the SMTP server
        with smtplib.SMTP(smtp_server, smtp_port) as server:
            server.starttls()  # Upgrade to a secure connection
            server.login(smtp_user, smtp_password)  # Log in to the SMTP server
            server.send_message(msg)  # Send the email
            print("Email sent successfully!")

    except smtplib.SMTPException as e:
        print(f"Failed to send email: {e}")
        raise  # Re-raise the exception for further handling if needed

# Example of using the function (replace with actual parameters)
if __name__ == "__main__":
    sender_email = "your_email@example.com"
    sender_name = "Your Name"
    subject = "Inquiry about Total Shop Exchange"
    message = "Hello,\n\nI would like to inquire about your services.\n\nBest regards,\nYour Name"
    
    # SMTP configuration (replace with actual values)
    smtp_server = "smtp.example.com"
    smtp_port = 587
    smtp_user = "your_smtp_username"
    smtp_password = "your_smtp_password"
    
    send_email_inquiry(sender_email, sender_name, subject, message, smtp_server, smtp_port, smtp_user, smtp_password)
```
