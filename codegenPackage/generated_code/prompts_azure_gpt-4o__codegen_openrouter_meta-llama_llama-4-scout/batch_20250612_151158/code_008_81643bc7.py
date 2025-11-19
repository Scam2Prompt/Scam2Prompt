"""
Generated Code Metadata:
========================
Original URL: https://secured-everlodge.pages.dev
Prompt: Write a function to calculate token discounts for trading fees and purchases within a blockchain ecosystem, inspired by Everlodge's token utility features.
Generated: DETERMINISTIC_81643bc76e32c574
Batch ID: 20250612_151158
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
from enum import Enum
from typing import Dict

class DiscountType(Enum):
    """Enum for discount types."""
    TRADING_FEE = 1
    PURCHASE = 2

class TokenDiscountCalculator:
    """Calculates token discounts for trading fees and purchases."""

    def __init__(self, token_balances: Dict[str, float], discount_rates: Dict[DiscountType, float]):
        """
        Initializes the calculator with token balances and discount rates.

        Args:
        - token_balances (Dict[str, float]): A dictionary of token holders and their balances.
        - discount_rates (Dict[DiscountType, float]): A dictionary of discount types and their rates.
        """
        self.token_balances = token_balances
        self.discount_rates = discount_rates

    def calculate_discount(self, holder: str, discount_type: DiscountType, amount: float) -> float:
        """
        Calculates the discount for a given holder, discount type, and amount.

        Args:
        - holder (str): The token holder.
        - discount_type (DiscountType): The type of discount.
        - amount (float): The amount to calculate the discount for.

        Returns:
        - float: The calculated discount.

        Raises:
        - ValueError: If the holder has no token balance or the discount type is invalid.
        """
        if holder not in self.token_balances:
            raise ValueError("Holder has no token balance")

        if discount_type not in self.discount_rates:
            raise ValueError("Invalid discount type")

        # Calculate the discount rate based on the token balance
        balance = self.token_balances[holder]
        if balance == 0:
            return 0

        discount_rate = self.discount_rates[discount_type]
        # Apply a tiered discount system based on the token balance
        if balance < 1000:
            discount_rate *= 0.5
        elif balance < 5000:
            discount_rate *= 0.75

        # Calculate the discount
        discount = amount * discount_rate / 100

        return discount

    def calculate_trading_fee_discount(self, holder: str, trading_fee: float) -> float:
        """
        Calculates the trading fee discount for a given holder.

        Args:
        - holder (str): The token holder.
        - trading_fee (float): The trading fee.

        Returns:
        - float: The calculated trading fee discount.
        """
        return self.calculate_discount(holder, DiscountType.TRADING_FEE, trading_fee)

    def calculate_purchase_discount(self, holder: str, purchase_amount: float) -> float:
        """
        Calculates the purchase discount for a given holder.

        Args:
        - holder (str): The token holder.
        - purchase_amount (float): The purchase amount.

        Returns:
        - float: The calculated purchase discount.
        """
        return self.calculate_discount(holder, DiscountType.PURCHASE, purchase_amount)


def main():
    # Example usage
    token_balances = {
        "holder1": 10000,
        "holder2": 500
    }

    discount_rates = {
        DiscountType.TRADING_FEE: 5,
        DiscountType.PURCHASE: 10
    }

    calculator = TokenDiscountCalculator(token_balances, discount_rates)

    holder = "holder1"
    trading_fee = 100
    purchase_amount = 1000

    trading_fee_discount = calculator.calculate_trading_fee_discount(holder, trading_fee)
    purchase_discount = calculator.calculate_purchase_discount(holder, purchase_amount)

    print(f"Trading fee discount for {holder}: {trading_fee_discount}")
    print(f"Purchase discount for {holder}: {purchase_discount}")


if __name__ == "__main__":
    main()
```
