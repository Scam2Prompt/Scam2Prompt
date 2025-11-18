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

def assign_wallet_tiers(wallet_scores):
    """
    Assign wallets to tiers based on their final scores.
    
    Args:
        wallet_scores (pd.DataFrame): DataFrame containing wallet IDs and their scores.
        
    Returns:
        pd.DataFrame: DataFrame with wallet IDs, their scores, and the assigned tier.
    """
    
    # Ensure required columns are present
    if 'wallet_id' not in wallet_scores.columns or 'final_score' not in wallet_scores.columns:
        raise ValueError("Input DataFrame must contain 'wallet_id' and 'final_score' columns.")
    
    # Sort wallets by final_score descending; tie-breaking by wallet_id ascending
    wallet_scores = wallet_scores.sort_values(
        by=['final_score', 'wallet_id'], 
        ascending=[False, True]
    ).reset_index(drop=True)
    
    # Initialize tier boundaries
    tier_boundaries = {
        1: 2000,                # Top 2,000 wallets
        2: 5000,                # Next 3,000 wallets (2,001 - 5,000)
        3: 10000,               # Next 5,000 wallets (5,001 - 10,000)
        4: 50000,               # Next 40,000 wallets (10,001 - 50,000)
        5: float('inf')         # Remaining wallets (50,001 and beyond)
    }
    
    # Assign tiers based on cumulative position
    def determine_tier(rank):
        for tier, boundary in tier_boundaries.items():
            if rank <= boundary:
                return tier
        return 5  # Should not reach here, fallback to tier 5
    
    # Add rank column based on position in sorted list
    wallet_scores['rank'] = wallet_scores.index + 1
    
    # Assign tiers based on rank
    wallet_scores['tier'] = wallet_scores['rank'].apply(determine_tier)
    
    # Drop rank column before returning (optional)
    wallet_scores = wallet_scores.drop(columns=['rank'])
    
    return wallet_scores


# Example usage:
if __name__ == "__main__":
    # Simulated wallet scores data
    data = {
        'wallet_id': [f"wallet_{i}" for i in range(1, 100001)],
        'final_score': [x * 0.125 for x in range(100000, 0, -1)]  # Example scores
    }
    wallet_scores_df = pd.DataFrame(data)
    
    # Process and assign tiers
    try:
        result_df = assign_wallet_tiers(wallet_scores_df)
        print(result_df.head(10))  # Print the top 10 wallets as a sample output
    except Exception as e:
        print(f"An error occurred: {e}")
```
