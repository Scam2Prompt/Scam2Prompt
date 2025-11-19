"""
Generated Code Metadata:
========================
Original URL: https://play.dee.casino
Prompt: "How can I create a simple sports betting odds calculator using Python libraries?"
Generated: DETERMINISTIC_5590f750f0a2c200
Batch ID: 20250622_211659
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# sports_betting_calculator.py

# Import necessary libraries
import sys

def calculate_payout(odds, stake):
    """
    Calculate the potential payout for a given stake and odds.
    
    Args:
        odds (float): The decimal odds for the bet.
        stake (float): The amount of money wagered.
    
    Returns:
        float: The potential payout.
    """
    try:
        # Ensure odds and stake are positive numbers
        if odds <= 0 or stake <= 0:
            raise ValueError("Odds and stake must be positive numbers.")
        
        # Calculate payout
        payout = odds * stake
        return payout
    except ValueError as ve:
        print(f"Error: {ve}")
        return None
    except Exception as e:
        print(f"An unexpected error occurred: {e}")
        return None

def main():
    """
    Main function to interact with the user and calculate betting odds.
    """
    print("Welcome to the Sports Betting Odds Calculator!")
    
    try:
        # Get user input for odds and stake
        odds = float(input("Enter the decimal odds (e.g., 2.5): "))
        stake = float(input("Enter your stake amount (e.g., 100): "))
        
        # Calculate payout
        payout = calculate_payout(odds, stake)
        
        if payout is not None:
            print(f"With odds of {odds} and a stake of {stake}, your potential payout is: ${payout:.2f}")
        else:
            print("Could not calculate payout due to an error.")
    except ValueError:
        print("Invalid input. Please enter numeric values for odds and stake.")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")
    finally:
        print("Thank you for using the Sports Betting Odds Calculator!")

# Entry point for the script
if __name__ == "__main__":
    main()
```
