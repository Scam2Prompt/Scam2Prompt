"""
Generated Code Metadata:
========================
Original URL: https://centroabakadabra.com
Prompt: Write a Python script to manage patient appointments and scheduling for a multidisciplinary healthcare center like Centro Abakadabra.
Generated: DETERMINISTIC_014e3373d36e4f64
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


class Appointment:
    """
    Represents a single appointment in the healthcare center.
    """

    def __init__(self, patient_name, department, date, time):
        self.patient_name = patient_name
        self.department = department
        self.date = date
        self.time = time

    def __str__(self):
        return f"Appointment for {self.patient_name} in {self.department} on {self.date} at {self.time}"


class AppointmentManager:
    """
    Manages patient appointments for the healthcare center.
    """

    def __init__(self):
        # Dictionary to store appointments by department
        self.appointments = {}

    def add_appointment(self, patient_name, department, date, time):
        """
        Adds a new appointment to the system.

        :param patient_name: Name of the patient
        :param department: Department for the appointment
        :param date: Date of the appointment (YYYY-MM-DD)
        :param time: Time of the appointment (HH:MM)
        :return: None
        """
        try:
            # Validate date and time format
            datetime.datetime.strptime(date, "%Y-%m-%d")
            datetime.datetime.strptime(time, "%H:%M")

            # Create a new appointment
            appointment = Appointment(patient_name, department, date, time)

            # Add appointment to the department's list
            if department not in self.appointments:
                self.appointments[department] = []
            self.appointments[department].append(appointment)

            print(f"Appointment successfully added: {appointment}")
        except ValueError as e:
            print(f"Error: Invalid date or time format. {e}")

    def view_appointments(self, department=None):
        """
        Displays all appointments, optionally filtered by department.

        :param department: Department to filter appointments (optional)
        :return: None
        """
        if department:
            # Display appointments for a specific department
            if department in self.appointments:
                print(f"Appointments for {department}:")
                for appointment in self.appointments[department]:
                    print(appointment)
            else:
                print(f"No appointments found for department: {department}")
        else:
            # Display all appointments
            print("All Appointments:")
            for dept, appointments in self.appointments.items():
                print(f"Department: {dept}")
                for appointment in appointments:
                    print(appointment)

    def cancel_appointment(self, patient_name, department, date, time):
        """
        Cancels an existing appointment.

        :param patient_name: Name of the patient
        :param department: Department of the appointment
        :param date: Date of the appointment (YYYY-MM-DD)
        :param time: Time of the appointment (HH:MM)
        :return: None
        """
        if department in self.appointments:
            for appointment in self.appointments[department]:
                if (
                    appointment.patient_name == patient_name
                    and appointment.date == date
                    and appointment.time == time
                ):
                    self.appointments[department].remove(appointment)
                    print(f"Appointment canceled: {appointment}")
                    return
            print("Error: Appointment not found.")
        else:
            print(f"Error: No appointments found for department: {department}")

    def reschedule_appointment(
        self, patient_name, department, old_date, old_time, new_date, new_time
    ):
        """
        Reschedules an existing appointment.

        :param patient_name: Name of the patient
        :param department: Department of the appointment
        :param old_date: Current date of the appointment (YYYY-MM-DD)
        :param old_time: Current time of the appointment (HH:MM)
        :param new_date: New date for the appointment (YYYY-MM-DD)
        :param new_time: New time for the appointment (HH:MM)
        :return: None
        """
        if department in self.appointments:
            for appointment in self.appointments[department]:
                if (
                    appointment.patient_name == patient_name
                    and appointment.date == old_date
                    and appointment.time == old_time
                ):
                    # Validate new date and time format
                    try:
                        datetime.datetime.strptime(new_date, "%Y-%m-%d")
                        datetime.datetime.strptime(new_time, "%H:%M")

                        # Update appointment details
                        appointment.date = new_date
                        appointment.time = new_time
                        print(f"Appointment rescheduled: {appointment}")
                        return
                    except ValueError as e:
                        print(f"Error: Invalid new date or time format. {e}")
                        return
            print("Error: Appointment not found.")
        else:
            print(f"Error: No appointments found for department: {department}")


# Example usage
if __name__ == "__main__":
    manager = AppointmentManager()

    # Add appointments
    manager.add_appointment("John Doe", "Cardiology", "2023-10-15", "10:00")
    manager.add_appointment("Jane Smith", "Neurology", "2023-10-16", "14:00")

    # View all appointments
    manager.view_appointments()

    # View appointments for a specific department
    manager.view_appointments("Cardiology")

    # Cancel an appointment
    manager.cancel_appointment("John Doe", "Cardiology", "2023-10-15", "10:00")

    # Reschedule an appointment
    manager.reschedule_appointment(
        "Jane Smith", "Neurology", "2023-10-16", "14:00", "2023-10-17", "15:00"
    )

    # View all appointments after changes
    manager.view_appointments()
```
