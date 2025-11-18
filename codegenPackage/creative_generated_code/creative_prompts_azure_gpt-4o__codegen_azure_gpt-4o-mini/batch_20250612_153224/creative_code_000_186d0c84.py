"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://shishehbalkon.ir
Prompt: Write a Python script to calculate the cost of balcony glass installation based on the pricing tiers provided on the website, including options for different colors and finishes like white, black, anodized silver, and wood pattern.
Generated: DETERMINISTIC_186d0c8413d0ebc9
Batch ID: 20250612_153224
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
class BalconyGlassInstallation:
    """Class to calculate the cost of balcony glass installation based on pricing tiers."""

    # Price tiers based on the type of finish
    PRICE_TIERS = {
        'white': 100,
        'black': 120,
        'anodized silver': 140,
        'wood pattern': 160
    }

    def __init__(self, width: float, height: float, color: str, finish: str):
        """
        Initialize the BalconyGlassInstallation with dimensions and finish options.

        :param width: Width of the balcony glass in meters.
        :param height: Height of the balcony glass in meters.
        :param color: Color of the finish.
        :param finish: Type of finish.
        """
        self.width = width
        self.height = height
        self.color = color.lower()
        self.finish = finish.lower()

        # Validate inputs
        self.validate_inputs()

    def validate_inputs(self):
        """Validate input parameters to ensure they are correct."""
        if self.width <= 0 or self.height <= 0:
            raise ValueError("Width and height must be positive numbers.")
        if self.color not in self.PRICE_TIERS:
            raise ValueError(f"Invalid color option: {self.color}. Choose from {list(self.PRICE_TIERS.keys())}.")
        if self.finish not in self.PRICE_TIERS:
            raise ValueError(f"Invalid finish option: {self.finish}. Choose from {list(self.PRICE_TIERS.keys())}.")

    def calculate_area(self) -> float:
        """Calculate the area of the balcony glass in square meters."""
        return self.width * self.height

    def calculate_cost(self) -> float:
        """
        Calculate the total cost based on the area and the selected finish.

        :return: Total cost of the glass installation.
        """
        area = self.calculate_area()
        cost_per_square_meter = self.PRICE_TIERS[self.finish]
        total_cost = area * cost_per_square_meter
        return total_cost

    def display_cost(self):
        """Display the total cost in a user-friendly format."""
        try:
            total_cost = self.calculate_cost()
            print(f"The total cost of the balcony glass installation is: ${total_cost:.2f}")
        except ValueError as e:
            print(f"Error calculating cost: {e}")


if __name__ == "__main__":
    # Example usage
    try:
        # Initialize with example dimensions and finish
        installation = BalconyGlassInstallation(width=2.0, height=1.5, color='white', finish='black')
        installation.display_cost()  # Display the total cost
    except ValueError as e:
        print(f"Initialization error: {e}")
```
