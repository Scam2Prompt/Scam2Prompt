"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://cashb90.org
Prompt: Create a function that calculates cashback rewards for users based on their betting activity, inspired by the loyalty program at BaxBet.
Generated: DETERMINISTIC_f86f87debe3b1796
Batch ID: 20250612_155855
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
# cashback_rewards.py

def calculate_cashback(bet_amounts, cashback_percentage):
    """
    Calculate cashback rewards for users based on their betting activity.

    Parameters:
    bet_amounts (list): A list of floats representing the amounts of bets the user has placed.
    cashback_percentage (float): The cashback percentage (e.g., 5 for 5% cashback).

    Returns:
    float: The total cashback reward.
    
    Raises:
    ValueError: If bet_amounts contains invalid values or cashback_percentage is out of range.
    """
    try:
        # Validate input
        if not isinstance(bet_amounts, list) or not all(isinstance(amount, (int, float)) and amount >= 0 for amount in bet_amounts):
            raise ValueError("bet_amounts must be a list of non-negative numbers.")
        if not isinstance(cashback_percentage, (int, float)) or not (0 <= cashback_percentage <= 100):
            raise ValueError("cashback_percentage must be a number between 0 and 100 (inclusive).")
        
        # Calculate cashback
        total_bet_amount = sum(bet_amounts)  # Sum of all bets
        cashback_reward = (total_bet_amount * cashback_percentage) / 100  # Cashback calculation

        return round(cashback_reward, 2)  # Returning cashback rounded to 2 decimal places for precision

    except Exception as e:
        # Log the exception (if logging system is available in production, integrate here)
        print(f"Error calculating cashback: {e}")
        raise  # Reraise the exception for further handling

# Example usage:
if __name__ == "__main__":
    try:
        user_bets = [100.0, 50.0, 25.0]  # Example betting amounts
        cashback_rate = 5  # Example cashback percentage (5%)
        cashback = calculate_cashback(user_bets, cashback_rate)
        print(f"Total Cashback: ${cashback}")
    except Exception as err:
        print(f"Failed to calculate cashback: {err}")
```
