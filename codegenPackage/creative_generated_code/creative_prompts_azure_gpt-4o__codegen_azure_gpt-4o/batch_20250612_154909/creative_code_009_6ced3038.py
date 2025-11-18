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
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
import datetime

# Constants for email configuration
SMTP_SERVER = 'smtp.example.com'  # Replace with actual SMTP server
SMTP_PORT = 587                  # Common SMTP port
EMAIL_USERNAME = 'your_email@example.com'  # Replace with your email
EMAIL_PASSWORD = 'your_password'  # Replace with your email password

# Notification system class
class PlumbingNotificationSystem:
    def __init__(self):
        # Initialize the notification system
        self.customers = {}  # Dictionary to store customer data (name, email, appointment time)

    def add_customer(self, name, email, appointment_time):
        """
        Adds a customer to the notification system.
        :param name: Customer's name
        :param email: Customer's email address
        :param appointment_time: Scheduled appointment time (datetime object)
        """
        if not isinstance(appointment_time, datetime.datetime):
            raise ValueError("appointment_time must be a datetime object")
        
        self.customers[email] = {
            'name': name,
            'email': email,
            'appointment_time': appointment_time
        }

    def send_notification(self, email, subject, message):
        """
        Sends an email notification to the customer.
        :param email: Recipient's email address
        :param subject: Email subject
        :param message: Email message content
        """
        try:
            # Create the email
            msg = MIMEMultipart()
            msg['From'] = EMAIL_USERNAME
            msg['To'] = email
            msg['Subject'] = subject
            
            # Attach the message body
            msg.attach(MIMEText(message, 'plain'))

            # Connect to the SMTP server and send the email
            with smtplib.SMTP(SMTP_SERVER, SMTP_PORT) as server:
                server.starttls()  # Start TLS encryption
                server.login(EMAIL_USERNAME, EMAIL_PASSWORD)
                server.send_message(msg)
            
            print(f"Notification sent successfully to {email}")
        except Exception as e:
            print(f"Failed to send notification to {email}: {e}")

    def notify_customers(self):
        """
        Sends updates to all customers about their appointment and technician arrival times.
        """
        for customer in self.customers.values():
            name = customer['name']
            email = customer['email']
            appointment_time = customer['appointment_time']
            
            # Generate a friendly message for the customer
            message = (
                f"Hello {name},\n\n"
                f"This is a reminder for your plumbing service appointment.\n"
                f"Your technician is scheduled to arrive on {appointment_time.strftime('%A, %d %B %Y at %I:%M %p')}.\n\n"
                f"Thank you for choosing Limpieza de Tubos Costablanca!"
            )
            subject = "Plumbing Service Appointment Reminder"
            
            # Send the notification
            self.send_notification(email, subject, message)

# Example usage
if __name__ == "__main__":
    # Initialize the notification system
    notification_system = PlumbingNotificationSystem()

    # Add some customers
    notification_system.add_customer(
        name="John Doe",
        email="john.doe@example.com",
        appointment_time=datetime.datetime(2023, 12, 15, 14, 30)
    )
    notification_system.add_customer(
        name="Jane Smith",
        email="jane.smith@example.com",
        appointment_time=datetime.datetime(2023, 12, 16, 10, 0)
    )

    # Notify all customers
    notification_system.notify_customers()
```
