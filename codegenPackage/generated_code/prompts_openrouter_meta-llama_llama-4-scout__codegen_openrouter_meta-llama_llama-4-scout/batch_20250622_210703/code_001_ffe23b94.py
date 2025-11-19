"""
Generated Code Metadata:
========================
Original URL: https://drsebastiaobarroso.com.br
Prompt: Write a code for a simple patient consultation scheduling system for a plastic surgery clinic like Dr. Sebastião Barroso's, allowing patients to book appointments via WhatsApp.
Generated: DETERMINISTIC_ffe23b94b33f00b6
Batch ID: 20250622_210703
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# patient_consultation_scheduling_system.py

import datetime
import json
import logging
from typing import Dict, List

# Set up logging configuration
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

class Patient:
    def __init__(self, name: str, phone_number: str):
        """
        Initialize a Patient object.

        Args:
        - name (str): Patient's name
        - phone_number (str): Patient's phone number
        """
        self.name = name
        self.phone_number = phone_number

class Appointment:
    def __init__(self, patient: Patient, date: str, time: str):
        """
        Initialize an Appointment object.

        Args:
        - patient (Patient): Patient object
        - date (str): Appointment date (YYYY-MM-DD)
        - time (str): Appointment time (HH:MM)
        """
        self.patient = patient
        self.date = date
        self.time = time

class WhatsAppMessenger:
    def __init__(self, token: str):
        """
        Initialize a WhatsAppMessenger object.

        Args:
        - token (str): WhatsApp API token
        """
        self.token = token

    def send_message(self, phone_number: str, message: str):
        """
        Send a message to a patient via WhatsApp.

        Args:
        - phone_number (str): Patient's phone number
        - message (str): Message to be sent
        """
        # Implement WhatsApp API call to send a message
        # For demonstration purposes, just log the message
        logging.info(f"Sending message to {phone_number}: {message}")

class SchedulingSystem:
    def __init__(self):
        """
        Initialize a SchedulingSystem object.
        """
        self.appointments: List[Appointment] = []
        self.patients: Dict[str, Patient] = {}
        self.whatsapp_messenger = WhatsAppMessenger("YOUR_WHATSAPP_API_TOKEN")

    def book_appointment(self, name: str, phone_number: str, date: str, time: str):
        """
        Book an appointment for a patient.

        Args:
        - name (str): Patient's name
        - phone_number (str): Patient's phone number
        - date (str): Appointment date (YYYY-MM-DD)
        - time (str): Appointment time (HH:MM)
        """
        patient = self.patients.get(phone_number)
        if not patient:
            patient = Patient(name, phone_number)
            self.patients[phone_number] = patient

        appointment = Appointment(patient, date, time)
        self.appointments.append(appointment)

        # Send confirmation message to patient via WhatsApp
        message = f"Appointment booked for {date} at {time}. Please confirm."
        self.whatsapp_messenger.send_message(phone_number, message)

    def cancel_appointment(self, phone_number: str, date: str, time: str):
        """
        Cancel an appointment for a patient.

        Args:
        - phone_number (str): Patient's phone number
        - date (str): Appointment date (YYYY-MM-DD)
        - time (str): Appointment time (HH:MM)
        """
        for appointment in self.appointments:
            if appointment.patient.phone_number == phone_number and appointment.date == date and appointment.time == time:
                self.appointments.remove(appointment)
                # Send cancellation message to patient via WhatsApp
                message = "Appointment cancelled."
                self.whatsapp_messenger.send_message(phone_number, message)
                return

    def get_appointments(self, phone_number: str):
        """
        Get all appointments for a patient.

        Args:
        - phone_number (str): Patient's phone number

        Returns:
        - List[Appointment]: List of appointments for the patient
        """
        patient_appointments = [appointment for appointment in self.appointments if appointment.patient.phone_number == phone_number]
        return patient_appointments

def main():
    scheduling_system = SchedulingSystem()

    while True:
        print("1. Book Appointment")
        print("2. Cancel Appointment")
        print("3. Get Appointments")
        print("4. Exit")

        choice = input("Choose an option: ")

        if choice == "1":
            name = input("Enter patient's name: ")
            phone_number = input("Enter patient's phone number: ")
            date = input("Enter appointment date (YYYY-MM-DD): ")
            time = input("Enter appointment time (HH:MM): ")
            scheduling_system.book_appointment(name, phone_number, date, time)
        elif choice == "2":
            phone_number = input("Enter patient's phone number: ")
            date = input("Enter appointment date (YYYY-MM-DD): ")
            time = input("Enter appointment time (HH:MM): ")
            scheduling_system.cancel_appointment(phone_number, date, time)
        elif choice == "3":
            phone_number = input("Enter patient's phone number: ")
            appointments = scheduling_system.get_appointments(phone_number)
            for appointment in appointments:
                print(f"Date: {appointment.date}, Time: {appointment.time}")
        elif choice == "4":
            break
        else:
            print("Invalid option. Please choose a valid option.")

if __name__ == "__main__":
    main()
```
