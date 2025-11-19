"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://passandbrazzz.blogspot.com
Prompt: Develop a script that sends a message to the seller of a commercial property, referencing the store of lighting for sale in São Paulo.
Generated: DETERMINISTIC_552ad12857160f28
Batch ID: 20250612_163924
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

class PropertyMessageSender:
    def __init__(self, smtp_server, smtp_port, username, password):
        """
        Initializes the PropertyMessageSender with SMTP server configuration.

        :param smtp_server: The SMTP server address.
        :param smtp_port: The SMTP server port.
        :param username: The email account username.
        :param password: The email account password.
        """
        self.smtp_server = smtp_server
        self.smtp_port = smtp_port
        self.username = username
        self.password = password

    def send_message(self, recipient_email, property_details):
        """
        Sends a message to the property seller.

        :param recipient_email: The email address of the seller.
        :param property_details: A dictionary containing details about the property.
        :raises Exception: If sending the email fails.
        """
        # Create the email content
        subject = f"Inquiry about {property_details['property_name']}"
        body = (f"Dear Seller,\n\n"
                f"I am interested in the store of lighting for sale in São Paulo. "
                f"Here are the details:\n"
                f"Property Name: {property_details['property_name']}\n"
                f"Location: {property_details['location']}\n"
                f"Price: {property_details['price']}\n\n"
                f"Could you please provide more information?\n\n"
                f"Best regards,\n"
                f"[Your Name]")

        # Prepare the email
        msg = MIMEMultipart()
        msg['From'] = self.username
        msg['To'] = recipient_email
        msg['Subject'] = subject
        msg.attach(MIMEText(body, 'plain'))

        try:
            # Connect to the SMTP server and send the email
            with smtplib.SMTP(self.smtp_server, self.smtp_port) as server:
                server.starttls()  # Upgrade the connection to a secure encrypted SSL/TLS connection
                server.login(self.username, self.password)
                server.send_message(msg)
                print("Email sent successfully.")
        except smtplib.SMTPException as e:
            print(f"Failed to send email: {e}")
            raise

def main():
    # SMTP server configuration
    SMTP_SERVER = 'smtp.example.com'
    SMTP_PORT = 587
    USERNAME = 'your_email@example.com'
    PASSWORD = 'your_password'

    # Property details
    property_details = {
        'property_name': 'Lighting Store',
        'location': 'São Paulo',
        'price': 'R$ 500.000'
    }

    # The seller's email address
    seller_email = 'seller@example.com'

    # Create the message sender instance
    message_sender = PropertyMessageSender(SMTP_SERVER, SMTP_PORT, USERNAME, PASSWORD)

    # Send the message
    message_sender.send_message(seller_email, property_details)

if __name__ == '__main__':
    main()
```
