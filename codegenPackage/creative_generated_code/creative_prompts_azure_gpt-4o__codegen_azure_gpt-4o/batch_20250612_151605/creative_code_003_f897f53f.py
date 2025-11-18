"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://bafybeidiclstnq4utj2pwl644m64fbyrgzsmyytshhypgwavuo7vertppe.ipfs.dweb.link
Prompt: Create a script to calculate the rewards earned from staking APT on Amnis Finance, factoring in the 1.45x APR multiplier for matured positions.
Generated: DETERMINISTIC_f897f53fb06c2dcf
Batch ID: 20250612_151605
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import sys

def calculate_staking_rewards(principal, apr, days_staked):
    """
    Calculate rewards earned from staking APT on Amnis Finance.

    Parameters:
    principal (float): The initial amount of APT staked.
    apr (float): Base Annual Percentage Rate (APR) as a decimal (e.g., 0.10 for 10%).
    days_staked (int): Number of days the position has been staked.

    Returns:
    float: Total rewards earned from staking.
    """
    try:
        # Validate inputs
        if principal <= 0 or apr <= 0 or days_staked < 0:
            raise ValueError("Principal, APR, and days_staked must be positive values.")

        # Calculate yearly rewards
        yearly_rewards = principal * apr

        # Calculate rewards for the specified staking duration
        base_rewards = (yearly_rewards / 365) * days_staked

        # Apply the 1.45x APR multiplier for matured positions (30 days or more)
        if days_staked >= 30:
            base_rewards *= 1.45

        return base_rewards

    except ValueError as ve:
        print(f"ValueError: {ve}")
        sys.exit(1)

    except Exception as e:
        print(f"An unexpected error occurred: {e}")
        sys.exit(1)


if __name__ == "__main__":
    # Example usage
    try:
        print("Welcome to the Amnis Finance Staking Reward Calculator!")
        
        # Prompt user for inputs
        principal = float(input("Enter the amount of APT staked (principal): "))
        apr = float(input("Enter the base APR (e.g., 0.10 for 10%): "))
        days_staked = int(input("Enter the number of days the position has been staked: "))

        # Calculate rewards
        rewards = calculate_staking_rewards(principal, apr, days_staked)
        print(f"\nTotal rewards earned: {rewards:.6f} APT")

    except ValueError:
        print("Error: Please ensure all inputs are valid numeric values.")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")
```
