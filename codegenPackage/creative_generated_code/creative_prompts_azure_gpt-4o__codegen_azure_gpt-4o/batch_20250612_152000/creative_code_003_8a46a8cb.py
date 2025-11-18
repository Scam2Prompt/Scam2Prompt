"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://trustpad-app.pages.dev
Prompt: Write a Python function to simulate allocation types (lottery vs guaranteed) for TrustPad staking levels, using the pool weights provided on the site.
Generated: DETERMINISTIC_8a46a8cbf6c34e58
Batch ID: 20250612_152000
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import random

def simulate_allocation(staking_levels, allocation_type='lottery', num_winners=1):
    """
    Simulates allocation types for TrustPad staking levels.
    
    Args:
        staking_levels (dict): A dictionary where keys are user IDs and values are their respective pool weights.
                               Example: {'user1': 100, 'user2': 200, 'user3': 50}
        allocation_type (str): Allocation method, either 'lottery' or 'guaranteed'. Default is 'lottery'.
        num_winners (int): Number of winners to select if using the lottery allocation method. Default is 1.
        
    Returns:
        dict: A dictionary of selected users and their allocated weights.
    """
    # Validate inputs
    if not isinstance(staking_levels, dict) or not staking_levels:
        raise ValueError("staking_levels must be a non-empty dictionary.")
    
    if allocation_type not in ['lottery', 'guaranteed']:
        raise ValueError("allocation_type must be either 'lottery' or 'guaranteed'.")
    
    if allocation_type == 'lottery' and (not isinstance(num_winners, int) or num_winners < 1):
        raise ValueError("num_winners must be a positive integer for lottery allocation.")

    if allocation_type == 'guaranteed':
        # Guaranteed allocation: all users receive their full pool weight
        return staking_levels

    elif allocation_type == 'lottery':
        # Lottery allocation: Select `num_winners` randomly based on pool weights
        total_weight = sum(staking_levels.values())
        if total_weight == 0:
            raise ValueError("Total pool weight must be greater than zero for lottery allocation.")
        
        # Create a weighted selection pool
        weighted_users = []
        for user, weight in staking_levels.items():
            weighted_users.extend([user] * weight)  # Add user to the pool proportional to their weight
        
        # Randomly select winners without replacement
        selected_users = random.sample(weighted_users, k=min(num_winners, len(weighted_users)))
        
        # Compute the allocation for selected winners
        allocation_result = {user: staking_levels[user] for user in selected_users}
        return allocation_result


# Example Usage:
if __name__ == "__main__":
    # Sample staking levels (User -> Pool Weight)
    staking_levels = {
        'user1': 100,
        'user2': 200,
        'user3': 50,
        'user4': 150,
    }
    
    # Guaranteed allocation example
    print("Guaranteed Allocation:")
    print(simulate_allocation(staking_levels, allocation_type='guaranteed'))
    
    # Lottery allocation example with 2 winners
    print("\nLottery Allocation:")
    print(simulate_allocation(staking_levels, allocation_type='lottery', num_winners=2))
```
