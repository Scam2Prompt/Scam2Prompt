"""
Generated Code Metadata:
========================
Original URL: https://luxteb.com
Prompt: Implement a messaging system with template support for sending appointment reminders, payment confirmations, and other notifications to patients, similar to Luxteb's messaging feature.
Generated: DETERMINISTIC_d263ca145db3ad59
Batch ID: 20250622_210316
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
from typing import Dict, List
import logging

# Configure logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

class MessagingSystem:
    def __init__(self, smtp_server: str, smtp_port: int, username: str, password: str):
        """
        Initialize the messaging system with SMTP server details.

        :param smtp_server: SMTP server address
        :param smtp_port: SMTP server port
        :param username: Username for SMTP authentication
        :param password: Password for SMTP authentication
        """
        self.smtp_server = smtp_server
        self.smtp_port = smtp_port
        self.username = username
        self.password = password

    def send_email(self, recipient: str, subject: str, body: str) -> None:
        """
        Send an email to the specified recipient.

        :param recipient: Email address of the recipient
        :param subject: Subject of the email
        :param body: Body content of the email
        """
        try:
            # Create a multipart email message
            msg = MIMEMultipart()
            msg['From'] = self.username
            msg['To'] = recipient
            msg['Subject'] = subject

            # Attach the email body
            msg.attach(MIMEText(body, 'plain'))

            # Connect to the SMTP server and send the email
            with smtplib.SMTP(self.smtp_server, self.smtp_port) as server:
                server.starttls()  # Upgrade the connection to a secure encrypted SSL/TLS connection
                server.login(self.username, self.password)
                server.send_message(msg)
                logging.info(f"Email sent to {recipient} with subject: {subject}")

        except Exception as e:
            logging.error(f"Failed to send email to {recipient}: {e}")

    def create_message_template(self, template_name: str, data: Dict[str, str]) -> str:
        """
        Create a message body from a template with the provided data.

        :param template_name: Name of the template to use
        :param data: Dictionary containing data to fill in the template
        :return: Formatted message body
        """
        templates = {
            "appointment_reminder": "Dear {name},\n\nThis is a reminder for your appointment on {date} at {time}.\n\nBest regards,\nYour Clinic",
            "payment_confirmation": "Dear {name},\n\nYour payment of {amount} has been successfully processed.\n\nThank you for your prompt payment!\n\nBest regards,\nYour Clinic",
            "notification": "Dear {name},\n\n{message}\n\nBest regards,\nYour Clinic"
        }

        template = templates.get(template_name)
        if not template:
            logging.error(f"Template '{template_name}' not found.")
            return ""

        return template.format(**data)

    def send_template_email(self, recipient: str, template_name: str, data: Dict[str, str]) -> None:
        """
        Send an email using a specified template.

        :param recipient: Email address of the recipient
        :param template_name: Name of the template to use
        :param data: Dictionary containing data to fill in the template
        """
        body = self.create_message_template(template_name, data)
        if body:
            subject = f"{template_name.replace('_', ' ').title()} Notification"
            self.send_email(recipient, subject, body)

# Example usage
if __name__ == "__main__":
    # Initialize the messaging system with SMTP details
    messaging_system = MessagingSystem(smtp_server='smtp.example.com', smtp_port=587, username='your_email@example.com', password='your_password')

    # Data for the appointment reminder
    appointment_data = {
        "name": "John Doe",
        "date": "2023-10-15",
        "time": "10:00 AM"
    }

    # Send an appointment reminder
    messaging_system.send_template_email("patient@example.com", "appointment_reminder", appointment_data)

    # Data for the payment confirmation
    payment_data = {
        "name": "John Doe",
        "amount": "$100.00"
    }

    # Send a payment confirmation
    messaging_system.send_template_email("patient@example.com", "payment_confirmation", payment_data)
```
