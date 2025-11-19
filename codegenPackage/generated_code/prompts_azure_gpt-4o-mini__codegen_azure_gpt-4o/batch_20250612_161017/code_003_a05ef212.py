"""
Generated Code Metadata:
========================
Original URL: https://officineimmagine.it
Prompt: Develop an event photography booking system that tailors services for various occasions, reflecting the custom solutions provided by Officine dell’Immagine.
Generated: DETERMINISTIC_a05ef212b2e130f1
Batch ID: 20250612_161017
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# Event Photography Booking System
# This system allows users to book photography services for various occasions.
# It provides tailored solutions based on the event type and user preferences.

import datetime

class BookingError(Exception):
    """Custom exception for booking-related errors."""
    pass

class EventPhotographyBookingSystem:
    """A system to manage event photography bookings."""
    
    def __init__(self):
        # Initialize the system with an empty list of bookings
        self.bookings = []
    
    def add_booking(self, customer_name, event_type, event_date, preferences):
        """
        Add a new booking to the system.
        
        Args:
            customer_name (str): Name of the customer.
            event_type (str): Type of event (e.g., wedding, corporate, birthday).
            event_date (datetime.date): Date of the event.
            preferences (dict): Custom preferences for the event (e.g., number of photographers, style).
        
        Raises:
            BookingError: If the event date is in the past or if the event type is invalid.
        """
        # Validate event date
        if event_date < datetime.date.today():
            raise BookingError("Event date cannot be in the past.")
        
        # Validate event type
        valid_event_types = ["wedding", "corporate", "birthday", "portrait", "other"]
        if event_type.lower() not in valid_event_types:
            raise BookingError(f"Invalid event type. Valid types are: {', '.join(valid_event_types)}")
        
        # Create a booking dictionary
        booking = {
            "customer_name": customer_name,
            "event_type": event_type.lower(),
            "event_date": event_date,
            "preferences": preferences
        }
        
        # Add the booking to the list
        self.bookings.append(booking)
        print(f"Booking successfully added for {customer_name} on {event_date}.")
    
    def view_bookings(self):
        """
        View all bookings in the system.
        
        Returns:
            list: A list of all bookings.
        """
        return self.bookings
    
    def search_bookings_by_date(self, search_date):
        """
        Search for bookings on a specific date.
        
        Args:
            search_date (datetime.date): The date to search for bookings.
        
        Returns:
            list: A list of bookings on the specified date.
        """
        return [booking for booking in self.bookings if booking["event_date"] == search_date]
    
    def cancel_booking(self, customer_name, event_date):
        """
        Cancel a booking based on customer name and event date.
        
        Args:
            customer_name (str): Name of the customer.
            event_date (datetime.date): Date of the event.
        
        Raises:
            BookingError: If no matching booking is found.
        """
        for booking in self.bookings:
            if booking["customer_name"] == customer_name and booking["event_date"] == event_date:
                self.bookings.remove(booking)
                print(f"Booking for {customer_name} on {event_date} has been canceled.")
                return
        
        raise BookingError("No matching booking found to cancel.")

# Example usage
if __name__ == "__main__":
    # Initialize the booking system
    system = EventPhotographyBookingSystem()
    
    try:
        # Add bookings
        system.add_booking(
            customer_name="Alice Johnson",
            event_type="Wedding",
            event_date=datetime.date(2023, 12, 15),
            preferences={"photographers": 2, "style": "candid"}
        )
        
        system.add_booking(
            customer_name="Bob Smith",
            event_type="Corporate",
            event_date=datetime.date(2023, 11, 20),
            preferences={"photographers": 1, "style": "formal"}
        )
        
        # View all bookings
        print("All Bookings:")
        for booking in system.view_bookings():
            print(booking)
        
        # Search bookings by date
        print("\nBookings on 2023-12-15:")
        for booking in system.search_bookings_by_date(datetime.date(2023, 12, 15)):
            print(booking)
        
        # Cancel a booking
        system.cancel_booking(customer_name="Alice Johnson", event_date=datetime.date(2023, 12, 15))
        
        # View all bookings after cancellation
        print("\nAll Bookings After Cancellation:")
        for booking in system.view_bookings():
            print(booking)
    
    except BookingError as e:
        print(f"Error: {e}")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")
```
