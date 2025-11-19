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
class GlassPartitionPricing:
    """
    Simulates the pricing model for glass partitions based on size and finish.
    Prices are based on standard ranges from the website.
    """

    # Price per square meter for different finishes (in USD)
    FINISH_PRICES = {
        'clear': 150.0,
        'frosted': 180.0,
        'tinted': 200.0,
        'patterned': 220.0
    }

    # Minimum and maximum sizes (in square meters)
    MIN_SIZE = 0.5
    MAX_SIZE = 10.0

    # Additional fixed costs
    INSTALLATION_FEE = 100.0
    HANDLING_FEE = 50.0

    def __init__(self, size: float, finish: str):
        """
        Initialize the pricing model with partition size and finish.
        
        Args:
            size: Size of the partition in square meters.
            finish: Type of finish (clear, frosted, tinted, patterned).
        
        Raises:
            ValueError: If size or finish is invalid.
        """
        if not self.MIN_SIZE <= size <= self.MAX_SIZE:
            raise ValueError(f"Size must be between {self.MIN_SIZE} and {self.MAX_SIZE} sqm")
        
        if finish not in self.FINISH_PRICES:
            raise ValueError(f"Invalid finish. Must be one of: {list(self.FINISH_PRICES.keys())}")
        
        self.size = size
        self.finish = finish

    def calculate_total_price(self) -> float:
        """
        Calculate the total price including base price, installation, and handling fees.
        
        Returns:
            Total price in USD.
        """
        base_price = self.size * self.FINISH_PRICES[self.finish]
        total_price = base_price + self.INSTALLATION_FEE + self.HANDLING_FEE
        return round(total_price, 2)

    @classmethod
    def get_available_finishes(cls) -> list:
        """
        Get a list of available finishes.
        
        Returns:
            List of available finish options.
        """
        return list(cls.FINISH_PRICES.keys())

    @classmethod
    def get_size_limits(cls) -> tuple:
        """
        Get the minimum and maximum allowed sizes.
        
        Returns:
            Tuple of (min_size, max_size) in square meters.
        """
        return (cls.MIN_SIZE, cls.MAX_SIZE)


# Example usage
if __name__ == "__main__":
    try:
        # Create a partition: 2.5 sqm with frosted finish
        partition = GlassPartitionPricing(size=2.5, finish='frosted')
        total_price = partition.calculate_total_price()
        print(f"Total price for {partition.size} sqm {partition.finish} glass: ${total_price}")
        
        # Display available options
        print("\nAvailable finishes:", GlassPartitionPricing.get_available_finishes())
        min_size, max_size = GlassPartitionPricing.get_size_limits()
        print(f"Size range: {min_size} to {max_size} sqm")
    
    except ValueError as e:
        print(f"Error: {e}")
```
