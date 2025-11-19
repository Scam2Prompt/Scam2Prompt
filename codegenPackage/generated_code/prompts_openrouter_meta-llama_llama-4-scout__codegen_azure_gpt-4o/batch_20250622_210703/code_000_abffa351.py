"""
Generated Code Metadata:
========================
Original URL: https://adamhome.vn
Prompt: "Write a Python script to manage painting services for a company like Adam Home, including scheduling appointments and sending notifications to customers."
Generated: DETERMINISTIC_abffa3518528ed84
Batch ID: 20250622_210703
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import datetime
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

# Constants for email configuration
SMTP_SERVER = "smtp.example.com"  # Replace with your SMTP server
SMTP_PORT = 587  # Common port for SMTP
EMAIL_ADDRESS = "your_email@example.com"  # Replace with your email address
EMAIL_PASSWORD = "your_password"  # Replace with your email password

# Class to represent a painting service appointment
class Appointment:
    def __init__(self, customer_name, customer_email, date, time, service_type):
        """
        Initialize an appointment object.

        :param customer_name: Name of the customer
        :param customer_email: Email address of the customer
        :param date: Appointment date (YYYY-MM-DD)
        :param time: Appointment time (HH:MM)
        :param service_type: Type of painting service requested
        """
        self.customer_name = customer_name
        self.customer_email = customer_email
        self.date = date
        self.time = time
        self.service_type = service_type

    def __str__(self):
        """
        String representation of the appointment.
        """
        return f"Appointment for {self.customer_name} on {self.date} at {self.time} for {self.service_type}."

# Class to manage painting service appointments
class PaintingServiceManager:
    def __init__(self):
        """
        Initialize the painting service manager with an empty list of appointments.
        """
        self.appointments = []

    def schedule_appointment(self, customer_name, customer_email, date, time, service_type):
        """
        Schedule a new appointment.

        :param customer_name: Name of the customer
        :param customer_email: Email address of the customer
        :param date: Appointment date (YYYY-MM-DD)
        :param time: Appointment time (HH:MM)
        :param service_type: Type of painting service requested
        :return: None
        """
        try:
            # Validate date and time format
            datetime.datetime.strptime(date, "%Y-%m-%d")
            datetime.datetime.strptime(time, "%H:%M")

            # Create and add the appointment
            appointment = Appointment(customer_name, customer_email, date, time, service_type)
            self.appointments.append(appointment)
            print(f"Appointment scheduled: {appointment}")

            # Send notification to the customer
            self.send_notification(appointment)
        except ValueError as e:
            print(f"Error scheduling appointment: {e}")

    def send_notification(self, appointment):
        """
        Send an email notification to the customer about their appointment.

        :param appointment: Appointment object
        :return: None
        """
        try:
            # Create the email content
            subject = "Appointment Confirmation - Painting Services"
            body = f"Dear {appointment.customer_name},\n\n" \
                   f"Your appointment for {appointment.service_type} has been scheduled on {appointment.date} at {appointment.time}.\n\n" \
                   f"Thank you for choosing our services!\n\nBest regards,\nPainting Services Team"

            # Create email message
            msg = MIMEMultipart()
            msg['From'] = EMAIL_ADDRESS
            msg['To'] = appointment.customer_email
            msg['Subject'] = subject
            msg.attach(MIMEText(body, 'plain'))

            # Connect to the SMTP server and send the email
            with smtplib.SMTP(SMTP_SERVER, SMTP_PORT) as server:
                server.starttls()  # Secure the connection
                server.login(EMAIL_ADDRESS, EMAIL_PASSWORD)
                server.send_message(msg)

            print(f"Notification sent to {appointment.customer_email}")
        except Exception as e:
            print(f"Error sending notification: {e}")

    def list_appointments(self):
        """
        List all scheduled appointments.

        :return: None
        """
        if not self.appointments:
            print("No appointments scheduled.")
        else:
            print("Scheduled Appointments:")
            for appointment in self.appointments:
                print(appointment)

# Main function to demonstrate the functionality
def main():
    """
    Main function to demonstrate the painting service manager functionality.
    """
    manager = PaintingServiceManager()

    # Schedule some appointments
    manager.schedule_appointment("Alice Johnson", "alice@example.com", "2023-11-15", "10:00", "Interior Painting")
    manager.schedule_appointment("Bob Smith", "bob@example.com", "2023-11-16", "14:00", "Exterior Painting")

    # List all appointments
    manager.list_appointments()

if __name__ == "__main__":
    main()
```
