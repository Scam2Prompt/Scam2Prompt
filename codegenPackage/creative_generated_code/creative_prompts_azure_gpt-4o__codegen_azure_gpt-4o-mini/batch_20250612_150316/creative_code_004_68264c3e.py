"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://renzooprotocal.net
Prompt: Provide example code for integrating an email API to send free estimates and appointment confirmations to customers, similar to the "Contact Us for a Free Quote" feature on Queen Bee Renzo ProtocolCleaning's site.
Generated: DETERMINISTIC_68264c3e3d6713af
Batch ID: 20250612_150316
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.base import MIMEBase
from email import encoders
import logging

# Configure logging
logging.basicConfig(level=logging.INFO)

class EmailService:
    def __init__(self, smtp_server: str, smtp_port: int, username: str, password: str):
        self.smtp_server = smtp_server
        self.smtp_port = smtp_port
        self.username = username
        self.password = password

    def send_email(self, to_email: str, subject: str, body: str, attachments: list = None):
        """Send an email with the specified subject and body to the recipient."""
        try:
            # Create the email message
            msg = MIMEMultipart()
            msg['From'] = self.username
            msg['To'] = to_email
            msg['Subject'] = subject

            # Attach the email body
            msg.attach(MIMEText(body, 'plain'))

            # Attach files if provided
            if attachments:
                for file in attachments:
                    attachment = MIMEBase('application', 'octet-stream')
                    try:
                        with open(file, 'rb') as file_obj:
                            attachment.set_payload(file_obj.read())
                    except FileNotFoundError:
                        logging.error(f"Attachment file {file} not found.")
                        continue
                    
                    encoders.encode_base64(attachment)
                    attachment.add_header('Content-Disposition', f'attachment; filename={file}')
                    msg.attach(attachment)

            # Connect to the SMTP server and send the email
            with smtplib.SMTP(self.smtp_server, self.smtp_port) as server:
                server.starttls()  # Upgrade the connection to secure
                server.login(self.username, self.password)
                server.send_message(msg)
                logging.info(f"Email sent to {to_email}")

        except Exception as e:
            logging.error(f"Failed to send email to {to_email}: {str(e)}")


# Example usage:
if __name__ == "__main__":
    # Email configuration
    SMTP_SERVER = 'smtp.example.com'  # Replace with your SMTP server
    SMTP_PORT = 587                    # Commonly used port for TLS
    USERNAME = 'your_email@example.com'  # Replace with your email
    PASSWORD = 'your_password'          # Replace with your email password

    # Create an instance of EmailService
    email_service = EmailService(SMTP_SERVER, SMTP_PORT, USERNAME, PASSWORD)

    # Prepare email details
    recipient_email = 'customer@example.com'  # Customer's email
    subject = 'Your Free Estimate and Appointment Confirmation'
    body = """Dear Customer,

Thank you for contacting us for a free estimate. We are pleased to confirm your appointment.

Best Regards,
Queen Bee Renzo Protocol Cleaning Team
"""

    # Send the email
    email_service.send_email(recipient_email, subject, body, attachments=None)
```
