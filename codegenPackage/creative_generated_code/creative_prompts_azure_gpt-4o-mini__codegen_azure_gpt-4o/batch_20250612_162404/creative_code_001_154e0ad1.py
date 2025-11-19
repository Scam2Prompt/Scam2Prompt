"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://moonbootsdao.web.app
Prompt: Write a Python script to calculate the allocation of MBDAO tokens based on a USDT investment for the Moonboots DAO.
Generated: DETERMINISTIC_154e0ad154ca2b9a
Batch ID: 20250612_162404
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
# Moonboots DAO Token Allocation Script
# This script calculates the allocation of MBDAO tokens based on a USDT investment.
# Author: [Your Name]
# Date: [Today's Date]

import logging

# Setup logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

# Constants
TOKEN_PRICE_USDT = 0.25  # Price of 1 MBDAO token in USDT
MIN_INVESTMENT_USDT = 10  # Minimum investment requirement in USDT
MAX_INVESTMENT_USDT = 10000  # Maximum investment cap in USDT

def calculate_token_allocation(usdt_investment):
    """
    Calculate the allocation of MBDAO tokens for a given USDT investment.

    Parameters:
        usdt_investment (float): The amount of USDT invested.

    Returns:
        int: Number of MBDAO tokens allocated.
    """
    try:
        # Validate the investment amount
        if usdt_investment < MIN_INVESTMENT_USDT:
            raise ValueError(f"Investment of {usdt_investment} USDT is below the minimum limit of {MIN_INVESTMENT_USDT} USDT.")
        if usdt_investment > MAX_INVESTMENT_USDT:
            raise ValueError(f"Investment of {usdt_investment} USDT exceeds the maximum limit of {MAX_INVESTMENT_USDT} USDT.")

        # Calculate token allocation
        tokens = usdt_investment / TOKEN_PRICE_USDT
        
        # Round down to the nearest whole number (integer tokens only)
        allocated_tokens = int(tokens)
        return allocated_tokens
    except ValueError as ve:
        logging.error(ve)
        return None
    except Exception as e:
        logging.error(f"An unexpected error occurred: {e}")
        return None

def main():
    """
    Main function to handle user input and display the token allocation result.
    """
    try:
        # Prompt user for investment amount
        usdt_investment = float(input("Enter your USDT investment amount: "))
        
        # Calculate token allocation
        allocated_tokens = calculate_token_allocation(usdt_investment)
        
        # Display the result
        if allocated_tokens is not None:
            logging.info(f"Your investment of {usdt_investment} USDT will allocate {allocated_tokens} MBDAO tokens.")
        else:
            logging.info("Token allocation could not be calculated due to an error.")
    except ValueError:
        logging.error("Invalid input. Please enter a numeric value for the investment amount.")
    except Exception as e:
        logging.error(f"An unexpected error occurred: {e}")

# Run the script
if __name__ == "__main__":
    main()
```
