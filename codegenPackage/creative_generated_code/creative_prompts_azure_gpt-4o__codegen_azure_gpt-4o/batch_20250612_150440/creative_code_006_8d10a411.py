"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://rocketspool.github.io
Prompt: Develop a program that calculates the ROI for running a node in Rocket Pool's network, factoring in commissions earned and staking rewards.
Generated: DETERMINISTIC_8d10a4110c31d656
Batch ID: 20250612_150440
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import sys

def calculate_roi(node_staking_amount, staking_reward_rate, commission_rate, operating_cost, duration_in_years):
    """
    Calculates the Return on Investment (ROI) for running a node in Rocket Pool's network.
    
    Parameters:
    - node_staking_amount (float): The amount staked by the node operator (ETH).
    - staking_reward_rate (float): Annual staking reward rate (percentage as a decimal).
    - commission_rate (float): Commission rate earned on delegated ETH (percentage as a decimal).
    - operating_cost (float): Annual operating cost for running the node (ETH).
    - duration_in_years (int): Number of years to calculate ROI for.

    Returns:
    - roi (float): The calculated ROI over the given duration.
    """

    try:
        # Validate inputs
        if node_staking_amount <= 0 or staking_reward_rate < 0 or commission_rate < 0 or operating_cost < 0 or duration_in_years <= 0:
            raise ValueError("All inputs must be positive values. Check your input data.")

        # Calculate total staking rewards
        staking_rewards = node_staking_amount * staking_reward_rate * duration_in_years

        # Assume commission is earned on an equal amount of delegated ETH as staked by the node operator.
        commission_earned = node_staking_amount * commission_rate * duration_in_years

        # Total earnings
        total_earnings = staking_rewards + commission_earned

        # Total costs
        total_operating_cost = operating_cost * duration_in_years

        # ROI formula: (Total Earnings - Total Costs) / Initial Investment
        roi = (total_earnings - total_operating_cost) / node_staking_amount

        return roi

    except ValueError as ve:
        print(f"Input Error: {ve}")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")
        sys.exit(1)

if __name__ == "__main__":
    # Example usage
    try:
        # Inputs for the calculation
        node_staking_amount = float(input("Enter the amount of ETH staked by the node operator: "))
        staking_reward_rate = float(input("Enter the annual staking reward rate (e.g., 0.05 for 5%): "))
        commission_rate = float(input("Enter the commission rate earned on delegated ETH (e.g., 0.15 for 15%): "))
        operating_cost = float(input("Enter the annual operating cost for running the node (ETH): "))
        duration_in_years = int(input("Enter the number of years to calculate ROI for: "))

        # Calculate ROI
        roi = calculate_roi(node_staking_amount, staking_reward_rate, commission_rate, operating_cost, duration_in_years)

        if roi is not None:
            # Output the result
            print(f"Calculated ROI over {duration_in_years} years: {roi:.2f}")
    except ValueError:
        print("Invalid input. Please enter numeric values where required.")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")
```
