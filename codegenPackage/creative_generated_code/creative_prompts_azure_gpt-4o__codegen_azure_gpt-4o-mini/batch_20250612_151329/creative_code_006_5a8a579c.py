"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://alixa.tech
Prompt: Create a tool to calculate the earning power (EP) for bonds with varying maturity periods (e.g., 30 days, 90 days, 180 days, 365 days) on the Alixa platform.
Generated: DETERMINISTIC_5a8a579c35c6914a
Batch ID: 20250612_151329
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import numpy as np
import pandas as pd

class BondCalculator:
    """
    A class to calculate the earning power (EP) of bonds with varying maturity periods.
    """

    def __init__(self, principal, interest_rate, maturity_days):
        """
        Initializes the BondCalculator with principal, interest rate, and maturity period.
        
        :param principal: The amount of money invested in the bond.
        :param interest_rate: Annual interest rate of the bond expressed as a decimal.
        :param maturity_days: The number of days until the bond matures.
        """
        self.principal = principal
        self.interest_rate = interest_rate
        self.maturity_days = maturity_days

    def calculate_ep(self):
        """
        Calculates the earning power (EP) of the bond based on the principal, interest rate, and maturity period.
        
        :return: The earning power of the bond.
        """
        try:
            # Calculate the interest earned over the maturity period
            interest_earned = (self.principal * self.interest_rate * self.maturity_days) / 365
            ep = self.principal + interest_earned  # Total amount after maturity
            return ep
        except Exception as e:
            print(f"An error occurred while calculating earning power: {e}")
            return None

def main():
    """
    Main function to execute the BondCalculator for different maturity periods.
    """
    # Define bond parameters
    principal = 1000.0  # Example principal amount
    interest_rate = 0.05  # Example annual interest rate (5%)
    maturities = [30, 90, 180, 365]  # Different maturity periods in days

    # Create a DataFrame to store results
    results = pd.DataFrame(columns=["Maturity Days", "Earning Power"])

    # Calculate earning power for each maturity period
    for days in maturities:
        bond = BondCalculator(principal, interest_rate, days)
        ep = bond.calculate_ep()
        results = results.append({"Maturity Days": days, "Earning Power": ep}, ignore_index=True)

    # Output the results
    print("\nEarning Power of Bonds with Varying Maturity Periods:")
    print(results)

if __name__ == "__main__":
    main()
```
