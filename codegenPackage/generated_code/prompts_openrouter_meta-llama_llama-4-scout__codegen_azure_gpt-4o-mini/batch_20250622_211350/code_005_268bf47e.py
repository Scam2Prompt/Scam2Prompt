"""
Generated Code Metadata:
========================
Original URL: https://bankless.pages.dev
Prompt: Design a function to calculate the $BASED token allocation for a user based on the number of NFTs they redeem and the redemption phase.
Generated: DETERMINISTIC_268bf47e13d21d4e
Batch ID: 20250622_211350
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
class TokenAllocationError(Exception):
    """Custom exception for token allocation errors."""
    pass

def calculate_based_token_allocation(nft_count: int, redemption_phase: str) -> float:
    """
    Calculate the $BASED token allocation for a user based on the number of NFTs they redeem
    and the redemption phase.

    Parameters:
    nft_count (int): The number of NFTs redeemed by the user.
    redemption_phase (str): The phase of redemption ('early', 'mid', 'late').

    Returns:
    float: The calculated $BASED token allocation.

    Raises:
    ValueError: If nft_count is negative or redemption_phase is invalid.
    """
    
    # Validate input parameters
    if nft_count < 0:
        raise ValueError("NFT count cannot be negative.")
    
    valid_phases = ['early', 'mid', 'late']
    if redemption_phase not in valid_phases:
        raise ValueError(f"Invalid redemption phase. Must be one of: {valid_phases}")

    # Define token allocation multipliers based on redemption phase
    phase_multipliers = {
        'early': 10.0,  # Early phase has the highest multiplier
        'mid': 5.0,     # Mid phase has a moderate multiplier
        'late': 2.0     # Late phase has the lowest multiplier
    }

    # Calculate the token allocation
    allocation = nft_count * phase_multipliers[redemption_phase]

    return allocation

# Example usage
if __name__ == "__main__":
    try:
        user_nft_count = 5
        user_redemption_phase = 'early'
        allocation = calculate_based_token_allocation(user_nft_count, user_redemption_phase)
        print(f"User's $BASED token allocation: {allocation}")
    except ValueError as e:
        print(f"Error calculating token allocation: {e}")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")
```
