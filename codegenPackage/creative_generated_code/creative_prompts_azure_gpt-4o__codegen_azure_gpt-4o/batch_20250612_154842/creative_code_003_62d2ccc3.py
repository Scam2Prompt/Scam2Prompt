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
import logging

# Configure logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

def send_email_inquiry(sender_email, sender_password, subject, message_body):
    """
    Sends an email inquiry to 'thebridge@totalshopexchange.com' using the provided sender credentials.

    Parameters:
    sender_email (str): The sender's email address.
    sender_password (str): The sender's email password (or app-specific password if applicable).
    subject (str): The subject of the email.
    message_body (str): The body content of the email.

    Returns:
    bool: True if the email was sent successfully, False otherwise.
    """
    # Recipient email address
    recipient_email = "thebridge@totalshopexchange.com"

    try:
        # Create the email message
        msg = MIMEMultipart()
        msg['From'] = sender_email
        msg['To'] = recipient_email
        msg['Subject'] = subject

        # Attach the message body
        msg.attach(MIMEText(message_body, 'plain'))

        # Connect to the SMTP server
        logging.info("Connecting to the SMTP server...")
        with smtplib.SMTP('smtp.gmail.com', 587) as server:  # Adjust the server and port if using a different provider
            server.starttls()  # Upgrade the connection to secure (TLS)
            logging.info("Logging into the SMTP server...")
            server.login(sender_email, sender_password)  # Log in using the sender's credentials
            
            # Send the email
            logging.info("Sending the email...")
            server.send_message(msg)

        logging.info("Email sent successfully.")
        return True

    except smtplib.SMTPException as e:
        logging.error(f"Failed to send email. SMTP exception occurred: {e}")
        return False

    except Exception as e:
        logging.error(f"An unexpected error occurred: {e}")
        return False


# Example usage
if __name__ == "__main__":
    # Replace with valid credentials and content before running in production
    sender_email = "your_email@example.com"
    sender_password = "your_password"
    subject = "Inquiry from Total Shop Exchange Website"
    message_body = "Hello, I would like to inquire about your services. Please get back to me at your earliest convenience."

    if send_email_inquiry(sender_email, sender_password, subject, message_body):
        print("Email sent successfully.")
    else:
        print("Failed to send email.")
```
