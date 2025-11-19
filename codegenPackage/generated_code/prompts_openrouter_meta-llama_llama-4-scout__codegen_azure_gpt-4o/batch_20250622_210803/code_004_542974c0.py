"""
Generated Code Metadata:
========================
Original URL: https://claimdoge20live.pages.dev
Prompt: "Design a staking rewards calculator for Dogecoin20 that takes into account the user's staked balance, percentage of the pool, and current annual returns percentage."
Generated: DETERMINISTIC_542974c041eccf1c
Batch ID: 20250622_210803
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# staking_rewards_calculator.py

def calculate_staking_rewards(staked_balance, pool_percentage, annual_return_percentage):
    """
    Calculate staking rewards for Dogecoin20.

    Parameters:
        staked_balance (float): The amount of Dogecoin20 staked by the user.
        pool_percentage (float): The user's percentage of the staking pool (0-100).
        annual_return_percentage (float): The annual return percentage offered by the staking program (0-100).

    Returns:
        float: The annual staking rewards for the user.
    """
    try:
        # Validate inputs
        if staked_balance < 0:
            raise ValueError("Staked balance cannot be negative.")
        if not (0 <= pool_percentage <= 100):
            raise ValueError("Pool percentage must be between 0 and 100.")
        if not (0 <= annual_return_percentage <= 100):
            raise ValueError("Annual return percentage must be between 0 and 100.")

        # Convert percentages to decimal values
        pool_percentage_decimal = pool_percentage / 100
        annual_return_decimal = annual_return_percentage / 100

        # Calculate rewards
        rewards = staked_balance * pool_percentage_decimal * annual_return_decimal
        return rewards

    except ValueError as e:
        # Handle invalid input errors
        print(f"Error: {e}")
        return None
    except Exception as e:
        # Handle unexpected errors
        print(f"An unexpected error occurred: {e}")
        return None


# Example usage
if __name__ == "__main__":
    try:
        # User inputs
        staked_balance = float(input("Enter your staked balance (Dogecoin20): "))
        pool_percentage = float(input("Enter your percentage of the staking pool (0-100): "))
        annual_return_percentage = float(input("Enter the annual return percentage (0-100): "))

        # Calculate rewards
        rewards = calculate_staking_rewards(staked_balance, pool_percentage, annual_return_percentage)

        if rewards is not None:
            print(f"Your annual staking rewards: {rewards:.2f} Dogecoin20")
        else:
            print("Failed to calculate staking rewards due to invalid input.")
    except ValueError:
        print("Invalid input. Please enter numeric values.")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")
```
