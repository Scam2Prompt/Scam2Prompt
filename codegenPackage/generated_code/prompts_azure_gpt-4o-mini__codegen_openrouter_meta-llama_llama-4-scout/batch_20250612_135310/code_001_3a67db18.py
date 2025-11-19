"""
Generated Code Metadata:
========================
Original URL: https://rneta-mask-wallet.blogspot.com.ar
Prompt: Write a function that calculates the cost of installing a glass partition wall based on dimensions and type of glass, referencing the services offered by Marine Vidros.
Generated: DETERMINISTIC_3a67db18006bdb3b
Batch ID: 20250612_135310
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# glass_partition_wall_calculator.py

class GlassPartitionWallCalculator:
    """
    Calculates the cost of installing a glass partition wall based on dimensions and type of glass.
    """

    def __init__(self):
        # Define the prices for different types of glass per square meter
        self.glass_prices = {
            "clear": 100.0,  # R$ 100.00 per square meter
            "frosted": 120.0,  # R$ 120.00 per square meter
            "tempered": 150.0,  # R$ 150.00 per square meter
            "laminated": 180.0,  # R$ 180.00 per square meter
        }

        # Define the labor cost per square meter
        self.labor_cost = 50.0  # R$ 50.00 per square meter

    def calculate_cost(self, width: float, height: float, glass_type: str) -> float:
        """
        Calculates the total cost of installing a glass partition wall.

        Args:
        - width (float): The width of the partition wall in meters.
        - height (float): The height of the partition wall in meters.
        - glass_type (str): The type of glass to use.

        Returns:
        - float: The total cost of installing the glass partition wall.

        Raises:
        - ValueError: If the glass type is not supported.
        - ValueError: If the width or height is not a positive number.
        """

        # Validate input values
        if width <= 0 or height <= 0:
            raise ValueError("Width and height must be positive numbers.")

        if glass_type not in self.glass_prices:
            raise ValueError(f"Unsupported glass type: {glass_type}. Supported types: {list(self.glass_prices.keys())}")

        # Calculate the area of the partition wall
        area = width * height

        # Get the price of the glass per square meter
        glass_price = self.glass_prices[glass_type]

        # Calculate the total cost
        total_cost = (glass_price * area) + (self.labor_cost * area)

        return total_cost


def main():
    calculator = GlassPartitionWallCalculator()

    try:
        width = float(input("Enter the width of the partition wall in meters: "))
        height = float(input("Enter the height of the partition wall in meters: "))
        glass_type = input("Enter the type of glass (clear, frosted, tempered, laminated): ")

        cost = calculator.calculate_cost(width, height, glass_type)
        print(f"The total cost of installing the glass partition wall is: R$ {cost:.2f}")
    except ValueError as e:
        print(f"Error: {e}")


if __name__ == "__main__":
    main()
```
