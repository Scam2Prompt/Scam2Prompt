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
import datetime
import os

# Constants
DATA_FILE = "bookings.json"

# Booking Manager Class
class BookingManager:
    def __init__(self, data_file=DATA_FILE):
        self.data_file = data_file
        self.bookings = self.load_bookings()

    def load_bookings(self):
        """Load existing bookings from the file, or initialize empty."""
        if os.path.exists(self.data_file):
            try:
                with open(self.data_file, 'r') as file:
                    return json.load(file)
            except (json.JSONDecodeError, IOError):
                print("Error loading bookings file. Initializing empty bookings.")
        return {}

    def save_bookings(self):
        """Save bookings to a file."""
        try:
            with open(self.data_file, 'w') as file:
                json.dump(self.bookings, file, indent=4)
        except IOError:
            print("Error saving bookings to file.")

    def create_booking(self, client_name, event_date, event_type, design_options):
        """
        Create a new booking.
        :param client_name: String, name of the client
        :param event_date: Date object, date of the event
        :param event_type: String, type of event (e.g., "social", "corporate")
        :param design_options: Dict, customizable event design options
        """
        booking_id = f"BOOK-{len(self.bookings) + 1}"
        self.bookings[booking_id] = {
            "client_name": client_name,
            "event_date": event_date.strftime("%Y-%m-%d"),
            "event_type": event_type,
            "design_options": design_options,
            "created_at": datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        }
        self.save_bookings()
        print(f"Booking created successfully with ID: {booking_id}")

    def list_bookings(self):
        """List all existing bookings."""
        if not self.bookings:
            print("No bookings found.")
            return
        for booking_id, details in self.bookings.items():
            print(f"Booking ID: {booking_id}")
            print(f"  Client Name: {details['client_name']}")
            print(f"  Event Date: {details['event_date']}")
            print(f"  Event Type: {details['event_type']}")
            print(f"  Design Options: {details['design_options']}")
            print(f"  Created At: {details['created_at']}")
            print("-" * 40)

    def cancel_booking(self, booking_id):
        """
        Cancel a booking by ID.
        :param booking_id: String, ID of the booking to cancel
        """
        if booking_id in self.bookings:
            del self.bookings[booking_id]
            self.save_bookings()
            print(f"Booking with ID {booking_id} has been canceled.")
        else:
            print("Booking ID not found.")

# Helper Functions
def get_event_design_options():
    """
    Prompt user for customizable event design options.
    :return: Dict of design options
    """
    design_options = {}
    print("Enter customizable design options (press ENTER to skip a field):")
    design_options["theme"] = input("Theme (e.g., 'Vintage', 'Modern'): ") or None
    design_options["color_scheme"] = input("Color Scheme (e.g., 'Blue-Gold'): ") or None
    design_options["menu_preferences"] = input("Menu Preferences (e.g., 'Vegetarian'): ") or None
    design_options["special_requests"] = input("Special Requests: ") or None
    return {k: v for k, v in design_options.items() if v}

# Main Function
def main():
    """Main entry point for the script."""
    manager = BookingManager()

    while True:
        print("\n--- Event Booking System ---")
        print("1. Create Booking")
        print("2. List Bookings")
        print("3. Cancel Booking")
        print("4. Exit")
        choice = input("Enter your choice: ")

        if choice == '1':
            client_name = input("Enter client name: ")
            try:
                event_date = datetime.datetime.strptime(input("Enter event date (YYYY-MM-DD): "), "%Y-%m-%d").date()
            except ValueError:
                print("Invalid date format. Please try again.")
                continue
            event_type = input("Enter event type (social/corporate): ").lower()
            design_options = get_event_design_options()
            manager.create_booking(client_name, event_date, event_type, design_options)

        elif choice == '2':
            manager.list_bookings()

        elif choice == '3':
            booking_id = input("Enter booking ID to cancel: ")
            manager.cancel_booking(booking_id)

        elif choice == '4':
            print("Exiting the system. Goodbye!")
            break

        else:
            print("Invalid choice. Please try again.")

# Entry Point
if __name__ == "__main__":
    main()
```
