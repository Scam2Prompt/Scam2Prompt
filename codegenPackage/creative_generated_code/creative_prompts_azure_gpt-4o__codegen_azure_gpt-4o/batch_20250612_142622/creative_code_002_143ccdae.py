"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://mixertumbler.pro
Prompt: Create a function in Python that calculates the random service fee (between 2%-5%) for a Bitcoin mixing transaction and outputs the final amount after the fee deduction.
Generated: DETERMINISTIC_143ccdae2c6c8d50
Batch ID: 20250612_142622
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import random

def calculate_bitcoin_mixing_fee(transaction_amount):
    """
    Calculates the final amount after deducting a random service fee for a Bitcoin mixing transaction.
    
    The service fee is randomly chosen between 2% and 5%.
    
    Args:
        transaction_amount (float): The initial transaction amount in Bitcoin.
        
    Returns:
        dict: A dictionary containing the original amount, service fee percentage, fee amount, and final amount.
    
    Raises:
        ValueError: If the transaction_amount is not positive.
    """
    # Validate input
    if transaction_amount <= 0:
        raise ValueError("Transaction amount must be greater than zero.")

    # Generate a random service fee percentage between 2% and 5%
    service_fee_percentage = random.uniform(2, 5)
    
    # Calculate the fee amount
    fee_amount = (service_fee_percentage / 100) * transaction_amount
    
    # Calculate the final amount after the fee deduction
    final_amount = transaction_amount - fee_amount

    # Create a detailed result dictionary
    result = {
        "original_amount": transaction_amount,
        "service_fee_percentage": round(service_fee_percentage, 2),
        "fee_amount": round(fee_amount, 8),  # Rounded to 8 decimal places for Bitcoin precision
        "final_amount": round(final_amount, 8)
    }
    
    return result

# Example usage:
if __name__ == "__main__":
    try:
        transaction_amount = float(input("Enter the Bitcoin transaction amount: "))
        result = calculate_bitcoin_mixing_fee(transaction_amount)
        print("Bitcoin Mixing Transaction Details:")
        for key, value in result.items():
            print(f"{key}: {value}")
    except ValueError as ve:
        print(f"Error: {ve}")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")
```
