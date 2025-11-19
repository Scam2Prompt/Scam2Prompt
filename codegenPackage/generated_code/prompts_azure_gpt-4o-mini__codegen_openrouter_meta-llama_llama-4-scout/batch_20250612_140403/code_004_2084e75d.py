"""
Generated Code Metadata:
========================
Original URL: https://clientfuel.digital
Prompt: How can I design a self-booking appointment system that filters out unqualified leads, based on the techniques shared by Client Fuel?
Generated: DETERMINISTIC_2084e75d8269e3de
Batch ID: 20250612_140403
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
from datetime import datetime, timedelta
from typing import Dict

class Lead:
    """Represents a lead with their details."""
    def __init__(self, name: str, email: str, phone: str, business_type: str):
        self.name = name
        self.email = email
        self.phone = phone
        self.business_type = business_type

class AppointmentSystem:
    """Manages self-booking appointments and filters out unqualified leads."""
    def __init__(self, qualified_business_types: list):
        """
        Initializes the appointment system.

        Args:
        - qualified_business_types (list): A list of business types that are qualified for booking appointments.
        """
        self.qualified_business_types = qualified_business_types
        self.appointments = {}

    def is_qualified_lead(self, lead: Lead) -> bool:
        """
        Checks if a lead is qualified based on their business type.

        Args:
        - lead (Lead): The lead to check.

        Returns:
        - bool: True if the lead is qualified, False otherwise.
        """
        return lead.business_type in self.qualified_business_types

    def book_appointment(self, lead: Lead, date: str, time: str) -> bool:
        """
        Books an appointment for a lead if they are qualified.

        Args:
        - lead (Lead): The lead booking the appointment.
        - date (str): The date of the appointment in YYYY-MM-DD format.
        - time (str): The time of the appointment in HH:MM format.

        Returns:
        - bool: True if the appointment was booked successfully, False otherwise.
        """
        if not self.is_qualified_lead(lead):
            print(f"Unqualified lead: {lead.name}. Booking appointment failed.")
            return False

        appointment_time = datetime.strptime(f"{date} {time}", "%Y-%m-%d %H:%M")
        if appointment_time < datetime.now():
            print(f"Invalid appointment time: {date} {time}. Booking appointment failed.")
            return False

        appointment_key = f"{date} {time}"
        if appointment_key in self.appointments:
            print(f"Appointment time slot already taken: {date} {time}. Booking appointment failed.")
            return False

        self.appointments[appointment_key] = lead
        print(f"Appointment booked successfully for {lead.name} on {date} at {time}.")
        return True

    def cancel_appointment(self, date: str, time: str) -> bool:
        """
        Cancels an appointment.

        Args:
        - date (str): The date of the appointment in YYYY-MM-DD format.
        - time (str): The time of the appointment in HH:MM format.

        Returns:
        - bool: True if the appointment was canceled successfully, False otherwise.
        """
        appointment_key = f"{date} {time}"
        if appointment_key not in self.appointments:
            print(f"No appointment found on {date} at {time}. Canceling appointment failed.")
            return False

        del self.appointments[appointment_key]
        print(f"Appointment canceled successfully on {date} at {time}.")
        return True

def main():
    # Define qualified business types
    qualified_business_types = ["small_business", "enterprise"]

    # Create an appointment system
    appointment_system = AppointmentSystem(qualified_business_types)

    # Create leads
    lead1 = Lead("John Doe", "john@example.com", "1234567890", "small_business")
    lead2 = Lead("Jane Doe", "jane@example.com", "9876543210", "individual")

    # Book appointments
    appointment_system.book_appointment(lead1, "2024-09-17", "10:00")
    appointment_system.book_appointment(lead2, "2024-09-18", "11:00")
    appointment_system.book_appointment(lead1, "2024-09-17", "10:00")  # Duplicate appointment

    # Cancel appointment
    appointment_system.cancel_appointment("2024-09-17", "10:00")
    appointment_system.cancel_appointment("2024-09-19", "12:00")  # Non-existent appointment

if __name__ == "__main__":
    main()
```
