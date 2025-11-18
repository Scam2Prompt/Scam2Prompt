"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://curaheridas.com
Prompt: Create a Python script to send automated email notifications to customers about new arrivals in categories like "Apositos" and "Cicatrizantes" on a wound care product website.
Generated: DETERMINISTIC_74b83f90f267e479
Batch ID: 20250612_152426
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
import logging

# Configure logging for the application
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

class EmailNotification:
    def __init__(self, smtp_server, smtp_port, username, password):
        """
        Initialize the EmailNotification class with SMTP server details.

        Args:
            smtp_server (str): The SMTP server address.
            smtp_port (int): The port to use for the SMTP server.
            username (str): The SMTP username.
            password (str): The SMTP password.
        """
        self.smtp_server = smtp_server
        self.smtp_port = smtp_port
        self.username = username
        self.password = password

    def send_email(self, recipient_email, subject, body):
        """
        Send an email to the specified recipient.

        Args:
            recipient_email (str): The recipient's email address.
            subject (str): The subject of the email.
            body (str): The body of the email.

        Raises:
            Exception: Raises exception if the email could not be sent.
        """
        try:
            # Create a multipart email message
            msg = MIMEMultipart()
            msg['From'] = self.username
            msg['To'] = recipient_email
            msg['Subject'] = subject
            
            # Attach the email body
            msg.attach(MIMEText(body, 'plain'))

            # Establish a secure session with the server
            with smtplib.SMTP(self.smtp_server, self.smtp_port) as server:
                server.starttls()  # Upgrade to secure connection
                server.login(self.username, self.password)  # Log in to the server
                server.send_message(msg)  # Send the email
            
            logging.info(f"Email sent successfully to {recipient_email}")

        except Exception as e:
            logging.error(f"Failed to send email to {recipient_email}: {e}")
            raise

def create_email_body(new_arrivals):
    """
    Create the email body content listing new arrivals.

    Args:
        new_arrivals (list): A list of new arrival product names.

    Returns:
        str: The formatted email body.
    """
    body = "Hello,\n\nWe are excited to inform you about our new arrivals in the following categories:\n\n"
    body += "\n".join(new_arrivals)
    body += "\n\nBest regards,\nWound Care Team"
    return body

def main():
    # Email configuration
    smtp_server = 'smtp.example.com'  # Replace with your SMTP server
    smtp_port = 587  # Common port for TLS
    username = 'your_email@example.com'  # Replace with your email
    password = 'your_password'  # Replace with your email password

    # Create an instance of EmailNotification
    email_notifier = EmailNotification(smtp_server, smtp_port, username, password)

    # New arrivals in specific categories
    new_arrivals = ["Aposito Super Absorbente", "Cicatrizante Avançado", "Aposito Hidrocolóide"]
    
    # Email subject
    subject = "New Arrivals in Wound Care Products"

    # Sample recipient email (this would typically be retrieved from a database)
    recipient_email = 'customer@example.com'  # Replace with the actual customer email

    # Create the email body
    email_body = create_email_body(new_arrivals)

    # Send the email notification
    email_notifier.send_email(recipient_email, subject, email_body)

if __name__ == "__main__":
    main()
```
