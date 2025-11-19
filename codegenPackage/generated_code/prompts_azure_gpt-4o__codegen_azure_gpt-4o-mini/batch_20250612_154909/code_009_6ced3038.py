"""
Generated Code Metadata:
========================
Original URL: https://www.limpiezadetuboscostablanca.net
Prompt: Write code to integrate a notification system for plumbing service updates, ensuring customers are informed about technician arrival times, as described in the customer-focused approach of Limpieza de Tubos Costablanca.
Generated: DETERMINISTIC_6ced303804a11a2c
Batch ID: 20250612_154909
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
from datetime import datetime, timedelta
import logging

# Configure logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

class NotificationService:
    def __init__(self, smtp_server, smtp_port, smtp_user, smtp_password):
        """
        Initializes the NotificationService with SMTP server details.
        
        :param smtp_server: SMTP server address
        :param smtp_port: SMTP server port
        :param smtp_user: SMTP username
        :param smtp_password: SMTP password
        """
        self.smtp_server = smtp_server
        self.smtp_port = smtp_port
        self.smtp_user = smtp_user
        self.smtp_password = smtp_password

    def send_email(self, recipient_email, subject, body):
        """
        Sends an email notification to the specified recipient.
        
        :param recipient_email: Email address of the recipient
        :param subject: Subject of the email
        :param body: Body content of the email
        """
        try:
            # Create the email message
            msg = MIMEMultipart()
            msg['From'] = self.smtp_user
            msg['To'] = recipient_email
            msg['Subject'] = subject
            
            # Attach the email body
            msg.attach(MIMEText(body, 'plain'))

            # Connect to the SMTP server and send the email
            with smtplib.SMTP(self.smtp_server, self.smtp_port) as server:
                server.starttls()  # Upgrade the connection to a secure encrypted SSL/TLS connection
                server.login(self.smtp_user, self.smtp_password)
                server.send_message(msg)
                logging.info(f"Email sent to {recipient_email} with subject: {subject}")
        except Exception as e:
            logging.error(f"Failed to send email to {recipient_email}: {e}")

    def notify_customer(self, customer_email, technician_name, arrival_time):
        """
        Notifies the customer about the technician's arrival time.
        
        :param customer_email: Email address of the customer
        :param technician_name: Name of the technician
        :param arrival_time: Expected arrival time of the technician
        """
        subject = "Plumbing Service Update: Technician Arrival Time"
        body = (f"Dear Customer,\n\n"
                f"We are pleased to inform you that our technician, {technician_name}, "
                f"is scheduled to arrive at your location on {arrival_time.strftime('%Y-%m-%d %H:%M')}.\n\n"
                f"Thank you for choosing Limpieza de Tubos Costablanca.\n\n"
                f"Best regards,\n"
                f"Limpieza de Tubos Costablanca Team")
        
        self.send_email(customer_email, subject, body)

def main():
    # SMTP configuration (replace with actual values)
    smtp_server = "smtp.example.com"
    smtp_port = 587
    smtp_user = "your_email@example.com"
    smtp_password = "your_password"

    # Create an instance of NotificationService
    notification_service = NotificationService(smtp_server, smtp_port, smtp_user, smtp_password)

    # Example customer and technician details
    customer_email = "customer@example.com"
    technician_name = "John Doe"
    arrival_time = datetime.now() + timedelta(minutes=30)  # Technician arrives in 30 minutes

    # Notify the customer
    notification_service.notify_customer(customer_email, technician_name, arrival_time)

if __name__ == "__main__":
    main()
```
