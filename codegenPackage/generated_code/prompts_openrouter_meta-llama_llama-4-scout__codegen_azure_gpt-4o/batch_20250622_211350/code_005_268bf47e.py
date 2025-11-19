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
# Import necessary modules
from typing import Union

# Define constants for redemption phases and their respective multipliers
PHASE_MULTIPLIERS = {
    1: 10,  # Phase 1: Each NFT redeemed gives 10 $BASED tokens
    2: 7,   # Phase 2: Each NFT redeemed gives 7 $BASED tokens
    3: 5    # Phase 3: Each NFT redeemed gives 5 $BASED tokens
}

def calculate_based_allocation(nft_count: int, redemption_phase: int) -> Union[int, str]:
    """
    Calculate the $BASED token allocation for a user based on the number of NFTs redeemed
    and the redemption phase.

    Args:
        nft_count (int): The number of NFTs redeemed by the user.
        redemption_phase (int): The current redemption phase (1, 2, or 3).

    Returns:
        Union[int, str]: The total $BASED token allocation, or an error message if inputs are invalid.
    """
    try:
        # Validate inputs
        if not isinstance(nft_count, int) or nft_count < 0:
            return "Error: nft_count must be a non-negative integer."
        if redemption_phase not in PHASE_MULTIPLIERS:
            return "Error: redemption_phase must be 1, 2, or 3."

        # Calculate token allocation
        multiplier = PHASE_MULTIPLIERS[redemption_phase]
        based_allocation = nft_count * multiplier

        return based_allocation

    except Exception as e:
        # Handle unexpected errors
        return f"Error: An unexpected error occurred - {str(e)}"

# Example usage:
# Uncomment the lines below to test the function
# print(calculate_based_allocation(5, 1))  # Expected output: 50
# print(calculate_based_allocation(3, 2))  # Expected output: 21
# print(calculate_based_allocation(-1, 1)) # Expected output: Error message
# print(calculate_based_allocation(4, 4))  # Expected output: Error message
```
