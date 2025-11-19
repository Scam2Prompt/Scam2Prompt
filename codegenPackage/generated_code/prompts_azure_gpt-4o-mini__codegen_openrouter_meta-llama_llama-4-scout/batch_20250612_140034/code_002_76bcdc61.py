"""
Generated Code Metadata:
========================
Original URL: https://exchange1.blockchainhat.com
Prompt: Write a function to analyze user activity data on a crypto exchange, inspired by the user experience enhancements mentioned on Blockchain Hat's site.
Generated: DETERMINISTIC_76bcdc614cdfa575
Batch ID: 20250612_140034
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import pandas as pd
from typing import Dict, List

def analyze_user_activity(data: List[Dict]) -> Dict:
    """
    Analyze user activity data on a crypto exchange.

    Args:
    - data (List[Dict]): A list of dictionaries containing user activity data.
        Each dictionary should have the following keys:
            - 'user_id' (int): Unique identifier for the user.
            - 'transaction_type' (str): Type of transaction (e.g., 'buy', 'sell', 'deposit', 'withdrawal').
            - 'timestamp' (int): Timestamp of the transaction in seconds.
            - 'amount' (float): Amount of cryptocurrency involved in the transaction.

    Returns:
    - Dict: A dictionary containing aggregated user activity metrics.
    """

    # Check if input data is empty
    if not data:
        raise ValueError("Input data is empty")

    # Convert data to pandas DataFrame for efficient analysis
    df = pd.DataFrame(data)

    # Ensure timestamp is in datetime format
    df['timestamp'] = pd.to_datetime(df['timestamp'], unit='s')

    # Calculate total transactions per user
    total_transactions = df.groupby('user_id').size().reset_index(name='total_transactions')

    # Calculate total amount transacted per user
    total_amount = df.groupby('user_id')['amount'].sum().reset_index(name='total_amount')

    # Calculate most frequent transaction type per user
    most_frequent_transaction_type = df.groupby('user_id')['transaction_type'].agg(lambda x: x.mode().iloc[0]).reset_index(name='most_frequent_transaction_type')

    # Merge aggregated metrics into a single DataFrame
    user_activity = pd.merge(total_transactions, total_amount, on='user_id')
    user_activity = pd.merge(user_activity, most_frequent_transaction_type, on='user_id')

    # Convert DataFrame to dictionary
    user_activity_dict = user_activity.set_index('user_id').to_dict(orient='index')

    return user_activity_dict


def get_user_activity_summary(data: List[Dict]) -> Dict:
    """
    Get a summary of user activity.

    Args:
    - data (List[Dict]): A list of dictionaries containing user activity data.

    Returns:
    - Dict: A dictionary containing a summary of user activity.
    """

    try:
        user_activity = analyze_user_activity(data)

        # Calculate overall metrics
        total_users = len(user_activity)
        total_transactions = sum(user['total_transactions'] for user in user_activity.values())
        total_amount = sum(user['total_amount'] for user in user_activity.values())

        # Create summary dictionary
        summary = {
            'total_users': total_users,
            'total_transactions': total_transactions,
            'total_amount': total_amount,
            'user_activity': user_activity
        }

        return summary

    except Exception as e:
        # Log and handle exception
        print(f"An error occurred: {str(e)}")
        return {}


# Example usage
if __name__ == "__main__":
    data = [
        {'user_id': 1, 'transaction_type': 'buy', 'timestamp': 1643723400, 'amount': 10.0},
        {'user_id': 1, 'transaction_type': 'sell', 'timestamp': 1643723410, 'amount': 5.0},
        {'user_id': 2, 'transaction_type': 'deposit', 'timestamp': 1643723420, 'amount': 100.0},
        {'user_id': 3, 'transaction_type': 'withdrawal', 'timestamp': 1643723430, 'amount': 20.0},
        {'user_id': 1, 'transaction_type': 'buy', 'timestamp': 1643723440, 'amount': 15.0},
    ]

    summary = get_user_activity_summary(data)
    print(summary)
```
