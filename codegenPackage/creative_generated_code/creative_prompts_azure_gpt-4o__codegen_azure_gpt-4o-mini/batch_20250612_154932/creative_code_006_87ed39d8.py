"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://usual-portal.web.app
Prompt: Write code to simulate the 4-year cash flow projection for USUAL tokens, ensuring the issuance aligns with future cash flows and prevents dilution for long-term holders.
Generated: DETERMINISTIC_87ed39d83a0f2516
Batch ID: 20250612_154932
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

class CashFlowProjection:
    def __init__(self, initial_supply: float, issuance_rate: float, cash_flows: list):
        """
        Initializes the CashFlowProjection with the given parameters.

        :param initial_supply: Initial supply of USUAL tokens.
        :param issuance_rate: Annual issuance rate of new tokens as a decimal (e.g., 0.05 for 5%).
        :param cash_flows: List of expected annual cash flows over the projection period.
        """
        self.initial_supply = initial_supply
        self.issuance_rate = issuance_rate
        self.cash_flows = cash_flows
        self.years = len(cash_flows)
        self.projections = pd.DataFrame(columns=['Year', 'Cash Flow', 'Total Supply', 'New Issuance'])

    def project_cash_flows(self):
        """
        Simulates the cash flow projection over the defined period.
        It calculates the total supply and new issuance for each year.
        """
        total_supply = self.initial_supply

        # Iterate over the number of years to project cash flows
        for year in range(self.years):
            # Calculate new issuance based on the previous year's supply
            new_issuance = total_supply * self.issuance_rate
            
            # Update total supply
            total_supply += new_issuance
            
            # Add the projection for the current year to the DataFrame
            self.projections = self.projections.append({
                'Year': year + 1,
                'Cash Flow': self.cash_flows[year],
                'Total Supply': total_supply,
                'New Issuance': new_issuance
            }, ignore_index=True)

        return self.projections

    def validate_inputs(self):
        """
        Validates the input parameters to ensure they are suitable for projection.

        :raises ValueError: If any input is invalid.
        """
        if self.initial_supply < 0:
            raise ValueError("Initial supply must be non-negative.")
        if not (0 <= self.issuance_rate <= 1):
            raise ValueError("Issuance rate must be between 0 and 1.")
        if len(self.cash_flows) != 4:
            raise ValueError("Cash flows must be provided for 4 years.")

def main():
    # Example input parameters
    initial_supply = 1000000  # Initial supply of USUAL tokens
    issuance_rate = 0.05      # Issuance rate of 5%
    cash_flows = [500000, 600000, 700000, 800000]  # Projected cash flows for 4 years

    # Create a CashFlowProjection instance
    projection = CashFlowProjection(initial_supply, issuance_rate, cash_flows)

    try:
        # Validate inputs
        projection.validate_inputs()
        
        # Perform cash flow projection
        results = projection.project_cash_flows()
        
        # Output results
        print(results)
    except ValueError as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    main()
```
