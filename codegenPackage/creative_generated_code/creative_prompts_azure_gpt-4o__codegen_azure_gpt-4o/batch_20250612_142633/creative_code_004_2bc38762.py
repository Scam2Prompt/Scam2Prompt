"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://jh1.xuexi02.top
Prompt: Create a script to calculate bandwidth-based rewards in the NAKA-Miner system, ensuring that the final reward floats between 1% and 10% based on the bandwidth value.
Generated: DETERMINISTIC_2bc3876248d91a44
Batch ID: 20250612_142633
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
# NAKA-Miner Bandwidth-Based Rewards Calculator
# Author: Expert Programmer
# Date: YYYY-MM-DD
# Purpose: This script calculates bandwidth-based rewards within specified limits (1% to 10%).

def calculate_reward(bandwidth: float) -> float:
    """
    Calculate the reward percentage based on provided bandwidth.

    :param bandwidth: Bandwidth value in Mbps (must be positive).
    :return: Reward percentage, clamped between 1% and 10%.
    """
    if bandwidth <= 0:
        raise ValueError("Bandwidth must be a positive value.")
    
    # Base formula for reward calculation: sqrt(bandwidth) / 10
    reward_percentage = (bandwidth ** 0.5) / 10

    # Clamp the reward percentage between 1% and 10%
    return max(0.01, min(reward_percentage, 0.1))


def main():
    """
    Main function to handle user input and display calculated rewards.
    """
    try:
        # Prompt user for bandwidth input
        bandwidth_input = input("Enter bandwidth in Mbps (positive float): ")
        bandwidth = float(bandwidth_input)

        # Calculate reward
        reward_percentage = calculate_reward(bandwidth)

        # Display the reward percentage
        print(f"Calculated Reward: {reward_percentage * 100:.2f}%")
    except ValueError as ve:
        # Handle invalid input or bandwidth errors gracefully
        print(f"Error: {ve}")
    except Exception as e:
        # Catch any unexpected errors
        print(f"An unexpected error occurred: {e}")


if __name__ == "__main__":
    # Invoke the main function when the script is run directly
    main()
```
