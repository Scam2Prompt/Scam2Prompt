"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://typeai-rewards.pages.dev
Prompt: Develop code to display the percentage share of ETH rewards for a user based on their staked $TYPE tokens in the TypeAI platform's 56-day pool.
Generated: DETERMINISTIC_8ed2bb408004d406
Batch ID: 20250612_152240
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
# Import necessary modules
import sys

def calculate_eth_reward_percentage(user_stake: float, total_stake: float) -> float:
    """
    Calculate the percentage share of ETH rewards for a user based on their staked $TYPE tokens.

    Args:
        user_stake (float): The amount of $TYPE tokens staked by the user.
        total_stake (float): The total amount of $TYPE tokens staked in the pool.

    Returns:
        float: The percentage share of ETH rewards for the user.
    """
    try:
        # Validate inputs
        if user_stake < 0 or total_stake <= 0:
            raise ValueError("Invalid stakes: user_stake must be non-negative and total_stake must be positive.")

        # Calculate percentage
        percentage_share = (user_stake / total_stake) * 100
        return percentage_share

    except Exception as e:
        # Handle any errors gracefully
        print(f"Error: {e}", file=sys.stderr)
        return 0.0


def main():
    """
    Main function to display the user's ETH reward percentage share.
    """
    try:
        # Example inputs - replace with dynamic inputs as needed
        user_stake = float(input("Enter the amount of $TYPE tokens staked by the user: "))
        total_stake = float(input("Enter the total amount of $TYPE tokens staked in the pool: "))

        # Calculate percentage share
        percentage_share = calculate_eth_reward_percentage(user_stake, total_stake)

        # Display the result
        print(f"The user's percentage share of ETH rewards: {percentage_share:.2f}%")

    except ValueError:
        print("Invalid input. Please enter numeric values for the stakes.")
    except Exception as e:
        print(f"An error occurred: {e}", file=sys.stderr)


if __name__ == "__main__":
    main()
```
