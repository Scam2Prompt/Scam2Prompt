"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://presales99bitcoins.pages.dev
Prompt: Generate code to calculate and display the estimated annual staking rewards for $99BTC tokens based on the current staking pool percentage.
Generated: DETERMINISTIC_a748aa4cda9e3ef2
Batch ID: 20250612_152235
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
# Import necessary libraries
import sys

def calculate_staking_rewards(token_amount, staking_percentage):
    """
    Calculate the estimated annual staking rewards based on token amount and staking percentage.

    Args:
        token_amount (float): The number of tokens being staked.
        staking_percentage (float): The annual staking reward percentage.

    Returns:
        float: The estimated annual staking rewards.
    """
    try:
        # Ensure inputs are valid
        if token_amount <= 0:
            raise ValueError("Token amount must be greater than 0.")
        if staking_percentage < 0 or staking_percentage > 100:
            raise ValueError("Staking percentage must be between 0 and 100.")
        
        # Calculate rewards
        annual_rewards = token_amount * (staking_percentage / 100)
        return annual_rewards
    except ValueError as e:
        # Handle invalid inputs
        print(f"Error: {e}", file=sys.stderr)
        return None
    except Exception as e:
        # Catch any other unexpected errors
        print(f"An unexpected error occurred: {e}", file=sys.stderr)
        return None

def main():
    """
    Main function to calculate and display staking rewards for $99BTC tokens.
    """
    try:
        # Input: Number of tokens and staking percentage
        token_amount = float(input("Enter the number of $99BTC tokens you want to stake: ").strip())
        staking_percentage = float(input("Enter the annual staking reward percentage: ").strip())
        
        # Calculate rewards
        rewards = calculate_staking_rewards(token_amount, staking_percentage)
        
        if rewards is not None:
            # Display the rewards
            print(f"Estimated annual staking rewards for {token_amount} $99BTC tokens: {rewards:.6f} tokens.")
    except ValueError:
        print("Invalid input. Please enter numeric values for both token amount and staking percentage.", file=sys.stderr)
    except Exception as e:
        print(f"An unexpected error occurred: {e}", file=sys.stderr)

# Entry point of the script
if __name__ == "__main__":
    main()
```
