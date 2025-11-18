"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://coinexchainltd.com
Prompt: Write code to calculate leverage up to 1:100 for professional traders, as offered by Coinex Chain Trading Company Ltd.
Generated: DETERMINISTIC_508268eb03311d6d
Batch ID: 20250612_153400
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
# Leverage Calculator for Professional Traders
# Offered by Coinex Chain Trading Company Ltd.
# This script calculates leverage up to 1:100 based on user input.

def calculate_leverage(trading_amount, leverage_ratio):
    """
    Calculate the effective trading capacity based on leverage.
    
    Args:
        trading_amount (float): The initial capital provided by the trader.
        leverage_ratio (int): The leverage ratio (e.g., 2 for 1:2, 100 for 1:100).
        
    Returns:
        float: The effective trading capacity after applying leverage.
        
    Raises:
        ValueError: If leverage_ratio is not between 1 and 100.
        ValueError: If trading_amount is less than or equal to 0.
    """
    if leverage_ratio < 1 or leverage_ratio > 100:
        raise ValueError("Leverage ratio must be between 1 and 100.")
    if trading_amount <= 0:
        raise ValueError("Trading amount must be greater than 0.")
    
    return trading_amount * leverage_ratio

def main():
    """
    Main function to interact with the trader and calculate leverage.
    """
    try:
        # Prompt the user for input
        trading_amount = float(input("Enter your trading amount (initial capital): "))
        leverage_ratio = int(input("Enter leverage ratio (e.g., 2 for 1:2, 100 for 1:100): "))
        
        # Calculate leverage
        effective_capacity = calculate_leverage(trading_amount, leverage_ratio)
        
        # Display the result
        print(f"With a leverage ratio of 1:{leverage_ratio}, your effective trading capacity is: {effective_capacity:.2f}")
    
    except ValueError as e:
        # Handle invalid input and display an error message
        print(f"Error: {e}")
    except Exception as e:
        # Catch any other unexpected errors
        print(f"An unexpected error occurred: {e}")

if __name__ == "__main__":
    # Entry point for the script
    main()
```
