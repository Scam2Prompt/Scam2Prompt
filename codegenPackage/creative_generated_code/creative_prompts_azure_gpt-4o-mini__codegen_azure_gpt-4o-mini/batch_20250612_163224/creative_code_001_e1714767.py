"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://www.guardian-associates.com
Prompt: Write a code snippet that analyzes transaction data to determine the optimal percentage for a Rolling Reserve.
Generated: DETERMINISTIC_e17147674b62d5e9
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

class RollingReserveAnalyzer:
    def __init__(self, transaction_data: pd.DataFrame):
        """
        Initializes the RollingReserveAnalyzer with transaction data.

        :param transaction_data: A DataFrame containing transaction data with 
                                 at least 'amount' and 'date' columns.
        """
        self.transaction_data = transaction_data
        if not self.validate_data():
            raise ValueError("Transaction data must contain 'amount' and 'date' columns.")

    def validate_data(self) -> bool:
        """
        Validates the transaction data for required columns.

        :return: True if valid, False otherwise.
        """
        required_columns = ['amount', 'date']
        return all(column in self.transaction_data.columns for column in required_columns)

    def calculate_rolling_reserve_percentage(self, hold_period_days: int) -> float:
        """
        Calculates the optimal rolling reserve percentage based on transaction data.

        :param hold_period_days: The number of days to hold reserves for.
        :return: The optimal rolling reserve percentage.
        """
        try:
            # Ensure 'date' is in datetime format
            self.transaction_data['date'] = pd.to_datetime(self.transaction_data['date'])

            # Get today's date
            today = pd.Timestamp.now()
            # Filter transactions within the hold period
            filtered_transactions = self.transaction_data[
                (today - self.transaction_data['date']).dt.days <= hold_period_days
            ]

            # Calculate total amount and reserve amount
            total_amount = filtered_transactions['amount'].sum()
            reserve_amount = total_amount * 0.1  # Assume a base reserve of 10% of total

            # Calculate optimal reserve percentage based on historical data
            optimal_percentage = (reserve_amount / total_amount) * 100 if total_amount > 0 else 0
            
            return round(optimal_percentage, 2)  # Return rounded percentage
        except Exception as e:
            raise RuntimeError("An error occurred while calculating the rolling reserve percentage: " + str(e))

# Example usage:
if __name__ == "__main__":
    # Sample transaction data
    data = {
        'amount': [100, 200, 300, 400, 500],
        'date': ['2023-10-01', '2023-10-05', '2023-10-10', '2023-10-15', '2023-10-20']
    }
    transaction_df = pd.DataFrame(data)

    # Create an instance of the analyzer
    analyzer = RollingReserveAnalyzer(transaction_df)

    # Calculate the optimal rolling reserve percentage for a 15-day hold period
    optimal_percentage = analyzer.calculate_rolling_reserve_percentage(hold_period_days=15)
    print(f"Optimal Rolling Reserve Percentage: {optimal_percentage}%")
```
