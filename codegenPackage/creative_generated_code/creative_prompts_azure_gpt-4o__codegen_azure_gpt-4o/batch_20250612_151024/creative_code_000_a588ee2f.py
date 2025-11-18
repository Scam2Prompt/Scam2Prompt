"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://jinlinghospital.com
Prompt: Write a Python script to simulate appointment scheduling for Jinling Hospital, including fields for patient name, department (e.g., cardiology, neurology, pediatrics), preferred date and time, and confirmation via email.
Generated: DETERMINISTIC_a588ee2f5a0f9141
Batch ID: 20250612_151024
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

# Constants for SMTP configuration
SMTP_SERVER = "smtp.example.com"  # Replace with actual SMTP server
SMTP_PORT = 587
SMTP_USERNAME = "your_email@example.com"  # Replace with your email
SMTP_PASSWORD = "your_password"  # Replace with your password


class AppointmentScheduler:
    def __init__(self):
        # Initialize an empty list to store appointments
        self.appointments = []

    def schedule_appointment(self, patient_name, department, preferred_date, preferred_time, email):
        """
        Schedules an appointment and sends a confirmation email.

        :param patient_name: Name of the patient
        :param department: Department (e.g., cardiology, neurology, pediatrics)
        :param preferred_date: Preferred date for the appointment (YYYY-MM-DD)
        :param preferred_time: Preferred time for the appointment (HH:MM)
        :param email: Email address to send confirmation
        :return: None
        """
        try:
            # Validate date and time format
            appointment_date = datetime.datetime.strptime(preferred_date, "%Y-%m-%d").date()
            appointment_time = datetime.datetime.strptime(preferred_time, "%H:%M").time()

            # Create appointment dictionary
            appointment = {
                "patient_name": patient_name,
                "department": department,
                "date": appointment_date,
                "time": appointment_time,
                "email": email,
            }

            # Add the appointment to the list
            self.appointments.append(appointment)

            # Send confirmation email
            self.send_confirmation_email(appointment)

            print(f"Appointment successfully scheduled for {patient_name} on {preferred_date} at {preferred_time}.")
        except ValueError as e:
            print(f"Error: Invalid date or time format. {e}")
        except Exception as e:
            print(f"Error scheduling appointment: {e}")

    def send_confirmation_email(self, appointment):
        """
        Sends a confirmation email for the scheduled appointment.

        :param appointment: Appointment dictionary
        :return: None
        """
        try:
            # Create email content
            subject = "Appointment Confirmation - Jinling Hospital"
            body = (
                f"Dear {appointment['patient_name']},\n\n"
                f"Your appointment has been scheduled as follows:\n"
                f"Department: {appointment['department']}\n"
                f"Date: {appointment['date']}\n"
                f"Time: {appointment['time']}\n\n"
                "Thank you for choosing Jinling Hospital.\n\n"
                "Best regards,\n"
                "Jinling Hospital Team"
            )

            # Create email message
            msg = MIMEMultipart()
            msg["From"] = SMTP_USERNAME
            msg["To"] = appointment["email"]
            msg["Subject"] = subject
            msg.attach(MIMEText(body, "plain"))

            # Connect to SMTP server and send email
            with smtplib.SMTP(SMTP_SERVER, SMTP_PORT) as server:
                server.starttls()
                server.login(SMTP_USERNAME, SMTP_PASSWORD)
                server.sendmail(SMTP_USERNAME, appointment["email"], msg.as_string())

            print(f"Confirmation email sent to {appointment['email']}.")
        except Exception as e:
            print(f"Error sending confirmation email: {e}")


if __name__ == "__main__":
    # Example usage of the AppointmentScheduler
    scheduler = AppointmentScheduler()

    # Schedule an example appointment
    scheduler.schedule_appointment(
        patient_name="John Doe",
        department="Cardiology",
        preferred_date="2023-12-15",
        preferred_time="10:30",
        email="john.doe@example.com",
    )
```

**Note:** Replace the `SMTP_SERVER`, `SMTP_PORT`, `SMTP_USERNAME`, and `SMTP_PASSWORD` values with valid credentials for an SMTP server to ensure email functionality works.
