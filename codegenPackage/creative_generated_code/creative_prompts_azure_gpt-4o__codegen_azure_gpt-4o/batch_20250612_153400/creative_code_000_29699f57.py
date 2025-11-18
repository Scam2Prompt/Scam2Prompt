"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://egld.pages.dev
Prompt: Write a Python script to calculate EGLD staking rewards using the formula provided on the MultiversX website: `[EGLD reward] = [Current EGLD holdings] * [ (EGLD Staked / Users Staking) * 775 ] * [Delegate Factor] * [Stake Factor]`.
Generated: DETERMINISTIC_29699f575157b181
Batch ID: 20250612_153400
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
# Python script to calculate EGLD staking rewards based on MultiversX formula

def calculate_egld_rewards(egld_holdings, egld_staked, users_staking, delegate_factor, stake_factor):
    """
    Calculate EGLD staking rewards based on given parameters.
    
    Formula: 
    [EGLD reward] = [Current EGLD holdings] * [ (EGLD Staked / Users Staking) * 775 ] * [Delegate Factor] * [Stake Factor]
    
    Parameters:
        egld_holdings (float): Current EGLD holdings of the user.
        egld_staked (float): Total EGLD staked.
        users_staking (int): Number of users staking.
        delegate_factor (float): Delegate factor (specific to staking provider).
        stake_factor (float): Stake factor (specific to protocol conditions).
        
    Returns:
        float: Calculated EGLD reward.
    """
    try:
        # Validate inputs
        if egld_holdings < 0 or egld_staked < 0 or users_staking <= 0 or delegate_factor < 0 or stake_factor < 0:
            raise ValueError("Input parameters must be positive numbers.")

        # Calculate rewards using the formula
        reward = (
            egld_holdings
            * ((egld_staked / users_staking) * 775)
            * delegate_factor
            * stake_factor
        )
        return reward
    except ZeroDivisionError:
        print("Error: Number of users staking cannot be zero.")
        return 0
    except ValueError as ve:
        print(f"Error: {ve}")
        return 0
    except Exception as e:
        print(f"An unexpected error occurred: {e}")
        return 0


def main():
    """
    Main function to collect user input and calculate EGLD rewards.
    """
    try:
        # Collect user inputs
        print("Enter the following values to calculate your EGLD staking rewards:")
        egld_holdings = float(input("Current EGLD holdings (e.g., 1.5): "))
        egld_staked = float(input("Total EGLD staked (e.g., 100000): "))
        users_staking = int(input("Number of users staking (e.g., 10000): "))
        delegate_factor = float(input("Delegate factor (e.g., 1.0): "))
        stake_factor = float(input("Stake factor (e.g., 1.0): "))

        # Calculate rewards
        reward = calculate_egld_rewards(
            egld_holdings,
            egld_staked,
            users_staking,
            delegate_factor,
            stake_factor,
        )

        # Display result
        print(f"\nYour calculated EGLD staking reward: {reward:.6f} EGLD")
    except ValueError:
        print("Invalid input. Please enter numbers only.")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")


if __name__ == "__main__":
    # Entry point for the script
    main()
```
