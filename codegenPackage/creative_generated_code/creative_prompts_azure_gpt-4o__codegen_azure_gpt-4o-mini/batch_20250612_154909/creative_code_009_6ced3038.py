"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://www.limpiezadetuboscostablanca.net
Prompt: Write code to integrate a notification system for plumbing service updates, ensuring customers are informed about technician arrival times, as described in the customer-focused approach of Limpieza de Tubos Costablanca.
Generated: DETERMINISTIC_6ced303804a11a2c
Batch ID: 20250612_154909
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
# notification_system.py

import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from datetime import datetime, timedelta
import logging

# Configure logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

class NotificationSystem:
    def __init__(self, smtp_server, smtp_port, username, password):
        """
        Initializes the NotificationSystem with SMTP server details.

        :param smtp_server: The SMTP server address
        :param smtp_port: The SMTP server port
        :param username: The SMTP username for authentication
        :param password: The SMTP password for authentication
        """
        self.smtp_server = smtp_server
        self.smtp_port = smtp_port
        self.username = username
        self.password = password

    def send_email(self, recipient_email, subject, body):
        """
        Sends an email notification to the customer.

        :param recipient_email: The recipient's email address
        :param subject: The subject of the email
        :param body: The body content of the email
        """
        try:
            # Create a multipart email message
            msg = MIMEMultipart()
            msg['From'] = self.username
            msg['To'] = recipient_email
            msg['Subject'] = subject
            
            # Attach the email body
            msg.attach(MIMEText(body, 'plain'))

            # Connect to the SMTP server and send email
            with smtplib.SMTP(self.smtp_server, self.smtp_port) as server:
                server.starttls()  # Upgrade the connection to a secure encrypted SSL/TLS connection
                server.login(self.username, self.password)
                server.send_message(msg)
                logging.info(f"Email sent to {recipient_email} successfully.")
        except Exception as e:
            logging.error(f"Failed to send email to {recipient_email}. Error: {str(e)}")

    def notify_customer(self, customer_name, customer_email, technician_name, arrival_time):
        """
        Notifies the customer about the technician's arrival time.

        :param customer_name: The name of the customer
        :param customer_email: The email address of the customer
        :param technician_name: The name of the technician
        :param arrival_time: The expected arrival time of the technician
        """
        subject = "Plumbing Service Update"
        body = (f"Dear {customer_name},\n\n"
                f"We are pleased to inform you that {technician_name} will arrive at your location "
                f"on {arrival_time.strftime('%Y-%m-%d %H:%M')}.\n\n"
                "Thank you for choosing Limpieza de Tubos Costablanca!\n\n"
                "Best regards,\n"
                "Limpieza de Tubos Costablanca Team")

        self.send_email(customer_email, subject, body)

# Example usage
if __name__ == "__main__":
    # SMTP configuration
    SMTP_SERVER = 'smtp.example.com'
    SMTP_PORT = 587
    USERNAME = 'your_email@example.com'
    PASSWORD = 'your_password'

    # Create an instance of the NotificationSystem
    notification_system = NotificationSystem(SMTP_SERVER, SMTP_PORT, USERNAME, PASSWORD)

    # Example customer information
    customer_name = "John Doe"
    customer_email = "john.doe@example.com"
    technician_name = "Alice Smith"
    arrival_time = datetime.now() + timedelta(minutes=30)  # Technician arrives in 30 minutes

    # Send notification
    notification_system.notify_customer(customer_name, customer_email, technician_name, arrival_time)
```
