"""
Generated Code Metadata:
========================
Original URL: https://shishehbalkon.ir
Prompt: Generate code to simulate the pricing model for glass partitions with varying sizes and finishes, referencing the specific price ranges and finishes mentioned on the website.
Generated: DETERMINISTIC_e4806d5cd6f211d9
Batch ID: 20250612_153224
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
class GlassPartition:
    """
    A class to represent a glass partition with specific dimensions and finishes.
    """

    # Price ranges for different finishes (in USD)
    PRICE_RANGES = {
        'clear': (50, 100),
        'frosted': (70, 120),
        'tinted': (80, 150),
        'laminated': (100, 200),
    }

    def __init__(self, width: float, height: float, finish: str):
        """
        Initializes a GlassPartition instance.

        :param width: Width of the glass partition in meters.
        :param height: Height of the glass partition in meters.
        :param finish: Finish type of the glass partition.
        :raises ValueError: If the width or height is non-positive or if the finish is invalid.
        """
        if width <= 0 or height <= 0:
            raise ValueError("Width and height must be positive values.")
        if finish not in self.PRICE_RANGES:
            raise ValueError(f"Invalid finish type. Available finishes: {list(self.PRICE_RANGES.keys())}")

        self.width = width
        self.height = height
        self.finish = finish

    def calculate_area(self) -> float:
        """
        Calculates the area of the glass partition.

        :return: Area in square meters.
        """
        return self.width * self.height

    def calculate_price(self) -> float:
        """
        Calculates the price of the glass partition based on its area and finish.

        :return: Estimated price in USD.
        """
        area = self.calculate_area()
        price_range = self.PRICE_RANGES[self.finish]
        # Calculate price based on area and finish price range
        price_per_square_meter = (price_range[0] + price_range[1]) / 2
        return area * price_per_square_meter

    def __str__(self) -> str:
        """
        Returns a string representation of the GlassPartition instance.

        :return: String description of the glass partition.
        """
        return (f"Glass Partition - Width: {self.width}m, Height: {self.height}m, "
                f"Finish: {self.finish}, Estimated Price: ${self.calculate_price():.2f}")


def main():
    """
    Main function to simulate the pricing model for glass partitions.
    """
    try:
        # Example usage
        partition1 = GlassPartition(width=2.0, height=3.0, finish='frosted')
        print(partition1)

        partition2 = GlassPartition(width=1.5, height=2.5, finish='tinted')
        print(partition2)

        # Uncomment the following line to see error handling in action
        # partition_invalid = GlassPartition(width=-1.0, height=2.0, finish='clear')

    except ValueError as e:
        print(f"Error: {e}")


if __name__ == "__main__":
    main()
```
