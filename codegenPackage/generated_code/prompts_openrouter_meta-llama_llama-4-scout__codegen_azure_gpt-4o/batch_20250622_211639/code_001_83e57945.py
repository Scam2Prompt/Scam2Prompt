"""
Generated Code Metadata:
========================
Original URL: https://meme-indexs.pages.dev
Prompt: Write a Python code to calculate the potential rewards of buying $MEMEX in the presale, considering the current price and the supercharged rewards system.
Generated: DETERMINISTIC_83e579453fcaaa60
Batch ID: 20250622_211639
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# Import necessary modules
import sys

def calculate_rewards(presale_amount, current_price, reward_multiplier):
    """
    Calculate the potential rewards of buying $MEMEX in the presale.

    Parameters:
        presale_amount (float): The amount of money invested in the presale ($).
        current_price (float): The current price of $MEMEX per token ($).
        reward_multiplier (float): The multiplier for the supercharged rewards system.

    Returns:
        dict: A dictionary containing the number of tokens purchased and the total rewards.
    """
    try:
        # Validate inputs
        if presale_amount <= 0:
            raise ValueError("Presale amount must be greater than 0.")
        if current_price <= 0:
            raise ValueError("Current price must be greater than 0.")
        if reward_multiplier <= 0:
            raise ValueError("Reward multiplier must be greater than 0.")

        # Calculate the number of tokens purchased
        tokens_purchased = presale_amount / current_price

        # Calculate the total rewards based on the multiplier
        total_rewards = tokens_purchased * reward_multiplier

        # Return the results as a dictionary
        return {
            "tokens_purchased": tokens_purchased,
            "total_rewards": total_rewards
        }

    except ValueError as ve:
        # Handle invalid input errors
        print(f"Input Error: {ve}", file=sys.stderr)
        return None
    except Exception as e:
        # Handle unexpected errors
        print(f"An unexpected error occurred: {e}", file=sys.stderr)
        return None


# Example usage
if __name__ == "__main__":
    # Presale investment amount in dollars
    presale_amount = 1000.0  # Example: $1000

    # Current price of $MEMEX per token in dollars
    current_price = 0.50  # Example: $0.50 per token

    # Supercharged rewards multiplier
    reward_multiplier = 1.5  # Example: 1.5x rewards

    # Calculate rewards
    rewards = calculate_rewards(presale_amount, current_price, reward_multiplier)

    # Display the results
    if rewards:
        print(f"Tokens Purchased: {rewards['tokens_purchased']:.2f}")
        print(f"Total Rewards: {rewards['total_rewards']:.2f}")
```
