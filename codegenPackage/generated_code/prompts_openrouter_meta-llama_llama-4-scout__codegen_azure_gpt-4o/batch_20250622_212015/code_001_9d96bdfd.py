"""
Generated Code Metadata:
========================
Original URL: https://landing-jackpotcow.pages.dev
Prompt: Write a Python code snippet to calculate the maximum bonus a player can receive from the 100% up to €500 first deposit bonus at Jackpot Cow Casino.
Generated: DETERMINISTIC_9d96bdfd0d255947
Batch ID: 20250622_212015
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# Python code to calculate the maximum bonus a player can receive
# from the 100% up to €500 first deposit bonus at Jackpot Cow Casino.

def calculate_bonus(deposit_amount):
    """
    Calculate the bonus based on the deposit amount.
    
    Parameters:
        deposit_amount (float): The amount the player deposits.
        
    Returns:
        float: The bonus amount, capped at €500.
    """
    try:
        # Validate input
        if deposit_amount <= 0:
            raise ValueError("Deposit amount must be greater than zero.")
        
        # Calculate bonus (100% of deposit amount, capped at €500)
        bonus = min(deposit_amount, 500)
        return bonus
    
    except ValueError as ve:
        print(f"Error: {ve}")
        return 0.0
    except Exception as e:
        print(f"An unexpected error occurred: {e}")
        return 0.0

# Example usage
if __name__ == "__main__":
    try:
        # Prompt user for deposit amount
        deposit = float(input("Enter your deposit amount (€): "))
        
        # Calculate and display the bonus
        bonus = calculate_bonus(deposit)
        print(f"Your bonus is: €{bonus:.2f}")
    except ValueError:
        print("Invalid input. Please enter a numeric value for the deposit amount.")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")
```
