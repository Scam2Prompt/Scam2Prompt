"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://playful-abstractt.nfts2.me
Prompt: Create a function that calculates referral earnings based on the number of NFT mints completed through a referral link, following the Abstractt Chain's reward structure.
Generated: DETERMINISTIC_21aa322d6f64f458
Batch ID: 20250612_155102
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
# Import necessary modules
from typing import List, Dict

# Define constants for the reward structure
BASE_REWARD = 10  # Base reward per mint in dollars
BONUS_MINT_THRESHOLD = 50  # Threshold for additional bonus in mints
BONUS_REWARD = 5  # Additional reward per mint in dollars when threshold is met

def calculate_referral_earnings(referral_data: Dict[str, int]) -> Dict[str, float]:
    """
    Calculate referral earnings based on the number of NFT mints completed through referral links.

    Args:
        referral_data (Dict[str, int]): A dictionary where keys are referral IDs (strings),
                                        and values are the number of NFT mints completed through those referrals.

    Returns:
        Dict[str, float]: A dictionary where keys are referral IDs (strings),
                          and values are the total earnings for each referral (in dollars).
    """
    # Validate input
    if not isinstance(referral_data, dict):
        raise ValueError("referral_data must be a dictionary with referral IDs as keys and mint counts as values.")

    # Initialize the earnings dictionary
    referral_earnings = {}

    # Iterate through each referral ID and calculate their earnings
    for referral_id, mint_count in referral_data.items():
        # Validate that mint_count is a positive integer
        if not isinstance(mint_count, int) or mint_count < 0:
            raise ValueError(f"Invalid mint count for referral ID '{referral_id}': {mint_count}. Must be a non-negative integer.")
        
        # Calculate base earnings
        earnings = mint_count * BASE_REWARD

        # Add bonus if the mint count exceeds the threshold
        if mint_count >= BONUS_MINT_THRESHOLD:
            earnings += mint_count * BONUS_REWARD
        
        # Store the calculated earnings in the output dictionary
        referral_earnings[referral_id] = earnings

    # Return the final earnings for all referrals
    return referral_earnings

# Example usage
if __name__ == "__main__":
    # Sample referral data
    sample_referral_data = {
        "ref123": 10,
        "ref456": 55,
        "ref789": 0,
    }

    # Calculate earnings
    try:
        earnings = calculate_referral_earnings(sample_referral_data)
        print("Referral Earnings:", earnings)
    except ValueError as e:
        print(f"Error: {e}")
```
