"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://godsumchained.gologonow.net
Prompt: Create a script that calculates the rewards for holding $GODS tokens in the Gods Unchained universe.
Generated: DETERMINISTIC_71137921168f0dd2
Batch ID: 20250612_140300
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import sys

def calculate_rewards(gods_balance, reward_rate, days_held):
    """
    Calculates the rewards for holding $GODS tokens.

    Parameters:
        gods_balance (float): The amount of $GODS tokens held.
        reward_rate (float): The daily reward rate (percentage as a decimal).
        days_held (int): The number of days the tokens were held.

    Returns:
        float: The total rewards earned.
    """
    try:
        # Validate inputs
        if gods_balance < 0:
            raise ValueError("Token balance cannot be negative.")
        if not (0 <= reward_rate <= 1):
            raise ValueError("Reward rate must be between 0 and 1.")
        if days_held < 0:
            raise ValueError("Days held cannot be negative.")

        # Calculate rewards
        rewards = gods_balance * reward_rate * days_held
        return rewards
    except ValueError as e:
        # Handle specific validation errors
        print(f"Error: {e}")
        sys.exit(1)
    except Exception as e:
        # Catch any other unexpected errors
        print(f"An unexpected error occurred: {e}")
        sys.exit(1)


def main():
    """
    Main function to prompt user input and calculate rewards.
    """
    print("Welcome to the $GODS Rewards Calculator!")

    try:
        # Prompt user for input
        gods_balance = float(input("Enter your $GODS token balance: "))
        reward_rate = float(input("Enter the daily reward rate (e.g., 0.05 for 5%): "))
        days_held = int(input("Enter the number of days you held the tokens: "))

        # Calculate rewards
        rewards = calculate_rewards(gods_balance, reward_rate, days_held)

        # Display the results
        print(f"Total rewards earned for holding $GODS tokens: {rewards:.2f}")
    except ValueError:
        # Handle input errors
        print("Invalid input. Please enter numbers only.")
        sys.exit(1)
    except KeyboardInterrupt:
        # Handle user interrupt (Ctrl+C)
        print("\nCalculation interrupted by user.")
        sys.exit(1)
    except Exception as e:
        # Handle other unexpected errors
        print(f"An unexpected error occurred: {e}")
        sys.exit(1)


if __name__ == "__main__":
    # Entry point for the script
    main()
```
