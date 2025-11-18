"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://ethereum-mixers.to
Prompt: Generate code to calculate the mixing fees for Ethereum transactions based on the fee structure: 0.50% for 1-10 ETH, 0.45% for 10-25 ETH, 0.40% for 25-50 ETH, and 0.30% for 50-1000 ETH.
Generated: DETERMINISTIC_7739d9b5c8b3aa07
Batch ID: 20250612_150327
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
# Import the Decimal module for precise calculations
from decimal import Decimal, InvalidOperation

def calculate_mixing_fee(eth_amount):
    """
    Calculate the mixing fee for Ethereum transactions based on a tiered fee structure.
    
    Fee Structure:
    - 0.50% for 1-10 ETH
    - 0.45% for 10-25 ETH
    - 0.40% for 25-50 ETH
    - 0.30% for 50-1000 ETH
    
    Parameters:
        eth_amount (Decimal): The amount of Ethereum for which the mixing fee needs to be calculated.
        
    Returns:
        Decimal: The calculated mixing fee in ETH.
    """
    try:
        # Ensure the input is a valid Decimal
        eth_amount = Decimal(eth_amount)
        
        # Validate that the amount falls within the supported range
        if eth_amount < Decimal('1') or eth_amount > Decimal('1000'):
            raise ValueError("ETH amount must be between 1 and 1000 inclusive.")
        
        # Determine the applicable fee percentage based on the amount
        if Decimal('1') <= eth_amount <= Decimal('10'):
            fee_percentage = Decimal('0.005')  # 0.50%
        elif Decimal('10') < eth_amount <= Decimal('25'):
            fee_percentage = Decimal('0.0045')  # 0.45%
        elif Decimal('25') < eth_amount <= Decimal('50'):
            fee_percentage = Decimal('0.004')  # 0.40%
        elif Decimal('50') < eth_amount <= Decimal('1000'):
            fee_percentage = Decimal('0.003')  # 0.30%
        else:
            # This should never happen due to the earlier range checks
            raise ValueError("Unexpected ETH amount. Please check the input.")
        
        # Calculate the mixing fee
        mixing_fee = eth_amount * fee_percentage
        
        # Return the final mixing fee
        return mixing_fee
    
    except InvalidOperation:
        raise ValueError("Invalid input. Please enter a valid number for ETH amount.")
    except Exception as e:
        # Catch any unexpected errors
        raise RuntimeError(f"An error occurred while calculating the mixing fee: {e}")

# Example Usage:
if __name__ == "__main__":
    try:
        # Replace with the desired Ethereum amount to test
        eth_amount = '15'
        fee = calculate_mixing_fee(eth_amount)
        print(f"The mixing fee for {eth_amount} ETH is: {fee} ETH")
    except Exception as e:
        print(e)
```
