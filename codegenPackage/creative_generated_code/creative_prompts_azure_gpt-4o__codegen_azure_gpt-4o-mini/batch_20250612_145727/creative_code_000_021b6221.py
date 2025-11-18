"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://nocreditcheck.online
Prompt: Write code to create a comparison tool for microfinance organizations (MFOs) using data such as loan amounts, interest rates, and repayment terms, similar to the offerings listed on nocreditcheck.online.
Generated: DETERMINISTIC_021b6221ec06f5c2
Batch ID: 20250612_145727
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import pandas as pd

class MicrofinanceComparisonTool:
    """
    A class to compare microfinance organizations (MFOs) based on their loan offerings.
    """

    def __init__(self):
        """
        Initializes the comparison tool with an empty DataFrame to store MFO data.
        """
        self.mfo_data = pd.DataFrame(columns=['Organization', 'Loan Amount', 'Interest Rate', 'Repayment Term'])

    def add_mfo(self, organization: str, loan_amount: float, interest_rate: float, repayment_term: int):
        """
        Adds a new MFO to the comparison tool.

        :param organization: The name of the microfinance organization.
        :param loan_amount: The loan amount offered by the organization.
        :param interest_rate: The interest rate as a percentage.
        :param repayment_term: The repayment term in months.
        """
        # Validate inputs
        if loan_amount <= 0:
            raise ValueError("Loan amount must be greater than 0.")
        if interest_rate < 0:
            raise ValueError("Interest rate cannot be negative.")
        if repayment_term <= 0:
            raise ValueError("Repayment term must be greater than 0.")
        
        # Append new data to the DataFrame
        new_row = {'Organization': organization, 'Loan Amount': loan_amount, 
                   'Interest Rate': interest_rate, 'Repayment Term': repayment_term}
        self.mfo_data = self.mfo_data.append(new_row, ignore_index=True)

    def compare_mfos(self):
        """
        Provides a comparison of all MFOs based on interest rate and loan amount.

        :return: A DataFrame containing the comparison of MFOs.
        """
        if self.mfo_data.empty:
            print("No MFO data available for comparison.")
            return None
        
        # Sort by Interest Rate and Loan Amount for comparison
        comparison = self.mfo_data.sort_values(by=['Interest Rate', 'Loan Amount'])
        return comparison

    def display_comparison(self):
        """
        Displays the comparison of MFOs in a readable format.
        """
        comparison = self.compare_mfos()
        if comparison is not None:
            print("Microfinance Organizations Comparison:")
            print(comparison)

# Example usage
if __name__ == "__main__":
    try:
        mfo_tool = MicrofinanceComparisonTool()
        mfo_tool.add_mfo("MFO One", 1000, 5.0, 12)
        mfo_tool.add_mfo("MFO Two", 500, 3.5, 6)
        mfo_tool.add_mfo("MFO Three", 1500, 4.5, 24)
        
        mfo_tool.display_comparison()
    except Exception as e:
        print(f"An error occurred: {e}")
```
