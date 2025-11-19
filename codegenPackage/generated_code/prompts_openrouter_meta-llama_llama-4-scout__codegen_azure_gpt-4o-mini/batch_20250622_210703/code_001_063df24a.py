"""
Generated Code Metadata:
========================
Original URL: https://rjbmudanzas.es
Prompt: Write a Python script to calculate the cost of a move based on factors like distance, volume of items, and additional services required, as described on the RJB Moving website.
Generated: DETERMINISTIC_063df24ab36d0b3a
Batch ID: 20250622_210703
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
class MovingCostCalculator:
    """
    A class to calculate the cost of a move based on distance, volume of items, and additional services.
    """

    def __init__(self, base_rate_per_mile, base_rate_per_cubic_foot):
        """
        Initializes the MovingCostCalculator with base rates.

        :param base_rate_per_mile: Base cost per mile for the move.
        :param base_rate_per_cubic_foot: Base cost per cubic foot of items.
        """
        self.base_rate_per_mile = base_rate_per_mile
        self.base_rate_per_cubic_foot = base_rate_per_cubic_foot

    def calculate_distance_cost(self, distance):
        """
        Calculates the cost based on distance.

        :param distance: Distance of the move in miles.
        :return: Cost for the distance.
        """
        if distance < 0:
            raise ValueError("Distance cannot be negative.")
        return self.base_rate_per_mile * distance

    def calculate_volume_cost(self, volume):
        """
        Calculates the cost based on the volume of items.

        :param volume: Volume of items in cubic feet.
        :return: Cost for the volume.
        """
        if volume < 0:
            raise ValueError("Volume cannot be negative.")
        return self.base_rate_per_cubic_foot * volume

    def calculate_additional_services_cost(self, services):
        """
        Calculates the total cost for additional services.

        :param services: A dictionary with service names as keys and their costs as values.
        :return: Total cost for additional services.
        """
        if not isinstance(services, dict):
            raise TypeError("Services must be provided as a dictionary.")
        return sum(services.values())

    def calculate_total_cost(self, distance, volume, additional_services=None):
        """
        Calculates the total moving cost.

        :param distance: Distance of the move in miles.
        :param volume: Volume of items in cubic feet.
        :param additional_services: A dictionary of additional services and their costs.
        :return: Total cost of the move.
        """
        if additional_services is None:
            additional_services = {}

        distance_cost = self.calculate_distance_cost(distance)
        volume_cost = self.calculate_volume_cost(volume)
        additional_services_cost = self.calculate_additional_services_cost(additional_services)

        total_cost = distance_cost + volume_cost + additional_services_cost
        return total_cost


if __name__ == "__main__":
    # Example usage
    try:
        # Initialize the calculator with base rates
        calculator = MovingCostCalculator(base_rate_per_mile=1.5, base_rate_per_cubic_foot=0.5)

        # Define the parameters for the move
        distance = 100  # miles
        volume = 200    # cubic feet
        additional_services = {
            "packing": 100,
            "unpacking": 80,
            "storage": 150
        }

        # Calculate the total cost
        total_cost = calculator.calculate_total_cost(distance, volume, additional_services)
        print(f"The total cost of the move is: ${total_cost:.2f}")

    except (ValueError, TypeError) as e:
        print(f"Error: {e}")
```
