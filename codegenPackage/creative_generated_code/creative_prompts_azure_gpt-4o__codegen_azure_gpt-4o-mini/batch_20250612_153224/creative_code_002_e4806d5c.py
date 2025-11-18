"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://shishehbalkon.ir
Prompt: Generate code to simulate the pricing model for glass partitions with varying sizes and finishes, referencing the specific price ranges and finishes mentioned on the website.
Generated: DETERMINISTIC_e4806d5cd6f211d9
Batch ID: 20250612_153224
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
class GlassPartition:
    """
    A class to represent a glass partition with specific size and finish.
    """

    # Price ranges for various finishes
    FINISH_PRICES = {
        'clear': (50, 100),
        'frosted': (70, 120),
        'tinted': (80, 130),
        'decorative': (100, 150),
    }

    def __init__(self, width: float, height: float, finish: str):
        """
        Initializes a GlassPartition instance with width, height, and finish.

        :param width: Width of the glass partition in meters.
        :param height: Height of the glass partition in meters.
        :param finish: Type of finish for the glass partition.
        :raises ValueError: If the finish type is not supported.
        """
        self.width = width
        self.height = height
        self.finish = finish.lower()

        if self.finish not in self.FINISH_PRICES:
            raise ValueError(f"Unsupported finish type: {self.finish}. "
                             f"Supported finishes: {list(self.FINISH_PRICES.keys())}")

    def calculate_area(self) -> float:
        """
        Calculate the area of the glass partition.

        :return: Area in square meters.
        """
        return self.width * self.height

    def calculate_price(self) -> float:
        """
        Calculate the price of the glass partition based on its finish.

        :return: Estimated price in currency units.
        """
        area = self.calculate_area()
        price_range = self.FINISH_PRICES[self.finish]
        # Average price per square meter for the given finish
        avg_price_per_sqm = (price_range[0] + price_range[1]) / 2
        total_price = avg_price_per_sqm * area
        return total_price

    def __str__(self) -> str:
        """
        String representation of the glass partition.

        :return: Informative string about the glass partition.
        """
        return (f"Glass Partition: {self.width}m x {self.height}m, "
                f"Finish: {self.finish.capitalize()}, "
                f"Estimated Price: ${self.calculate_price():.2f}")


if __name__ == "__main__":
    try:
        # Example usage
        width = float(input("Enter the width of the partition (m): "))
        height = float(input("Enter the height of the partition (m): "))
        finish = input("Enter the finish type (clear, frosted, tinted, decorative): ")

        partition = GlassPartition(width, height, finish)
        print(partition)

    except ValueError as e:
        # Handle errors gracefully
        print(f"Error: {e}")
```
