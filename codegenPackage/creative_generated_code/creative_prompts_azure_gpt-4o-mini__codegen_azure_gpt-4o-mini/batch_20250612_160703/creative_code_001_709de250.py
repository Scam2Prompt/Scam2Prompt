"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://stars-ksa.com
Prompt: Write a Python script that sends an email notification to customers after their commercial cleaning service is completed, referencing the customer satisfaction guarantee from Star Cleaning Services.
Generated: DETERMINISTIC_709de250435ffa6b
Batch ID: 20250612_160703
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
from email.mime.base import MIMEBase
from email import encoders
import logging

# Set up logging for error handling
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

class EmailNotifier:
    def __init__(self, smtp_server, port, sender_email, sender_password):
        """
        Initialize the EmailNotifier with SMTP server details.
        
        :param smtp_server: The SMTP server address.
        :param port: The SMTP server port.
        :param sender_email: The email address to send notifications from.
        :param sender_password: The password for the sender email account.
        """
        self.smtp_server = smtp_server
        self.port = port
        self.sender_email = sender_email
        self.sender_password = sender_password

    def send_email(self, recipient_email, customer_name):
        """
        Send an email notification to the customer after service completion.
        
        :param recipient_email: The customer's email address.
        :param customer_name: The customer's name for personalized greeting.
        """
        subject = "Thank You for Choosing Star Cleaning Services!"
        body = (f"Dear {customer_name},\n\n"
                "Thank you for using our commercial cleaning services. We hope you are satisfied with the results!\n"
                "Remember, our satisfaction guarantee ensures that if you're not completely happy, we'll make it right.\n\n"
                "Best regards,\n"
                "Star Cleaning Services")

        # Create a multipart email message
        msg = MIMEMultipart()
        msg['From'] = self.sender_email
        msg['To'] = recipient_email
        msg['Subject'] = subject

        # Attach the body with the msg instance
        msg.attach(MIMEText(body, 'plain'))

        try:
            # Connect to the server and send the email
            with smtplib.SMTP(self.smtp_server, self.port) as server:
                server.starttls()  # Upgrade the connection to a secure encrypted SSL/TLS connection
                server.login(self.sender_email, self.sender_password)
                server.sendmail(self.sender_email, recipient_email, msg.as_string())
                logging.info(f"Email successfully sent to {recipient_email}")
        except Exception as e:
            logging.error(f"Failed to send email to {recipient_email}: {e}")

if __name__ == "__main__":
    # Configuration for the email server
    SMTP_SERVER = "smtp.your-email-provider.com"
    PORT = 587  # For SSL
    SENDER_EMAIL = "your-email@example.com"
    SENDER_PASSWORD = "your-email-password"

    # Example usage
    notifier = EmailNotifier(SMTP_SERVER, PORT, SENDER_EMAIL, SENDER_PASSWORD)
    
    # Replace with actual customer details
    recipient_email = "customer@example.com"
    customer_name = "John Doe"

    notifier.send_email(recipient_email, customer_name)
```
