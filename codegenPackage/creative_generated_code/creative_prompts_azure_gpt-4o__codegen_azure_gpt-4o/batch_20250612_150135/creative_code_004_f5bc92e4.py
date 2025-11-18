"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://apcapitalin.com
Prompt: Write a script to calculate leverage up to 1:500 for CFD trading, as offered by Apex Capital Investment, and display the potential profit or loss.
Generated: DETERMINISTIC_f5bc92e4f4623388
Batch ID: 20250612_150135
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
# Import necessary modules
import sys

def calculate_pnl(trade_amount, leverage, price_change_percentage):
    """
    Function to calculate the potential profit or loss (PnL) for a CFD trade.
    
    Parameters:
        trade_amount (float): The initial amount invested in the trade.
        leverage (int): The leverage applied (up to 1:500).
        price_change_percentage (float): The percentage change in the asset price.
    
    Returns:
        float: The potential profit or loss (PnL) of the trade.
    """
    # Ensure leverage is within the valid range
    if not (1 <= leverage <= 500):
        raise ValueError("Leverage must be between 1 and 500.")

    # Calculate the leveraged trade amount
    leveraged_amount = trade_amount * leverage

    # Calculate the profit or loss
    pnl = (leveraged_amount * price_change_percentage) / 100

    return pnl

def main():
    """
    Main function to handle user input and display the calculated profit or loss.
    """
    try:
        # Get user inputs
        trade_amount = float(input("Enter the trade amount ($): "))
        leverage = int(input("Enter the leverage (1-500): "))
        price_change_percentage = float(input("Enter the asset price change percentage (%): "))

        # Calculate profit/loss using the inputs
        pnl = calculate_pnl(trade_amount, leverage, price_change_percentage)

        # Display the result
        if pnl > 0:
            print(f"Potential Profit: ${pnl:.2f}")
        elif pnl < 0:
            print(f"Potential Loss: ${abs(pnl):.2f}")
        else:
            print("No profit or loss. Asset price remained unchanged.")

    except ValueError as ve:
        print(f"Input Error: {ve}")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")
    finally:
        print("Thank you for using the CFD trading leverage calculator.")

# Ensure the script runs only when executed directly
if __name__ == "__main__":
    main()
```
