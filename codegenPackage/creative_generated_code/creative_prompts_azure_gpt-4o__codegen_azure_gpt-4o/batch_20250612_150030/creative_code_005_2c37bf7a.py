"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://bep20.art
Prompt: Develop a script to calculate the additional BNB rewards for new users who meet the criteria of three transactions and a 10% bonus.
Generated: DETERMINISTIC_2c37bf7a02976b99
Batch ID: 20250612_150030
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

Here is the clean, well-documented, production-ready Python code for your request:

```python
import decimal

def calculate_bnb_rewards(transactions, base_reward, bonus_percentage=10):
    """
    Calculates the additional BNB rewards for new users who meet the criteria.

    Parameters:
    - transactions (list): List of transaction amounts (decimal.Decimal) made by the user.
    - base_reward (decimal.Decimal): The base reward amount in BNB.
    - bonus_percentage (int): The bonus percentage to be applied (default is 10%).

    Returns:
    - decimal.Decimal: The total reward including the bonus if criteria are met.
    - str: A message indicating whether the user qualifies or not.
    """
    try:
        # Ensure the inputs are valid
        if not isinstance(transactions, list) or not all(isinstance(txn, decimal.Decimal) for txn in transactions):
            raise ValueError("Transactions must be a list of decimal.Decimal values.")
        if not isinstance(base_reward, decimal.Decimal):
            raise ValueError("Base reward must be a decimal.Decimal value.")
        if not isinstance(bonus_percentage, int) or bonus_percentage < 0:
            raise ValueError("Bonus percentage must be a non-negative integer.")

        # Check the criteria (at least 3 transactions)
        if len(transactions) >= 3:
            # Calculate the bonus
            bonus = base_reward * decimal.Decimal(bonus_percentage) / 100
            total_reward = base_reward + bonus
            return total_reward, "User qualifies for the bonus."
        else:
            return base_reward, "User does not qualify for the bonus. Fewer than 3 transactions."
    
    except Exception as e:
        # Handle unexpected errors gracefully
        return decimal.Decimal(0), f"Error: {e}"


# Usage example
if __name__ == "__main__":
    # Initialize decimal context for precision
    decimal.getcontext().prec = 18

    # Input data
    user_transactions = [decimal.Decimal("0.5"), decimal.Decimal("1.0"), decimal.Decimal("0.25")]
    base_reward = decimal.Decimal("2.0")

    # Calculate rewards
    rewards, message = calculate_bnb_rewards(user_transactions, base_reward)

    # Output the results
    print(f"Total Rewards: {rewards} BNB")
    print(f"Message: {message}")
```
