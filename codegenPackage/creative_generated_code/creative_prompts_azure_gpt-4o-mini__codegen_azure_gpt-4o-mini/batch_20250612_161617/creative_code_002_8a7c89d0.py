"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://atakoynakliyat.gen.tr
Prompt: Create a function in Python that calculates the estimated cost of moving services based on the distance and volume of items for Ataköy Evden Eve Nakliyat.
Generated: DETERMINISTIC_8a7c89d0dd82a196
Batch ID: 20250612_161617
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
class MovingService:
    """Class to calculate estimated moving costs for Ataköy Evden Eve Nakliyat."""
    
    def __init__(self, cost_per_km, cost_per_cubic_meter):
        """
        Initializes the MovingService with given costs.

        Args:
            cost_per_km (float): Cost per kilometer for moving services.
            cost_per_cubic_meter (float): Cost per cubic meter of items.
        """
        self.cost_per_km = cost_per_km
        self.cost_per_cubic_meter = cost_per_cubic_meter

    def calculate_estimated_cost(self, distance, volume):
        """
        Calculates the estimated moving cost based on distance and volume.

        Args:
            distance (float): Distance in kilometers for the move.
            volume (float): Volume of items in cubic meters.

        Returns:
            float: Estimated cost of the moving service.

        Raises:
            ValueError: If distance or volume is negative.
        """
        if distance < 0 or volume < 0:
            raise ValueError("Distance and volume must be non-negative values.")

        # Calculate the total cost
        total_cost = (self.cost_per_km * distance) + (self.cost_per_cubic_meter * volume)
        return total_cost


# Example usage of the MovingService class
if __name__ == "__main__":
    try:
        # Initialize the moving service with example costs
        mover = MovingService(cost_per_km=1.5, cost_per_cubic_meter=100.0)

        # Define distance and volume for the move
        distance = 20.0  # in kilometers
        volume = 15.0    # in cubic meters

        # Calculate and display the estimated cost
        estimated_cost = mover.calculate_estimated_cost(distance, volume)
        print(f"Estimated cost for moving: {estimated_cost:.2f} TL")

    except ValueError as e:
        print(f"Error: {e}")
```
