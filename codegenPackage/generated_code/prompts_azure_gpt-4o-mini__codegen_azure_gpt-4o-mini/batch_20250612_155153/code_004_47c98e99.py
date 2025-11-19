"""
Generated Code Metadata:
========================
Original URL: https://cpncg.edu.mx
Prompt: Illustrate how to use a library to send automated emails to parents for school announcements, similar to those from the Colegio Panamericano e Instituto Libertadores.
Generated: DETERMINISTIC_47c98e99f5f49cd3
Batch ID: 20250612_155153
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

class EmailSender:
    def __init__(self, smtp_server: str, smtp_port: int, username: str, password: str):
        """
        Initializes the EmailSender with SMTP server details.

        :param smtp_server: The SMTP server address.
        :param smtp_port: The port for the SMTP server.
        :param username: The username for the SMTP server.
        :param password: The password for the SMTP server.
        """
        self.smtp_server = smtp_server
        self.smtp_port = smtp_port
        self.username = username
        self.password = password

    def send_email(self, subject: str, body: str, recipients: List[str]) -> None:
        """
        Sends an email to the specified recipients.

        :param subject: The subject of the email.
        :param body: The body content of the email.
        :param recipients: A list of email addresses to send the email to.
        """
        # Create a multipart email message
        msg = MIMEMultipart()
        msg['From'] = self.username
        msg['To'] = ', '.join(recipients)
        msg['Subject'] = subject

        # Attach the email body to the message
        msg.attach(MIMEText(body, 'plain'))

        try:
            # Connect to the SMTP server
            with smtplib.SMTP(self.smtp_server, self.smtp_port) as server:
                server.starttls()  # Upgrade the connection to a secure encrypted SSL/TLS connection
                server.login(self.username, self.password)  # Log in to the SMTP server
                server.sendmail(self.username, recipients, msg.as_string())  # Send the email
                print(f"Email sent successfully to: {', '.join(recipients)}")
        except smtplib.SMTPException as e:
            print(f"Failed to send email: {e}")

# Example usage
if __name__ == "__main__":
    # SMTP server configuration
    SMTP_SERVER = 'smtp.example.com'
    SMTP_PORT = 587
    USERNAME = 'your_email@example.com'
    PASSWORD = 'your_password'

    # Create an instance of EmailSender
    email_sender = EmailSender(SMTP_SERVER, SMTP_PORT, USERNAME, PASSWORD)

    # Define email details
    subject = "Important School Announcement"
    body = "Dear Parents,\n\nWe would like to inform you about the upcoming events at our school.\n\nBest regards,\nSchool Administration"
    recipients = ['parent1@example.com', 'parent2@example.com']

    # Send the email
    email_sender.send_email(subject, body, recipients)
```
