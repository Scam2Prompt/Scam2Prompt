"""
Generated Code Metadata:
========================
Original URL: https://roshako.com
Prompt: Create a function in Python to automate the generation of a quotation request email for industrial products, using Roshako's contact details and product categories.
Generated: DETERMINISTIC_79c04920b0a7482a
Batch ID: 20250612_154355
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
from typing import List

# Define a class to handle quotation requests
class QuotationRequestEmail:
    def __init__(self, sender_email: str, sender_name: str, smtp_server: str, smtp_port: int):
        """
        Initialize the QuotationRequestEmail with sender details and SMTP server configuration.

        :param sender_email: Email address of the sender
        :param sender_name: Name of the sender
        :param smtp_server: SMTP server address
        :param smtp_port: SMTP server port
        """
        self.sender_email = sender_email
        self.sender_name = sender_name
        self.smtp_server = smtp_server
        self.smtp_port = smtp_port

    def create_email(self, recipient_email: str, product_categories: List[str]) -> MIMEMultipart:
        """
        Create a quotation request email.

        :param recipient_email: Email address of the recipient
        :param product_categories: List of product categories for the quotation
        :return: A MIMEMultipart email object
        """
        # Create the email object
        email = MIMEMultipart()
        email['From'] = f"{self.sender_name} <{self.sender_email}>"
        email['To'] = recipient_email
        email['Subject'] = "Quotation Request for Industrial Products"

        # Create the email body
        body = f"Dear Sir/Madam,\n\nI would like to request a quotation for the following product categories:\n"
        body += "\n".join(f"- {category}" for category in product_categories)
        body += "\n\nThank you for your assistance.\n\nBest regards,\n" + self.sender_name

        # Attach the body to the email
        email.attach(MIMEText(body, 'plain'))
        return email

    def send_email(self, recipient_email: str, product_categories: List[str]) -> None:
        """
        Send the quotation request email.

        :param recipient_email: Email address of the recipient
        :param product_categories: List of product categories for the quotation
        """
        try:
            # Create the email
            email = self.create_email(recipient_email, product_categories)

            # Connect to the SMTP server and send the email
            with smtplib.SMTP(self.smtp_server, self.smtp_port) as server:
                server.starttls()  # Upgrade the connection to a secure encrypted SSL/TLS connection
                server.login(self.sender_email, 'your_password')  # Replace 'your_password' with the actual password
                server.send_message(email)

            print("Quotation request email sent successfully.")

        except smtplib.SMTPException as e:
            print(f"Error sending email: {e}")
        except Exception as e:
            print(f"An unexpected error occurred: {e}")

# Example usage
if __name__ == "__main__":
    # Roshako's contact details
    sender_email = "roshako@example.com"
    sender_name = "Roshako"
    smtp_server = "smtp.example.com"
    smtp_port = 587

    # Create an instance of the QuotationRequestEmail class
    quotation_email = QuotationRequestEmail(sender_email, sender_name, smtp_server, smtp_port)

    # Define recipient and product categories
    recipient_email = "supplier@example.com"
    product_categories = ["Industrial Machinery", "Safety Equipment", "Electrical Components"]

    # Send the quotation request email
    quotation_email.send_email(recipient_email, product_categories)
```
