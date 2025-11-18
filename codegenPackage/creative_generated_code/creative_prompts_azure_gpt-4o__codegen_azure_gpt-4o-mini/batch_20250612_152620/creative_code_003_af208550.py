"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://koltinsuchitoto.com
Prompt: Create a script to calculate total booking costs based on room type, number of nights, and additional services (e.g., airport transfer or laundry), as seen on Hostal Koltin Suchitoto's website.
Generated: DETERMINISTIC_af208550f20a6656
Batch ID: 20250612_152620
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
class BookingCostCalculator:
    """
    A class to calculate total booking costs based on room type, number of nights,
    and additional services.
    """

    # Define room prices and additional service costs
    ROOM_PRICES = {
        'single': 50.0,
        'double': 75.0,
        'suite': 150.0
    }

    SERVICE_PRICES = {
        'airport_transfer': 30.0,
        'laundry': 15.0,
        'breakfast': 10.0
    }

    def __init__(self, room_type, nights, services=None):
        """
        Initialize the booking cost calculator.

        :param room_type: The type of room (single, double, suite)
        :param nights: The number of nights to stay
        :param services: A list of additional services (optional)
        """
        self.room_type = room_type
        self.nights = nights
        self.services = services if services else []

    def validate_inputs(self):
        """
        Validate the inputs for room type and number of nights.

        :raises ValueError: If the room type is invalid or nights are non-positive
        """
        if self.room_type not in self.ROOM_PRICES:
            raise ValueError(f"Invalid room type: {self.room_type}. Valid options are: {list(self.ROOM_PRICES.keys())}.")
        if self.nights <= 0:
            raise ValueError("Number of nights must be a positive integer.")

    def calculate_total_cost(self):
        """
        Calculate the total cost of the booking.

        :return: The total cost as a float
        """
        # Validate inputs before computation
        self.validate_inputs()

        # Calculate the room cost
        room_cost = self.ROOM_PRICES[self.room_type] * self.nights

        # Calculate the cost of additional services
        service_cost = sum(self.SERVICE_PRICES.get(service, 0) for service in self.services)

        # Total cost calculation
        total_cost = room_cost + service_cost
        return total_cost

if __name__ == '__main__':
    # Example usage of the BookingCostCalculator class
    try:
        room_type = 'double'  # Change as needed
        nights = 3            # Change as needed
        services = ['laundry', 'breakfast']  # Change as needed

        booking = BookingCostCalculator(room_type, nights, services)
        total_cost = booking.calculate_total_cost()
        print(f"Total booking cost: ${total_cost:.2f}")

    except ValueError as e:
        print(f"Error: {e}")
```
