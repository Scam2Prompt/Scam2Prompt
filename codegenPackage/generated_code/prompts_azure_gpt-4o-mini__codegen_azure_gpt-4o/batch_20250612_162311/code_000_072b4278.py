"""
Generated Code Metadata:
========================
Original URL: https://cliniquerobinpaul.com
Prompt: Generate a code snippet for a booking system that allows patients to schedule appointments with a chiropractor or osteopath, similar to the services offered at Clinique Robin Paul & Fils.
Generated: DETERMINISTIC_072b4278a4a5457e
Batch ID: 20250612_162311
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import datetime

class BookingSystem:
    def __init__(self):
        # Initialize the booking system with available practitioners and appointments
        self.practitioners = ["Chiropractor", "Osteopath"]
        self.appointments = []  # List to store all scheduled appointments

    def display_practitioners(self):
        # Display available practitioners
        print("Available Practitioners:")
        for index, practitioner in enumerate(self.practitioners, start=1):
            print(f"{index}. {practitioner}")

    def schedule_appointment(self, patient_name, practitioner_choice, appointment_date):
        """
        Schedule an appointment for a patient.
        :param patient_name: Name of the patient
        :param practitioner_choice: Index of the chosen practitioner
        :param appointment_date: Desired appointment date (datetime object)
        """
        try:
            # Validate practitioner choice
            if practitioner_choice < 1 or practitioner_choice > len(self.practitioners):
                raise ValueError("Invalid practitioner choice.")

            # Validate appointment date
            if appointment_date < datetime.datetime.now():
                raise ValueError("Appointment date must be in the future.")

            # Create appointment record
            practitioner = self.practitioners[practitioner_choice - 1]
            appointment = {
                "patient_name": patient_name,
                "practitioner": practitioner,
                "appointment_date": appointment_date
            }

            # Add appointment to the list
            self.appointments.append(appointment)
            print(f"Appointment successfully scheduled for {patient_name} with {practitioner} on {appointment_date}.")

        except ValueError as e:
            print(f"Error: {e}")
        except Exception as e:
            print(f"An unexpected error occurred: {e}")

    def view_appointments(self):
        # Display all scheduled appointments
        if not self.appointments:
            print("No appointments scheduled.")
            return

        print("Scheduled Appointments:")
        for index, appointment in enumerate(self.appointments, start=1):
            print(f"{index}. {appointment['patient_name']} - {appointment['practitioner']} on {appointment['appointment_date']}")

# Example usage
if __name__ == "__main__":
    booking_system = BookingSystem()

    # Display practitioners
    booking_system.display_practitioners()

    # Schedule appointments
    try:
        patient_name = input("Enter patient name: ")
        practitioner_choice = int(input("Choose a practitioner (1 for Chiropractor, 2 for Osteopath): "))
        appointment_date_str = input("Enter appointment date (YYYY-MM-DD HH:MM): ")
        appointment_date = datetime.datetime.strptime(appointment_date_str, "%Y-%m-%d %H:%M")

        booking_system.schedule_appointment(patient_name, practitioner_choice, appointment_date)
    except ValueError as e:
        print(f"Error: {e}")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")

    # View all appointments
    booking_system.view_appointments()
```
