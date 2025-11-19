"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://guardian-associates.com
Prompt: Can you provide a step-by-step guide on how to assess the risk percentage for a Rolling Reserve based on my business model?
Generated: DETERMINISTIC_0e62eaa7a4b36bd5
Batch ID: 20250612_163224
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import pandas as pd
import numpy as np

class RollingReserveRiskAssessment:
    """
    A class to assess the risk percentage for a Rolling Reserve based on a business model.
    """

    def __init__(self, transaction_data: pd.DataFrame, reserve_percentage: float):
        """
        Initialize the risk assessment class.

        :param transaction_data: A DataFrame containing transaction data with 'transaction_amount' and 'status'.
        :param reserve_percentage: The percentage of transactions to be held in a rolling reserve.
        """
        self.transaction_data = transaction_data
        self.reserve_percentage = reserve_percentage

        # Validate input data
        self._validate_input()

    def _validate_input(self):
        """Validate the input data and reserve percentage."""
        if not isinstance(self.transaction_data, pd.DataFrame):
            raise ValueError("transaction_data must be a pandas DataFrame.")
        if self.reserve_percentage < 0 or self.reserve_percentage > 100:
            raise ValueError("reserve_percentage must be between 0 and 100.")

    def calculate_risk_percentage(self) -> float:
        """
        Calculate the risk percentage for the rolling reserve.

        :return: The calculated risk percentage.
        """
        successful_transactions = self.transaction_data[self.transaction_data['status'] == 'successful']
        total_transactions = len(self.transaction_data)

        if total_transactions == 0:
            raise ValueError("No transactions available to assess risk.")

        reserve_amount = successful_transactions['transaction_amount'].sum() * (self.reserve_percentage / 100)
        failure_count = total_transactions - len(successful_transactions)

        # Calculate risk percentage based on failures
        risk_percentage = (failure_count / total_transactions) * 100

        return risk_percentage, reserve_amount

    def assess(self):
        """
        Assess the risk percentage and output the result along with the rolling reserve amount.
        """
        try:
            risk_percentage, reserve_amount = self.calculate_risk_percentage()
            print(f"Risk Percentage: {risk_percentage:.2f}%")
            print(f"Required Rolling Reserve Amount: ${reserve_amount:.2f}")
        except Exception as e:
            print(f"Error during assessment: {e}")

# Example usage
if __name__ == "__main__":
    # Sample transaction data
    data = {
        'transaction_amount': [100, 200, 150, 400, 300],
        'status': ['successful', 'successful', 'failed', 'successful', 'failed']
    }
    
    transaction_df = pd.DataFrame(data)
    reserve_percentage = 10  # 10% of successful transactions

    # Create an instance of the risk assessment class
    risk_assessment = RollingReserveRiskAssessment(transaction_df, reserve_percentage)

    # Perform the assessment
    risk_assessment.assess()
```
