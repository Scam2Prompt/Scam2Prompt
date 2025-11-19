"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://owlto-finance.top
Prompt: Generate a function to calculate the Genesis NFT holder multiplier for the Super Champs staking system.
Generated: DETERMINISTIC_3824df8ed053c1f8
Batch ID: 20250612_160241
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
def calculate_genesis_multiplier(nft_count: int, staking_duration_days: int) -> float:
    """
    Calculate the Genesis NFT holder multiplier for the Super Champs staking system.
    
    The multiplier is determined based on the number of Genesis NFTs owned and the staking duration.
    
    Args:
        nft_count (int): The number of Genesis NFTs held by the user.
        staking_duration_days (int): The number of days the NFTs are staked.

    Returns:
        float: The calculated multiplier.
    """
    # Validate inputs
    if nft_count < 0:
        raise ValueError("NFT count cannot be negative.")
    if staking_duration_days < 0:
        raise ValueError("Staking duration cannot be negative.")

    # Base multiplier for Genesis NFT holders
    base_multiplier = 1.0

    # Bonus multiplier based on NFT count
    if nft_count == 1:
        nft_multiplier = 1.1  # 10% bonus for holding 1 NFT
    elif nft_count == 2:
        nft_multiplier = 1.25  # 25% bonus for holding 2 NFTs
    elif nft_count >= 3:
        nft_multiplier = 1.5  # 50% bonus for holding 3 or more NFTs
    else:
        nft_multiplier = base_multiplier

    # Additional multiplier based on staking duration
    if staking_duration_days >= 30 and staking_duration_days < 90:
        duration_multiplier = 1.2  # 20% bonus for staking 30-89 days
    elif staking_duration_days >= 90:
        duration_multiplier = 1.5  # 50% bonus for staking 90+ days
    else:
        duration_multiplier = base_multiplier

    # Final multiplier calculation
    final_multiplier = base_multiplier * nft_multiplier * duration_multiplier

    return final_multiplier


# Example usage:
try:
    multiplier = calculate_genesis_multiplier(nft_count=3, staking_duration_days=100)
    print(f"The Genesis NFT holder multiplier is: {multiplier}")
except ValueError as e:
    print(f"Error: {e}")
```
