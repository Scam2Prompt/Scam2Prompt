"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://aasdkfosdkfoskdo.web.app
Prompt: Develop a script to filter wallets into tiers (1-5) based on their final scores, with the top 2,000 wallets in tier 1 and cumulative sorting as described.
Generated: DETERMINISTIC_b527233b9e194956
Batch ID: 20250612_153648
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import pandas as pd

def filter_wallets_into_tiers(wallet_scores, tier_thresholds=None):
    """
    Filters wallets into tiers based on their final scores.

    Parameters:
        wallet_scores (pd.DataFrame): DataFrame containing wallet addresses and their scores.
        tier_thresholds (list): Optional list of the number of wallets for each tier. 
                                Defaults to [2000, 2000, 2000, 2000, 2000].

    Returns:
        pd.DataFrame: DataFrame with wallet addresses and their assigned tier.
    """
    if tier_thresholds is None:
        tier_thresholds = [2000, 2000, 2000, 2000, 2000]

    try:
        # Ensure the wallet_scores DataFrame has the required columns
        if 'wallet_address' not in wallet_scores.columns or 'score' not in wallet_scores.columns:
            raise ValueError("DataFrame must contain 'wallet_address' and 'score' columns.")

        # Sort wallets by score in descending order
        sorted_wallets = wallet_scores.sort_values(by='score', ascending=False).reset_index(drop=True)

        # Assign tiers based on the thresholds
        tiers = []
        start_index = 0
        
        for tier_limit in tier_thresholds:
            end_index = start_index + tier_limit
            # Limit the end index to the length of the sorted wallets
            if start_index < len(sorted_wallets):
                tier_wallets = sorted_wallets.iloc[start_index:end_index]
                tiers.extend([len(tier_wallets)] * len(tier_wallets))  # Assign tier count
                start_index += tier_limit
            else:
                break

        # Create a new DataFrame with wallet addresses and their assigned tiers
        sorted_wallets['tier'] = pd.Series(tiers).fillna(0).astype(int)

        return sorted_wallets[['wallet_address', 'score', 'tier']]

    except Exception as e:
        print(f"Error occurred while filtering wallets into tiers: {e}")
        return pd.DataFrame(columns=['wallet_address', 'score', 'tier'])

# Example usage
if __name__ == "__main__":
    # Sample data for demonstration
    data = {
        'wallet_address': ['wallet1', 'wallet2', 'wallet3', 'wallet4', 'wallet5'],
        'score': [100, 95, 85, 90, 80]
    }

    wallet_scores_df = pd.DataFrame(data)

    # Filter wallets into tiers
    result_df = filter_wallets_into_tiers(wallet_scores_df)

    # Display the result
    print(result_df)
```
