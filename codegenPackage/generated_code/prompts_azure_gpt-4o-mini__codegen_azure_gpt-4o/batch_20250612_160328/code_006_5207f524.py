"""
Generated Code Metadata:
========================
Original URL: https://financial-justice.com
Prompt: How can I write a script to analyze trading patterns and flag suspicious activities that may indicate a Ponzi scheme?
Generated: DETERMINISTIC_5207f524c50740ab
Batch ID: 20250612_160328
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import pandas as pd
import numpy as np
from datetime import datetime

# Define constants for suspicious activity thresholds
MINIMUM_INVESTORS = 50  # Minimum number of investors to consider
HIGH_RETURN_THRESHOLD = 0.2  # 20% return in a short period
UNUSUAL_WITHDRAWAL_RATIO = 0.8  # 80% of funds withdrawn in a short period
SHORT_TIME_PERIOD_DAYS = 30  # Time period to analyze suspicious activity

# Function to analyze trading patterns and flag suspicious activities
def analyze_trading_patterns(data):
    """
    Analyze trading patterns to flag suspicious activities that may indicate a Ponzi scheme.

    Parameters:
        data (pd.DataFrame): A DataFrame containing trading data with the following columns:
            - 'investor_id': Unique ID for each investor
            - 'transaction_date': Date of the transaction
            - 'transaction_type': Type of transaction ('deposit' or 'withdrawal')
            - 'amount': Amount of the transaction

    Returns:
        pd.DataFrame: A DataFrame containing flagged suspicious activities.
    """
    try:
        # Ensure the input data has the required columns
        required_columns = {'investor_id', 'transaction_date', 'transaction_type', 'amount'}
        if not required_columns.issubset(data.columns):
            raise ValueError(f"Input data must contain the following columns: {required_columns}")

        # Convert transaction_date to datetime for easier manipulation
        data['transaction_date'] = pd.to_datetime(data['transaction_date'])

        # Group data by investor_id and analyze patterns
        suspicious_activities = []
        for investor_id, group in data.groupby('investor_id'):
            # Sort transactions by date
            group = group.sort_values(by='transaction_date')

            # Calculate total deposits and withdrawals
            total_deposits = group[group['transaction_type'] == 'deposit']['amount'].sum()
            total_withdrawals = group[group['transaction_type'] == 'withdrawal']['amount'].sum()

            # Calculate withdrawal-to-deposit ratio
            withdrawal_ratio = total_withdrawals / total_deposits if total_deposits > 0 else 0

            # Check for high returns in a short period
            group['cumulative_balance'] = group.apply(
                lambda row: row['amount'] if row['transaction_type'] == 'deposit' else -row['amount'], axis=1
            ).cumsum()
            high_return_flag = False
            for i in range(len(group) - 1):
                start_date = group.iloc[i]['transaction_date']
                end_date = group.iloc[i + 1]['transaction_date']
                days_diff = (end_date - start_date).days
                if days_diff <= SHORT_TIME_PERIOD_DAYS:
                    start_balance = group.iloc[i]['cumulative_balance']
                    end_balance = group.iloc[i + 1]['cumulative_balance']
                    if start_balance > 0 and (end_balance - start_balance) / start_balance > HIGH_RETURN_THRESHOLD:
                        high_return_flag = True
                        break

            # Flag suspicious activity based on criteria
            if withdrawal_ratio > UNUSUAL_WITHDRAWAL_RATIO or high_return_flag:
                suspicious_activities.append({
                    'investor_id': investor_id,
                    'total_deposits': total_deposits,
                    'total_withdrawals': total_withdrawals,
                    'withdrawal_ratio': withdrawal_ratio,
                    'high_return_flag': high_return_flag
                })

        # Convert suspicious activities to a DataFrame
        return pd.DataFrame(suspicious_activities)

    except Exception as e:
        # Handle errors gracefully
        print(f"Error analyzing trading patterns: {e}")
        return pd.DataFrame()

# Example usage
if __name__ == "__main__":
    # Sample trading data
    sample_data = pd.DataFrame({
        'investor_id': [1, 1, 1, 2, 2, 3, 3, 3],
        'transaction_date': [
            '2023-01-01', '2023-01-15', '2023-02-01',
            '2023-01-01', '2023-01-20',
            '2023-01-01', '2023-01-10', '2023-01-25'
        ],
        'transaction_type': ['deposit', 'withdrawal', 'deposit', 'deposit', 'withdrawal', 'deposit', 'deposit', 'withdrawal'],
        'amount': [1000, 800, 1200, 500, 400, 2000, 1500, 3000]
    })

    # Analyze trading patterns
    flagged_activities = analyze_trading_patterns(sample_data)

    # Display flagged suspicious activities
    print("Suspicious Activities:")
    print(flagged_activities)
```
