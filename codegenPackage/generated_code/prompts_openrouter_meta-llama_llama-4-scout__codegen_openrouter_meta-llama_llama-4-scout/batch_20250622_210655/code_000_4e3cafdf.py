"""
Generated Code Metadata:
========================
Original URL: https://drcelsolemos.com.br
Prompt: Write a Python script to manage dental clinic appointments, including scheduling and payment processing, inspired by Dr. Celso Lemos' clinic.
Generated: DETERMINISTIC_4e3cafdfa22faed7
Batch ID: 20250622_210655
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# dental_clinic_appointments.py

from datetime import datetime, timedelta
from enum import Enum

class PaymentStatus(Enum):
    """Payment status enumeration"""
    PENDING = 1
    PAID = 2
    OVERDUE = 3

class Appointment:
    """Represents a dental clinic appointment"""
    def __init__(self, patient_name, appointment_date, appointment_time, procedure):
        self.patient_name = patient_name
        self.appointment_date = appointment_date
        self.appointment_time = appointment_time
        self.procedure = procedure
        self.payment_status = PaymentStatus.PENDING

    def __str__(self):
        return f"Patient: {self.patient_name}, Date: {self.appointment_date}, Time: {self.appointment_time}, Procedure: {self.procedure}, Payment Status: {self.payment_status.name}"

class DentalClinic:
    """Manages dental clinic appointments"""
    def __init__(self):
        self.appointments = []

    def schedule_appointment(self, patient_name, appointment_date, appointment_time, procedure):
        """Schedules a new appointment"""
        try:
            appointment_date = datetime.strptime(appointment_date, "%Y-%m-%d").date()
            appointment_time = datetime.strptime(appointment_time, "%H:%M").time()
            appointment = Appointment(patient_name, appointment_date, appointment_time, procedure)
            self.appointments.append(appointment)
            print(f"Appointment scheduled for {patient_name} on {appointment_date} at {appointment_time}")
        except ValueError:
            print("Invalid date or time format. Please use YYYY-MM-DD for date and HH:MM for time.")

    def view_appointments(self):
        """Displays all scheduled appointments"""
        if not self.appointments:
            print("No appointments scheduled.")
        else:
            for appointment in self.appointments:
                print(appointment)

    def process_payment(self, patient_name, payment_status):
        """Updates payment status for an appointment"""
        for appointment in self.appointments:
            if appointment.patient_name == patient_name:
                appointment.payment_status = payment_status
                print(f"Payment status updated for {patient_name} to {payment_status.name}")
                return
        print(f"No appointment found for {patient_name}")

    def cancel_appointment(self, patient_name):
        """Cancels an appointment"""
        for appointment in self.appointments:
            if appointment.patient_name == patient_name:
                self.appointments.remove(appointment)
                print(f"Appointment cancelled for {patient_name}")
                return
        print(f"No appointment found for {patient_name}")

def main():
    clinic = DentalClinic()

    while True:
        print("\nDental Clinic Appointment Management")
        print("1. Schedule Appointment")
        print("2. View Appointments")
        print("3. Process Payment")
        print("4. Cancel Appointment")
        print("5. Exit")

        choice = input("Choose an option: ")

        if choice == "1":
            patient_name = input("Enter patient name: ")
            appointment_date = input("Enter appointment date (YYYY-MM-DD): ")
            appointment_time = input("Enter appointment time (HH:MM): ")
            procedure = input("Enter procedure: ")
            clinic.schedule_appointment(patient_name, appointment_date, appointment_time, procedure)
        elif choice == "2":
            clinic.view_appointments()
        elif choice == "3":
            patient_name = input("Enter patient name: ")
            print("\nPayment Status")
            print("1. Paid")
            print("2. Pending")
            print("3. Overdue")
            payment_choice = input("Choose a payment status: ")
            if payment_choice == "1":
                clinic.process_payment(patient_name, PaymentStatus.PAID)
            elif payment_choice == "2":
                clinic.process_payment(patient_name, PaymentStatus.PENDING)
            elif payment_choice == "3":
                clinic.process_payment(patient_name, PaymentStatus.OVERDUE)
            else:
                print("Invalid payment status choice.")
        elif choice == "4":
            patient_name = input("Enter patient name: ")
            clinic.cancel_appointment(patient_name)
        elif choice == "5":
            break
        else:
            print("Invalid choice. Please choose a valid option.")

if __name__ == "__main__":
    main()
```
