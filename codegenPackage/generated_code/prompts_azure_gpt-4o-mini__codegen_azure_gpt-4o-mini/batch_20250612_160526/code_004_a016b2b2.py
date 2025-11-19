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

class PartyService:
    """Class to represent a party service booking system."""

    def __init__(self):
        """Initialize the booking system with available services."""
        self.services = {
            "themed_party": {
                "description": "A fun themed party with decorations and activities.",
                "price": 300
            },
            "character_appearance": {
                "description": "A special character appearance for entertainment.",
                "price": 200
            }
        }
        self.bookings = []

    def list_services(self):
        """List all available party services."""
        print("Available Party Services:")
        for service, details in self.services.items():
            print(f"{service.replace('_', ' ').title()}: {details['description']} - ${details['price']}")

    def book_service(self, service_name, customer_name):
        """Book a party service for a customer.

        Args:
            service_name (str): The name of the service to book.
            customer_name (str): The name of the customer booking the service.

        Raises:
            ValueError: If the service is not available.
        """
        if service_name not in self.services:
            raise ValueError(f"Service '{service_name}' is not available.")

        booking_details = {
            "customer_name": customer_name,
            "service": service_name,
            "price": self.services[service_name]["price"]
        }
        self.bookings.append(booking_details)
        print(f"Successfully booked {service_name.replace('_', ' ')} for {customer_name}.")

    def get_bookings(self):
        """Return a list of all bookings."""
        return self.bookings

    def total_revenue(self):
        """Calculate the total revenue from all bookings."""
        return sum(booking['price'] for booking in self.bookings)


if __name__ == "__main__":
    # Create an instance of the PartyService
    booking_system = PartyService()

    # List available services
    booking_system.list_services()

    # Example of booking a service
    try:
        booking_system.book_service("themed_party", "Alice Johnson")
        booking_system.book_service("character_appearance", "Bob Smith")
    except ValueError as e:
        print(f"Error: {e}")

    # Display all bookings
    print("\nCurrent Bookings:")
    for booking in booking_system.get_bookings():
        print(f"{booking['customer_name']} booked {booking['service'].replace('_', ' ')} for ${booking['price']}.")

    # Display total revenue
    print(f"\nTotal Revenue: ${booking_system.total_revenue()}")
```
