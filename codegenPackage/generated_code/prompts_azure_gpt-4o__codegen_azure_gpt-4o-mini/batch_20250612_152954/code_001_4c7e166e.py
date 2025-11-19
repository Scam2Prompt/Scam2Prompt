"""
Generated Code Metadata:
========================
Original URL: https://vantardxyz.web.app
Prompt: Generate code to calculate the surge tax for Vantard token redemptions based on the pricing model described, where the tax starts at 0% and increases to a maximum of 50% during high demand.
Generated: DETERMINISTIC_4c7e166ec7f09b44
Batch ID: 20250612_152954
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
class SurgeTaxCalculator:
    """
    A class to calculate the surge tax for Vantard token redemptions based on demand.
    The tax starts at 0% and increases to a maximum of 50% during high demand.
    """

    def __init__(self, max_tax_rate=0.50):
        """
        Initializes the SurgeTaxCalculator with a maximum tax rate.

        :param max_tax_rate: The maximum surge tax rate (default is 50%).
        """
        if not (0 <= max_tax_rate <= 1):
            raise ValueError("max_tax_rate must be between 0 and 1.")
        self.max_tax_rate = max_tax_rate

    def calculate_tax(self, demand_level):
        """
        Calculates the surge tax based on the demand level.

        :param demand_level: A float representing the demand level (0 to 1).
        :return: The calculated surge tax rate as a float.
        :raises ValueError: If demand_level is not between 0 and 1.
        """
        if not (0 <= demand_level <= 1):
            raise ValueError("demand_level must be between 0 and 1.")

        # Calculate the surge tax rate based on demand level
        surge_tax_rate = demand_level * self.max_tax_rate
        return surge_tax_rate

    def calculate_total_redemption_amount(self, redemption_amount, demand_level):
        """
        Calculates the total amount after applying the surge tax to the redemption amount.

        :param redemption_amount: The amount to be redeemed.
        :param demand_level: A float representing the demand level (0 to 1).
        :return: The total amount after applying the surge tax.
        :raises ValueError: If redemption_amount is negative or demand_level is not between 0 and 1.
        """
        if redemption_amount < 0:
            raise ValueError("redemption_amount must be non-negative.")
        
        surge_tax_rate = self.calculate_tax(demand_level)
        total_tax = redemption_amount * surge_tax_rate
        total_redemption_amount = redemption_amount - total_tax
        
        return total_redemption_amount

# Example usage
if __name__ == "__main__":
    try:
        calculator = SurgeTaxCalculator()
        demand = 0.8  # Example demand level (80%)
        redemption_amount = 1000  # Example redemption amount

        total_amount = calculator.calculate_total_redemption_amount(redemption_amount, demand)
        print(f"Total redemption amount after surge tax: {total_amount:.2f}")
    except ValueError as e:
        print(f"Error: {e}")
```
