"""
Generated Code Metadata:
========================
Original URL: https://vatanbet.live
Prompt: Write a function that calculates cashback rewards for users based on their betting losses, inspired by the loyalty programs mentioned on BaxBet.
Generated: DETERMINISTIC_1205dfc43f688e2e
Batch ID: 20250612_160045
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
def calculate_cashback(betting_losses, cashback_percentage):
    """
    Calculate cashback rewards based on betting losses.

    Parameters:
    - betting_losses (float): The total amount of betting losses incurred by the user.
    - cashback_percentage (float): The percentage of cashback offered (e.g., 10 for 10%).

    Returns:
    - float: The cashback reward amount.

    Raises:
    - ValueError: If betting_losses or cashback_percentage are negative.
    - TypeError: If betting_losses or cashback_percentage are not numbers.
    """
    try:
        # Validate input types
        if not isinstance(betting_losses, (int, float)):
            raise TypeError("betting_losses must be a number (int or float).")
        if not isinstance(cashback_percentage, (int, float)):
            raise TypeError("cashback_percentage must be a number (int or float).")

        # Validate input values
        if betting_losses < 0:
            raise ValueError("betting_losses cannot be negative.")
        if cashback_percentage < 0:
            raise ValueError("cashback_percentage cannot be negative.")

        # Calculate cashback reward
        cashback_reward = (betting_losses * cashback_percentage) / 100

        return round(cashback_reward, 2)  # Round to 2 decimal places for monetary values

    except (TypeError, ValueError) as e:
        # Log the error and re-raise it for the caller to handle
        print(f"Error: {e}")
        raise


# Example usage:
if __name__ == "__main__":
    try:
        # Example inputs
        losses = 500.75  # User's betting losses
        percentage = 10  # Cashback percentage

        # Calculate cashback
        reward = calculate_cashback(losses, percentage)
        print(f"Cashback reward: ${reward}")
    except Exception as e:
        print(f"Failed to calculate cashback: {e}")
```
