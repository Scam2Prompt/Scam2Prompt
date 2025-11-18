"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://ethgasback.pages.dev
Prompt: Create a program to display the staking pool size and calculate potential ETH rewards based on the staking duration options (14, 28, or 56 days) from the Paal AI staking platform.
Generated: DETERMINISTIC_d88ea7aee08aabac
Batch ID: 20250612_150552
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import sys

# Constants for reward rates (percentage per duration)
REWARD_RATES = {
    14: 0.02,  # 2% for 14 days
    28: 0.05,  # 5% for 28 days
    56: 0.12   # 12% for 56 days
}

# Function to display the staking pool size
def display_staking_pool_size():
    try:
        # Mocked staking pool size (In a real-world scenario, this data might come from an API or database)
        staking_pool_size = 1000.0  # Example pool size in ETH
        print(f"Current staking pool size: {staking_pool_size:.2f} ETH")
        return staking_pool_size
    except Exception as e:
        print(f"Error retrieving staking pool size: {e}")
        sys.exit(1)

# Function to calculate potential rewards
def calculate_rewards(amount, duration):
    try:
        # Check if the duration is valid
        if duration not in REWARD_RATES:
            raise ValueError(f"Invalid staking duration. Choose from {list(REWARD_RATES.keys())}.")
        
        # Calculate the reward
        reward_rate = REWARD_RATES[duration]
        reward = amount * reward_rate
        return reward
    except Exception as e:
        print(f"Error calculating rewards: {e}")
        sys.exit(1)

# Main function
def main():
    try:
        # Display the staking pool size
        staking_pool_size = display_staking_pool_size()
        
        # Get user input for staking amount
        staking_amount = float(input("Enter the amount of ETH you want to stake: "))
        if staking_amount <= 0:
            raise ValueError("Staking amount must be greater than zero.")
        if staking_amount > staking_pool_size:
            raise ValueError("Staking amount exceeds the available pool size.")
        
        # Get user input for staking duration
        print("Choose a staking duration (14, 28, or 56 days): ")
        staking_duration = int(input())
        
        # Calculate potential rewards
        reward = calculate_rewards(staking_amount, staking_duration)
        print(f"By staking {staking_amount:.2f} ETH for {staking_duration} days, "
              f"you can earn approximately {reward:.2f} ETH as a reward.")
    
    except ValueError as ve:
        print(f"Input error: {ve}")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")
        sys.exit(1)

# Entry point of the program
if __name__ == "__main__":
    main()
```
