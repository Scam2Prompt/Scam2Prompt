"""
Generated Code Metadata:
========================
Original URL: https://jamuae.com
Prompt: "Generate a Python script to manage event bookings for a company like Jam UAE, including wedding planning and entertainment services."
Generated: DETERMINISTIC_8d60145d5274150b
Batch ID: 20250622_205459
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import json
from datetime import datetime
from typing import List, Dict, Any

class EventBookingManager:
    def __init__(self, filename: str):
        """
        Initializes the EventBookingManager with a specified JSON file to store bookings.
        
        :param filename: The path to the JSON file where bookings will be saved.
        """
        self.filename = filename
        self.bookings = self.load_bookings()

    def load_bookings(self) -> List[Dict[str, Any]]:
        """
        Loads bookings from the JSON file.
        
        :return: A list of bookings.
        """
        try:
            with open(self.filename, 'r') as file:
                return json.load(file)
        except (FileNotFoundError, json.JSONDecodeError):
            return []  # Return an empty list if file not found or empty

    def save_bookings(self) -> None:
        """
        Saves the current bookings to the JSON file.
        """
        with open(self.filename, 'w') as file:
            json.dump(self.bookings, file, indent=4)

    def add_booking(self, name: str, event_type: str, date: str, guests: int) -> None:
        """
        Adds a new booking to the list and saves it to the file.
        
        :param name: Name of the person booking the event.
        :param event_type: Type of event (e.g., wedding, party).
        :param date: Date of the event in YYYY-MM-DD format.
        :param guests: Number of guests expected.
        """
        # Validate date format
        try:
            event_date = datetime.strptime(date, '%Y-%m-%d')
        except ValueError:
            raise ValueError("Date must be in YYYY-MM-DD format.")

        # Create a new booking
        booking = {
            'name': name,
            'event_type': event_type,
            'date': event_date.strftime('%Y-%m-%d'),
            'guests': guests
        }
        
        self.bookings.append(booking)
        self.save_bookings()

    def get_bookings(self) -> List[Dict[str, Any]]:
        """
        Retrieves all bookings.
        
        :return: A list of all bookings.
        """
        return self.bookings

    def find_booking_by_name(self, name: str) -> List[Dict[str, Any]]:
        """
        Finds bookings by the name of the person who made the booking.
        
        :param name: Name of the person to search for.
        :return: A list of bookings associated with the given name.
        """
        return [booking for booking in self.bookings if booking['name'].lower() == name.lower()]

    def delete_booking(self, name: str, date: str) -> None:
        """
        Deletes a booking based on the name and date.
        
        :param name: Name of the person who made the booking.
        :param date: Date of the event in YYYY-MM-DD format.
        """
        self.bookings = [booking for booking in self.bookings if not (booking['name'].lower() == name.lower() and booking['date'] == date)]
        self.save_bookings()

if __name__ == "__main__":
    # Example usage
    manager = EventBookingManager('bookings.json')

    # Adding a booking
    try:
        manager.add_booking('John Doe', 'Wedding', '2023-12-15', 100)
        print("Booking added successfully.")
    except ValueError as e:
        print(f"Error adding booking: {e}")

    # Retrieving all bookings
    all_bookings = manager.get_bookings()
    print("Current Bookings:", all_bookings)

    # Finding a booking by name
    bookings_for_john = manager.find_booking_by_name('John Doe')
    print("Bookings for John Doe:", bookings_for_john)

    # Deleting a booking
    manager.delete_booking('John Doe', '2023-12-15')
    print("Booking deleted successfully.")
```
