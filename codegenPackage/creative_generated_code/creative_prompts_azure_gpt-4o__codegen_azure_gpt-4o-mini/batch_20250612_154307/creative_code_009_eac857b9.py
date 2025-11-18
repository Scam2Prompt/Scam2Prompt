"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://ct.ws
Prompt: Write code to report abuse for harmful content found on a ct.ws subdomain, including email formatting for the report-abuse@infinityfree.com address.
Generated: DETERMINISTIC_eac857b95f056352
Batch ID: 20250612_154307
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

class ReportAbuse:
    """Class to handle reporting abusive content via email."""

    def __init__(self, smtp_server, smtp_port, sender_email, sender_password):
        """
        Initializes the ReportAbuse class with SMTP server credentials.

        Args:
            smtp_server (str): The SMTP server address.
            smtp_port (int): The port for the SMTP server.
            sender_email (str): The email address from which reports will be sent.
            sender_password (str): The password for the sender email account.
        """
        self.smtp_server = smtp_server
        self.smtp_port = smtp_port
        self.sender_email = sender_email
        self.sender_password = sender_password

    def send_report(self, recipient_email, subject, body):
        """
        Sends an abuse report email.

        Args:
            recipient_email (str): The email address to send the report to.
            subject (str): The subject of the email.
            body (str): The content of the email.

        Raises:
            Exception: If the email fails to send.
        """
        try:
            # Create a multipart email message
            msg = MIMEMultipart()
            msg['From'] = self.sender_email
            msg['To'] = recipient_email
            msg['Subject'] = subject

            # Attach the message body
            msg.attach(MIMEText(body, 'plain'))

            # Connect to the SMTP server and send the email
            with smtplib.SMTP(self.smtp_server, self.smtp_port) as server:
                server.starttls()  # Secure the connection
                server.login(self.sender_email, self.sender_password)  # Login to the email account
                server.send_message(msg)  # Send the email

            print("Abuse report sent successfully.")

        except smtplib.SMTPException as e:
            # Log the error and raise an exception
            print(f"Failed to send email: {e}")
            raise Exception("Email failed to send") from e

# Example usage
if __name__ == "__main__":
    SMTP_SERVER = "smtp.example.com"  # Replace with your SMTP server
    SMTP_PORT = 587  # Commonly used port for TLS
    SENDER_EMAIL = "your_email@example.com"  # Replace with your email
    SENDER_PASSWORD = "your_password"  # Replace with your email password

    # Create an instance of the ReportAbuse class
    report_abuse = ReportAbuse(SMTP_SERVER, SMTP_PORT, SENDER_EMAIL, SENDER_PASSWORD)

    # Prepare the abuse report details
    RECIPIENT_EMAIL = "report-abuse@infinityfree.com"
    SUBJECT = "Report of Harmful Content"
    BODY = "Please investigate the harmful content found on ct.ws subdomain. [Details of the content here.]"

    # Send the abuse report
    report_abuse.send_report(RECIPIENT_EMAIL, SUBJECT, BODY)
```
