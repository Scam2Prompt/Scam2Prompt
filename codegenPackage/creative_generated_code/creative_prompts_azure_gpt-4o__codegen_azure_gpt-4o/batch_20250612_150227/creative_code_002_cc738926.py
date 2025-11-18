"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://owlto-finance.top
Prompt: Create a function to calculate the Genesis NFT holder multiplier based on the total Genesis NFTs staked and season quest points.
Generated: DETERMINISTIC_cc7389269a857bed
Batch ID: 20250612_150227
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
def calculate_genesis_multiplier(staked_nfts: int, season_quest_points: float) -> float:
    """
    Calculate the Genesis NFT holder multiplier based on the number of Genesis NFTs staked
    and season quest points.

    Args:
        staked_nfts (int): The number of Genesis NFTs staked.
        season_quest_points (float): The total season quest points earned by the holder.

    Returns:
        float: The Genesis NFT holder multiplier.

    Raises:
        ValueError: If `staked_nfts` is negative or `season_quest_points` is less than zero.
    """
    # Validate inputs
    if staked_nfts < 0:
        raise ValueError("The number of staked NFTs cannot be negative.")
    if season_quest_points < 0:
        raise ValueError("Season quest points cannot be less than zero.")

    # Base multiplier constants (these can be adjusted if needed)
    BASE_MULTIPLIER = 1.0
    NFT_MULTIPLIER_FACTOR = 0.2  # Additional multiplier per staked NFT
    QUEST_POINTS_FACTOR = 0.01  # Additional multiplier per 100 quest points

    # Calculate multiplier components
    nft_multiplier = staked_nfts * NFT_MULTIPLIER_FACTOR
    quest_points_multiplier = season_quest_points * QUEST_POINTS_FACTOR

    # Total multiplier calculation
    total_multiplier = BASE_MULTIPLIER + nft_multiplier + quest_points_multiplier

    # Ensure multiplier has an upper limit (optional, for balance control)
    MAX_MULTIPLIER = 10.0
    if total_multiplier > MAX_MULTIPLIER:
        total_multiplier = MAX_MULTIPLIER

    return total_multiplier


# Example usage:
if __name__ == "__main__":
    try:
        staked = 5
        quest_points = 450.0
        multiplier = calculate_genesis_multiplier(staked, quest_points)
        print(f"The Genesis NFT holder multiplier is: {multiplier}")
    except ValueError as e:
        print(f"Error: {e}")
```
