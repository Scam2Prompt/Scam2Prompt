"""
Generated Code Metadata:
========================
Original URL: https://windscreensreplacementmelbourne.com.au
Prompt: Write a code snippet for a booking system that allows users to schedule windscreen repairs, inspired by the services offered at Cheap Windscreens Melbourne.
Generated: DETERMINISTIC_bf7ceeac45cde606
Batch ID: 20250612_164058
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
from datetime import datetime, timedelta
import json

class BookingSystem:
    def __init__(self):
        # Initialize an empty list to store bookings
        self.bookings = []

    def add_booking(self, customer_name, contact_number, repair_date):
        """
        Adds a new booking to the system.

        :param customer_name: Name of the customer
        :param contact_number: Contact number of the customer
        :param repair_date: Date and time for the repair
        :raises ValueError: If the repair date is in the past or not a valid datetime
        """
        if repair_date < datetime.now():
            raise ValueError("Repair date must be in the future.")
        
        booking = {
            'customer_name': customer_name,
            'contact_number': contact_number,
            'repair_date': repair_date.strftime("%Y-%m-%d %H:%M:%S")
        }
        self.bookings.append(booking)
        print(f"Booking confirmed for {customer_name} on {repair_date}.")

    def view_bookings(self):
        """Displays all current bookings."""
        if not self.bookings:
            print("No bookings found.")
            return
        
        print("Current Bookings:")
        for booking in self.bookings:
            print(f"Customer: {booking['customer_name']}, Contact: {booking['contact_number']}, Date: {booking['repair_date']}")

    def save_bookings(self, filename='bookings.json'):
        """
        Saves the current bookings to a JSON file.

        :param filename: Name of the file to save bookings
        """
        try:
            with open(filename, 'w') as file:
                json.dump(self.bookings, file, indent=4)
            print(f"Bookings saved to {filename}.")
        except IOError as e:
            print(f"Error saving bookings: {e}")

    def load_bookings(self, filename='bookings.json'):
        """
        Loads bookings from a JSON file.

        :param filename: Name of the file to load bookings from
        """
        try:
            with open(filename, 'r') as file:
                self.bookings = json.load(file)
            print(f"Bookings loaded from {filename}.")
        except (IOError, json.JSONDecodeError) as e:
            print(f"Error loading bookings: {e}")

# Example usage
if __name__ == "__main__":
    booking_system = BookingSystem()
    
    # Load existing bookings if any
    booking_system.load_bookings()

    # Add a new booking
    try:
        booking_system.add_booking("John Doe", "0412345678", datetime.now() + timedelta(days=1))
    except ValueError as e:
        print(e)

    # View all bookings
    booking_system.view_bookings()

    # Save bookings to file
    booking_system.save_bookings()
```
