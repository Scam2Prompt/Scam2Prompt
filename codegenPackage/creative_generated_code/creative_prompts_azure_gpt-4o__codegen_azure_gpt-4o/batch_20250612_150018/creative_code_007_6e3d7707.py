"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://mitofi-launchpad.pages.dev
Prompt: Generate a script to calculate the overflow subscription allocation for BLACK tokens based on the Mito Launchpad's subscription style and staked INJ contributions.
Generated: DETERMINISTIC_6e3d770789a16afa
Batch ID: 20250612_150018
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import math

# Constants for the allocation calculation
TOTAL_TOKENS = 1000000  # Total BLACK tokens available for allocation
MAX_SUBSCRIPTION_POOL = 500000  # Maximum subscription contribution allowed
MIN_STAKE_REQUIREMENT = 100  # Minimum INJ staked required for eligibility

# Error classes for specific exceptions
class SubscriptionError(Exception):
    pass

class StakeError(Exception):
    pass

def calculate_black_token_allocation(staked_inj, subscription_contribution):
    """
    Calculate BLACK token allocation based on staked INJ and subscription contribution.

    Parameters:
        staked_inj (float): The amount of INJ staked by the user.
        subscription_contribution (float): The user's subscription contribution.

    Returns:
        float: Allocated BLACK tokens for the user.

    Raises:
        StakeError: If the user does not meet the minimum staking requirement.
        SubscriptionError: If the subscription contribution exceeds the maximum pool.
    """
    # Validate minimum staking requirement
    if staked_inj < MIN_STAKE_REQUIREMENT:
        raise StakeError(f"Minimum staking requirement of {MIN_STAKE_REQUIREMENT} INJ not met.")
    
    # Validate subscription contribution
    if subscription_contribution > MAX_SUBSCRIPTION_POOL:
        raise SubscriptionError(f"Subscription contribution exceeds the maximum pool limit of {MAX_SUBSCRIPTION_POOL}.")
    
    # Calculate the user's subscription weight based on staked INJ
    user_weight = math.sqrt(staked_inj)
    
    # Calculate total subscription weight for all contributions
    # In production, retrieve this value from a data source containing all participants' contributions
    # For simplicity, we'll assume a predefined total weight (e.g., based on other participants)
    total_weight = 1000  # Example value, this should be dynamically calculated
    
    # Calculate proportional allocation of BLACK tokens
    allocation_ratio = user_weight / total_weight
    user_allocation = allocation_ratio * TOTAL_TOKENS
    
    return user_allocation

if __name__ == "__main__":
    # Example user input
    try:
        staked_inj = float(input("Enter the amount of INJ staked: "))
        subscription_contribution = float(input("Enter your subscription contribution: "))
        
        # Calculate token allocation
        allocation = calculate_black_token_allocation(staked_inj, subscription_contribution)
        print(f"Your allocated BLACK tokens: {allocation:.2f}")
    except ValueError:
        print("Invalid input. Please enter numeric values for staked INJ and subscription contribution.")
    except StakeError as e:
        print(f"Stake Error: {e}")
    except SubscriptionError as e:
        print(f"Subscription Error: {e}")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")
```
