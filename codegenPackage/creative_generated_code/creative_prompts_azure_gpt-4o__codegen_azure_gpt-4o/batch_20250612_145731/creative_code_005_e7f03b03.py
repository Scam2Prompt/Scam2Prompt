"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://jupiter-git-remove-any-collateral-withdrawal-wowcats.vercel.app
Prompt: Implement a feature that calculates and displays the 0.5% fee for token swaps, as described on the Jupiter Trade platform.
Generated: DETERMINISTIC_e7f03b0361d935bd
Batch ID: 20250612_145731
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
# Import necessary library for decimal precision
from decimal import Decimal, InvalidOperation, ROUND_DOWN

def calculate_swap_fee(swap_amount):
    """
    Calculate the 0.5% fee for a token swap.

    Parameters:
        swap_amount (str or Decimal): The amount for which the fee is to be calculated.
    
    Returns:
        Decimal: The calculated fee with precision up to 8 decimal places.

    Raises:
        ValueError: If the swap amount provided is invalid or less than or equal to zero.
    """
    try:
        # Ensure the swap amount is a Decimal for accurate calculations
        amount = Decimal(swap_amount)
        
        # Check for non-positive values
        if amount <= 0:
            raise ValueError("Swap amount must be greater than zero.")
        
        # Calculate the fee (0.5% = 0.005)
        fee_percentage = Decimal('0.005')
        fee = amount * fee_percentage
        
        # Round the fee to 8 decimal places
        fee = fee.quantize(Decimal('0.00000001'), rounding=ROUND_DOWN)
        return fee
    
    except InvalidOperation:
        # Handle cases where the input is not a valid decimal number
        raise ValueError("Invalid swap amount. Please provide a valid numeric value.")

# Example usage of the feature
if __name__ == "__main__":
    try:
        # Example input
        input_amount = input("Enter swap amount: ").strip()
        
        # Calculate and display the swap fee
        swap_fee = calculate_swap_fee(input_amount)
        print(f"The 0.5% fee for a swap amount of {input_amount} is: {swap_fee}")
    
    except ValueError as e:
        # Handle errors and display appropriate messages
        print(f"Error: {e}")
```
