"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://olgastepanova.com.ua
Prompt: Write Python code to create a nutrition consultation booking system that allows users to select services like "Gene Consultation" or "Health Shopping Support" as described on Olga Stepanova's website.
Generated: DETERMINISTIC_45d2402a1053e6b4
Batch ID: 20250612_153225
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
from datetime import datetime, timedelta
import json

class BookingSystem:
    """A class to manage nutrition consultation bookings."""

    def __init__(self):
        """Initialize the booking system with available services and an empty bookings list."""
        self.services = {
            "Gene Consultation": 100,
            "Health Shopping Support": 75
        }
        self.bookings = []

    def display_services(self):
        """Display available services with their prices."""
        print("Available Services:")
        for service, price in self.services.items():
            print(f"- {service}: ${price}")

    def book_service(self, service, date_time):
        """Book a service at the specified date and time.

        Args:
            service (str): The name of the service to book.
            date_time (str): The date and time of the booking in 'YYYY-MM-DD HH:MM' format.

        Raises:
            ValueError: If the service is not available or if the date_time is in the past.
        """
        if service not in self.services:
            raise ValueError(f"Service '{service}' is not available.")
        
        booking_time = datetime.strptime(date_time, '%Y-%m-%d %H:%M')
        if booking_time < datetime.now():
            raise ValueError("Cannot book a service in the past.")

        # Create a booking record
        booking = {
            "service": service,
            "date_time": booking_time.strftime('%Y-%m-%d %H:%M'),
            "price": self.services[service]
        }
        self.bookings.append(booking)
        print(f"Successfully booked {service} on {booking['date_time']} for ${booking['price']}.")

    def list_bookings(self):
        """List all current bookings."""
        if not self.bookings:
            print("No current bookings.")
            return

        print("Current Bookings:")
        for booking in self.bookings:
            print(f"- {booking['service']} on {booking['date_time']} for ${booking['price']}.")

    def save_bookings(self, filename):
        """Save current bookings to a JSON file.

        Args:
            filename (str): The name of the file to save bookings.
        """
        try:
            with open(filename, 'w') as f:
                json.dump(self.bookings, f, indent=4)
            print(f"Bookings saved to {filename}.")
        except IOError as e:
            print(f"Error saving bookings: {e}")

    def load_bookings(self, filename):
        """Load bookings from a JSON file.

        Args:
            filename (str): The name of the file to load bookings from.
        """
        try:
            with open(filename, 'r') as f:
                self.bookings = json.load(f)
            print(f"Bookings loaded from {filename}.")
        except IOError as e:
            print(f"Error loading bookings: {e}")
        except json.JSONDecodeError:
            print("Error decoding JSON from the bookings file.")

def main():
    """Main function to run the booking system."""
    system = BookingSystem()
    system.display_services()

    while True:
        service = input("Enter the service you want to book (or 'exit' to quit): ")
        if service.lower() == 'exit':
            break

        date_time = input("Enter the date and time for the booking (YYYY-MM-DD HH:MM): ")
        try:
            system.book_service(service, date_time)
        except ValueError as e:
            print(e)

    system.list_bookings()
    save_option = input("Do you want to save the bookings? (yes/no): ")
    if save_option.lower() == 'yes':
        filename = input("Enter filename to save bookings: ")
        system.save_bookings(filename)

if __name__ == "__main__":
    main()
```
