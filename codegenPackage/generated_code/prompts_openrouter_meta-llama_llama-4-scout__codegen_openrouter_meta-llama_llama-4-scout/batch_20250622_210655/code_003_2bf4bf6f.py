"""
Generated Code Metadata:
========================
Original URL: https://okulistatrzebnica.pl
Prompt: Write a Python script to manage the appointment schedule for an ophthalmology clinic, including storing patient information, scheduling appointments, and sending reminders.
Generated: DETERMINISTIC_2bf4bf6f1b9115d2
Batch ID: 20250622_210655
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import datetime
import json
import os
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

class Patient:
    """Represents a patient with their information."""

    def __init__(self, name, email, phone):
        """
        Initializes a Patient object.

        Args:
            name (str): The patient's name.
            email (str): The patient's email address.
            phone (str): The patient's phone number.
        """
        self.name = name
        self.email = email
        self.phone = phone

class Appointment:
    """Represents an appointment with a patient."""

    def __init__(self, patient, date, time):
        """
        Initializes an Appointment object.

        Args:
            patient (Patient): The patient for the appointment.
            date (str): The date of the appointment (YYYY-MM-DD).
            time (str): The time of the appointment (HH:MM).
        """
        self.patient = patient
        self.date = date
        self.time = time

class OphthalmologyClinic:
    """Manages the appointment schedule for an ophthalmology clinic."""

    def __init__(self, patients_file='patients.json', appointments_file='appointments.json'):
        """
        Initializes an OphthalmologyClinic object.

        Args:
            patients_file (str): The file to store patient information.
            appointments_file (str): The file to store appointment information.
        """
        self.patients_file = patients_file
        self.appointments_file = appointments_file
        self.patients = self.load_patients()
        self.appointments = self.load_appointments()

    def load_patients(self):
        """Loads patient information from the patients file."""
        if os.path.exists(self.patients_file):
            with open(self.patients_file, 'r') as f:
                data = json.load(f)
                return {patient['email']: Patient(patient['name'], patient['email'], patient['phone']) for patient in data}
        else:
            return {}

    def save_patients(self):
        """Saves patient information to the patients file."""
        data = [{'name': patient.name, 'email': patient.email, 'phone': patient.phone} for patient in self.patients.values()]
        with open(self.patients_file, 'w') as f:
            json.dump(data, f, indent=4)

    def load_appointments(self):
        """Loads appointment information from the appointments file."""
        if os.path.exists(self.appointments_file):
            with open(self.appointments_file, 'r') as f:
                data = json.load(f)
                return {f"{appointment['date']} {appointment['time']}": Appointment(self.patients.get(appointment['patient_email']), appointment['date'], appointment['time']) for appointment in data}
        else:
            return {}

    def save_appointments(self):
        """Saves appointment information to the appointments file."""
        data = [{'patient_email': appointment.patient.email, 'date': appointment.date, 'time': appointment.time} for appointment in self.appointments.values()]
        with open(self.appointments_file, 'w') as f:
            json.dump(data, f, indent=4)

    def add_patient(self, name, email, phone):
        """
        Adds a new patient.

        Args:
            name (str): The patient's name.
            email (str): The patient's email address.
            phone (str): The patient's phone number.

        Raises:
            ValueError: If a patient with the same email already exists.
        """
        if email in self.patients:
            raise ValueError("Patient with the same email already exists")
        self.patients[email] = Patient(name, email, phone)
        self.save_patients()

    def schedule_appointment(self, patient_email, date, time):
        """
        Schedules a new appointment.

        Args:
            patient_email (str): The email of the patient.
            date (str): The date of the appointment (YYYY-MM-DD).
            time (str): The time of the appointment (HH:MM).

        Raises:
            ValueError: If the patient does not exist or an appointment with the same date and time already exists.
        """
        if patient_email not in self.patients:
            raise ValueError("Patient does not exist")
        if f"{date} {time}" in self.appointments:
            raise ValueError("Appointment with the same date and time already exists")
        self.appointments[f"{date} {time}"] = Appointment(self.patients[patient_email], date, time)
        self.save_appointments()

    def send_reminders(self):
        """Sends reminders for upcoming appointments."""
        today = datetime.date.today().strftime('%Y-%m-%d')
        for appointment in self.appointments.values():
            appointment_date = datetime.datetime.strptime(appointment.date, '%Y-%m-%d')
            if appointment_date >= datetime.datetime.today() and appointment_date <= datetime.datetime.today() + datetime.timedelta(days=1):
                self.send_email(appointment.patient.email, f"Reminder: Appointment on {appointment.date} at {appointment.time}")

    def send_email(self, recipient, message):
        """
        Sends an email to the recipient.

        Args:
            recipient (str): The recipient's email address.
            message (str): The email message.

        Raises:
            Exception: If there is an error sending the email.
        """
        try:
            msg = MIMEMultipart()
            msg['From'] = 'your-email@gmail.com'
            msg['To'] = recipient
            msg.attach(MIMEText(message, 'plain'))
            server = smtplib.SMTP('smtp.gmail.com', 587)
            server.starttls()
            server.login(msg['From'], 'your-password')
            text = msg.as_string()
            server.sendmail(msg['From'], msg['To'], text)
            server.quit()
        except Exception as e:
            print(f"Error sending email: {e}")

def main():
    clinic = OphthalmologyClinic()

    while True:
        print("\n1. Add patient")
        print("2. Schedule appointment")
        print("3. Send reminders")
        print("4. Exit")
        choice = input("Choose an option: ")

        if choice == '1':
            name = input("Enter patient name: ")
            email = input("Enter patient email: ")
            phone = input("Enter patient phone: ")
            try:
                clinic.add_patient(name, email, phone)
                print("Patient added successfully")
            except ValueError as e:
                print(str(e))
        elif choice == '2':
            patient_email = input("Enter patient email: ")
            date = input("Enter appointment date (YYYY-MM-DD): ")
            time = input("Enter appointment time (HH:MM): ")
            try:
                clinic.schedule_appointment(patient_email, date, time)
                print("Appointment scheduled successfully")
            except ValueError as e:
                print(str(e))
        elif choice == '3':
            clinic.send_reminders()
            print("Reminders sent successfully")
        elif choice == '4':
            break
        else:
            print("Invalid option")

if __name__ == '__main__':
    main()
```
