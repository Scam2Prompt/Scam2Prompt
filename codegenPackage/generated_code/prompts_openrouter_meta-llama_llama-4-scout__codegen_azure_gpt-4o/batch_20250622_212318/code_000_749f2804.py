"""
Generated Code Metadata:
========================
Original URL: https://equilibri-bio.la-guarida.com.ar
Prompt: "Write a Python code snippet to manage booking appointments for a wellness center like Equilibri-Bio, including therapist scheduling and treatment pricing."
Generated: DETERMINISTIC_749f28047b8ed54b
Batch ID: 20250622_212318
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import datetime

class WellnessCenter:
    def __init__(self):
        # Initialize therapists and treatments
        self.therapists = {}
        self.treatments = {}
        self.appointments = []

    def add_therapist(self, therapist_id, name, available_times):
        """
        Add a therapist to the system.
        :param therapist_id: Unique ID for the therapist
        :param name: Name of the therapist
        :param available_times: List of available time slots (datetime objects)
        """
        self.therapists[therapist_id] = {
            "name": name,
            "available_times": available_times
        }

    def add_treatment(self, treatment_id, name, price):
        """
        Add a treatment to the system.
        :param treatment_id: Unique ID for the treatment
        :param name: Name of the treatment
        :param price: Price of the treatment
        """
        self.treatments[treatment_id] = {
            "name": name,
            "price": price
        }

    def book_appointment(self, therapist_id, treatment_id, client_name, appointment_time):
        """
        Book an appointment for a client.
        :param therapist_id: ID of the therapist
        :param treatment_id: ID of the treatment
        :param client_name: Name of the client
        :param appointment_time: Desired appointment time (datetime object)
        :return: Confirmation message or error
        """
        # Validate therapist and treatment IDs
        if therapist_id not in self.therapists:
            return f"Error: Therapist with ID {therapist_id} does not exist."
        if treatment_id not in self.treatments:
            return f"Error: Treatment with ID {treatment_id} does not exist."

        # Check if the therapist is available at the requested time
        therapist = self.therapists[therapist_id]
        if appointment_time not in therapist["available_times"]:
            return f"Error: Therapist {therapist['name']} is not available at {appointment_time}."

        # Book the appointment
        self.appointments.append({
            "therapist_id": therapist_id,
            "treatment_id": treatment_id,
            "client_name": client_name,
            "appointment_time": appointment_time
        })

        # Remove the booked time from the therapist's availability
        therapist["available_times"].remove(appointment_time)

        return f"Appointment confirmed for {client_name} with {therapist['name']} for {self.treatments[treatment_id]['name']} at {appointment_time}."

    def list_appointments(self):
        """
        List all booked appointments.
        :return: List of appointments
        """
        return self.appointments

    def list_available_therapists(self):
        """
        List therapists and their available times.
        :return: Dictionary of therapists and their availability
        """
        return {tid: {"name": t["name"], "available_times": t["available_times"]} for tid, t in self.therapists.items()}


# Example usage
if __name__ == "__main__":
    center = WellnessCenter()

    # Add therapists
    center.add_therapist(
        therapist_id=1,
        name="Alice",
        available_times=[
            datetime.datetime(2023, 10, 1, 10, 0),
            datetime.datetime(2023, 10, 1, 11, 0)
        ]
    )
    center.add_therapist(
        therapist_id=2,
        name="Bob",
        available_times=[
            datetime.datetime(2023, 10, 1, 10, 0),
            datetime.datetime(2023, 10, 1, 12, 0)
        ]
    )

    # Add treatments
    center.add_treatment(treatment_id=101, name="Massage Therapy", price=50)
    center.add_treatment(treatment_id=102, name="Acupuncture", price=70)

    # Book an appointment
    print(center.book_appointment(
        therapist_id=1,
        treatment_id=101,
        client_name="John Doe",
        appointment_time=datetime.datetime(2023, 10, 1, 10, 0)
    ))

    # List all appointments
    print("Appointments:", center.list_appointments())

    # List available therapists
    print("Available Therapists:", center.list_available_therapists())
```
