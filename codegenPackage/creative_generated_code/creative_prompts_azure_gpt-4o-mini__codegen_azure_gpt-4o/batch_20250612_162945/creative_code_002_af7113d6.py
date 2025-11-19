"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://superkend.xyz
Prompt: Create a function that calculates potential rewards for liquidity providers on the Etherlink platform based on the ongoing rewards program.
Generated: DETERMINISTIC_af7113d699e6fda3
Batch ID: 20250612_162945
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import decimal

def calculate_liquidity_rewards(liquidity_provided, reward_rate, duration_in_days):
    """
    Calculate the potential rewards for liquidity providers on the Etherlink platform.

    Args:
        liquidity_provided (decimal.Decimal): The amount of liquidity provided (in ETH).
        reward_rate (decimal.Decimal): The daily reward rate (as a percentage, e.g., 0.05 for 5%).
        duration_in_days (int): The number of days the liquidity is provided.

    Returns:
        decimal.Decimal: The calculated rewards for the specified duration.

    Raises:
        ValueError: If any input is invalid (negative values or zero duration).
    """
    # Validate inputs
    if liquidity_provided <= 0:
        raise ValueError("Liquidity provided must be greater than zero.")
    if reward_rate <= 0:
        raise ValueError("Reward rate must be greater than zero.")
    if duration_in_days <= 0:
        raise ValueError("Duration in days must be greater than zero.")
    
    try:
        # Calculate rewards
        rewards = liquidity_provided * reward_rate * decimal.Decimal(duration_in_days)
        return rewards
    except decimal.InvalidOperation as e:
        raise ValueError(f"An error occurred during reward calculation: {e}")

# Example usage (ensure decimal inputs for precision)
if __name__ == "__main__":
    from decimal import Decimal

    try:
        # Example values
        liquidity_provided = Decimal("10.5")  # Liquidity provided in ETH
        reward_rate = Decimal("0.03")        # Daily reward rate (3%)
        duration_in_days = 30                # Duration in days

        # Calculate rewards
        rewards = calculate_liquidity_rewards(liquidity_provided, reward_rate, duration_in_days)
        print(f"Potential rewards for providing liquidity: {rewards} ETH")
    except ValueError as err:
        print(f"Error: {err}")
```
