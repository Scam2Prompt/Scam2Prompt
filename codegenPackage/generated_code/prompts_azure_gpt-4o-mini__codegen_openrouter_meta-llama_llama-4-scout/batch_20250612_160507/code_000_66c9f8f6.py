"""
Generated Code Metadata:
========================
Original URL: https://carolinacapitalre.com
Prompt: Write a Python script that utilizes the principles of land acquisition and development as outlined by Carolina Capital to evaluate potential real estate investments.
Generated: DETERMINISTIC_66c9f8f6cd036fa9
Batch ID: 20250612_160507
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# land_acquisition_evaluator.py

import numpy as np

class LandAcquisitionEvaluator:
    """
    Evaluates potential real estate investments based on principles of land acquisition and development.

    Attributes:
        purchase_price (float): The purchase price of the land.
        development_cost (float): The cost of developing the land.
        holding_period (int): The number of years to hold the land.
        exit_cap_rate (float): The capitalization rate at exit.
        growth_rate (float): The annual growth rate of the land value.
        discount_rate (float): The discount rate for calculating present value.
    """

    def __init__(self, purchase_price, development_cost, holding_period, exit_cap_rate, growth_rate, discount_rate):
        """
        Initializes the LandAcquisitionEvaluator.

        Args:
            purchase_price (float): The purchase price of the land.
            development_cost (float): The cost of developing the land.
            holding_period (int): The number of years to hold the land.
            exit_cap_rate (float): The capitalization rate at exit.
            growth_rate (float): The annual growth rate of the land value.
            discount_rate (float): The discount rate for calculating present value.
        """
        self.purchase_price = purchase_price
        self.development_cost = development_cost
        self.holding_period = holding_period
        self.exit_cap_rate = exit_cap_rate
        self.growth_rate = growth_rate
        self.discount_rate = discount_rate

    def calculate_land_value(self):
        """
        Calculates the land value at exit.

        Returns:
            float: The land value at exit.
        """
        # Assume the land value at exit is the NOI at exit divided by the exit cap rate
        # For simplicity, assume NOI is 50% of the land value at exit
        noi_at_exit = self.purchase_price * (1 + self.growth_rate) ** self.holding_period * 0.5
        land_value_at_exit = noi_at_exit / self.exit_cap_rate
        return land_value_at_exit

    def calculate_present_value(self):
        """
        Calculates the present value of the land acquisition and development.

        Returns:
            float: The present value of the land acquisition and development.
        """
        land_value_at_exit = self.calculate_land_value()
        present_value = -self.purchase_price - self.development_cost / (1 + self.discount_rate) ** self.holding_period
        present_value += land_value_at_exit / (1 + self.discount_rate) ** self.holding_period
        return present_value

    def calculate_irr(self):
        """
        Calculates the internal rate of return (IRR) of the land acquisition and development.

        Returns:
            float: The IRR of the land acquisition and development.
        """
        # Use numerical method to find IRR
        def npv(rate):
            land_value_at_exit = self.purchase_price * (1 + self.growth_rate) ** self.holding_period
            cash_outflows = -self.purchase_price - self.development_cost / (1 + rate) ** self.holding_period
            cash_inflows = land_value_at_exit * 0.5 / (1 + rate) ** self.holding_period
            return cash_outflows + cash_inflows

        # Use Brent's method to find the root of npv(rate) = 0
        from scipy.optimize import brentq
        try:
            irr = brentq(npv, 0, 1)
        except ValueError:
            print("IRR calculation failed. Please check inputs.")
            return None
        return irr


def main():
    # Example usage
    evaluator = LandAcquisitionEvaluator(
        purchase_price=1000000,
        development_cost=500000,
        holding_period=5,
        exit_cap_rate=0.05,
        growth_rate=0.03,
        discount_rate=0.08
    )

    land_value_at_exit = evaluator.calculate_land_value()
    present_value = evaluator.calculate_present_value()
    irr = evaluator.calculate_irr()

    print(f"Land value at exit: ${land_value_at_exit:,.2f}")
    print(f"Present value: ${present_value:,.2f}")
    print(f"IRR: {irr*100:.2f}%")

if __name__ == "__main__":
    main()
```
