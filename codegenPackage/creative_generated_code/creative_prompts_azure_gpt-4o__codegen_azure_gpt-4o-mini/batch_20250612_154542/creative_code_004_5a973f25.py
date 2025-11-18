"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://raydium-ui-v3-inner-o75wsdpq3-raydium.vercel.app
Prompt: Create a script to calculate the minimum received amount for a token swap on Raydium, factoring in price impact and fees.
Generated: DETERMINISTIC_5a973f25a7f91fe4
Batch ID: 20250612_154542
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import requests

class TokenSwapCalculator:
    """
    A class to calculate the minimum received amount for a token swap on Raydium,
    factoring in price impact and fees.
    """

    def __init__(self, token_in_amount, price_impact, fee_percentage):
        """
        Initializes the TokenSwapCalculator with given parameters.

        :param token_in_amount: Amount of the input token for the swap
        :param price_impact: Price impact percentage during the swap (0 to 100)
        :param fee_percentage: Fee percentage charged during the swap (0 to 100)
        """
        self.token_in_amount = token_in_amount
        self.price_impact = price_impact / 100  # Convert to decimal
        self.fee_percentage = fee_percentage / 100  # Convert to decimal

    def calculate_min_received(self):
        """
        Calculates the minimum amount received after considering
        price impact and fees.

        :return: Minimum amount received after swap
        """
        # Validate inputs
        self._validate_inputs()

        # Calculate the effective amount after price impact
        effective_amount = self.token_in_amount * (1 - self.price_impact)

        # Calculate the fee deducted from the effective amount
        fee_deduction = effective_amount * self.fee_percentage

        # Minimum received amount after fee deduction
        min_received = effective_amount - fee_deduction

        return min_received

    def _validate_inputs(self):
        """
        Validates the input parameters to ensure they are within
        acceptable ranges.

        :raises ValueError: If any input parameter is out of range
        """
        if self.token_in_amount <= 0:
            raise ValueError("Token input amount must be greater than 0.")
        if not (0 <= self.price_impact <= 100):
            raise ValueError("Price impact must be between 0 and 100.")
        if not (0 <= self.fee_percentage <= 100):
            raise ValueError("Fee percentage must be between 0 and 100.")

def main():
    # Example usage of the TokenSwapCalculator
    try:
        amount_to_swap = 1000  # Amount of token to swap
        price_impact = 2.5      # 2.5% price impact
        fee_percentage = 0.3     # 0.3% fee

        calculator = TokenSwapCalculator(amount_to_swap, price_impact, fee_percentage)
        min_received = calculator.calculate_min_received()

        print(f"Minimum amount received: {min_received:.2f}")

    except ValueError as e:
        print(f"Input error: {e}")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")

if __name__ == "__main__":
    main()
```
