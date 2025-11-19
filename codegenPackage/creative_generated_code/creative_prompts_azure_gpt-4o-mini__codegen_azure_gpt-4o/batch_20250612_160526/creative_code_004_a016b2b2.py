"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://wonderplanet.ee
Prompt: Write a code example that integrates a booking system for party services, referencing the unique offerings of Wonderplanet.ee, including themed parties and special character appearances.
Generated: DETERMINISTIC_a016b2b208ad2bc4
Batch ID: 20250612_160526
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
# booking_system.py

import datetime

class BookingError(Exception):
    """Custom exception for booking errors."""
    pass

class PartyBookingSystem:
    """
    A system to manage party service bookings.
    Features:
    - Themed parties
    - Special character appearances
    """

    def __init__(self):
        self.bookings = []  # List to store bookings

    def create_booking(self, customer_name, event_date, party_theme, special_characters):
        """
        Create a new party booking.
        
        Args:
        - customer_name (str): Name of the customer.
        - event_date (datetime.date): Date of the event.
        - party_theme (str): Theme of the party.
        - special_characters (list): List of characters to appear at the party.

        Returns:
        - dict: Details of the created booking.

        Raises:
        - BookingError: If the event date is in the past.
        """
        if event_date < datetime.date.today():
            raise BookingError("Event date cannot be in the past.")
        
        booking = {
            "customer_name": customer_name,
            "event_date": event_date,
            "party_theme": party_theme,
            "special_characters": special_characters,
            "booking_id": len(self.bookings) + 1
        }

        self.bookings.append(booking)
        return booking

    def view_bookings(self):
        """
        Retrieve all bookings.

        Returns:
        - list: List of all bookings.
        """
        return self.bookings

    def find_booking_by_id(self, booking_id):
        """
        Find a booking by its ID.

        Args:
        - booking_id (int): The unique ID of the booking.

        Returns:
        - dict: Details of the booking if found.
        
        Raises:
        - BookingError: If no booking is found with the given ID.
        """
        for booking in self.bookings:
            if booking["booking_id"] == booking_id:
                return booking
        raise BookingError(f"No booking found with ID {booking_id}.")

# Example usage
if __name__ == "__main__":
    # Instantiate the party booking system
    system = PartyBookingSystem()
    
    try:
        # Create a booking
        booking = system.create_booking(
            customer_name="Alice Smith",
            event_date=datetime.date(2023, 12, 15),
            party_theme="Wonderland Adventure",
            special_characters=["Mad Hatter", "Alice", "White Rabbit"]
        )
        print("Booking created successfully:", booking)
        
        # View all bookings
        print("All bookings:", system.view_bookings())
        
        # Find a specific booking by ID
        print("Booking details by ID:", system.find_booking_by_id(1))
        
    except BookingError as e:
        print("Error:", e)
    except Exception as e:
        print("An unexpected error occurred:", e)
```
