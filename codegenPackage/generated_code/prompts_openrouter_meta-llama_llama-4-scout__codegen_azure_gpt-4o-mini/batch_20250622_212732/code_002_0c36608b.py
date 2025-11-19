"""
Generated Code Metadata:
========================
Original URL: https://saltydazeusvi.com
Prompt: "Write a code snippet to calculate the cost of a boat charter trip based on factors like duration, type of boat (e.g., Salt Deck, Salt Shaker), and number of passengers."
Generated: DETERMINISTIC_0c36608b89ea598b
Batch ID: 20250622_212732
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
class BoatCharter:
    """
    A class to represent a boat charter trip and calculate its cost.
    """

    # Base rates for different types of boats (per hour)
    BOAT_RATES = {
        'Salt Deck': 200,
        'Salt Shaker': 150
    }

    def __init__(self, boat_type: str, duration: float, num_passengers: int):
        """
        Initializes the BoatCharter instance.

        :param boat_type: Type of the boat (e.g., 'Salt Deck', 'Salt Shaker')
        :param duration: Duration of the trip in hours
        :param num_passengers: Number of passengers for the trip
        """
        self.boat_type = boat_type
        self.duration = duration
        self.num_passengers = num_passengers

        # Validate inputs
        self.validate_inputs()

    def validate_inputs(self):
        """
        Validates the input parameters for the boat charter.
        Raises ValueError if any input is invalid.
        """
        if self.boat_type not in self.BOAT_RATES:
            raise ValueError(f"Invalid boat type: {self.boat_type}. Choose from {list(self.BOAT_RATES.keys())}.")
        if self.duration <= 0:
            raise ValueError("Duration must be a positive number.")
        if self.num_passengers <= 0:
            raise ValueError("Number of passengers must be a positive integer.")

    def calculate_cost(self) -> float:
        """
        Calculates the total cost of the boat charter trip.

        :return: Total cost of the trip
        """
        base_rate = self.BOAT_RATES[self.boat_type]
        total_cost = base_rate * self.duration
        return total_cost

    def __str__(self):
        """
        Returns a string representation of the boat charter details.
        """
        return (f"Boat Type: {self.boat_type}, Duration: {self.duration} hours, "
                f"Passengers: {self.num_passengers}, Total Cost: ${self.calculate_cost():.2f}")


# Example usage
if __name__ == "__main__":
    try:
        # Create a boat charter instance
        charter = BoatCharter(boat_type='Salt Deck', duration=3, num_passengers=5)
        print(charter)
    except ValueError as e:
        print(f"Error: {e}")
```
