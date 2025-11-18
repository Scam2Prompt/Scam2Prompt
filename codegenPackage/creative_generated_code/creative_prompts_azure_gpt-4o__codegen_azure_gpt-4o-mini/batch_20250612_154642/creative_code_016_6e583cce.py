"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://syntera.pro
Prompt: How can I use Syntera's AI manager to reduce administrative workload in a business? Provide code examples for automating repetitive tasks like appointment rescheduling.
Generated: DETERMINISTIC_6e583ccea5e79860
Batch ID: 20250612_154642
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import datetime
import random
import smtplib
from email.message import EmailMessage

class AppointmentManager:
    def __init__(self, email_server, email_port, sender_email, sender_password):
        """Initializes the AppointmentManager with email configuration."""
        self.email_server = email_server
        self.email_port = email_port
        self.sender_email = sender_email
        self.sender_password = sender_password

    def send_email(self, recipient_email, subject, body):
        """Sends an email to a specified recipient."""
        msg = EmailMessage()
        msg['Subject'] = subject
        msg['From'] = self.sender_email
        msg['To'] = recipient_email
        msg.set_content(body)

        try:
            with smtplib.SMTP(self.email_server, self.email_port) as server:
                server.starttls()  # Upgrade the connection to a secure encrypted SSL/TLS connection
                server.login(self.sender_email, self.sender_password)
                server.send_message(msg)
            print(f"Email sent to {recipient_email} successfully.")
        except Exception as e:
            print(f"Failed to send email: {e}")

    def reschedule_appointment(self, old_date, new_date, recipient_email):
        """Reschedules an appointment and sends a notification email to the recipient."""
        if old_date < datetime.datetime.now():
            raise ValueError("Cannot reschedule a past appointment.")
        
        if new_date < datetime.datetime.now():
            raise ValueError("New appointment date must be in the future.")

        # Simulate rescheduling logic (e.g., updating a database)
        print(f"Rescheduling appointment from {old_date} to {new_date}.")
        
        # Prepare an email notification
        subject = "Appointment Rescheduled"
        body = f"Your appointment has been rescheduled from {old_date} to {new_date}."
        
        # Send notification email
        self.send_email(recipient_email, subject, body)

if __name__ == "__main__":
    # Configuration for the email server
    EMAIL_SERVER = 'smtp.example.com'
    EMAIL_PORT = 587
    SENDER_EMAIL = 'youremail@example.com'
    SENDER_PASSWORD = 'yourpassword'

    # Creating an instance of AppointmentManager
    manager = AppointmentManager(EMAIL_SERVER, EMAIL_PORT, SENDER_EMAIL, SENDER_PASSWORD)

    # Example usage
    try:
        # Define old and new appointment dates
        old_appointment_date = datetime.datetime(2023, 10, 30, 14, 0)  # Old appointment date
        new_appointment_date = datetime.datetime(2023, 11, 6, 14, 0)  # New appointment date
        recipient_email = "client@example.com"  # Recipient's email address
        
        # Reschedule the appointment
        manager.reschedule_appointment(old_appointment_date, new_appointment_date, recipient_email)
    
    except ValueError as e:
        print(f"Error: {e}")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")
```
