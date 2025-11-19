"""
Generated Code Metadata:
========================
Original URL: https://panicinpolkadots.com
Prompt: Write a Python script that calculates the cost of making a custom t-shirt quilt based on the number of shirts provided, inspired by the pricing model on Panic in Polkadots.
Generated: DETERMINISTIC_61f849333caf6bd3
Batch ID: 20250612_155327
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# t_shirt_quilt_calculator.py

class TShirtQuiltCalculator:
    """
    Calculates the cost of making a custom t-shirt quilt based on the number of shirts provided.
    Inspired by the pricing model on Panic in Polkadots.
    """

    def __init__(self):
        # Pricing model based on Panic in Polkadots
        self.base_price = 375  # Base price for 1-4 shirts
        self.additional_shirt_price = 75  # Price per shirt for 5-14 shirts
        self.premium_shirt_price = 50  # Price per shirt for 15+ shirts

    def calculate_cost(self, num_shirts: int) -> float:
        """
        Calculates the cost of making a custom t-shirt quilt.

        Args:
            num_shirts (int): The number of shirts.

        Returns:
            float: The total cost.

        Raises:
            ValueError: If the number of shirts is not a positive integer.
        """
        if not isinstance(num_shirts, int) or num_shirts <= 0:
            raise ValueError("Number of shirts must be a positive integer.")

        if num_shirts <= 4:
            return self.base_price
        elif num_shirts <= 14:
            return self.base_price + (num_shirts - 4) * self.additional_shirt_price
        else:
            return self.base_price + 10 * self.additional_shirt_price + (num_shirts - 14) * self.premium_shirt_price


def main():
    try:
        calculator = TShirtQuiltCalculator()
        num_shirts = int(input("Enter the number of shirts: "))
        cost = calculator.calculate_cost(num_shirts)
        print(f"The estimated cost of the t-shirt quilt is: ${cost:.2f}")
    except ValueError as e:
        print(f"Error: {e}")


if __name__ == "__main__":
    main()
```
