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

def calculate_optimal_rolling_reserve(transactions):
    """
    Analyzes transaction data to determine the optimal percentage for a Rolling Reserve.
    
    Args:
        transactions (pd.DataFrame): A DataFrame containing transaction data with the following columns:
            - 'transaction_id': Unique identifier for each transaction.
            - 'amount': Transaction amount (positive for earnings, negative for refunds/chargebacks).
            - 'date': Date of transaction in 'YYYY-MM-DD' format.
    
    Returns:
        float: The optimal rolling reserve percentage.
    """
    try:
        # Ensure required columns exist in the DataFrame
        required_columns = {'transaction_id', 'amount', 'date'}
        if not required_columns.issubset(transactions.columns):
            raise ValueError(f"Missing required columns. Expected columns: {required_columns}")
        
        # Parse 'date' column to ensure proper datetime format
        transactions['date'] = pd.to_datetime(transactions['date'], errors='coerce')
        if transactions['date'].isnull().any():
            raise ValueError("Invalid dates detected in 'date' column.")

        # Calculate rolling reserve percentage based on chargebacks/refunds vs total revenue
        total_revenue = transactions[transactions['amount'] > 0]['amount'].sum()
        total_chargebacks = transactions[transactions['amount'] < 0]['amount'].sum() * -1  # Convert negative values to positive
        
        if total_revenue == 0:
            raise ValueError("Total revenue is zero. Cannot calculate rolling reserve percentage.")
        
        rolling_reserve_percentage = (total_chargebacks / total_revenue) * 100

        return round(rolling_reserve_percentage, 2)  # Return percentage rounded to two decimal places

    except Exception as e:
        # Proper error handling with meaningful error messages
        print(f"Error calculating rolling reserve: {e}")
        return None


# Example usage
if __name__ == "__main__":
    # Sample transaction data
    data = {
        'transaction_id': [1, 2, 3, 4, 5],
        'amount': [100, 200, -50, 300, -30],
        'date': ['2023-10-01', '2023-10-02', '2023-10-03', '2023-10-04', '2023-10-05'],
    }
    transactions_df = pd.DataFrame(data)

    # Calculate and display the optimal rolling reserve percentage
    optimal_percentage = calculate_optimal_rolling_reserve(transactions_df)
    if optimal_percentage is not None:
        print(f"Optimal Rolling Reserve Percentage: {optimal_percentage}%")
```
