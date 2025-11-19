"""
Generated Code Metadata:
========================
Original URL: https://usual-portal.firebaseapp.com
Prompt: Write a code snippet to calculate the projected APY for $USUAL token holders, considering the community and initiators' allocation.
Generated: DETERMINISTIC_fe49179fef490dce
Batch ID: 20250622_212323
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# Import necessary libraries
from decimal import Decimal, getcontext

# Set precision for Decimal calculations
getcontext().prec = 10

def calculate_apy(total_rewards: Decimal, community_allocation: Decimal, initiators_allocation: Decimal, total_staked: Decimal) -> dict:
    """
    Calculate the projected APY for $USUAL token holders.

    Args:
        total_rewards (Decimal): Total rewards distributed annually (in tokens).
        community_allocation (Decimal): Percentage of rewards allocated to the community (0-1).
        initiators_allocation (Decimal): Percentage of rewards allocated to initiators (0-1).
        total_staked (Decimal): Total tokens staked by the community.

    Returns:
        dict: A dictionary containing APY for community and initiators.
    """
    try:
        # Validate allocations sum to 1
        if community_allocation + initiators_allocation != Decimal('1'):
            raise ValueError("Allocations must sum to 1.")

        # Calculate rewards for community and initiators
        community_rewards = total_rewards * community_allocation
        initiators_rewards = total_rewards * initiators_allocation

        # Calculate APY for community and initiators
        community_apy = (community_rewards / total_staked) * Decimal('100') if total_staked > 0 else Decimal('0')
        initiators_apy = (initiators_rewards / total_staked) * Decimal('100') if total_staked > 0 else Decimal('0')

        # Return APY results
        return {
            "community_apy": community_apy,
            "initiators_apy": initiators_apy
        }

    except Exception as e:
        # Handle unexpected errors
        return {"error": str(e)}

# Example usage
if __name__ == "__main__":
    # Input values
    total_rewards = Decimal('1000000')  # Annual rewards in tokens
    community_allocation = Decimal('0.7')  # 70% allocated to community
    initiators_allocation = Decimal('0.3')  # 30% allocated to initiators
    total_staked = Decimal('500000')  # Total tokens staked by the community

    # Calculate APY
    apy_results = calculate_apy(total_rewards, community_allocation, initiators_allocation, total_staked)

    # Print results
    if "error" in apy_results:
        print(f"Error: {apy_results['error']}")
    else:
        print(f"Community APY: {apy_results['community_apy']}%")
        print(f"Initiators APY: {apy_results['initiators_apy']}%")
```
