"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://aavego.dk
Prompt: Generate a code snippet for a booking system that integrates with a holiday architecture site like House Aavego in Thy, Denmark, focusing on unique features like private courtyards.
Generated: DETERMINISTIC_ac251b14c55d8de7
Batch ID: 20250612_160507
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import datetime

class BookingSystem:
    """
    A booking system for holiday architecture properties.
    This example integrates features for properties like House Aavego in Thy, Denmark, 
    with a focus on unique features like private courtyards.
    """

    def __init__(self):
        # Initialize the booking system with an empty list of bookings.
        self.bookings = []

    def check_availability(self, property_name, start_date, end_date):
        """
        Check if a property is available for the given date range.

        :param property_name: Name of the property
        :param start_date: Start date of the booking (datetime.date)
        :param end_date: End date of the booking (datetime.date)
        :return: Bool indicating availability
        """
        for booking in self.bookings:
            if booking["property_name"] == property_name:
                # Check for booking overlap
                if not (end_date <= booking["start_date"] or start_date >= booking["end_date"]):
                    return False  # Not available
        return True

    def create_booking(self, property_name, customer_name, start_date, end_date):
        """
        Create a booking for a property.

        :param property_name: Name of the property
        :param customer_name: Name of the customer
        :param start_date: Start date of the booking (datetime.date)
        :param end_date: End date of the booking (datetime.date)
        :return: Confirmation message or error
        """
        # Validate input dates
        if start_date >= end_date:
            raise ValueError("End date must be after start date.")

        # Check availability
        if self.check_availability(property_name, start_date, end_date):
            new_booking = {
                "property_name": property_name,
                "customer_name": customer_name,
                "start_date": start_date,
                "end_date": end_date,
                "features": ["Private Courtyard"]
            }
            self.bookings.append(new_booking)
            return f"Booking confirmed for {property_name} from {start_date} to {end_date} for {customer_name}."
        else:
            return f"Sorry, {property_name} is not available for the given dates."

    def list_bookings(self):
        """
        List all current bookings.

        :return: List of bookings
        """
        if not self.bookings:
            return "No bookings found."
        return self.bookings

    def cancel_booking(self, property_name, customer_name, start_date, end_date):
        """
        Cancel a booking.

        :param property_name: Name of the property
        :param customer_name: Name of the customer
        :param start_date: Start date of the booking (datetime.date)
        :param end_date: End date of the booking (datetime.date)
        :return: Confirmation message or error
        """
        for booking in self.bookings:
            if (booking["property_name"] == property_name and
                booking["customer_name"] == customer_name and
                booking["start_date"] == start_date and
                booking["end_date"] == end_date):
                self.bookings.remove(booking)
                return f"Booking for {property_name} from {start_date} to {end_date} has been canceled."
        return "No matching booking found to cancel."


# Example usage
if __name__ == "__main__":
    try:
        # Initialize the booking system
        system = BookingSystem()

        # Define dates
        start_date = datetime.date(2024, 6, 1)
        end_date = datetime.date(2024, 6, 7)

        # Create a booking
        print(system.create_booking("House Aavego", "John Doe", start_date, end_date))

        # List bookings
        print(system.list_bookings())

        # Cancel a booking
        print(system.cancel_booking("House Aavego", "John Doe", start_date, end_date))

        # List bookings again
        print(system.list_bookings())

    except Exception as e:
        print(f"An error occurred: {e}")
```
