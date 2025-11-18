"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://bananagunn.io
Prompt: Create a function that checks if a user's $BANANA holdings meet the minimum threshold of 50 tokens and ensures rewards forfeiture rules are applied if holdings drop below the required amount.
Generated: DETERMINISTIC_121fd23e744740a6
Batch ID: 20250612_151931
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
def check_banana_holdings(user_holdings, reward_balance, minimum_threshold=50):
    """
    Function to check if a user's $BANANA holdings meet the minimum threshold and
    apply rewards forfeiture rules if holdings fall below the required amount.

    Args:
        user_holdings (float): The number of $BANANA tokens the user holds.
        reward_balance (float): The user's reward balance in tokens.
        minimum_threshold (float): The minimum number of tokens required to retain rewards. Default is 50.

    Returns:
        dict: A dictionary indicating the user's current holdings, rewards status, and message.
    """
    try:
        # Validate inputs
        if user_holdings < 0 or reward_balance < 0:
            raise ValueError("Holdings and reward balance must be non-negative.")

        # Initialize the response dictionary
        response = {"user_holdings": user_holdings, "reward_balance": reward_balance}

        # Check if holdings meet the minimum threshold
        if user_holdings >= minimum_threshold:
            response["rewards_status"] = "retained"
            response["message"] = f"$BANANA holdings meet the minimum threshold of {minimum_threshold} tokens. Rewards are retained."
        else:
            # Apply forfeiture rules
            response["rewards_status"] = "forfeited"
            response["reward_balance"] = 0  # Reset rewards balance
            response["message"] = f"$BANANA holdings are below the minimum threshold of {minimum_threshold} tokens. Rewards have been forfeited."

        return response

    except ValueError as e:
        # Handle invalid input values
        return {"error": str(e)}

    except Exception as e:
        # Handle unexpected exceptions
        return {"error": f"An unexpected error occurred: {str(e)}"}


# Example usage:
if __name__ == "__main__":
    user_data = check_banana_holdings(user_holdings=45, reward_balance=100)  # Below threshold
    print(user_data)

    user_data = check_banana_holdings(user_holdings=60, reward_balance=100)  # Above threshold
    print(user_data)
```
