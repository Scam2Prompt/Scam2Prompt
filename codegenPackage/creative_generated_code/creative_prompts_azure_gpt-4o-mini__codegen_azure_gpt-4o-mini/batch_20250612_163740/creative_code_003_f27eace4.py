"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://www.trendsetterzs.com
Prompt: Develop a code snippet that automates the process of sending inquiries to Trendsetterzs, highlighting their commitment to ethical and sustainable sourcing in the fashion industry.
Generated: DETERMINISTIC_f27eace4f278a2f9
Batch ID: 20250612_163740
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
from typing import List

class InquirySender:
    def __init__(self, smtp_server: str, port: int, sender_email: str, password: str):
        """
        Initializes the InquirySender with SMTP server details.
        
        :param smtp_server: The SMTP server address.
        :param port: The port number for the SMTP server.
        :param sender_email: The sender's email address.
        :param password: The password for the sender's email account.
        """
        self.smtp_server = smtp_server
        self.port = port
        self.sender_email = sender_email
        self.password = password

    def create_email(self, recipient_email: str, subject: str, body: str) -> MIMEMultipart:
        """
        Creates an email message.
        
        :param recipient_email: The recipient's email address.
        :param subject: The subject of the email.
        :param body: The body content of the email.
        :return: A MIMEMultipart email message.
        """
        msg = MIMEMultipart()
        msg['From'] = self.sender_email
        msg['To'] = recipient_email
        msg['Subject'] = subject

        msg.attach(MIMEText(body, 'plain'))
        return msg

    def send_inquiry(self, recipient_email: str):
        """
        Sends an inquiry email to the specified recipient.
        
        :param recipient_email: The recipient's email address.
        """
        subject = "Inquiry About Ethical and Sustainable Sourcing"
        body = (
            "Dear Trendsetterzs Team,\n\n"
            "I hope this message finds you well. "
            "I am reaching out to inquire about your commitment to ethical and sustainable sourcing in the fashion industry. "
            "As a conscious consumer, I am keen on understanding how your practices align with sustainability goals and ethical standards.\n\n"
            "Thank you for your time, and I look forward to your response.\n\n"
            "Best regards,\n"
            "Your Name"
        )

        try:
            # Create email
            email_message = self.create_email(recipient_email, subject, body)

            # Connect to the SMTP server and send the email
            with smtplib.SMTP(self.smtp_server, self.port) as server:
                server.starttls()  # Upgrade the connection to secure
                server.login(self.sender_email, self.password)  # Login to the server
                server.sendmail(self.sender_email, recipient_email, email_message.as_string())  # Send email
            
            print("Inquiry sent successfully!")
        except smtplib.SMTPException as e:
            print(f"An error occurred while sending the email: {e}")
        except Exception as e:
            print(f"An unexpected error occurred: {e}")

# Example usage (Uncomment the lines below to use)
# inquiry_sender = InquirySender("smtp.example.com", 587, "your_email@example.com", "your_password")
# inquiry_sender.send_inquiry("recipient@example.com")
```
