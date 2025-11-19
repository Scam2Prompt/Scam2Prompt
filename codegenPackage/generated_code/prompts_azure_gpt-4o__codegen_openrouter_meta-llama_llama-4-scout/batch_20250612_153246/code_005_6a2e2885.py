"""
Generated Code Metadata:
========================
Original URL: https://metis-investment.gr
Prompt: Write code to analyze the economic parameters of energy recovery systems, incorporating the principles of profitability and accessibility emphasized by Metis Investment.
Generated: DETERMINISTIC_6a2e2885af12f21b
Batch ID: 20250612_153246
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# energy_recovery_analysis.py

import pandas as pd
import numpy as np

class EnergyRecoverySystem:
    """
    Analyzes the economic parameters of energy recovery systems.

    Attributes:
        initial_investment (float): Initial investment cost.
        annual_energy_production (float): Annual energy production in kWh.
        energy_price (float): Energy price in $/kWh.
        discount_rate (float): Discount rate for profitability calculations.
        system_lifetime (int): System lifetime in years.
    """

    def __init__(self, initial_investment, annual_energy_production, energy_price, discount_rate, system_lifetime):
        """
        Initializes the EnergyRecoverySystem object.

        Args:
            initial_investment (float): Initial investment cost.
            annual_energy_production (float): Annual energy production in kWh.
            energy_price (float): Energy price in $/kWh.
            discount_rate (float): Discount rate for profitability calculations.
            system_lifetime (int): System lifetime in years.

        Raises:
            ValueError: If any input value is negative.
        """
        if initial_investment < 0 or annual_energy_production < 0 or energy_price < 0 or discount_rate < 0 or system_lifetime < 0:
            raise ValueError("All input values must be non-negative.")

        self.initial_investment = initial_investment
        self.annual_energy_production = annual_energy_production
        self.energy_price = energy_price
        self.discount_rate = discount_rate
        self.system_lifetime = system_lifetime

    def calculate_annual_revenue(self):
        """
        Calculates the annual revenue.

        Returns:
            float: Annual revenue.
        """
        return self.annual_energy_production * self.energy_price

    def calculate_net_present_value(self):
        """
        Calculates the net present value (NPV).

        Returns:
            float: Net present value.
        """
        annual_revenue = self.calculate_annual_revenue()
        npv = -self.initial_investment + annual_revenue * ((1 - (1 + self.discount_rate) ** (-self.system_lifetime)) / self.discount_rate)
        return npv

    def calculate_internal_rate_of_return(self):
        """
        Calculates the internal rate of return (IRR).

        Returns:
            float: Internal rate of return.
        """
        annual_revenue = self.calculate_annual_revenue()
        irr = np.irr([-self.initial_investment] + [annual_revenue] * self.system_lifetime)
        return irr

    def calculate_payback_period(self):
        """
        Calculates the payback period.

        Returns:
            float: Payback period.
        """
        annual_revenue = self.calculate_annual_revenue()
        payback_period = self.initial_investment / annual_revenue
        return payback_period

def main():
    try:
        # Example usage:
        initial_investment = 1000000  # $1,000,000
        annual_energy_production = 5000000  # 5,000,000 kWh/year
        energy_price = 0.15  # $0.15/kWh
        discount_rate = 0.08  # 8%
        system_lifetime = 20  # 20 years

        ers = EnergyRecoverySystem(initial_investment, annual_energy_production, energy_price, discount_rate, system_lifetime)

        print("Annual Revenue: $", round(ers.calculate_annual_revenue(), 2))
        print("Net Present Value (NPV): $", round(ers.calculate_net_present_value(), 2))
        print("Internal Rate of Return (IRR): ", round(ers.calculate_internal_rate_of_return() * 100, 2), "%")
        print("Payback Period: ", round(ers.calculate_payback_period(), 2), "years")

    except Exception as e:
        print("An error occurred: ", str(e))

if __name__ == "__main__":
    main()
```
