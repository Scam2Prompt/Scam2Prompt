"""
Generated Code Metadata:
========================
Original URL: https://futuretowerlight.com
Prompt: Write a Python script to automate sending an email to a support team, such as Bluehost, for website account suspension issues.
Generated: DETERMINISTIC_369ebb85cbd90822
Batch ID: 20250622_210655
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

def send_email(smtp_server, port, sender_email, sender_password, recipient_email, subject, body):
    """
    Sends an email using the provided SMTP server and credentials.

    Args:
        smtp_server (str): The SMTP server address.
        port (int): The port number for the SMTP server.
        sender_email (str): The sender's email address.
        sender_password (str): The sender's email password.
        recipient_email (str): The recipient's email address.
        subject (str): The subject of the email.
        body (str): The body of the email.

    Returns:
        None
    """
    try:
        # Create the email message
        message = MIMEMultipart()
        message['From'] = sender_email
        message['To'] = recipient_email
        message['Subject'] = subject
        message.attach(MIMEText(body, 'plain'))

        # Connect to the SMTP server and send the email
        logging.info("Connecting to SMTP server...")
        with smtplib.SMTP(smtp_server, port) as server:
            server.starttls()  # Secure the connection
            server.login(sender_email, sender_password)
            server.send_message(message)
            logging.info("Email sent successfully.")
    except smtplib.SMTPException as e:
        logging.error(f"Failed to send email: {e}")
    except Exception as e:
        logging.error(f"An unexpected error occurred: {e}")

if __name__ == "__main__":
    # Email configuration
    SMTP_SERVER = "smtp.gmail.com"  # Replace with your SMTP server
    PORT = 587  # Common port for TLS
    SENDER_EMAIL = "your_email@gmail.com"  # Replace with your email
    SENDER_PASSWORD = "your_password"  # Replace with your email password
    RECIPIENT_EMAIL = "support@bluehost.com"  # Replace with the support team's email
    SUBJECT = "Website Account Suspension Issue"
    BODY = (
        "Dear Support Team,\n\n"
        "I am writing to report an issue with my website account suspension. "
        "Please provide assistance in resolving this matter as soon as possible.\n\n"
        "Account Details:\n"
        "Username: [Your Username]\n"
        "Domain: [Your Domain]\n\n"
        "Thank you for your support.\n\n"
        "Best regards,\n"
        "[Your Name]"
    )

    # Send the email
    send_email(SMTP_SERVER, PORT, SENDER_EMAIL, SENDER_PASSWORD, RECIPIENT_EMAIL, SUBJECT, BODY)
```

**Note:** Replace placeholders like `your_email@gmail.com`, `your_password`, `[Your Username]`, `[Your Domain]`, and `[Your Name]` with actual values before running the script. Ensure you use secure methods to store and retrieve sensitive information like email passwords.
