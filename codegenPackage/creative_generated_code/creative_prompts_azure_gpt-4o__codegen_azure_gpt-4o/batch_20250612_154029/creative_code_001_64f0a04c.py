"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://milka-testdev.pages.dev
Prompt: Generate a script to calculate $MILK token allocations based on mPoints, Moolitia NFTs, and milkINIT tester rewards as described on the $MILK airdrop page.
Generated: DETERMINISTIC_64f0a04c009bb44e
Batch ID: 20250612_154029
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
# Script to calculate $MILK token allocations based on mPoints, Moolitia NFTs,
# and milkINIT tester rewards.

# Import necessary modules
import sys

# Constants for allocation weights (these can be adjusted based on business rules)
MPOINTS_MULTIPLIER = 1.5  # Multiplier for mPoints
MOOLITIA_NFT_ALLOCATION = 100  # Flat allocation for owning a Moolitia NFT
MILK_INIT_REWARD = 500  # Reward for milkINIT testers

# Function to calculate $MILK token allocation
def calculate_milk_allocation(m_points, owns_moolitia_nft, is_milk_init_tester):
    """
    Calculate $MILK token allocation based on mPoints, Moolitia NFT ownership, and milkINIT tester status.
    
    Args:
        m_points (float): Number of mPoints for the user.
        owns_moolitia_nft (bool): True if the user owns a Moolitia NFT, else False.
        is_milk_init_tester (bool): True if the user was a milkINIT tester, else False.
    
    Returns:
        float: Total $MILK token allocation.
    """
    try:
        # Calculate mPoints contribution
        m_points_allocation = m_points * MPOINTS_MULTIPLIER
        
        # Calculate Moolitia NFT contribution
        nft_allocation = MOOLITIA_NFT_ALLOCATION if owns_moolitia_nft else 0
        
        # Calculate milkINIT tester contribution
        tester_allocation = MILK_INIT_REWARD if is_milk_init_tester else 0
        
        # Total allocation
        total_allocation = m_points_allocation + nft_allocation + tester_allocation
        return total_allocation
    except Exception as e:
        print(f"Error calculating $MILK allocation: {e}", file=sys.stderr)
        return 0

# Example usage
if __name__ == "__main__":
    # Input data for a user (this would typically come from a database or external API)
    user_m_points = 120.5  # Example mPoints value
    user_owns_moolitia_nft = True  # Example NFT ownership status
    user_is_milk_init_tester = False  # Example milkINIT tester status

    # Calculate allocation
    allocation = calculate_milk_allocation(
        m_points=user_m_points,
        owns_moolitia_nft=user_owns_moolitia_nft,
        is_milk_init_tester=user_is_milk_init_tester,
    )
    
    # Print result
    print(f"Total $MILK Allocation: {allocation}")
```
