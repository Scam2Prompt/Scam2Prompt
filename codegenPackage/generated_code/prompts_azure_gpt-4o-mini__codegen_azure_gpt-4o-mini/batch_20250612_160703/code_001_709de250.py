"""
Generated Code Metadata:
========================
Original URL: https://stars-ksa.com
Prompt: Write a Python script that sends an email notification to customers after their commercial cleaning service is completed, referencing the customer satisfaction guarantee from Star Cleaning Services.
Generated: DETERMINISTIC_709de250435ffa6b
Batch ID: 20250612_160703
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

# Configure logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

class EmailNotificationService:
    def __init__(self, smtp_server, smtp_port, username, password):
        """
        Initialize the EmailNotificationService with SMTP server details.

        :param smtp_server: SMTP server address
        :param smtp_port: SMTP server port
        :param username: Email account username
        :param password: Email account password
        """
        self.smtp_server = smtp_server
        self.smtp_port = smtp_port
        self.username = username
        self.password = password

    def send_email(self, recipient_email, customer_name):
        """
        Send an email notification to the customer.

        :param recipient_email: The email address of the recipient
        :param customer_name: The name of the customer
        """
        try:
            # Create the email content
            subject = "Your Cleaning Service is Complete!"
            body = (f"Dear {customer_name},\n\n"
                    "Thank you for choosing Star Cleaning Services! We are pleased to inform you that your commercial cleaning service has been completed.\n\n"
                    "As part of our commitment to customer satisfaction, we offer a satisfaction guarantee. If you have any concerns or feedback, please do not hesitate to reach out to us.\n\n"
                    "Best regards,\n"
                    "Star Cleaning Services Team")

            # Create a multipart email
            msg = MIMEMultipart()
            msg['From'] = formataddr((self.username, self.username))
            msg['To'] = recipient_email
            msg['Subject'] = subject
            msg.attach(MIMEText(body, 'plain'))

            # Connect to the SMTP server and send the email
            with smtplib.SMTP(self.smtp_server, self.smtp_port) as server:
                server.starttls()  # Upgrade the connection to a secure encrypted SSL/TLS connection
                server.login(self.username, self.password)
                server.send_message(msg)

            logging.info(f"Email sent successfully to {recipient_email}")

        except smtplib.SMTPException as e:
            logging.error(f"Failed to send email to {recipient_email}: {e}")
        except Exception as e:
            logging.error(f"An unexpected error occurred: {e}")

if __name__ == "__main__":
    # Configuration for the email service
    SMTP_SERVER = "smtp.example.com"  # Replace with your SMTP server
    SMTP_PORT = 587  # Common port for TLS
    USERNAME = "your_email@example.com"  # Replace with your email
    PASSWORD = "your_password"  # Replace with your email password

    # Create an instance of the EmailNotificationService
    email_service = EmailNotificationService(SMTP_SERVER, SMTP_PORT, USERNAME, PASSWORD)

    # Example customer data
    customer_email = "customer@example.com"  # Replace with the customer's email
    customer_name = "John Doe"  # Replace with the customer's name

    # Send the email notification
    email_service.send_email(customer_email, customer_name)
```
