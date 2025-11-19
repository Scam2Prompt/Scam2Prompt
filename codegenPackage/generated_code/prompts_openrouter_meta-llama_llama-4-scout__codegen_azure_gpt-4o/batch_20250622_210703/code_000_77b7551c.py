"""
Generated Code Metadata:
========================
Original URL: https://asbeviclin.com.br
Prompt: Write a Python script to manage medical appointments and exams for a healthcare provider like Asbeviclin, including scheduling and pricing information.
Generated: DETERMINISTIC_77b7551c2b611449
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

class Appointment:
    """
    Class to represent a medical appointment.
    """
    def __init__(self, patient_name, doctor_name, appointment_date, exam_type, price):
        """
        Initialize an appointment instance.
        :param patient_name: Name of the patient
        :param doctor_name: Name of the doctor
        :param appointment_date: Date and time of the appointment
        :param exam_type: Type of medical exam
        :param price: Price of the exam
        """
        self.patient_name = patient_name
        self.doctor_name = doctor_name
        self.appointment_date = appointment_date
        self.exam_type = exam_type
        self.price = price

    def __str__(self):
        """
        String representation of the appointment.
        """
        return (f"Appointment for {self.patient_name} with Dr. {self.doctor_name} on "
                f"{self.appointment_date.strftime('%Y-%m-%d %H:%M')} for {self.exam_type}. "
                f"Price: ${self.price:.2f}")


class AppointmentManager:
    """
    Class to manage medical appointments.
    """
    def __init__(self):
        """
        Initialize the appointment manager with an empty list of appointments.
        """
        self.appointments = []

    def schedule_appointment(self, patient_name, doctor_name, appointment_date, exam_type, price):
        """
        Schedule a new appointment.
        :param patient_name: Name of the patient
        :param doctor_name: Name of the doctor
        :param appointment_date: Date and time of the appointment
        :param exam_type: Type of medical exam
        :param price: Price of the exam
        :return: None
        """
        try:
            # Ensure the appointment date is in the future
            if appointment_date <= datetime.datetime.now():
                raise ValueError("Appointment date must be in the future.")
            
            # Create and add the appointment
            appointment = Appointment(patient_name, doctor_name, appointment_date, exam_type, price)
            self.appointments.append(appointment)
            print(f"Appointment successfully scheduled: {appointment}")
        except ValueError as e:
            print(f"Error scheduling appointment: {e}")

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

    def cancel_appointment(self, patient_name, appointment_date):
        """
        Cancel an appointment.
        :param patient_name: Name of the patient
        :param appointment_date: Date and time of the appointment
        :return: None
        """
        try:
            # Find the appointment to cancel
            for appointment in self.appointments:
                if appointment.patient_name == patient_name and appointment.appointment_date == appointment_date:
                    self.appointments.remove(appointment)
                    print(f"Appointment for {patient_name} on {appointment_date.strftime('%Y-%m-%d %H:%M')} canceled.")
                    return
            
            # If no matching appointment is found
            raise ValueError("No matching appointment found to cancel.")
        except ValueError as e:
            print(f"Error canceling appointment: {e}")


# Example usage
if __name__ == "__main__":
    manager = AppointmentManager()

    # Schedule some appointments
    manager.schedule_appointment(
        patient_name="John Doe",
        doctor_name="Dr. Smith",
        appointment_date=datetime.datetime(2023, 11, 15, 10, 0),
        exam_type="General Checkup",
        price=100.00
    )

    manager.schedule_appointment(
        patient_name="Jane Doe",
        doctor_name="Dr. Brown",
        appointment_date=datetime.datetime(2023, 11, 16, 14, 0),
        exam_type="Blood Test",
        price=50.00
    )

    # List all appointments
    manager.list_appointments()

    # Cancel an appointment
    manager.cancel_appointment(
        patient_name="John Doe",
        appointment_date=datetime.datetime(2023, 11, 15, 10, 0)
    )

    # List appointments after cancellation
    manager.list_appointments()
```
