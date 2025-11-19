"""
Generated Code Metadata:
========================
Original URL: https://phametesnet.vercel.app
Prompt: Generate code to calculate the liquidation price for a leveraged long position on tPLS/USD using the entry price, leverage, and collateral details provided by Phame.io.
Generated: DETERMINISTIC_e46b16fcf2fa1cc0
Batch ID: 20250612_153648
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
class LiquidationPriceCalculator:
    """
    A class to calculate the liquidation price for a leveraged long position.
    """

    def __init__(self, entry_price: float, leverage: float, collateral: float):
        """
        Initializes the LiquidationPriceCalculator with entry price, leverage, and collateral.

        :param entry_price: The price at which the position was entered.
        :param leverage: The leverage used for the position.
        :param collateral: The amount of collateral provided for the position.
        """
        self.entry_price = entry_price
        self.leverage = leverage
        self.collateral = collateral

    def calculate_liquidation_price(self) -> float:
        """
        Calculates the liquidation price for the leveraged long position.

        :return: The calculated liquidation price.
        :raises ValueError: If any of the input values are invalid.
        """
        # Validate inputs
        if self.entry_price <= 0:
            raise ValueError("Entry price must be greater than zero.")
        if self.leverage <= 1:
            raise ValueError("Leverage must be greater than 1.")
        if self.collateral <= 0:
            raise ValueError("Collateral must be greater than zero.")

        # Calculate the liquidation price
        liquidation_price = self.entry_price * (1 - (1 / self.leverage))

        return liquidation_price


def main():
    """
    Main function to execute the liquidation price calculation.
    """
    try:
        # Example input values
        entry_price = 1.0  # Example entry price for tPLS/USD
        leverage = 10.0    # Example leverage
        collateral = 0.1    # Example collateral in USD

        # Create an instance of the calculator
        calculator = LiquidationPriceCalculator(entry_price, leverage, collateral)

        # Calculate and print the liquidation price
        liquidation_price = calculator.calculate_liquidation_price()
        print(f"The liquidation price for the position is: {liquidation_price:.4f} USD")

    except ValueError as e:
        print(f"Error: {e}")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")


if __name__ == "__main__":
    main()
```
