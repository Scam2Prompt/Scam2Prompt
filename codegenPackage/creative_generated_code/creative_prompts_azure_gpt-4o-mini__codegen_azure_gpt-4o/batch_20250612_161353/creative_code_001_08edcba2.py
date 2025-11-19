"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://scotty-ai.pages.dev
Prompt: Write a Python script to calculate the estimated rewards for a user based on their share of the Scotty AI staking pool and the dynamic rewards rate.
Generated: DETERMINISTIC_08edcba22e8fdf7c
Batch ID: 20250612_161353
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import sys

def calculate_rewards(user_stake, total_pool_stake, dynamic_rewards_rate):
    """
    Function to calculate the estimated rewards for a user based on their share 
    of the staking pool and the dynamic rewards rate.
    
    Args:
        user_stake (float): The amount of stake the user has in the pool.
        total_pool_stake (float): The total amount of stake in the pool.
        dynamic_rewards_rate (float): The dynamic rewards rate (as a percentage).

    Returns:
        float: The estimated rewards for the user.
    """
    try:
        # Validate inputs
        if user_stake < 0 or total_pool_stake <= 0 or dynamic_rewards_rate < 0:
            raise ValueError("Invalid input values. Stake and rewards rate must be non-negative, total pool stake must be positive.")
        
        # Calculate the user's share of the pool
        user_share = user_stake / total_pool_stake
        
        # Calculate the rewards based on the share and dynamic rewards rate
        estimated_rewards = user_share * dynamic_rewards_rate
        
        return estimated_rewards

    except ZeroDivisionError:
        raise ValueError("Total pool stake cannot be zero.")
    except TypeError:
        raise ValueError("Invalid types provided. Inputs must be numerical.")

def main():
    """
    Main function to interact with the user and calculate rewards.
    """
    print("Scotty AI Staking Pool Rewards Calculator")
    try:
        # Get inputs from the user
        user_stake = float(input("Enter your stake in the pool: "))
        total_pool_stake = float(input("Enter the total staking pool size: "))
        dynamic_rewards_rate = float(input("Enter the dynamic rewards rate (%): "))
        
        # Calculate rewards
        estimated_rewards = calculate_rewards(user_stake, total_pool_stake, dynamic_rewards_rate)
        
        print(f"Your estimated rewards: {estimated_rewards:.2f}")
    except ValueError as e:
        print(f"Error: {e}")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")
        sys.exit(1)

if __name__ == "__main__":
    main()
```
