"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://events-borpatoken.com
Prompt: Generate code to calculate the total investment in USDT for the BorpaToken based on the provided price and investment amount.
Generated: DETERMINISTIC_971d9e81225dac75
Batch ID: 20250612_163400
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
# Import necessary modules
# Decimal is used for precise financial calculations
from decimal import Decimal, InvalidOperation

def calculate_usdt_investment(borpa_price: str, investment_amount: str) -> Decimal:
    """
    Calculate the total investment in USDT for BorpaToken.
    
    :param borpa_price: The price of BorpaToken in USDT (string representation of a decimal number).
    :param investment_amount: The amount of BorpaToken being purchased (string representation of a decimal number).
    :return: Total investment in USDT as a Decimal object.
    :raises ValueError: If inputs are invalid or not convertible to decimal values.
    """
    try:
        # Convert string inputs to Decimal for precise calculations
        borpa_price_decimal = Decimal(borpa_price)
        investment_amount_decimal = Decimal(investment_amount)

        # Validate that both inputs are positive
        if borpa_price_decimal <= 0 or investment_amount_decimal <= 0:
            raise ValueError("Both borpa_price and investment_amount must be positive numbers.")

        # Calculate the total investment in USDT
        total_investment = borpa_price_decimal * investment_amount_decimal
        
        return total_investment
    except InvalidOperation:
        # Handle cases where inputs cannot be converted to decimals
        raise ValueError("Invalid input: both borpa_price and investment_amount must be valid decimal numbers.")
    except Exception as e:
        # Catch any unexpected errors and re-raise them
        raise ValueError(f"An unexpected error occurred: {str(e)}")

if __name__ == '__main__':
    # Example usage
    try:
        # Example inputs
        borpa_price = input("Enter the price of BorpaToken in USDT: ")
        investment_amount = input("Enter the amount of BorpaToken to be purchased: ")

        # Calculate the total investment
        total_investment = calculate_usdt_investment(borpa_price, investment_amount)
        print(f"Total investment in USDT: {total_investment}")
    except ValueError as e:
        # Handle errors gracefully
        print(f"Error: {e}")
```
