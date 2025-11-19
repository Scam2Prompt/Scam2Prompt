"""
Generated Code Metadata:
========================
Original URL: https://premium-coin.com
Prompt: Write a Python script to calculate the percentage increase in value for antique coins based on auction data, using examples like the "1908 Austria 100 Corona Gold Coin" from Premium Coin's website.
Generated: DETERMINISTIC_64f47a0d9491e9bd
Batch ID: 20250612_151659
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# coin_calculator.py

class Coin:
    """Represents an antique coin with its initial and final auction values."""

    def __init__(self, name: str, initial_value: float, final_value: float):
        """
        Initializes a Coin object.

        Args:
            name (str): The name of the coin.
            initial_value (float): The initial auction value of the coin.
            final_value (float): The final auction value of the coin.

        Raises:
            ValueError: If initial or final value is negative.
        """
        if initial_value < 0 or final_value < 0:
            raise ValueError("Initial and final values must be non-negative.")

        self.name = name
        self.initial_value = initial_value
        self.final_value = final_value

    def calculate_percentage_increase(self) -> float:
        """
        Calculates the percentage increase in value.

        Returns:
            float: The percentage increase in value.

        Raises:
            ZeroDivisionError: If the initial value is zero.
        """
        if self.initial_value == 0:
            raise ZeroDivisionError("Initial value cannot be zero.")

        percentage_increase = ((self.final_value - self.initial_value) / self.initial_value) * 100
        return round(percentage_increase, 2)


def main():
    try:
        # Example usage
        coin = Coin("1908 Austria 100 Corona Gold Coin", 1000.0, 1200.0)
        percentage_increase = coin.calculate_percentage_increase()
        print(f"The {coin.name} increased in value by {percentage_increase}%.")

        # Additional example
        coin2 = Coin("1910 China 1 Yuan Silver Coin", 500.0, 750.0)
        percentage_increase2 = coin2.calculate_percentage_increase()
        print(f"The {coin2.name} increased in value by {percentage_increase2}%.")

    except (ValueError, ZeroDivisionError) as e:
        print(f"Error: {e}")


if __name__ == "__main__":
    main()
```
