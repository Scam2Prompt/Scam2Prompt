"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://rayatrecruitment.com
Prompt: Write a script to send automated email acknowledgments to applicants after successful payment, as described in the Rayat Shikshan Sanstha application process.
Generated: DETERMINISTIC_088245cdb740e692
Batch ID: 20250612_154721
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

# Setup logging configuration
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

class EmailSender:
    def __init__(self, smtp_server, smtp_port, smtp_user, smtp_password):
        """Initialize email sender with SMTP server details."""
        self.smtp_server = smtp_server
        self.smtp_port = smtp_port
        self.smtp_user = smtp_user
        self.smtp_password = smtp_password

    def send_email(self, recipient_email, subject, body):
        """Send email to the specified recipient."""
        try:
            # Create the email message
            msg = MIMEMultipart()
            msg['From'] = self.smtp_user
            msg['To'] = recipient_email
            msg['Subject'] = subject

            # Attach the body with the msg instance
            msg.attach(MIMEText(body, 'plain'))

            # Start the SMTP server and send the email
            with smtplib.SMTP(self.smtp_server, self.smtp_port) as server:
                server.starttls()  # Upgrade the connection to a secure encrypted SSL/TLS
                server.login(self.smtp_user, self.smtp_password)
                server.sendmail(msg['From'], msg['To'], msg.as_string())

            logging.info(f"Email sent successfully to {recipient_email}")

        except smtplib.SMTPException as e:
            logging.error(f"Failed to send email to {recipient_email}: {e}")
            raise

def send_acknowledgment_email(applicant_name, applicant_email, payment_details):
    """Prepare and send acknowledgment email for successful payment."""
    smtp_server = "smtp.example.com"
    smtp_port = 587
    smtp_user = "your_email@example.com"
    smtp_password = "your_password"

    email_sender = EmailSender(smtp_server, smtp_port, smtp_user, smtp_password)

    subject = "Payment Acknowledgment"
    body = f"""
    Dear {applicant_name},

    Thank you for your payment. We have received the following details:
    
    {payment_details}

    Your application is currently being processed. If you have any questions, please reach out to us.

    Best Regards,
    Rayat Shikshan Sanstha
    """

    email_sender.send_email(applicant_email, subject, body)

if __name__ == "__main__":
    # Sample data; in a real application, this would come from form submissions or a database
    applicant_name = "John Doe"
    applicant_email = "john.doe@example.com"
    payment_details = "Transaction ID: 123456789, Amount: $100"

    try:
        send_acknowledgment_email(applicant_name, applicant_email, payment_details)
    except Exception as e:
        logging.error(f"Error occurred: {e}")
```
