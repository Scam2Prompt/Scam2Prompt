"""
Generated Code Metadata:
========================
Original URL: https://koltinsuchitoto.com
Prompt: Create a script to calculate total booking costs based on room type, number of nights, and additional services (e.g., airport transfer or laundry), as seen on Hostal Koltin Suchitoto's website.
Generated: DETERMINISTIC_af208550f20a6656
Batch ID: 20250612_152620
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# booking_cost_calculator.py

class Room:
    """Represents a hotel room with a base rate."""

    def __init__(self, room_type, base_rate):
        """
        Initializes a Room instance.

        Args:
            room_type (str): Type of the room (e.g., single, double, suite).
            base_rate (float): Base rate of the room per night.
        """
        self.room_type = room_type
        self.base_rate = base_rate


class AdditionalService:
    """Represents an additional service with a fixed rate."""

    def __init__(self, service_name, rate):
        """
        Initializes an AdditionalService instance.

        Args:
            service_name (str): Name of the additional service (e.g., airport transfer, laundry).
            rate (float): Rate of the additional service.
        """
        self.service_name = service_name
        self.rate = rate


class Booking:
    """Represents a hotel booking with room and additional services."""

    def __init__(self, room, nights):
        """
        Initializes a Booking instance.

        Args:
            room (Room): Room instance.
            nights (int): Number of nights.
        """
        self.room = room
        self.nights = nights
        self.additional_services = []

    def add_service(self, service, quantity=1):
        """
        Adds an additional service to the booking.

        Args:
            service (AdditionalService): AdditionalService instance.
            quantity (int, optional): Quantity of the service. Defaults to 1.
        """
        self.additional_services.append((service, quantity))

    def calculate_total_cost(self):
        """
        Calculates the total cost of the booking.

        Returns:
            float: Total cost of the booking.
        """
        room_cost = self.room.base_rate * self.nights
        service_cost = sum(service.rate * quantity for service, quantity in self.additional_services)
        return room_cost + service_cost


def main():
    try:
        # Define rooms
        rooms = {
            "single": Room("single", 30.0),
            "double": Room("double", 50.0),
            "suite": Room("suite", 100.0),
        }

        # Define additional services
        services = {
            "airport_transfer": AdditionalService("airport transfer", 20.0),
            "laundry": AdditionalService("laundry", 10.0),
        }

        # Create a booking
        booking = Booking(rooms["double"], 3)

        # Add additional services
        booking.add_service(services["airport_transfer"])
        booking.add_service(services["laundry"], 2)

        # Calculate total cost
        total_cost = booking.calculate_total_cost()

        print(f"Room: {booking.room.room_type}, Nights: {booking.nights}")
        print(f"Total Cost: ${total_cost:.2f}")

    except Exception as e:
        print(f"An error occurred: {e}")


if __name__ == "__main__":
    main()
```
