"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://solnarize-in.pages.dev
Prompt: Generate code to calculate the pre-sale price and listing price conversion for $SRIZE tokens based on the given SOL exchange rates.
Generated: DETERMINISTIC_2d26930efbb168b5
Batch ID: 20250612_151143
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
# Script to calculate the pre-sale price and listing price conversion for $SRIZE tokens
# based on the given SOL exchange rates.

# Required Libraries
import sys

def calculate_prices(sol_rate, presale_srize_per_sol, listing_srize_per_sol):
    """
    Calculate the pre-sale and listing prices of $SRIZE tokens based on SOL rates.
    
    Parameters:
    sol_rate (float): The current exchange rate of SOL to USD.
    presale_srize_per_sol (int): Number of $SRIZE tokens per SOL during pre-sale.
    listing_srize_per_sol (int): Number of $SRIZE tokens per SOL during listing.
    
    Returns:
    dict: A dictionary containing pre-sale and listing price of $SRIZE in USD.
    """
    try:
        # Validation: Ensure inputs are positive floats/integers
        if sol_rate <= 0 or presale_srize_per_sol <= 0 or listing_srize_per_sol <= 0:
            raise ValueError("All input values must be positive numbers.")

        # Calculate pre-sale price and listing price
        presale_price_usd = sol_rate / presale_srize_per_sol
        listing_price_usd = sol_rate / listing_srize_per_sol

        # Return results
        return {
            "pre_sale_price_usd": round(presale_price_usd, 2),
            "listing_price_usd": round(listing_price_usd, 2)
        }
    except ValueError as ve:
        # Handle invalid input values
        print(f"ValueError: {ve}")
        sys.exit(1)
    except Exception as e:
        # Handle unexpected errors
        print(f"An unexpected error occurred: {e}")
        sys.exit(1)

def main():
    """
    Main function to run the token price calculation logic.
    """
    print("Welcome to the $SRIZE Token Price Calculator!")

    # Get user inputs
    try:
        sol_rate = float(input("Enter the current SOL to USD exchange rate: "))
        presale_srize_per_sol = int(input("Enter the number of $SRIZE tokens per SOL during pre-sale: "))
        listing_srize_per_sol = int(input("Enter the number of $SRIZE tokens per SOL during listing: "))
    except ValueError:
        print("Invalid input. Please enter numeric values for the exchange rate and token quantities.")
        sys.exit(1)

    # Calculate prices
    prices = calculate_prices(sol_rate, presale_srize_per_sol, listing_srize_per_sol)

    # Display results
    print("\nResults:")
    print(f"Pre-sale Price of $SRIZE (in USD): ${prices['pre_sale_price_usd']}")
    print(f"Listing Price of $SRIZE (in USD): ${prices['listing_price_usd']}")

if __name__ == "__main__":
    main()
```
