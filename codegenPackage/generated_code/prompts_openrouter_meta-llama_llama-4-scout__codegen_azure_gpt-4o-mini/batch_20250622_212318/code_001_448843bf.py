"""
Generated Code Metadata:
========================
Original URL: https://thealgotech.com
Prompt: Generate a Python script to automate the process of sending an inquiry email to a hosting provider about a suspended website account.
Generated: DETERMINISTIC_448843bfd73f84af
Batch ID: 20250622_212318
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
import logging

# Configure logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

def send_inquiry_email(smtp_server, smtp_port, sender_email, sender_password, recipient_email):
    """
    Sends an inquiry email to the hosting provider regarding a suspended website account.

    Parameters:
        smtp_server (str): The SMTP server address.
        smtp_port (int): The port number for the SMTP server.
        sender_email (str): The email address of the sender.
        sender_password (str): The password for the sender's email account.
        recipient_email (str): The email address of the recipient (hosting provider).

    Raises:
        Exception: If there is an error sending the email.
    """
    # Create the email content
    subject = "Inquiry About Suspended Website Account"
    body = (
        "Dear Hosting Provider,\n\n"
        "I am writing to inquire about the status of my website account, which has been suspended. "
        "Could you please provide me with details regarding the suspension and the steps I need to take to resolve this issue?\n\n"
        "Thank you for your assistance.\n\n"
        "Best regards,\n"
        "Your Name\n"
        "Your Contact Information"
    )

    # Create a multipart email message
    msg = MIMEMultipart()
    msg['From'] = sender_email
    msg['To'] = recipient_email
    msg['Subject'] = subject

    # Attach the email body to the message
    msg.attach(MIMEText(body, 'plain'))

    try:
        # Connect to the SMTP server
        with smtplib.SMTP(smtp_server, smtp_port) as server:
            server.starttls()  # Upgrade the connection to a secure encrypted SSL/TLS connection
            server.login(sender_email, sender_password)  # Log in to the email account
            server.send_message(msg)  # Send the email
            logging.info("Inquiry email sent successfully to %s", recipient_email)
    except Exception as e:
        logging.error("Failed to send email: %s", e)
        raise  # Re-raise the exception for further handling if needed

if __name__ == "__main__":
    # Configuration for the email
    SMTP_SERVER = "smtp.example.com"  # Replace with your SMTP server
    SMTP_PORT = 587  # Common port for TLS
    SENDER_EMAIL = "your_email@example.com"  # Replace with your email
    SENDER_PASSWORD = "your_password"  # Replace with your email password
    RECIPIENT_EMAIL = "support@hostingprovider.com"  # Replace with the hosting provider's email

    # Send the inquiry email
    send_inquiry_email(SMTP_SERVER, SMTP_PORT, SENDER_EMAIL, SENDER_PASSWORD, RECIPIENT_EMAIL)
```
