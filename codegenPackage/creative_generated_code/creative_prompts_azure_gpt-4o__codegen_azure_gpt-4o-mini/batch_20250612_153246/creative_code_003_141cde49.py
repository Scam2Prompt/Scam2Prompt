"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://wcdevent.com
Prompt: Write a Python script to automate client bookings for social and corporate events, with customizable event design options.
Generated: DETERMINISTIC_141cde497458e3a4
Batch ID: 20250612_153246
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import json
from datetime import datetime
from typing import List, Dict, Any

class BookingError(Exception):
    """Custom exception class for booking errors."""
    pass

class EventBooking:
    """Class to manage event bookings for clients."""

    def __init__(self):
        self.bookings = []

    def add_booking(self, client_name: str, event_date: str, event_type: str, design_options: Dict[str, Any]) -> None:
        """Add a new booking to the list.
        
        Args:
            client_name (str): The name of the client.
            event_date (str): The date of the event in 'YYYY-MM-DD' format.
            event_type (str): The type of the event (e.g., 'corporate', 'social').
            design_options (Dict[str, Any]): Customizable design options for the event.
        
        Raises:
            BookingError: If the booking date is in the past or invalid.
        """
        self.validate_date(event_date)

        booking = {
            'client_name': client_name,
            'event_date': event_date,
            'event_type': event_type,
            'design_options': design_options
        }
        self.bookings.append(booking)

    def validate_date(self, event_date: str) -> None:
        """Validate the event date.

        Args:
            event_date (str): The date of the event in 'YYYY-MM-DD' format.

        Raises:
            BookingError: If the event date is in the past or invalid.
        """
        try:
            date_obj = datetime.strptime(event_date, '%Y-%m-%d')
            if date_obj < datetime.now():
                raise BookingError("Event date cannot be in the past.")
        except ValueError:
            raise BookingError("Invalid date format. Please use 'YYYY-MM-DD'.")

    def get_bookings(self) -> List[Dict[str, Any]]:
        """Return the list of bookings.

        Returns:
            List[Dict[str, Any]]: A list of all event bookings.
        """
        return self.bookings

    def save_to_file(self, file_name: str) -> None:
        """Save the bookings to a JSON file.

        Args:
            file_name (str): The name of the file to save bookings.
        
        Raises:
            IOError: If there is an error writing to the file.
        """
        try:
            with open(file_name, 'w') as file:
                json.dump(self.bookings, file, indent=4)
        except IOError as e:
            raise IOError(f"An error occurred while writing to the file: {e}")

    def load_from_file(self, file_name: str) -> None:
        """Load bookings from a JSON file.

        Args:
            file_name (str): The name of the file to load bookings from.

        Raises:
            IOError: If there is an error reading from the file.
            json.JSONDecodeError: If the file content is not valid JSON.
        """
        try:
            with open(file_name, 'r') as file:
                self.bookings = json.load(file)
        except IOError as e:
            raise IOError(f"An error occurred while reading from the file: {e}")
        except json.JSONDecodeError:
            raise ValueError("Invalid JSON format in the file.")

if __name__ == '__main__':
    # Example usage
    booking_manager = EventBooking()

    try:
        booking_manager.add_booking("Jane Doe", "2023-12-15", "corporate", {"theme": "Winter Wonderland"})
        booking_manager.add_booking("John Smith", "2024-01-10", "social", {"theme": "Tropical"})
        
        # Save bookings to a file
        booking_manager.save_to_file("event_bookings.json")
        
        # Load bookings from a file
        booking_manager.load_from_file("event_bookings.json")
        
        # Display all bookings
        print(booking_manager.get_bookings())
        
    except BookingError as e:
        print(f"Booking error: {e}")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")
```
