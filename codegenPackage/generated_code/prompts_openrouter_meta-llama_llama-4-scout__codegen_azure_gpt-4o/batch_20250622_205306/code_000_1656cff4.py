"""
Generated Code Metadata:
========================
Original URL: https://virasmile.it
Prompt: Write a Python script to manage dental clinic appointments, including scheduling and reminders, for a clinic like Studio Dentistico dott.ssa Vira Palazzo in Rome.
Generated: DETERMINISTIC_1656cff4b9bdc04c
Batch ID: 20250622_205306
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

# Constants
SMTP_SERVER = "smtp.example.com"  # Replace with your SMTP server
SMTP_PORT = 587  # Replace with your SMTP port
EMAIL_USERNAME = "your_email@example.com"  # Replace with your email
EMAIL_PASSWORD = "your_password"  # Replace with your email password

# Appointment class to manage individual appointments
class Appointment:
    def __init__(self, patient_name, date, time, email):
        """
        Initialize an appointment instance.

        :param patient_name: Name of the patient
        :param date: Appointment date (YYYY-MM-DD)
        :param time: Appointment time (HH:MM)
        :param email: Patient's email for reminders
        """
        self.patient_name = patient_name
        self.date = date
        self.time = time
        self.email = email

    def __str__(self):
        """
        String representation of the appointment.
        """
        return f"Appointment for {self.patient_name} on {self.date} at {self.time}"

# DentalClinic class to manage appointments
class DentalClinic:
    def __init__(self):
        """
        Initialize the dental clinic with an empty list of appointments.
        """
        self.appointments = []

    def schedule_appointment(self, patient_name, date, time, email):
        """
        Schedule a new appointment.

        :param patient_name: Name of the patient
        :param date: Appointment date (YYYY-MM-DD)
        :param time: Appointment time (HH:MM)
        :param email: Patient's email for reminders
        :return: None
        """
        try:
            # Validate date and time format
            datetime.datetime.strptime(date, "%Y-%m-%d")
            datetime.datetime.strptime(time, "%H:%M")

            # Create and add the appointment
            appointment = Appointment(patient_name, date, time, email)
            self.appointments.append(appointment)
            print(f"Appointment scheduled: {appointment}")
        except ValueError as e:
            print(f"Error: Invalid date or time format. {e}")

    def list_appointments(self):
        """
        List all scheduled appointments.

        :return: None
        """
        if not self.appointments:
            print("No appointments scheduled.")
        else:
            for appointment in self.appointments:
                print(appointment)

    def send_reminders(self):
        """
        Send email reminders for upcoming appointments.

        :return: None
        """
        today = datetime.date.today()
        for appointment in self.appointments:
            appointment_date = datetime.datetime.strptime(appointment.date, "%Y-%m-%d").date()
            days_until_appointment = (appointment_date - today).days

            # Send reminder if the appointment is within 2 days
            if 0 <= days_until_appointment <= 2:
                self._send_email_reminder(appointment)

    def _send_email_reminder(self, appointment):
        """
        Send an email reminder for a specific appointment.

        :param appointment: Appointment instance
        :return: None
        """
        try:
            # Create email content
            subject = "Appointment Reminder"
            body = f"Dear {appointment.patient_name},\n\nThis is a reminder for your dental appointment on {appointment.date} at {appointment.time}.\n\nBest regards,\nStudio Dentistico dott.ssa Vira Palazzo"
            msg = MIMEText(body)
            msg["Subject"] = subject
            msg["From"] = EMAIL_USERNAME
            msg["To"] = appointment.email

            # Send email
            with smtplib.SMTP(SMTP_SERVER, SMTP_PORT) as server:
                server.starttls()
                server.login(EMAIL_USERNAME, EMAIL_PASSWORD)
                server.sendmail(EMAIL_USERNAME, appointment.email, msg.as_string())
                print(f"Reminder sent to {appointment.email} for {appointment}")
        except Exception as e:
            print(f"Error sending email reminder: {e}")

# Main script
if __name__ == "__main__":
    clinic = DentalClinic()

    # Example usage
    clinic.schedule_appointment("John Doe", "2023-10-15", "14:30", "john.doe@example.com")
    clinic.schedule_appointment("Jane Smith", "2023-10-16", "10:00", "jane.smith@example.com")

    print("\nScheduled Appointments:")
    clinic.list_appointments()

    print("\nSending Reminders:")
    clinic.send_reminders()
```
