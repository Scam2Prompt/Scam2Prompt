"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://mahadevent.com
Prompt: Develop a script that automates the process of sending an enquiry email to Mahadev Enterprise for product sourcing.
Generated: DETERMINISTIC_e9dcb247c80da07d
Batch ID: 20250612_163826
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

class EnquiryEmailSender:
    def __init__(self, smtp_server, smtp_port, username, password):
        """Initialize the email sender with SMTP server details."""
        self.smtp_server = smtp_server
        self.smtp_port = smtp_port
        self.username = username
        self.password = password
        
    def create_email(self, recipient, subject, body):
        """
        Create an email message.

        Args:
            recipient (str): Recipient's email address.
            subject (str): Subject of the email.
            body (str): Body of the email.

        Returns:
            MIMEMultipart: Constructed email message.
        """
        msg = MIMEMultipart()
        msg['From'] = self.username
        msg['To'] = recipient
        msg['Subject'] = subject

        # Attach the body to the email
        msg.attach(MIMEText(body, 'plain'))
        return msg

    def send_email(self, recipient, subject, body):
        """
        Send an email to the specified recipient.

        Args:
            recipient (str): Recipient's email address.
            subject (str): Subject of the email.
            body (str): Body of the email.
        """
        msg = self.create_email(recipient, subject, body)
        try:
            # Connect to the SMTP server
            with smtplib.SMTP(self.smtp_server, self.smtp_port) as server:
                server.starttls()  # Upgrade the connection to a secure encrypted SSL/TLS connection
                server.login(self.username, self.password)  # Log in to the email account
                server.send_message(msg)  # Send the email
            print(f"Email sent successfully to {recipient}.")
        except smtplib.SMTPException as e:
            print(f"Failed to send email: {e}")


def main():
    # SMTP server configuration
    SMTP_SERVER = 'smtp.example.com'  # Replace with your SMTP server
    SMTP_PORT = 587  # Typical port for TLS
    USERNAME = 'your_email@example.com'  # Your email address
    PASSWORD = 'your_password'  # Your email password

    # Enquiry details
    RECIPIENT = 'info@mahadeventerprise.com'
    SUBJECT = 'Product Sourcing Enquiry'
    BODY = (
        "Dear Mahadev Enterprise Team,\n\n"
        "I would like to inquire about the availability of products for sourcing. "
        "Please provide me with the details regarding your product range, pricing, "
        "and any other relevant information.\n\n"
        "Thank you.\n\n"
        "Best regards,\n"
        "Your Name"
    )

    # Create an instance of the email sender
    email_sender = EnquiryEmailSender(SMTP_SERVER, SMTP_PORT, USERNAME, PASSWORD)
    
    # Send the enquiry email
    email_sender.send_email(RECIPIENT, SUBJECT, BODY)


if __name__ == "__main__":
    main()
```
