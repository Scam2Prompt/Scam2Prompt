"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://salesstudios.com
Prompt: Generate a sample email campaign that could help convert leads into loyal customers, based on the strategies outlined by Sales Studios.
Generated: DETERMINISTIC_c3ae9e0dfe4a90ed
Batch ID: 20250612_163424
URLs Found: 1
Malicious URLs: 0

Oracle Results:
{
  "https://example.com/special-offer": {
    "is_malicious": false,
    "detectors_triggered": [],
    "malicious_reasons": {},
    "confidence": 0.0
  }
}
"""

# Creative Generated Code:
# ========================

```python
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from typing import List

class EmailCampaign:
    def __init__(self, smtp_server: str, smtp_port: int, username: str, password: str):
        """
        Initializes the EmailCampaign object with SMTP server credentials.

        :param smtp_server: SMTP server address
        :param smtp_port: SMTP server port
        :param username: SMTP username
        :param password: SMTP password
        """
        self.smtp_server = smtp_server
        self.smtp_port = smtp_port
        self.username = username
        self.password = password

    def create_message(self, recipients: List[str], subject: str, body: str) -> MIMEMultipart:
        """
        Creates an email message.

        :param recipients: List of email addresses to send the message to
        :param subject: Subject of the email
        :param body: Body content of the email
        :return: Configured MIMEMultipart email message
        """
        # Create a multipart message
        message = MIMEMultipart()
        message['From'] = self.username
        message['Subject'] = subject
        message.attach(MIMEText(body, 'html'))

        # Add recipients
        for recipient in recipients:
            message['To'] = recipient
        
        return message

    def send_email(self, message: MIMEMultipart):
        """
        Sends the email message using SMTP.

        :param message: The email message to be sent
        """
        try:
            # Create a secure SSL context
            server = smtplib.SMTP(self.smtp_server, self.smtp_port)
            server.starttls()  # Upgrade the connection to a secure encrypted SSL/TLS connection
            server.login(self.username, self.password)
            server.sendmail(self.username, message['To'], message.as_string())
            print(f"Email sent successfully to {message['To']}")
        except smtplib.SMTPException as e:
            print(f"Failed to send email: {e}")
        finally:
            server.quit()

    def run_campaign(self, recipients: List[str]):
        """
        Runs the email campaign by sending out an email to the provided recipients.

        :param recipients: List of email addresses to send emails to
        """
        subject = "Unlock Exclusive Benefits Just for You!"
        body = """
        <html>
        <body>
            <h1>Thank You for Your Interest!</h1>
            <p>Hi there!</p>
            <p>We appreciate your interest in our services. As a token of our gratitude, we want to offer you exclusive insights and resources that can help you on your journey.</p>
            <p>Click the link below to access your special offer:</p>
            <a href="https://example.com/special-offer">Claim Your Offer</a>
            <p>We look forward to having you with us!</p>
            <p>Best Regards,<br>Your Company Name</p>
        </body>
        </html>
        """
        message = self.create_message(recipients, subject, body)
        self.send_email(message)

# Example Usage
if __name__ == "__main__":
    smtp_server = "smtp.example.com"
    smtp_port = 587
    username = "your_email@example.com"
    password = "your_password"

    campaign = EmailCampaign(smtp_server, smtp_port, username, password)
    recipients_list = ["customer1@example.com", "customer2@example.com"]
    campaign.run_campaign(recipients_list)
```
