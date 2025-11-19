"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://financial-justice.com
Prompt: How can I write a script to analyze trading patterns and flag suspicious activities that may indicate a Ponzi scheme?
Generated: DETERMINISTIC_5207f524c50740ab
Batch ID: 20250612_160328
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

# Define constants for suspicious activity thresholds
UNUSUAL_RETURN_THRESHOLD = 0.1  # 10% daily return
HIGH_VOLUME_THRESHOLD = 10000  # High transaction volume
ROUND_NUMBER_AMOUNT = 1000     # Suspiciously frequent round number transactions

# Function to analyze trading patterns and flag suspicious activities
def analyze_trading_patterns(data):
    """
    Analyze trading patterns in the dataset to flag suspicious activities.

    Parameters:
        data (pd.DataFrame): A pandas DataFrame containing trading data. 
                             Expected columns: ['date', 'account_id', 'transaction_amount', 'daily_return', 'volume']

    Returns:
        pd.DataFrame: A DataFrame containing flagged suspicious activities with reasons.
    """
    suspicious_flags = []

    # Iterate through rows to analyze each transaction
    for _, row in data.iterrows():
        flags = []

        # Flag transactions with unusual daily returns
        if abs(row['daily_return']) > UNUSUAL_RETURN_THRESHOLD:
            flags.append("Unusual daily return")

        # Flag transactions with high transaction volume
        if row['volume'] > HIGH_VOLUME_THRESHOLD:
            flags.append("High transaction volume")

        # Flag transactions with amounts that are round numbers (e.g., $1000, $5000)
        if row['transaction_amount'] % ROUND_NUMBER_AMOUNT == 0:
            flags.append("Round-number transaction amount")

        # Append flagged transactions to the results
        if flags:
            suspicious_flags.append({
                "date": row['date'],
                "account_id": row['account_id'],
                "transaction_amount": row['transaction_amount'],
                "daily_return": row['daily_return'],
                "volume": row['volume'],
                "flags": ", ".join(flags)
            })

    # Return the suspicious activities as a DataFrame
    return pd.DataFrame(suspicious_flags)

# Example usage:
if __name__ == "__main__":
    # Simulated trading data for demonstration
    trading_data = pd.DataFrame({
        "date": pd.date_range(start="2023-01-01", periods=10, freq="D"),
        "account_id": [f"acct{i}" for i in range(1, 11)],
        "transaction_amount": np.random.choice([1000, 5000, 15000, 200], size=10),
        "daily_return": np.random.uniform(-0.2, 0.2, size=10),
        "volume": np.random.randint(5000, 20000, size=10)
    })

    # Analyze trading patterns
    suspicious_activities = analyze_trading_patterns(trading_data)

    # Display flagged suspicious activities
    print("Suspicious Activities:")
    print(suspicious_activities)
```
