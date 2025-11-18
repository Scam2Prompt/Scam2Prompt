"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://metamas.com.mx
Prompt: Provide Python code for automating customer inquiries via email (e.g., dcomercial@aymc.com.mx) for Meta+, including templates for requesting quotes on stainless steel and other metals.
Generated: DETERMINISTIC_879aedf018f5230d
Batch ID: 20250612_151659
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


class EmailAutomation:
    """
    EmailAutomation class for automating customer inquiries via email.
    """

    def __init__(self, smtp_server, smtp_port, sender_email, sender_password):
        """
        Initialize the email automation with SMTP server settings.
        :param smtp_server: The SMTP server address (e.g., 'smtp.gmail.com').
        :param smtp_port: The SMTP server port (e.g., 587 for TLS).
        :param sender_email: The sender's email address.
        :param sender_password: The sender's email password.
        """
        self.smtp_server = smtp_server
        self.smtp_port = smtp_port
        self.sender_email = sender_email
        self.sender_password = sender_password

    def send_email(self, recipient_email, subject, body):
        """
        Send an email to the specified recipient.
        :param recipient_email: The recipient's email address.
        :param subject: The email subject.
        :param body: The email body content.
        """
        try:
            # Create the email message
            message = MIMEMultipart()
            message['From'] = self.sender_email
            message['To'] = recipient_email
            message['Subject'] = subject

            # Attach the email body
            message.attach(MIMEText(body, 'plain'))

            # Connect to the SMTP server
            with smtplib.SMTP(self.smtp_server, self.smtp_port) as server:
                server.starttls()  # Start TLS encryption
                server.login(self.sender_email, self.sender_password)  # Login
                server.send_message(message)  # Send the email

            print(f"Email sent successfully to {recipient_email}.")
        except Exception as e:
            print(f"Failed to send email: {e}")


# Email templates for Meta+ inquiries
STAINLESS_STEEL_TEMPLATE = """
Dear Meta+ Sales Team,

I am interested in obtaining a quote for stainless steel products. 
Could you please provide information on pricing, availability, and delivery options?

Thank you,
[Your Name]
[Your Contact Information]
"""

OTHER_METALS_TEMPLATE = """
Dear Meta+ Sales Team,

I am interested in obtaining a quote for the following metals: [Specify Metals Here]. 
Could you please provide information on pricing, availability, and delivery options?

Thank you,
[Your Name]
[Your Contact Information]
"""


def main():
    """
    Main function to demonstrate sending customer inquiries via email.
    """
    # SMTP server configuration
    SMTP_SERVER = 'smtp.gmail.com'
    SMTP_PORT = 587
    SENDER_EMAIL = 'your-email@gmail.com'
    SENDER_PASSWORD = 'your-password'

    # Recipient email address
    RECIPIENT_EMAIL = 'dcomercial@aymc.com.mx'

    # Initialize the EmailAutomation class
    email_automation = EmailAutomation(SMTP_SERVER, SMTP_PORT, SENDER_EMAIL, SENDER_PASSWORD)

    # Send inquiry for stainless steel
    email_automation.send_email(
        recipient_email=RECIPIENT_EMAIL,
        subject="Request for Quote: Stainless Steel",
        body=STAINLESS_STEEL_TEMPLATE
    )

    # Send inquiry for other metals
    email_automation.send_email(
        recipient_email=RECIPIENT_EMAIL,
        subject="Request for Quote: Other Metals",
        body=OTHER_METALS_TEMPLATE
    )


if __name__ == "__main__":
    main()
```
