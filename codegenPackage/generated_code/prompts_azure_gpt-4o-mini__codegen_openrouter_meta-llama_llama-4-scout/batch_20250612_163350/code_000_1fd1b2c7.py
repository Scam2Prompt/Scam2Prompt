"""
Generated Code Metadata:
========================
Original URL: https://duchessgarden.sn
Prompt: Generate a code snippet to create a booking system for spa treatments like massages and beauty services, similar to those offered at Duchess Garden.
Generated: DETERMINISTIC_1fd1b2c7ccfadfa0
Batch ID: 20250612_163350
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
from datetime import datetime, timedelta
from enum import Enum

# Define an Enum for treatment types
class TreatmentType(Enum):
    MASSAGE = "Massage"
    FACIAL = "Facial"
    MANICURE = "Manicure"
    PEDICURE = "Pedicure"

# Define a class for Treatment
class Treatment:
    def __init__(self, treatment_type, duration, price):
        """
        Initialize a Treatment object.

        Args:
            treatment_type (TreatmentType): The type of treatment.
            duration (int): The duration of the treatment in minutes.
            price (float): The price of the treatment.
        """
        self.treatment_type = treatment_type
        self.duration = duration
        self.price = price

# Define a class for Booking
class Booking:
    def __init__(self, customer_name, treatment, start_time):
        """
        Initialize a Booking object.

        Args:
            customer_name (str): The name of the customer.
            treatment (Treatment): The treatment being booked.
            start_time (datetime): The start time of the booking.
        """
        self.customer_name = customer_name
        self.treatment = treatment
        self.start_time = start_time
        self.end_time = start_time + timedelta(minutes=treatment.duration)

    def __str__(self):
        return f"Booking for {self.customer_name}: {self.treatment.treatment_type.value} from {self.start_time.strftime('%Y-%m-%d %H:%M')} to {self.end_time.strftime('%Y-%m-%d %H:%M')}"

# Define a class for SpaBookingSystem
class SpaBookingSystem:
    def __init__(self):
        """
        Initialize a SpaBookingSystem object.
        """
        self.treatments = []
        self.bookings = []

    def add_treatment(self, treatment):
        """
        Add a treatment to the system.

        Args:
            treatment (Treatment): The treatment to add.
        """
        self.treatments.append(treatment)

    def book_treatment(self, customer_name, treatment_type, start_time):
        """
        Book a treatment.

        Args:
            customer_name (str): The name of the customer.
            treatment_type (TreatmentType): The type of treatment.
            start_time (datetime): The start time of the booking.

        Returns:
            Booking: The booked treatment, or None if the treatment is not available.
        """
        treatment = next((t for t in self.treatments if t.treatment_type == treatment_type), None)
        if treatment is None:
            print(f"Treatment {treatment_type.value} not available.")
            return None

        # Check for conflicts with existing bookings
        for booking in self.bookings:
            if start_time < booking.end_time and start_time + timedelta(minutes=treatment.duration) > booking.start_time:
                print("Time slot not available.")
                return None

        booking = Booking(customer_name, treatment, start_time)
        self.bookings.append(booking)
        return booking

    def print_bookings(self):
        """
        Print all bookings.
        """
        for booking in self.bookings:
            print(booking)

def main():
    # Create a spa booking system
    system = SpaBookingSystem()

    # Add treatments
    system.add_treatment(Treatment(TreatmentType.MASSAGE, 60, 50.0))
    system.add_treatment(Treatment(TreatmentType.FACIAL, 90, 75.0))

    # Book treatments
    booking1 = system.book_treatment("John Doe", TreatmentType.MASSAGE, datetime(2024, 9, 16, 10, 0))
    booking2 = system.book_treatment("Jane Doe", TreatmentType.FACIAL, datetime(2024, 9, 16, 11, 0))
    booking3 = system.book_treatment("John Doe", TreatmentType.MASSAGE, datetime(2024, 9, 16, 10, 30))  # Should conflict with booking1

    # Print bookings
    system.print_bookings()

if __name__ == "__main__":
    main()
```
