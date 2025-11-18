"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://dogecoin20-d.web.app
Prompt: Write a script to calculate the diluted market cap of DOGE20 tokens based on its fixed supply and current token price.
Generated: DETERMINISTIC_b62e221da19d630f
Batch ID: 20250612_152656
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
# calculate_diluted_market_cap.py

# Import necessary modules
import sys

def calculate_diluted_market_cap(supply: int, price: float) -> float:
    """
    Calculate the diluted market cap of DOGE20 tokens.
    
    :param supply: Fixed supply of DOGE20 tokens (integer).
    :param price: Current price per DOGE20 token (float).
    :return: Diluted market cap (float).
    """
    try:
        # Validate inputs
        if supply <= 0:
            raise ValueError("Supply must be a positive integer.")
        if price < 0:
            raise ValueError("Price must be a non-negative float.")

        # Calculate diluted market cap
        diluted_market_cap = supply * price
        return diluted_market_cap
    except ValueError as ve:
        # Handle validation errors
        print(f"Error: {ve}")
        sys.exit(1)
    except Exception as e:
        # Handle other unexpected errors
        print(f"An unexpected error occurred: {e}")
        sys.exit(1)

if __name__ == "__main__":
    # Fixed supply of DOGE20 tokens (example: 10,000,000)
    FIXED_SUPPLY = 10000000
    
    try:
        # Prompt user for the current price per DOGE20 token
        user_input_price = input("Enter the current price per DOGE20 token (e.g., 0.05): ")
        
        # Convert user input to float
        current_price = float(user_input_price)
        
        # Calculate and display the diluted market cap
        diluted_market_cap = calculate_diluted_market_cap(FIXED_SUPPLY, current_price)
        print(f"Diluted Market Cap of DOGE20 tokens: ${diluted_market_cap:,.2f}")
    except ValueError:
        print("Invalid input. Please enter a valid numeric value for the price.")
        sys.exit(1)
    except Exception as e:
        print(f"An unexpected error occurred: {e}")
        sys.exit(1)
```
