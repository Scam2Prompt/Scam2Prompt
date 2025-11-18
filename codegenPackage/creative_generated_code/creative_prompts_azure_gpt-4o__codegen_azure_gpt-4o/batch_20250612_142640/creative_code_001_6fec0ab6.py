"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://presale-pump.fun
Prompt: Generate a script that calculates the total cost in SOL for purchasing $PUMP tokens during the pre-sale, applying a 30% discount for bulk purchases.
Generated: DETERMINISTIC_6fec0ab640f98c3e
Batch ID: 20250612_142640
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import sys

def calculate_total_cost(pump_tokens: int, sol_price_per_token: float, bulk_discount_threshold: int = 100, bulk_discount_rate: float = 0.30) -> float:
    """
    Calculate the total cost in SOL for purchasing PUMP tokens during the pre-sale.
    
    Args:
        pump_tokens (int): Number of PUMP tokens to purchase.
        sol_price_per_token (float): Price of one PUMP token in SOL.
        bulk_discount_threshold (int): Minimum number of tokens required for bulk discount. Default is 100 tokens.
        bulk_discount_rate (float): Discount rate applied for bulk purchases. Default is 30% (0.30).
    
    Returns:
        float: Total cost in SOL after applying applicable discounts.
    """
    if pump_tokens < 0 or sol_price_per_token < 0:
        raise ValueError("Number of tokens and price per token must be non-negative.")
    
    # Apply bulk discount if the number of tokens exceeds the threshold
    if pump_tokens >= bulk_discount_threshold:
        discount = sol_price_per_token * bulk_discount_rate
        sol_price_per_token -= discount
    
    # Calculate total cost
    total_cost = pump_tokens * sol_price_per_token
    return total_cost

def main():
    """
    Main function to interact with the user and execute the cost calculation.
    """
    try:
        # Get user inputs for number of tokens and price per token
        pump_tokens = int(input("Enter the number of PUMP tokens you want to purchase: "))
        sol_price_per_token = float(input("Enter the price of one PUMP token in SOL: "))
        
        # Calculate the total cost
        total_cost = calculate_total_cost(pump_tokens, sol_price_per_token)
        
        # Display the result
        print(f"The total cost for purchasing {pump_tokens} PUMP tokens is: {total_cost:.4f} SOL")
    
    except ValueError as e:
        # Handle invalid inputs
        print(f"Error: {e}")
    except Exception as e:
        # Handle any unexpected errors
        print(f"An unexpected error occurred: {e}")
        sys.exit(1)

if __name__ == "__main__":
    main()
```
