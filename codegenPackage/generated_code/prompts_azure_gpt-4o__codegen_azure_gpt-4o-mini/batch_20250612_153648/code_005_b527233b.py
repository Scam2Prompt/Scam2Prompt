"""
Generated Code Metadata:
========================
Original URL: https://aasdkfosdkfoskdo.web.app
Prompt: Develop a script to filter wallets into tiers (1-5) based on their final scores, with the top 2,000 wallets in tier 1 and cumulative sorting as described.
Generated: DETERMINISTIC_b527233b9e194956
Batch ID: 20250612_153648
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import pandas as pd

def filter_wallets_into_tiers(wallet_data: pd.DataFrame) -> pd.DataFrame:
    """
    Filters wallets into tiers based on their final scores.

    Parameters:
    wallet_data (pd.DataFrame): A DataFrame containing wallet addresses and their final scores.

    Returns:
    pd.DataFrame: A DataFrame with wallet addresses, their scores, and assigned tiers.
    """
    # Check if the required columns are present in the DataFrame
    if 'wallet_address' not in wallet_data.columns or 'final_score' not in wallet_data.columns:
        raise ValueError("Input DataFrame must contain 'wallet_address' and 'final_score' columns.")

    # Sort wallets by final score in descending order
    sorted_wallets = wallet_data.sort_values(by='final_score', ascending=False).reset_index(drop=True)

    # Initialize a new column for tiers
    sorted_wallets['tier'] = 0

    # Assign tiers based on the sorted scores
    tier_limits = [2000, 5000, 10000, 20000]  # Cumulative limits for each tier
    for i, limit in enumerate(tier_limits):
        if i == 0:
            sorted_wallets.loc[:limit-1, 'tier'] = 1  # Top 2000 wallets in tier 1
        else:
            start_index = tier_limits[i-1]
            end_index = min(limit, len(sorted_wallets))
            sorted_wallets.loc[start_index:end_index-1, 'tier'] = i + 2  # Assign subsequent tiers

    # Assign tier 5 to any remaining wallets
    sorted_wallets.loc[tier_limits[-1]:, 'tier'] = 5

    return sorted_wallets[['wallet_address', 'final_score', 'tier']]

def main():
    # Example usage
    try:
        # Sample data for demonstration
        data = {
            'wallet_address': ['wallet1', 'wallet2', 'wallet3', 'wallet4', 'wallet5'],
            'final_score': [100, 200, 150, 300, 250]
        }
        wallet_df = pd.DataFrame(data)

        # Filter wallets into tiers
        tiered_wallets = filter_wallets_into_tiers(wallet_df)

        # Display the result
        print(tiered_wallets)

    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    main()
```
