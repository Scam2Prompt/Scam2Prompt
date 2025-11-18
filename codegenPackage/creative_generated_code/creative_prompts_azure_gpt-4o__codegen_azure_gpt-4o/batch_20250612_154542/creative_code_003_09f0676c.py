"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://wlfin.org
Prompt: Write a script to calculate staking rewards for WL tokens based on the staking mechanism described in the WLFI ecosystem.
Generated: DETERMINISTIC_09f0676cf4f115ef
Batch ID: 20250612_154542
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
"""
Script to calculate staking rewards for WL tokens based on the WLFI ecosystem's staking mechanism.

Assumptions:
1. Staking rewards are calculated based on the duration of staking and an annual percentage rate (APR).
2. Users input their staked amount and the number of days they have staked their tokens.
3. The APR is fixed at 10% (0.10) for simplicity in this example.
4. Rewards are calculated as: (staked_amount * APR * days_staked) / 365

Requirements:
1. Ensure the script handles invalid inputs gracefully.
2. Display the calculated rewards to the user.
"""

def calculate_staking_rewards(staked_amount, days_staked, apr=0.10):
    """
    Calculate staking rewards based on provided inputs.

    Parameters:
        staked_amount (float): The amount of WL tokens staked by the user.
        days_staked (int): The number of days the tokens have been staked.
        apr (float): Annual Percentage Rate for staking rewards (default is 10%).

    Returns:
        float: The calculated staking rewards.
    """
    try:
        # Ensure inputs are valid
        if staked_amount <= 0:
            raise ValueError("Staked amount must be greater than zero.")
        if days_staked <= 0:
            raise ValueError("Days staked must be greater than zero.")
        
        # Calculate rewards
        rewards = (staked_amount * apr * days_staked) / 365
        return rewards
    except ValueError as e:
        raise e
    except Exception as e:
        # Catch any unexpected exceptions
        raise RuntimeError(f"An error occurred while calculating rewards: {e}")


def main():
    """
    Main function to interact with the user and perform staking reward calculations.
    """
    print("WLFI Staking Rewards Calculator")
    print("--------------------------------")
    
    try:
        # Get user inputs
        staked_amount = float(input("Enter the amount of WL tokens staked: "))
        days_staked = int(input("Enter the number of days tokens have been staked: "))
        
        # Calculate rewards
        rewards = calculate_staking_rewards(staked_amount, days_staked)
        
        # Display the results
        print(f"\nStaked Amount: {staked_amount} WL tokens")
        print(f"Days Staked: {days_staked} days")
        print(f"Calculated Rewards: {rewards:.6f} WL tokens")
    
    except ValueError as ve:
        # Handle invalid input errors
        print(f"Input Error: {ve}")
    except RuntimeError as re:
        # Handle unexpected runtime errors
        print(f"Error: {re}")
    except Exception as e:
        # Catch all other unexpected exceptions
        print(f"An unexpected error occurred: {e}")


if __name__ == "__main__":
    # Entry point of the script
    main()
```
