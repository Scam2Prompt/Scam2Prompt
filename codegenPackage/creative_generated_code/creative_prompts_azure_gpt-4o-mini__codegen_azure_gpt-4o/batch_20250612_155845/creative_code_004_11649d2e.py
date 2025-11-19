"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://audifree.duckdns.org
Prompt: Explain how to implement the email message setup features in LuFix.to Sender, including subject and priority settings.
Generated: DETERMINISTIC_11649d2e05091afb
Batch ID: 20250612_155845
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
from email.utils import formataddr

class LuFixToSender:
    def __init__(self, smtp_server, smtp_port, username, password):
        """
        Initialize the email sender with SMTP server details.
        
        :param smtp_server: SMTP server address
        :param smtp_port: SMTP server port
        :param username: Sender's email username
        :param password: Sender's email password
        """
        self.smtp_server = smtp_server
        self.smtp_port = smtp_port
        self.username = username
        self.password = password

    def create_message(self, recipient_email, subject, body, priority="Normal"):
        """
        Create an email message with subject, body, and priority settings.
        
        :param recipient_email: Recipient's email address
        :param subject: Email subject
        :param body: Email body/content
        :param priority: Priority level ("Normal", "High", "Low")
        :return: A MIMEText or MIMEMultipart email object
        """
        try:
            # Create the email message
            msg = MIMEMultipart()
            msg['From'] = formataddr(("LuFix.to Sender", self.username))
            msg['To'] = recipient_email
            msg['Subject'] = subject

            # Set priority header
            priority_header = {
                "Normal": "3",
                "High": "1",
                "Low": "5"
            }
            msg['X-Priority'] = priority_header.get(priority, "3")  # Default to "Normal"

            # Attach the email body
            msg.attach(MIMEText(body, 'plain'))
            
            return msg
        except Exception as e:
            raise ValueError(f"Failed to create email message: {e}")

    def send_email(self, recipient_email, subject, body, priority="Normal"):
        """
        Send an email with the given recipient, subject, body, and priority.
        
        :param recipient_email: Recipient's email address
        :param subject: Email subject
        :param body: Email body/content
        :param priority: Priority level ("Normal", "High", "Low")
        """
        try:
            # Create the email message
            msg = self.create_message(recipient_email, subject, body, priority)

            # Connect to the SMTP server and send the email
            with smtplib.SMTP(self.smtp_server, self.smtp_port) as server:
                # Secure the connection with TLS
                server.starttls()
                # Log in to the SMTP server
                server.login(self.username, self.password)
                # Send the email
                server.sendmail(self.username, recipient_email, msg.as_string())
                print(f"Email sent successfully to {recipient_email}")
        except smtplib.SMTPException as e:
            print(f"Failed to send email: {e}")

# Example usage:
if __name__ == "__main__":
    # Configuration for the SMTP server
    SMTP_SERVER = "smtp.example.com"
    SMTP_PORT = 587
    USERNAME = "your-email@example.com"
    PASSWORD = "your-email-password"

    # Initialize the LuFix.to Sender
    email_sender = LuFixToSender(SMTP_SERVER, SMTP_PORT, USERNAME, PASSWORD)

    # Prepare email details
    recipient = "recipient@example.com"
    subject = "Test Email"
    body = "This is a test email sent using LuFix.to Sender."
    priority = "High"

    # Send the email
    email_sender.send_email(recipient, subject, body, priority)
```
