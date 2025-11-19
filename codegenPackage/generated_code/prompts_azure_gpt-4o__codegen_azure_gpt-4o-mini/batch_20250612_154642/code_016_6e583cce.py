"""
Generated Code Metadata:
========================
Original URL: https://syntera.pro
Prompt: How can I use Syntera's AI manager to reduce administrative workload in a business? Provide code examples for automating repetitive tasks like appointment rescheduling.
Generated: DETERMINISTIC_6e583ccea5e79860
Batch ID: 20250612_154642
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import datetime
import random
import smtplib
from email.mime.text import MIMEText
from typing import List, Dict

class Appointment:
    """Class to represent an appointment."""
    
    def __init__(self, appointment_id: int, date: datetime.date, time: datetime.time, client_email: str):
        self.appointment_id = appointment_id
        self.date = date
        self.time = time
        self.client_email = client_email

    def __str__(self):
        return f"Appointment(ID: {self.appointment_id}, Date: {self.date}, Time: {self.time}, Client: {self.client_email})"

class AppointmentManager:
    """Class to manage appointments and automate rescheduling."""
    
    def __init__(self):
        self.appointments: List[Appointment] = []

    def add_appointment(self, appointment: Appointment):
        """Add a new appointment to the list."""
        self.appointments.append(appointment)

    def reschedule_appointment(self, appointment_id: int, new_date: datetime.date, new_time: datetime.time):
        """Reschedule an existing appointment."""
        for appointment in self.appointments:
            if appointment.appointment_id == appointment_id:
                appointment.date = new_date
                appointment.time = new_time
                self.send_confirmation_email(appointment)
                return appointment
        raise ValueError("Appointment ID not found.")

    def send_confirmation_email(self, appointment: Appointment):
        """Send a confirmation email to the client about the rescheduled appointment."""
        subject = "Appointment Rescheduled"
        body = f"Your appointment has been rescheduled to {appointment.date} at {appointment.time}."
        self.send_email(appointment.client_email, subject, body)

    @staticmethod
    def send_email(to_email: str, subject: str, body: str):
        """Send an email using SMTP."""
        try:
            # Configure your SMTP server and credentials
            smtp_server = "smtp.example.com"
            smtp_port = 587
            smtp_user = "your_email@example.com"
            smtp_password = "your_password"

            msg = MIMEText(body)
            msg['Subject'] = subject
            msg['From'] = smtp_user
            msg['To'] = to_email

            with smtplib.SMTP(smtp_server, smtp_port) as server:
                server.starttls()  # Upgrade the connection to a secure encrypted SSL/TLS connection
                server.login(smtp_user, smtp_password)
                server.send_message(msg)
        except Exception as e:
            print(f"Failed to send email: {e}")

# Example usage
if __name__ == "__main__":
    manager = AppointmentManager()
    
    # Adding some appointments
    manager.add_appointment(Appointment(1, datetime.date(2023, 10, 15), datetime.time(14, 30), "client1@example.com"))
    manager.add_appointment(Appointment(2, datetime.date(2023, 10, 16), datetime.time(10, 0), "client2@example.com"))

    # Rescheduling an appointment
    try:
        rescheduled_appointment = manager.reschedule_appointment(1, datetime.date(2023, 10, 20), datetime.time(15, 0))
        print(f"Rescheduled: {rescheduled_appointment}")
    except ValueError as e:
        print(e)
```
