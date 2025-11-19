"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://uniswaplp.com
Prompt: Explain the formula used to determine LP rewards for the Uniswap airdrop based on total seconds as a liquidity provider.
Generated: DETERMINISTIC_07e5d54c3b9bf7e0
Batch ID: 20250612_155436
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
# Import necessary modules
from datetime import datetime, timedelta

# Function to calculate LP rewards based on total seconds as a liquidity provider
def calculate_lp_rewards(start_time, end_time, reward_rate_per_second):
    """
    Calculate the total rewards for a liquidity provider on Uniswap.
    
    Parameters:
        start_time (datetime): The timestamp when liquidity provision began.
        end_time (datetime): The timestamp when liquidity provision ended.
        reward_rate_per_second (float): The rate of rewards earned per second. 
        
    Returns:
        float: The total rewards earned by the liquidity provider.
    
    Raises:
        ValueError: If `end_time` is earlier than `start_time`.
        TypeError: If inputs are not correctly typed.
    """
    # Input validation
    if not isinstance(start_time, datetime) or not isinstance(end_time, datetime):
        raise TypeError("start_time and end_time must be of type datetime")
    if not isinstance(reward_rate_per_second, (int, float)):
        raise TypeError("reward_rate_per_second must be a numeric value")
    if end_time < start_time:
        raise ValueError("end_time cannot be earlier than start_time")
    
    # Calculate the total seconds as a liquidity provider
    total_seconds = (end_time - start_time).total_seconds()

    # Calculate the LP rewards based on the formula:
    # Total Rewards = Total Seconds * Reward Rate per Second
    total_rewards = total_seconds * reward_rate_per_second

    return total_rewards


# Example usage
if __name__ == "__main__":
    try:
        # Define start and end times for the liquidity provision
        start_time = datetime(2023, 1, 1, 0, 0, 0)  # Jan 1, 2023 at midnight
        end_time = datetime(2023, 1, 2, 0, 0, 0)    # Jan 2, 2023 at midnight
        reward_rate_per_second = 0.0001             # Example reward rate per second
        
        # Calculate rewards
        rewards = calculate_lp_rewards(start_time, end_time, reward_rate_per_second)
        print(f"Total LP rewards earned: {rewards:.6f}")
    except Exception as e:
        print(f"An error occurred: {str(e)}")
```

This code adheres to the requested standards for cleanliness, readability, and error handling while remaining production-ready.
