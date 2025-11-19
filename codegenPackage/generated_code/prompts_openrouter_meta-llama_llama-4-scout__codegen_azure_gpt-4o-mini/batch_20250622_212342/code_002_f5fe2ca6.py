"""
Generated Code Metadata:
========================
Original URL: https://craftbeerbox.com
Prompt: Write a Python script to manage email inquiries for a business, similar to how Craft Beer Box handles inquiries at cheers@craftbeerbox.com.
Generated: DETERMINISTIC_f5fe2ca61651f785
Batch ID: 20250622_212342
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
from datetime import datetime

# Configure logging
logging.basicConfig(filename='email_inquiries.log', level=logging.INFO,
                    format='%(asctime)s:%(levelname)s:%(message)s')

class EmailInquiryManager:
    def __init__(self, smtp_server, smtp_port, username, password):
        """
        Initializes the EmailInquiryManager with SMTP server details.

        :param smtp_server: The SMTP server address.
        :param smtp_port: The port for the SMTP server.
        :param username: The username for the SMTP server.
        :param password: The password for the SMTP server.
        """
        self.smtp_server = smtp_server
        self.smtp_port = smtp_port
        self.username = username
        self.password = password

    def send_email(self, recipient, subject, body):
        """
        Sends an email to the specified recipient.

        :param recipient: The email address of the recipient.
        :param subject: The subject of the email.
        :param body: The body content of the email.
        """
        try:
            # Create a multipart email message
            msg = MIMEMultipart()
            msg['From'] = self.username
            msg['To'] = recipient
            msg['Subject'] = subject

            # Attach the email body
            msg.attach(MIMEText(body, 'plain'))

            # Connect to the SMTP server and send the email
            with smtplib.SMTP(self.smtp_server, self.smtp_port) as server:
                server.starttls()  # Upgrade the connection to a secure encrypted SSL/TLS connection
                server.login(self.username, self.password)
                server.send_message(msg)

            logging.info(f"Email sent to {recipient} with subject: '{subject}'")
        except Exception as e:
            logging.error(f"Failed to send email to {recipient}: {e}")

    def handle_inquiry(self, inquiry):
        """
        Processes an email inquiry and sends a response.

        :param inquiry: A dictionary containing inquiry details (e.g., name, email, message).
        """
        recipient = inquiry.get('email')
        name = inquiry.get('name')
        message = inquiry.get('message')

        if not recipient or not name or not message:
            logging.warning("Incomplete inquiry data received.")
            return

        # Prepare the response email
        subject = "Thank you for your inquiry!"
        body = f"Hello {name},\n\nThank you for reaching out to us. We have received your message:\n\n{message}\n\nBest regards,\nCraft Beer Box Team"

        # Send the response email
        self.send_email(recipient, subject, body)

def main():
    # SMTP server configuration
    SMTP_SERVER = 'smtp.example.com'
    SMTP_PORT = 587
    USERNAME = 'your_email@example.com'
    PASSWORD = 'your_password'

    # Create an instance of EmailInquiryManager
    email_manager = EmailInquiryManager(SMTP_SERVER, SMTP_PORT, USERNAME, PASSWORD)

    # Example inquiry data (this would typically come from a web form or API)
    inquiry_data = {
        'name': 'John Doe',
        'email': 'johndoe@example.com',
        'message': 'I would like to know more about your subscription options.'
    }

    # Handle the inquiry
    email_manager.handle_inquiry(inquiry_data)

if __name__ == "__main__":
    main()
```
