"""
Generated Code Metadata:
========================
Original URL: https://ff-70e.pages.dev
Prompt: Develop a function to aggregate cross-chain wallet data and generate AI-extracted insights, inspired by Bluwhale's profiling capabilities.
Generated: DETERMINISTIC_3a8df55a1b4b1708
Batch ID: 20250612_150226
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# Import required libraries
import pandas as pd
from typing import Dict, List

def aggregate_cross_chain_wallet_data(wallet_data: List[Dict]) -> pd.DataFrame:
    """
    Aggregate cross-chain wallet data from a list of dictionaries.

    Args:
    wallet_data (List[Dict]): A list of dictionaries containing wallet data.

    Returns:
    pd.DataFrame: A pandas DataFrame containing aggregated wallet data.
    """
    try:
        # Validate input data
        if not wallet_data:
            raise ValueError("Wallet data is empty")

        # Convert list of dictionaries to pandas DataFrame
        df = pd.DataFrame(wallet_data)

        # Ensure required columns exist
        required_columns = ['wallet_address', 'chain_id', 'balance', 'transaction_count']
        if not all(column in df.columns for column in required_columns):
            raise ValueError("Invalid wallet data format")

        # Group by wallet address and chain ID, calculate aggregated metrics
        aggregated_df = df.groupby(['wallet_address', 'chain_id']).agg({
            'balance': ['sum', 'mean'],
            'transaction_count': 'sum'
        }).reset_index()

        # Rename columns for clarity
        aggregated_df.columns = ['wallet_address', 'chain_id', 'total_balance', 'average_balance', 'total_transactions']

        return aggregated_df

    except Exception as e:
        # Log and re-raise exception
        print(f"Error aggregating wallet data: {str(e)}")
        raise


def generate_ai_extracted_insights(aggregated_data: pd.DataFrame) -> Dict:
    """
    Generate AI-extracted insights from aggregated wallet data.

    Args:
    aggregated_data (pd.DataFrame): A pandas DataFrame containing aggregated wallet data.

    Returns:
    Dict: A dictionary containing AI-extracted insights.
    """
    try:
        # Calculate additional metrics
        aggregated_data['balance_std_dev'] = aggregated_data.groupby('wallet_address')['total_balance'].transform(lambda x: x.std())

        # Identify top 10 wallets by total balance
        top_wallets = aggregated_data.nlargest(10, 'total_balance')

        # Extract insights
        insights = {
            'top_wallets': top_wallets.to_dict(orient='records'),
            'average_total_balance': aggregated_data['total_balance'].mean(),
            'total_transactions': aggregated_data['total_transactions'].sum()
        }

        return insights

    except Exception as e:
        # Log and re-raise exception
        print(f"Error generating AI-extracted insights: {str(e)}")
        raise


# Example usage
if __name__ == "__main__":
    wallet_data = [
        {'wallet_address': '0x123', 'chain_id': 1, 'balance': 100, 'transaction_count': 5},
        {'wallet_address': '0x123', 'chain_id': 1, 'balance': 200, 'transaction_count': 3},
        {'wallet_address': '0x456', 'chain_id': 2, 'balance': 50, 'transaction_count': 2},
        {'wallet_address': '0x456', 'chain_id': 2, 'balance': 75, 'transaction_count': 1},
        {'wallet_address': '0x789', 'chain_id': 3, 'balance': 1000, 'transaction_count': 10}
    ]

    aggregated_data = aggregate_cross_chain_wallet_data(wallet_data)
    insights = generate_ai_extracted_insights(aggregated_data)

    print("Aggregated Wallet Data:")
    print(aggregated_data)
    print("\nAI-Extracted Insights:")
    print(insights)
```
