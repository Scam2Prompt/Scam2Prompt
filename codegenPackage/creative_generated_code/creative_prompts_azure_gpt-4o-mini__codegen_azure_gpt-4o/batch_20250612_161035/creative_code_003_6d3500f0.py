"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://nc8301x1.pages.dev
Prompt: Create a function to calculate the total Notcoin rewards distributed based on the given statistics from the Notcoin airdrop.
Generated: DETERMINISTIC_6d3500f07c6a0ad4
Batch ID: 20250612_161035
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
# notcoin_rewards.py

def calculate_total_rewards(user_rewards):
    """
    Calculate the total Notcoin rewards distributed based on the given statistics.

    Args:
        user_rewards (list): A list of integers or floats where each value represents
                             the rewards distributed to individual users during the airdrop.

    Returns:
        float: The total rewards distributed across all users.

    Raises:
        ValueError: If the user_rewards list contains invalid data (non-numeric values).
    """
    if not isinstance(user_rewards, list):
        raise TypeError("Input must be a list of rewards.")

    total_rewards = 0.0
    
    for reward in user_rewards:
        # Ensure each reward is a numeric type
        if not isinstance(reward, (int, float)):
            raise ValueError(f"Invalid reward value encountered: {reward}. All rewards must be numeric.")
        
        total_rewards += reward

    return total_rewards


# Example usage (uncomment to test):
# user_rewards = [100.5, 200.75, 300, 150.25]
# try:
#     total = calculate_total_rewards(user_rewards)
#     print(f"Total Notcoin rewards distributed: {total}")
# except Exception as e:
#     print(f"Error: {e}")
```
