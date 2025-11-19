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

def filter_wallets_into_tiers(wallets_df, score_column, tier_column, top_n=2000):
    """
    Filter wallets into tiers (1-5) based on their final scores.

    Args:
    - wallets_df (pd.DataFrame): DataFrame containing wallet information.
    - score_column (str): Column name for the final scores.
    - tier_column (str): Column name to store the tier information.
    - top_n (int): Number of top wallets for tier 1. Defaults to 2000.

    Returns:
    - pd.DataFrame: DataFrame with tier information added.
    """

    # Ensure the input DataFrame is not empty
    if wallets_df.empty:
        raise ValueError("Input DataFrame is empty")

    # Check if the score column exists in the DataFrame
    if score_column not in wallets_df.columns:
        raise ValueError(f"The column '{score_column}' does not exist in the DataFrame")

    # Sort the wallets by their scores in descending order
    sorted_wallets_df = wallets_df.sort_values(by=score_column, ascending=False).reset_index(drop=True)

    # Calculate the tier breaks
    total_wallets = len(sorted_wallets_df)
    tier_breaks = [top_n]
    for i in range(1, 5):
        # Assuming even distribution for simplicity, adjust as needed
        tier_breaks.append(tier_breaks[-1] + (total_wallets - top_n) // 5)

    # Assign tiers to wallets
    sorted_wallets_df[tier_column] = pd.cut(sorted_wallets_df.index, 
                                            bins=[-1] + tier_breaks + [total_wallets], 
                                            labels=[1, 2, 3, 4, 5], 
                                            right=False, 
                                            include_lowest=True)

    return sorted_wallets_df


def main():
    # Example usage
    wallets_data = {
        'wallet_id': range(10000),
        'final_score': [100 - i for i in range(10000)]  # Example scores
    }
    wallets_df = pd.DataFrame(wallets_data)

    try:
        result_df = filter_wallets_into_tiers(wallets_df, 'final_score', 'tier')
        print(result_df.head())
    except Exception as e:
        print(f"An error occurred: {e}")


if __name__ == "__main__":
    main()
```
