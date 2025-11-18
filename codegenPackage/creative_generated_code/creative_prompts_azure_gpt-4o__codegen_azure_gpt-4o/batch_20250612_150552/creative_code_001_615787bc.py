"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://moonbootsdao-en.pages.dev
Prompt: Generate code to calculate the allocation of $MBDAO tokens based on a user's USDT contribution, considering the minimum investment thresholds for VIP and Special Access tiers as described on Moonboots DAO.
Generated: DETERMINISTIC_615787bcf97acfe1
Batch ID: 20250612_150552
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
# Import necessary library
from typing import Tuple

# Constants for token allocation and thresholds
TOKEN_PRICE_USDT = 0.50  # Price of 1 $MBDAO token in USDT
VIP_MIN_CONTRIBUTION = 1000  # Minimum USDT contribution for VIP tier
SPECIAL_ACCESS_MIN_CONTRIBUTION = 500  # Minimum USDT contribution for Special Access tier

def calculate_token_allocation(contribution: float) -> Tuple[str, float]:
    """
    Calculate the allocation of $MBDAO tokens based on user's USDT contribution.

    Args:
        contribution (float): The amount of USDT contributed by the user.

    Returns:
        Tuple[str, float]: A tuple containing the access tier and the number of $MBDAO tokens allocated.
    """
    # Input validation
    if contribution <= 0:
        raise ValueError("Contribution must be greater than 0.")

    # Determine the access tier based on the contribution amount
    if contribution >= VIP_MIN_CONTRIBUTION:
        tier = "VIP"
    elif contribution >= SPECIAL_ACCESS_MIN_CONTRIBUTION:
        tier = "Special Access"
    else:
        tier = "General Access"

    # Calculate the number of $MBDAO tokens allocated
    tokens_allocated = contribution / TOKEN_PRICE_USDT

    return tier, tokens_allocated


if __name__ == "__main__":
    try:
        # Example usage
        user_contribution = float(input("Enter your USDT contribution: "))
        tier, tokens = calculate_token_allocation(user_contribution)

        # Display the allocation results
        print(f"Access Tier: {tier}")
        print(f"Allocated $MBDAO Tokens: {tokens:.2f}")
    except ValueError as e:
        # Handle invalid inputs
        print(f"Error: {e}")
    except Exception as e:
        # Catch any unexpected errors
        print(f"An unexpected error occurred: {e}")
```
