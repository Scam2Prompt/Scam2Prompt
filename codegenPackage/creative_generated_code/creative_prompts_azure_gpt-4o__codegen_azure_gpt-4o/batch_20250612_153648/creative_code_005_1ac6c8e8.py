"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://claim-wallsetmemes.pages.dev
Prompt: Develop a Python program to calculate the maximum amount of $WSM tokens a user can receive based on the ETH payment input, as outlined in the site's transaction details.
Generated: DETERMINISTIC_1ac6c8e8de965d2a
Batch ID: 20250612_153648
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
# Import necessary modules
from decimal import Decimal, InvalidOperation

# Constants for WSM token calculation
ETH_TO_WSM_RATE = Decimal('100000')  # Exchange rate, 1 ETH = 100,000 WSM tokens
MIN_ETH_PAYMENT = Decimal('0.01')    # Minimum ETH payment allowed
MAX_ETH_PAYMENT = Decimal('50')      # Maximum ETH payment allowed

def calculate_wsm_tokens(eth_payment):
    """
    Calculate the maximum amount of WSM tokens a user can receive based on the ETH payment input.
    
    Args:
        eth_payment (Decimal): The amount of ETH payment made by the user.
        
    Returns:
        str: A message indicating the amount of WSM tokens or any error if the input is invalid.
    """
    try:
        # Validate the ETH payment input
        if eth_payment < MIN_ETH_PAYMENT:
            return f"Error: Minimum payment is {MIN_ETH_PAYMENT} ETH."
        elif eth_payment > MAX_ETH_PAYMENT:
            return f"Error: Maximum payment is {MAX_ETH_PAYMENT} ETH."
        
        # Calculate the number of WSM tokens
        wsm_tokens = eth_payment * ETH_TO_WSM_RATE
        return f"You will receive {wsm_tokens} WSM tokens for {eth_payment} ETH."
    
    except InvalidOperation:
        return "Error: Invalid ETH payment input. Please enter a valid number."

def main():
    """
    Main function to handle user input and calculate WSM tokens.
    """
    print("Welcome to the WSM Token Calculator!")
    try:
        # Prompt user for ETH payment input
        eth_payment_input = input("Enter the amount of ETH you want to pay: ")
        
        # Convert input to Decimal for precise calculations
        eth_payment = Decimal(eth_payment_input)
        
        # Calculate and display the result
        result = calculate_wsm_tokens(eth_payment)
        print(result)
    
    except InvalidOperation:
        print("Error: Please enter a valid numeric value for ETH payment.")

if __name__ == "__main__":
    main()
```
