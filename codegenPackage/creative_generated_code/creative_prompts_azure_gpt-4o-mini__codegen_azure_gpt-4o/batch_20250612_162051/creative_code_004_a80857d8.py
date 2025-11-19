"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://lifegracehospital.com
Prompt: Write a Python function to automate sending an email to info@lifegracehospital.com for appointment inquiries.
Generated: DETERMINISTIC_a80857d86bcff0db
Batch ID: 20250612_162051
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

# Configure logging for error handling and debugging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

def send_email(subject: str, body: str, to_email: str = "info@lifegracehospital.com") -> bool:
    """
    Sends an email to the specified recipient address for appointment inquiries.

    Args:
        subject (str): The subject of the email.
        body (str): The body content of the email.
        to_email (str): The recipient's email address (default: info@lifegracehospital.com).

    Returns:
        bool: Returns True if the email is sent successfully, otherwise False.
    """
    # Define SMTP configuration
    smtp_server = "smtp.gmail.com"  # Replace with your SMTP server
    smtp_port = 587                 # SMTP port for TLS
    sender_email = "your_email@gmail.com"  # Replace with your email address
    sender_password = "your_password"      # Replace with your email password

    try:
        # Create the email headers and body
        message = MIMEMultipart()
        message["From"] = sender_email
        message["To"] = to_email
        message["Subject"] = subject

        # Add the email body
        message.attach(MIMEText(body, "plain"))

        # Connect to the SMTP server and send the email
        with smtplib.SMTP(smtp_server, smtp_port) as server:
            server.starttls()  # Secure the connection using TLS
            server.login(sender_email, sender_password)  # Login to the SMTP server
            server.sendmail(sender_email, to_email, message.as_string())  # Send the email

        logging.info("Email sent successfully to %s", to_email)
        return True

    except smtplib.SMTPException as e:
        logging.error("Failed to send email: %s", str(e))
        return False

# Example usage
if __name__ == "__main__":
    subject = "Appointment Inquiry"
    body = "Dear Life Grace Hospital,\n\nI would like to inquire about available appointment slots.\n\nThank you."
    if send_email(subject, body):
        print("Email sent successfully.")
    else:
        print("Failed to send email.")
```

> **Notes**: Replace the `sender_email` and `sender_password` with actual credentials. Consider using environment variables or a secrets manager to store sensitive information instead of hardcoding them into the script.
