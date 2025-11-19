"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://blasterturismo.com
Prompt: Generate a code snippet to create a travel package booking system for Blaster Agência de Turismo, including options for 1 to 4-day itineraries in Ametista do Sul.
Generated: DETERMINISTIC_a99fb1488c51993a
Batch ID: 20250612_162050
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import datetime

class Itinerary:
    """Class to represent a travel itinerary."""

    def __init__(self, duration, activities):
        """
        Initializes a new Itinerary.
        
        :param duration: Duration of the itinerary in days (1 to 4).
        :param activities: List of activities included in the itinerary.
        """
        if duration < 1 or duration > 4:
            raise ValueError("Duration must be between 1 and 4 days.")
        
        self.duration = duration
        self.activities = activities
        self.start_date = None

    def set_start_date(self, start_date):
        """Sets the start date for the itinerary."""
        if not isinstance(start_date, datetime.date):
            raise ValueError("Start date must be a datetime.date object.")
        
        self.start_date = start_date

    def get_itinerary_summary(self):
        """Returns a summary of the itinerary."""
        summary = f"Itinerary Duration: {self.duration} days\n"
        summary += "Activities:\n"
        for activity in self.activities:
            summary += f" - {activity}\n"
        if self.start_date:
            summary += f"Start Date: {self.start_date.strftime('%Y-%m-%d')}\n"
        return summary


class BookingSystem:
    """Class to manage the travel package booking system."""

    def __init__(self):
        """Initializes a new Booking System with no itineraries."""
        self.itineraries = []

    def create_itinerary(self, duration, activities):
        """
        Creates a new itinerary and adds it to the booking system.
        
        :param duration: Duration of the itinerary in days (1 to 4).
        :param activities: List of activities included in the itinerary.
        :return: The created Itinerary object.
        """
        try:
            itinerary = Itinerary(duration, activities)
            self.itineraries.append(itinerary)
            return itinerary
        except ValueError as e:
            print(f"Error creating itinerary: {e}")

    def get_all_itineraries(self):
        """Returns a list of all itineraries in the booking system."""
        return self.itineraries


# Example usage
if __name__ == "__main__":
    booking_system = BookingSystem()

    # Creating itineraries
    itinerary1 = booking_system.create_itinerary(3, ["City Tour", "Museum Visit", "Local Cuisine Tasting"])
    itinerary1.set_start_date(datetime.date(2024, 5, 1))

    itinerary2 = booking_system.create_itinerary(2, ["Hiking", "Waterfall Visit"])
    itinerary2.set_start_date(datetime.date(2024, 6, 10))

    # Displaying itineraries
    for itinerary in booking_system.get_all_itineraries():
        print(itinerary.get_itinerary_summary())
```
