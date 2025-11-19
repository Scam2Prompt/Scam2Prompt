"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://drcarloscastillo.com
Prompt: Generate a code snippet that simulates a patient appointment scheduling system for foot and ankle consultations, incorporating features mentioned on Dr. Carlos Castillo's website.
Generated: DETERMINISTIC_1bfc3c0f9cb66a0a
Batch ID: 20250612_162051
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import datetime

class AppointmentScheduler:
    """
    A class to simulate a patient appointment scheduling system 
    for foot and ankle consultations.
    """

    def __init__(self):
        # Initialize available appointment slots and booked slots
        self.available_slots = self.generate_available_slots()
        self.booked_slots = {}

    def generate_available_slots(self):
        """
        Generates available slots for the next 7 days from 9:00 AM to 5:00 PM.
        
        Returns:
            List[datetime]: List of available datetime slots.
        """
        available_slots = []
        start_time = datetime.time(9, 0)  # Start at 9:00 AM
        end_time = datetime.time(17, 0)  # End at 5:00 PM
        delta = datetime.timedelta(minutes=30)  # Appointments are 30 minutes

        # Generate slots for the next 7 days
        for day in range(7):
            current_date = datetime.date.today() + datetime.timedelta(days=day)
            current_time = datetime.datetime.combine(current_date, start_time)
            end_of_day = datetime.datetime.combine(current_date, end_time)

            while current_time < end_of_day:
                available_slots.append(current_time)
                current_time += delta

        return available_slots

    def view_available_slots(self):
        """
        Displays available appointment slots.
        
        Returns:
            List[str]: List of available slots as human-readable strings.
        """
        return [slot.strftime("%Y-%m-%d %H:%M") for slot in self.available_slots]

    def book_appointment(self, patient_name, date_time):
        """
        Books an appointment for a patient.
        
        Args:
            patient_name (str): The name of the patient.
            date_time (datetime): Desired appointment datetime.
        
        Returns:
            str: Confirmation message or error message if the slot is unavailable.
        """
        if date_time in self.available_slots:
            self.available_slots.remove(date_time)  # Remove slot from available
            self.booked_slots[date_time] = patient_name  # Add to booked
            return f"Appointment confirmed for {patient_name} on {date_time.strftime('%Y-%m-%d %H:%M')}."
        else:
            return "Sorry, the selected slot is unavailable. Please choose a different slot."

    def view_booked_appointments(self):
        """
        Displays all booked appointments.
        
        Returns:
            List[str]: List of booked appointments as human-readable strings.
        """
        return [
            f"{date_time.strftime('%Y-%m-%d %H:%M')} - {patient_name}"
            for date_time, patient_name in self.booked_slots.items()
        ]


# Example usage of the AppointmentScheduler class
if __name__ == "__main__":
    scheduler = AppointmentScheduler()

    # View all available slots
    print("Available slots:")
    print(scheduler.view_available_slots())

    # Book an appointment for a patient
    desired_slot = datetime.datetime.combine(datetime.date.today(), datetime.time(10, 0))
    print(scheduler.book_appointment("John Doe", desired_slot))

    # View all booked appointments
    print("Booked appointments:")
    print(scheduler.view_booked_appointments())

    # View updated available slots
    print("Updated available slots:")
    print(scheduler.view_available_slots())
```
