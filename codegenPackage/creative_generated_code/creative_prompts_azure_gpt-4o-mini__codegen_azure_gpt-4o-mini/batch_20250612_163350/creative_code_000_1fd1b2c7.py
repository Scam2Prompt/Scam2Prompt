"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://duchessgarden.sn
Prompt: Generate a code snippet to create a booking system for spa treatments like massages and beauty services, similar to those offered at Duchess Garden.
Generated: DETERMINISTIC_1fd1b2c7ccfadfa0
Batch ID: 20250612_163350
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
from datetime import datetime, timedelta
from typing import List, Optional, Dict

# Define a class to represent a spa treatment
class Treatment:
    def __init__(self, name: str, duration: int, price: float):
        """
        Initialize a treatment with a name, duration (in minutes), and price.
        :param name: Name of the treatment.
        :param duration: Duration of the treatment in minutes.
        :param price: Price of the treatment.
        """
        self.name = name
        self.duration = duration
        self.price = price

# Define a class to represent a booking
class Booking:
    def __init__(self, treatment: Treatment, customer_name: str, booking_time: datetime):
        """
        Initialize a booking for a specific treatment.
        :param treatment: The Treatment object.
        :param customer_name: Name of the customer making the booking.
        :param booking_time: The datetime for the booking.
        """
        self.treatment = treatment
        self.customer_name = customer_name
        self.booking_time = booking_time

# Define the BookingSystem class to manage treatments and bookings
class BookingSystem:
    def __init__(self):
        """
        Initialize the booking system with a list of treatments and bookings.
        """
        self.treatments: List[Treatment] = []
        self.bookings: List[Booking] = []

    def add_treatment(self, name: str, duration: int, price: float) -> None:
        """
        Add a new treatment to the system.
        :param name: Name of the treatment.
        :param duration: Duration of the treatment in minutes.
        :param price: Price of the treatment.
        """
        treatment = Treatment(name, duration, price)
        self.treatments.append(treatment)

    def book_treatment(self, treatment_name: str, customer_name: str, booking_time: datetime) -> Optional[Booking]:
        """
        Book a treatment for a customer.
        :param treatment_name: Name of the treatment to book.
        :param customer_name: Name of the customer making the booking.
        :param booking_time: The datetime for the booking.
        :return: The created Booking object or None if treatment is not found.
        """
        treatment = self.find_treatment(treatment_name)
        if treatment:
            booking = Booking(treatment, customer_name, booking_time)
            self.bookings.append(booking)
            return booking
        print("Treatment not found!")
        return None

    def find_treatment(self, name: str) -> Optional[Treatment]:
        """
        Find a treatment by name.
        :param name: The name of the treatment to search for.
        :return: The Treatment object or None if not found.
        """
        for treatment in self.treatments:
            if treatment.name.lower() == name.lower():
                return treatment
        return None

    def list_treatments(self) -> List[Dict[str, str]]:
        """
        List all available treatments with their details.
        :return: A list of dictionaries containing treatment details.
        """
        return [{'name': treatment.name, 'duration': treatment.duration, 'price': treatment.price} for treatment in self.treatments]

# Example usage:
if __name__ == "__main__":
    booking_system = BookingSystem()
    
    # Add treatments
    booking_system.add_treatment("Aromatherapy Massage", 60, 80.0)
    booking_system.add_treatment("Facial Treatment", 45, 70.0)

    # List treatments
    treatments = booking_system.list_treatments()
    print("Available Treatments:", treatments)

    # Book a treatment
    booking_time = datetime.now() + timedelta(days=1)  # Book for tomorrow
    booking = booking_system.book_treatment("Aromatherapy Massage", "John Doe", booking_time)
    
    if booking:
        print(f"Booking confirmed for {booking.customer_name} on {booking.booking_time} for {booking.treatment.name}.")
```
