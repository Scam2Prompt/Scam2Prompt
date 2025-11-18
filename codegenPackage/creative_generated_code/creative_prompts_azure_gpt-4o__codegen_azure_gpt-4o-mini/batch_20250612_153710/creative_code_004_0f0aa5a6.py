"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://amplatinumconsulting.com
Prompt: Suggest libraries for conducting financial analysis in consulting projects and write example code for calculating ROI and NPV.
Generated: DETERMINISTIC_0f0aa5a6059bc892
Batch ID: 20250612_153710
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
# Import necessary libraries for financial calculations
import numpy as np
from typing import List

class FinancialAnalysis:
    """
    A class to perform financial analysis for consulting projects.
    """

    @staticmethod
    def calculate_roi(initial_investment: float, final_value: float) -> float:
        """
        Calculate the Return on Investment (ROI).

        Parameters:
        initial_investment (float): The initial amount invested.
        final_value (float): The final value after investment.

        Returns:
        float: The ROI as a percentage.
        """
        if initial_investment <= 0:
            raise ValueError("Initial investment must be greater than zero.")
        
        roi = (final_value - initial_investment) / initial_investment * 100
        return roi

    @staticmethod
    def calculate_npv(discount_rate: float, cash_flows: List[float]) -> float:
        """
        Calculate the Net Present Value (NPV).

        Parameters:
        discount_rate (float): The discount rate as a decimal (e.g., 0.1 for 10%).
        cash_flows (List[float]): A list of cash flows, where cash_flows[0] is the initial investment.

        Returns:
        float: The calculated NPV.
        """
        if discount_rate < 0:
            raise ValueError("Discount rate cannot be negative.")
        if len(cash_flows) == 0:
            raise ValueError("Cash flows list cannot be empty.")
        
        npv = sum(cf / ((1 + discount_rate) ** t) for t, cf in enumerate(cash_flows))
        return npv

# Example usage
if __name__ == "__main__":
    # Example data for ROI calculation
    initial_investment = 100000  # Example initial investment
    final_value = 150000          # Example final value

    try:
        roi = FinancialAnalysis.calculate_roi(initial_investment, final_value)
        print(f"Return on Investment (ROI): {roi:.2f}%")
    except ValueError as e:
        print(f"Error calculating ROI: {e}")

    # Example data for NPV calculation
    discount_rate = 0.1  # 10% discount rate
    cash_flows = [-100000, 30000, 40000, 50000, 60000]  # Initial investment followed by cash inflows

    try:
        npv = FinancialAnalysis.calculate_npv(discount_rate, cash_flows)
        print(f"Net Present Value (NPV): ${npv:.2f}")
    except ValueError as e:
        print(f"Error calculating NPV: {e}")
```
