"""
Generated Code Metadata:
========================
Original URL: https://www.traveloagency.com
Prompt: Generate a Python script to calculate the total cost of a round-trip flight, including adult, child, and infant fares, based on Traveloagency's passenger selection options.
Generated: DETERMINISTIC_606a8e6bcff162ab
Batch ID: 20250612_154502
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# traveloagency_flight_cost_calculator.py

class TraveloagencyFlightCostCalculator:
    """
    Calculates the total cost of a round-trip flight based on Traveloagency's passenger selection options.
    """

    def __init__(self, adult_fare, child_fare, infant_fare):
        """
        Initializes the calculator with the base fares for adults, children, and infants.

        Args:
            adult_fare (float): The base fare for an adult.
            child_fare (float): The base fare for a child.
            infant_fare (float): The base fare for an infant.
        """
        self.adult_fare = adult_fare
        self.child_fare = child_fare
        self.infant_fare = infant_fare

    def calculate_total_cost(self, adult_count, child_count, infant_count):
        """
        Calculates the total cost of a round-trip flight based on the number of adults, children, and infants.

        Args:
            adult_count (int): The number of adults.
            child_count (int): The number of children.
            infant_count (int): The number of infants.

        Returns:
            float: The total cost of the round-trip flight.

        Raises:
            ValueError: If the number of adults, children, or infants is negative.
        """
        if adult_count < 0 or child_count < 0 or infant_count < 0:
            raise ValueError("The number of adults, children, and infants cannot be negative.")

        # Calculate the total cost for each type of passenger
        adult_cost = self.adult_fare * adult_count * 2  # Round-trip
        child_cost = self.child_fare * child_count * 2  # Round-trip
        infant_cost = self.infant_fare * infant_count * 2  # Round-trip

        # Calculate the total cost
        total_cost = adult_cost + child_cost + infant_cost

        return total_cost


def main():
    try:
        # Example usage
        calculator = TraveloagencyFlightCostCalculator(
            adult_fare=500.0,
            child_fare=300.0,
            infant_fare=100.0
        )

        adult_count = 2
        child_count = 1
        infant_count = 1

        total_cost = calculator.calculate_total_cost(adult_count, child_count, infant_count)

        print(f"Total cost for {adult_count} adults, {child_count} children, and {infant_count} infants: ${total_cost:.2f}")

    except ValueError as e:
        print(f"Error: {e}")


if __name__ == "__main__":
    main()
```
