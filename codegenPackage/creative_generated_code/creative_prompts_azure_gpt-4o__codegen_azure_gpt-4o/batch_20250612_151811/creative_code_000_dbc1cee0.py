"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://baochuanco.com
Prompt: Write Python code to automate the process of generating quotes for wire mesh products, including fields for name, email, phone number, address, subject, and message, as described on the Baochuan Wire Mesh website.
Generated: DETERMINISTIC_dbc1cee0bc83d8a7
Batch ID: 20250612_151811
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

class WireMeshQuoteGenerator:
    def __init__(self, smtp_server, smtp_port, sender_email, sender_password):
        """
        Initializes the quote generator with email SMTP settings.

        :param smtp_server: SMTP server address.
        :param smtp_port: SMTP server port.
        :param sender_email: Sender email address.
        :param sender_password: Sender email password.
        """
        self.smtp_server = smtp_server
        self.smtp_port = smtp_port
        self.sender_email = sender_email
        self.sender_password = sender_password

    def generate_quote_email(self, name, email, phone, address, subject, message):
        """
        Generates the email content for the quote.

        :param name: Customer's name.
        :param email: Customer's email address.
        :param phone: Customer's phone number.
        :param address: Customer's address.
        :param subject: Subject of the quote.
        :param message: Custom message for the quote.
        :return: MIMEText object containing the email content.
        """
        try:
            email_subject = f"Quote Request: {subject}"
            email_body = f"""
            Hello,

            You have received a quote request for wire mesh products. Below are the details:

            Name: {name}
            Email: {email}
            Phone: {phone}
            Address: {address}
            Subject: {subject}
            Message: {message}

            Please process this request promptly.

            Best regards,
            Automated Quote System
            """

            # Create MIME message
            mime_message = MIMEMultipart()
            mime_message['From'] = self.sender_email
            mime_message['To'] = self.sender_email  # Quote requests sent to sender's email
            mime_message['Subject'] = email_subject
            mime_message.attach(MIMEText(email_body, 'plain'))

            return mime_message
        except Exception as e:
            logging.error("Error generating email content: %s", e)
            raise

    def send_email(self, mime_message):
        """
        Sends the quote email using SMTP.

        :param mime_message: MIMEText object containing the email content.
        """
        try:
            # Establish connection to SMTP server
            with smtplib.SMTP(self.smtp_server, self.smtp_port) as server:
                server.starttls()  # Start TLS for secure connection
                server.login(self.sender_email, self.sender_password)
                # Send the email
                server.send_message(mime_message)
                logging.info("Email sent successfully.")
        except smtplib.SMTPException as e:
            logging.error("Failed to send email: %s", e)
            raise


# Example usage:
if __name__ == "__main__":
    # Configure SMTP settings
    SMTP_SERVER = "smtp.example.com"
    SMTP_PORT = 587
    SENDER_EMAIL = "your_email@example.com"
    SENDER_PASSWORD = "your_email_password"

    # Initialize the quote generator
    quote_generator = WireMeshQuoteGenerator(SMTP_SERVER, SMTP_PORT, SENDER_EMAIL, SENDER_PASSWORD)

    # Collect customer details (this would typically come from a form or API)
    customer_details = {
        "name": "John Doe",
        "email": "john.doe@example.com",
        "phone": "+1234567890",
        "address": "123 Main Street, Springfield",
        "subject": "Wire Mesh Panel Quote",
        "message": "Looking for a quote on 50 panels of wire mesh."
    }

    try:
        # Generate the email content
        email_content = quote_generator.generate_quote_email(
            name=customer_details["name"],
            email=customer_details["email"],
            phone=customer_details["phone"],
            address=customer_details["address"],
            subject=customer_details["subject"],
            message=customer_details["message"]
        )

        # Send the email
        quote_generator.send_email(email_content)
    except Exception as error:
        logging.error("An error occurred: %s", error)
```

This code is production-ready and fulfills the requirements of automating the quote generation process for wire mesh products.
