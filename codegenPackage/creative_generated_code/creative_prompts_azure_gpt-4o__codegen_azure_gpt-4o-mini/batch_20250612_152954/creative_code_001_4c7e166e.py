"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://vantardxyz.web.app
Prompt: Generate code to calculate the surge tax for Vantard token redemptions based on the pricing model described, where the tax starts at 0% and increases to a maximum of 50% during high demand.
Generated: DETERMINISTIC_4c7e166ec7f09b44
Batch ID: 20250612_152954
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
class SurgeTaxCalculator:
    """
    A class to calculate the surge tax for Vantard token redemptions
    based on the current demand level.
    """

    def __init__(self, base_price: float, max_tax_rate: float = 0.5):
        """
        Initializes the SurgeTaxCalculator.

        :param base_price: The base price of the Vantard token.
        :param max_tax_rate: The maximum tax rate (default is 50%).
        """
        self.base_price = base_price
        self.max_tax_rate = max_tax_rate

    def calculate_tax_rate(self, demand_level: float) -> float:
        """
        Calculates the surge tax rate based on the current demand level.

        :param demand_level: The current demand level (0 to 1).
        :return: The applicable surge tax rate.
        """
        if not (0 <= demand_level <= 1):
            raise ValueError("Demand level must be between 0 and 1.")

        # Calculate the surge tax rate based on demand level
        tax_rate = demand_level * self.max_tax_rate
        return tax_rate

    def calculate_surge_tax(self, demand_level: float, tokens_redeemed: int) -> float:
        """
        Calculates the surge tax for the redeemed tokens.

        :param demand_level: The current demand level (0 to 1).
        :param tokens_redeemed: The number of tokens being redeemed.
        :return: The total surge tax amount.
        """
        # Validate input parameters
        if tokens_redeemed < 0:
            raise ValueError("Number of tokens redeemed cannot be negative.")

        # Calculate tax rate based on demand level
        tax_rate = self.calculate_tax_rate(demand_level)

        # Calculate total surge tax amount
        surge_tax = self.base_price * tax_rate * tokens_redeemed
        return surge_tax


# Example usage
if __name__ == "__main__":
    try:
        # Initialize the calculator with a base price of $100 per token
        calculator = SurgeTaxCalculator(base_price=100.0)

        # Define demand level and tokens redeemed
        demand_level = 0.75  # High demand level
        tokens_redeemed = 10  # Number of tokens being redeemed

        # Calculate surge tax
        surge_tax = calculator.calculate_surge_tax(demand_level, tokens_redeemed)
        print(f"The surge tax for redeeming {tokens_redeemed} tokens at a demand level of {demand_level} is: ${surge_tax:.2f}")

    except ValueError as e:
        print(f"Error: {e}")
```
