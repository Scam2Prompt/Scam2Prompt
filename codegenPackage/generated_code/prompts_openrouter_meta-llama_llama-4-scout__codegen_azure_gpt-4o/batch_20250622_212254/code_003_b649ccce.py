"""
Generated Code Metadata:
========================
Original URL: https://khaleeji.com
Prompt: How can I use a library like Python's `smtplib` to handle email inquiries for a domain sale listing, similar to the contact information provided for khaleeji.com?
Generated: DETERMINISTIC_b649ccce22c99d2b
Batch ID: 20250622_212254
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
from email.utils import formataddr
import logging

# Configure logging for error tracking
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

# Email configuration
SMTP_SERVER = "smtp.gmail.com"  # Replace with your SMTP server
SMTP_PORT = 587  # Standard port for TLS
EMAIL_ADDRESS = "your_email@example.com"  # Replace with your email address
EMAIL_PASSWORD = "your_password"  # Replace with your email password (use environment variables in production)
RECIPIENT_EMAIL = "recipient@example.com"  # Replace with the recipient's email address

def send_inquiry_email(sender_name, sender_email, message_body):
    """
    Sends an email inquiry for a domain sale listing.

    Args:
        sender_name (str): Name of the sender.
        sender_email (str): Email address of the sender.
        message_body (str): The message content from the sender.

    Returns:
        bool: True if the email was sent successfully, False otherwise.
    """
    try:
        # Create the email message
        msg = MIMEMultipart()
        msg['From'] = formataddr((sender_name, sender_email))
        msg['To'] = RECIPIENT_EMAIL
        msg['Subject'] = "Domain Sale Inquiry"

        # Email body
        body = f"""
        You have received a new inquiry for your domain sale listing.

        Sender Name: {sender_name}
        Sender Email: {sender_email}

        Message:
        {message_body}
        """
        msg.attach(MIMEText(body, 'plain'))

        # Connect to the SMTP server and send the email
        with smtplib.SMTP(SMTP_SERVER, SMTP_PORT) as server:
            server.starttls()  # Upgrade the connection to a secure encrypted SSL/TLS connection
            server.login(EMAIL_ADDRESS, EMAIL_PASSWORD)  # Login to the SMTP server
            server.sendmail(EMAIL_ADDRESS, RECIPIENT_EMAIL, msg.as_string())  # Send the email

        logging.info("Email sent successfully.")
        return True

    except smtplib.SMTPException as e:
        logging.error(f"Failed to send email: {e}")
        return False
    except Exception as e:
        logging.error(f"An unexpected error occurred: {e}")
        return False

# Example usage
if __name__ == "__main__":
    # Replace these with actual input values
    sender_name = "John Doe"
    sender_email = "johndoe@example.com"
    message_body = "I am interested in purchasing your domain. Please let me know the price."

    if send_inquiry_email(sender_name, sender_email, message_body):
        print("Inquiry email sent successfully.")
    else:
        print("Failed to send inquiry email.")
```

### Notes:
- Replace placeholder values (e.g., `your_email@example.com`, `your_password`) with actual credentials or use environment variables for better security.
- Ensure that "Allow less secure apps" is enabled for the email account if using Gmail, or configure an app password for enhanced security.
- Avoid hardcoding sensitive information in production; use environment variables or a secure secrets manager.
