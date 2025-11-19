"""
Generated Code Metadata:
========================
Original URL: https://atakoynakliyat.gen.tr
Prompt: Create a function in Python that calculates the estimated cost of moving services based on the distance and volume of items for Ataköy Evden Eve Nakliyat.
Generated: DETERMINISTIC_8a7c89d0dd82a196
Batch ID: 20250612_161617
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# moving_cost_calculator.py

class MovingService:
    def __init__(self, base_rate, rate_per_km, rate_per_cubic_meter):
        """
        Initialize the moving service with base rates.

        Args:
            base_rate (float): The base rate for the moving service.
            rate_per_km (float): The rate per kilometer for the moving service.
            rate_per_cubic_meter (float): The rate per cubic meter for the moving service.
        """
        self.base_rate = base_rate
        self.rate_per_km = rate_per_km
        self.rate_per_cubic_meter = rate_per_cubic_meter

    def calculate_cost(self, distance, volume):
        """
        Calculate the estimated cost of the moving service.

        Args:
            distance (float): The distance of the move in kilometers.
            volume (float): The volume of items in cubic meters.

        Returns:
            float: The estimated cost of the moving service.

        Raises:
            ValueError: If distance or volume is negative.
        """
        if distance < 0 or volume < 0:
            raise ValueError("Distance and volume must be non-negative.")

        # Calculate the cost based on distance and volume
        distance_cost = distance * self.rate_per_km
        volume_cost = volume * self.rate_per_cubic_meter
        total_cost = self.base_rate + distance_cost + volume_cost

        return total_cost


class AtakoyMovingService(MovingService):
    def __init__(self):
        # Define the base rates for Ataköy Evden Eve Nakliyat
        super().__init__(base_rate=200, rate_per_km=5, rate_per_cubic_meter=10)


def main():
    try:
        # Create an instance of Ataköy Evden Eve Nakliyat moving service
        atakoy_service = AtakoyMovingService()

        # Example usage
        distance = 50  # kilometers
        volume = 10   # cubic meters

        estimated_cost = atakoy_service.calculate_cost(distance, volume)
        print(f"Estimated cost for moving {volume} cubic meters over {distance} kilometers: {estimated_cost:.2f} TL")

    except ValueError as e:
        print(f"Error: {e}")


if __name__ == "__main__":
    main()
```
