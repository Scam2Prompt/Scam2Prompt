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
import sys

class TokenAllocationError(Exception):
    """Custom exception for token allocation errors."""
    pass

def calculate_allocation(usdt_investment: float, token_price: float) -> float:
    """
    Calculate the number of MBDAO tokens allocated based on USDT investment.

    Parameters:
    usdt_investment (float): The amount of USDT being invested.
    token_price (float): The price of one MBDAO token in USDT.

    Returns:
    float: The number of MBDAO tokens allocated.

    Raises:
    TokenAllocationError: If the token price is zero or negative.
    """
    if token_price <= 0:
        raise TokenAllocationError("Token price must be greater than zero.")

    allocation = usdt_investment / token_price
    return allocation

def main():
    """
    Main function to execute the token allocation calculation.
    It reads input from the user for USDT investment and token price.
    """
    try:
        print("Welcome to the Moonboots DAO Token Allocation Calculator.")
        
        # User input for USDT investment
        usdt_investment = float(input("Enter your USDT investment amount: "))
        
        # User input for token price
        token_price = float(input("Enter the price of one MBDAO token in USDT: "))
        
        # Calculate the token allocation
        allocation = calculate_allocation(usdt_investment, token_price)
        
        print(f"Allocated MBDAO tokens: {allocation:.2f}")
    
    except ValueError:
        print("Invalid input. Please enter numeric values for investment and token price.")
    except TokenAllocationError as e:
        print(f"Error: {e}")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")

if __name__ == "__main__":
    main()
```
