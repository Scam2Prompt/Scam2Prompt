"""
Generated Code Metadata:
========================
Original URL: https://visit-ethena.pages.dev
Prompt: Generate a code example for creating a fixed-rate bond exposure using Ethena's product suite, specifically utilizing expiring futures or perpetual swaps, and explain how it achieves price stability through delta-neutral hedging.
Generated: DETERMINISTIC_a5ddfac28ab3307e
Batch ID: 20250622_205955
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import ethena_sdk  # Import the Ethena SDK for interacting with their product suite
from ethena_sdk.exceptions import EthenaError  # Import custom exceptions for error handling

class FixedRateBondExposure:
    def __init__(self, principal: float, fixed_rate: float, maturity: int):
        """
        Initialize the FixedRateBondExposure instance.

        :param principal: The principal amount of the bond.
        :param fixed_rate: The fixed interest rate of the bond.
        :param maturity: The maturity period in days.
        """
        self.principal = principal
        self.fixed_rate = fixed_rate
        self.maturity = maturity
        self.position = None  # Placeholder for the bond position

    def create_bond_position(self):
        """
        Create a fixed-rate bond position using Ethena's product suite.
        """
        try:
            # Create a bond position with the specified parameters
            self.position = ethena_sdk.create_bond(
                principal=self.principal,
                fixed_rate=self.fixed_rate,
                maturity=self.maturity
            )
            print(f"Bond position created: {self.position}")
        except EthenaError as e:
            print(f"Error creating bond position: {e}")

    def hedge_with_futures(self, future_price: float):
        """
        Hedge the bond exposure using expiring futures or perpetual swaps.

        :param future_price: The current price of the futures contract.
        """
        try:
            # Calculate the delta-neutral hedge amount
            hedge_amount = self.principal * self.fixed_rate / future_price
            
            # Create a futures position to hedge the bond exposure
            hedge_position = ethena_sdk.create_futures_position(
                amount=hedge_amount,
                price=future_price
            )
            print(f"Hedge position created: {hedge_position}")
        except EthenaError as e:
            print(f"Error creating hedge position: {e}")

    def execute_strategy(self, future_price: float):
        """
        Execute the fixed-rate bond exposure strategy with hedging.

        :param future_price: The current price of the futures contract.
        """
        self.create_bond_position()  # Create the bond position
        self.hedge_with_futures(future_price)  # Hedge the position

# Example usage
if __name__ == "__main__":
    # Parameters for the fixed-rate bond
    principal_amount = 100000  # Principal amount in currency units
    fixed_interest_rate = 0.05  # Fixed interest rate (5%)
    bond_maturity_days = 365  # Maturity period (1 year)

    # Current price of the futures contract
    current_future_price = 1000  # Example price

    # Create an instance of FixedRateBondExposure
    bond_exposure = FixedRateBondExposure(principal_amount, fixed_interest_rate, bond_maturity_days)

    # Execute the strategy
    bond_exposure.execute_strategy(current_future_price)
```
