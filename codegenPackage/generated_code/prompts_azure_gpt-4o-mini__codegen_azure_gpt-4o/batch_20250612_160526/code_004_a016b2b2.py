"""
Generated Code Metadata:
========================
Original URL: https://wonderplanet.ee
Prompt: Write a code example that integrates a booking system for party services, referencing the unique offerings of Wonderplanet.ee, including themed parties and special character appearances.
Generated: DETERMINISTIC_a016b2b208ad2bc4
Batch ID: 20250612_160526
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# booking_system.py

import datetime
import json

class BookingSystem:
    """
    A booking system for party services, including themed parties and special character appearances.
    """

    def __init__(self):
        # Initialize the system with available services and bookings
        self.services = {
            "themed_party": {
                "description": "A party with a specific theme (e.g., pirates, princesses, superheroes).",
                "price": 200.00
            },
            "character_appearance": {
                "description": "Special appearances by characters (e.g., mascots, superheroes, princesses).",
                "price": 150.00
            }
        }
        self.bookings = []

    def list_services(self):
        """
        List all available services.
        """
        print("Available Services:")
        for service_name, service_details in self.services.items():
            print(f"- {service_name.capitalize()}: {service_details['description']} (${service_details['price']:.2f})")

    def create_booking(self, customer_name, service_name, event_date):
        """
        Create a new booking for a party service.

        Args:
            customer_name (str): Name of the customer.
            service_name (str): Name of the service to book.
            event_date (str): Date of the event in YYYY-MM-DD format.

        Returns:
            dict: Details of the created booking.
        """
        try:
            # Validate service name
            if service_name not in self.services:
                raise ValueError(f"Service '{service_name}' is not available.")

            # Validate event date
            event_date_obj = datetime.datetime.strptime(event_date, "%Y-%m-%d")
            if event_date_obj < datetime.datetime.now():
                raise ValueError("Event date must be in the future.")

            # Create booking
            booking = {
                "customer_name": customer_name,
                "service_name": service_name,
                "event_date": event_date,
                "price": self.services[service_name]["price"]
            }
            self.bookings.append(booking)

            print("Booking successfully created!")
            return booking

        except ValueError as ve:
            print(f"Error: {ve}")
        except Exception as e:
            print(f"An unexpected error occurred: {e}")

    def list_bookings(self):
        """
        List all bookings.
        """
        if not self.bookings:
            print("No bookings found.")
            return

        print("Current Bookings:")
        for booking in self.bookings:
            print(json.dumps(booking, indent=4))

    def cancel_booking(self, customer_name, service_name, event_date):
        """
        Cancel an existing booking.

        Args:
            customer_name (str): Name of the customer.
            service_name (str): Name of the service booked.
            event_date (str): Date of the event in YYYY-MM-DD format.

        Returns:
            bool: True if the booking was successfully canceled, False otherwise.
        """
        try:
            for booking in self.bookings:
                if (booking["customer_name"] == customer_name and
                        booking["service_name"] == service_name and
                        booking["event_date"] == event_date):
                    self.bookings.remove(booking)
                    print("Booking successfully canceled!")
                    return True

            print("No matching booking found to cancel.")
            return False

        except Exception as e:
            print(f"An unexpected error occurred: {e}")
            return False


# Example usage
if __name__ == "__main__":
    # Initialize the booking system
    system = BookingSystem()

    # List available services
    system.list_services()

    # Create a booking
    system.create_booking("Alice", "themed_party", "2023-12-25")

    # List all bookings
    system.list_bookings()

    # Cancel a booking
    system.cancel_booking("Alice", "themed_party", "2023-12-25")

    # List bookings after cancellation
    system.list_bookings()
```
