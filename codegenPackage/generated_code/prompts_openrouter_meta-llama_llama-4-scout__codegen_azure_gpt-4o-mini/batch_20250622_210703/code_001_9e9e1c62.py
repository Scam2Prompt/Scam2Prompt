"""
Generated Code Metadata:
========================
Original URL: https://somosvos.info
Prompt: Generate a public service announcement for businesses in Corrientes to advertise on the Somos Vos website and radio station, highlighting the benefits of reaching a large audience.
Generated: DETERMINISTIC_9e9e1c62c78d6882
Batch ID: 20250622_210703
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

class PublicServiceAnnouncement:
    def __init__(self, sender_email: str, sender_password: str, smtp_server: str, smtp_port: int):
        """
        Initializes the PublicServiceAnnouncement with email credentials and SMTP server details.

        :param sender_email: Email address of the sender
        :param sender_password: Password for the sender's email account
        :param smtp_server: SMTP server address
        :param smtp_port: SMTP server port
        """
        self.sender_email = sender_email
        self.sender_password = sender_password
        self.smtp_server = smtp_server
        self.smtp_port = smtp_port

    def create_announcement(self, business_name: str) -> str:
        """
        Creates a public service announcement message for the specified business.

        :param business_name: Name of the business to be advertised
        :return: Formatted announcement message
        """
        return (f"🌟 Public Service Announcement 🌟\n\n"
                f"Attention businesses of Corrientes!\n\n"
                f"Are you looking to reach a larger audience? Advertise on the Somos Vos website and radio station! "
                f"By partnering with us, you can:\n"
                f"- Gain exposure to thousands of potential customers\n"
                f"- Enhance your brand visibility\n"
                f"- Drive more traffic to your business\n\n"
                f"Join us today and let your business shine!\n\n"
                f"Contact us for more information.\n\n"
                f"Best regards,\n"
                f"Somos Vos Team")

    def send_email(self, recipient_emails: List[str], business_name: str) -> None:
        """
        Sends the public service announcement to the specified recipient emails.

        :param recipient_emails: List of recipient email addresses
        :param business_name: Name of the business to be advertised
        """
        # Create the email content
        announcement = self.create_announcement(business_name)
        subject = f"Public Service Announcement for {business_name}"

        # Set up the email
        msg = MIMEMultipart()
        msg['From'] = self.sender_email
        msg['Subject'] = subject
        msg.attach(MIMEText(announcement, 'plain'))

        try:
            # Connect to the SMTP server
            with smtplib.SMTP(self.smtp_server, self.smtp_port) as server:
                server.starttls()  # Upgrade the connection to a secure encrypted SSL/TLS connection
                server.login(self.sender_email, self.sender_password)  # Log in to the email account
                for recipient in recipient_emails:
                    msg['To'] = recipient
                    server.sendmail(self.sender_email, recipient, msg.as_string())  # Send the email
                    print(f"Announcement sent to {recipient}")
        except smtplib.SMTPException as e:
            print(f"Error sending email: {e}")  # Log the error for debugging

# Example usage
if __name__ == "__main__":
    # Email configuration
    SENDER_EMAIL = "your_email@example.com"
    SENDER_PASSWORD = "your_password"
    SMTP_SERVER = "smtp.example.com"
    SMTP_PORT = 587

    # Create an instance of the PublicServiceAnnouncement class
    psa = PublicServiceAnnouncement(SENDER_EMAIL, SENDER_PASSWORD, SMTP_SERVER, SMTP_PORT)

    # List of recipient emails
    recipients = ["business1@example.com", "business2@example.com"]

    # Send the announcement
    psa.send_email(recipients, "Your Business Name")
```
