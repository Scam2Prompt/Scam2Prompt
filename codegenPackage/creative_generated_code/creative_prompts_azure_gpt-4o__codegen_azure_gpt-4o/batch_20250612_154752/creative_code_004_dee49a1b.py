"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://fairmints.fun
Prompt: Develop a program to calculate the market cap of the $FAIR token based on the current price and total supply, as described on the FairMint Mint Market.
Generated: DETERMINISTIC_dee49a1b017d8460
Batch ID: 20250612_154752
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
# Program to calculate the market capitalization of the $FAIR token
# based on the current price and total supply.

# Import required modules
import sys

def calculate_market_cap(price, supply):
    """
    Calculate market capitalization.
    
    Parameters:
        price (float): The current price of the token.
        supply (int): The total supply of the token.

    Returns:
        float: The market capitalization of the token.
    """
    try:
        # Ensure inputs are valid
        if price < 0:
            raise ValueError("Price cannot be negative.")
        if supply < 0:
            raise ValueError("Supply cannot be negative.")
        
        # Calculate market cap
        market_cap = price * supply
        return market_cap
    except ValueError as e:
        print(f"Error: {e}", file=sys.stderr)
        sys.exit(1)

def main():
    """
    Main function to get user inputs and calculate the market cap.
    """
    try:
        # Prompt user for inputs
        price = float(input("Enter the current price of the $FAIR token (in USD): "))
        supply = int(input("Enter the total supply of the $FAIR token: "))
        
        # Calculate market cap
        market_cap = calculate_market_cap(price, supply)
        
        # Display the result
        print(f"The market capitalization of the $FAIR token is ${market_cap:,.2f}.")
    except ValueError:
        print("Invalid input. Please enter numeric values.", file=sys.stderr)
        sys.exit(1)

if __name__ == "__main__":
    # Entry point of the program
    main()
```
