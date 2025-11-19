"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://fffrfh.pages.dev
Prompt: Write a function to calculate the potential MOR tokens earned based on the amount of stETH staked and the total staked amount in the Morpheus network.
Generated: DETERMINISTIC_ebbc121d405020e8
Batch ID: 20250612_163742
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
def calculate_mor_tokens(staked_amount, total_staked, reward_pool=1000000):
    """
    Calculate MOR tokens earned based on the amount of stETH staked and the total staked amount in the Morpheus network.

    Args:
        staked_amount (float): The amount of stETH staked by the user.
        total_staked (float): The total stETH staked in the Morpheus network.
        reward_pool (float, optional): Total MOR tokens available in the reward pool. Defaults to 1,000,000 MOR tokens.

    Returns:
        float: The calculated MOR tokens earned by the user.
    """
    try:
        # Input validation
        if staked_amount < 0:
            raise ValueError("Staked amount cannot be negative.")
        if total_staked <= 0:
            raise ValueError("Total staked amount must be greater than zero.")

        # Calculate MOR tokens earned
        mor_tokens_earned = (staked_amount / total_staked) * reward_pool

        return mor_tokens_earned

    except ZeroDivisionError:
        # Handle division by zero error
        print("Error: Total staked amount cannot be zero.")
        return 0
    except ValueError as e:
        # Handle invalid input values
        print(f"Input Error: {e}")
        return 0
    except Exception as e:
        # Handle any other unexpected errors
        print(f"Unexpected Error: {e}")
        return 0


# Example usage
if __name__ == "__main__":
    try:
        # Example inputs
        user_staked = 500  # User's stETH staked
        network_total_staked = 10000  # Total stETH staked in the network

        # Calculate MOR tokens
        mor_tokens = calculate_mor_tokens(user_staked, network_total_staked)
        print(f"MOR tokens earned: {mor_tokens:.2f}")
    except Exception as e:
        print(f"Error occurred during execution: {e}")
```
