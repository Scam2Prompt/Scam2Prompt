"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://purplebr.com
Prompt: Create a function that simulates the rollingan bonus calculation for an online betting platform, inspired by DewaTogel's bonus structure.
Generated: DETERMINISTIC_b4d68632716d46e4
Batch ID: 20250612_161616
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import random
import logging

# Set up logging for the application
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

def calculate_rolling_bonus(bet_amount: float, rolling_percentage: float) -> float:
    """
    Simulates the rolling bonus calculation for an online betting platform.

    Parameters:
        bet_amount (float): The amount of money bet by the user.
        rolling_percentage (float): The percentage of the bet amount to be returned as a bonus.

    Returns:
        float: The calculated rolling bonus amount.

    Raises:
        ValueError: If bet_amount or rolling_percentage is invalid (e.g., negative values).
    """
    try:
        # Validate input
        if bet_amount <= 0:
            raise ValueError("Bet amount must be greater than 0.")
        if not (0 <= rolling_percentage <= 100):
            raise ValueError("Rolling percentage must be within the range of 0 to 100.")
        
        # Calculate the rolling bonus
        bonus = bet_amount * (rolling_percentage / 100)
        
        # Log the calculation for tracking
        logging.info(f"Bet Amount: {bet_amount}, Rolling Percentage: {rolling_percentage}%, Bonus: {bonus}")
        
        return bonus
    
    except ValueError as e:
        # Log the error and re-raise the exception for upstream handling
        logging.error(f"Error in calculating rolling bonus: {e}")
        raise

# Example usage in production (this would typically be part of a different script/module)
if __name__ == "__main__":
    try:
        # Simulate user input
        user_bet_amount = float(input("Enter your bet amount: "))
        user_rolling_percentage = float(input("Enter the rolling percentage: "))
        
        # Calculate the rolling bonus
        bonus = calculate_rolling_bonus(user_bet_amount, user_rolling_percentage)
        print(f"Your rolling bonus is: ${bonus:.2f}")
    
    except ValueError as err:
        print(f"Input error: {err}")
    except Exception as e:
        # Catch any unexpected errors
        logging.error(f"An unexpected error occurred: {e}")
```
