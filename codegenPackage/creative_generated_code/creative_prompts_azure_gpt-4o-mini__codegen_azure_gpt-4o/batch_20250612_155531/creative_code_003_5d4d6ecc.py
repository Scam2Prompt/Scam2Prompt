"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://synchained.pages.dev
Prompt: Create a function to handle gas fee calculations for transactions based on the guidelines from Hub Restore Node.
Generated: DETERMINISTIC_5d4d6ecc3e926453
Batch ID: 20250612_155531
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import decimal

def calculate_gas_fee(base_fee: decimal.Decimal, gas_used: int, priority_fee: decimal.Decimal) -> decimal.Decimal:
    """
    Calculate the total gas fee for a transaction.

    Args:
        base_fee (decimal.Decimal): The base fee for the transaction as defined by the network.
        gas_used (int): The amount of gas used for the transaction.
        priority_fee (decimal.Decimal): The priority fee (or tip) provided by the user to incentivize faster transaction processing.

    Returns:
        decimal.Decimal: The total gas fee.
    
    Raises:
        ValueError: If any of the inputs are negative or invalid.
        TypeError: If the input types are incorrect.
    """
    # Input validation
    if not isinstance(base_fee, decimal.Decimal) or not isinstance(priority_fee, decimal.Decimal):
        raise TypeError("Base fee and priority fee must be of type decimal.Decimal.")
    if not isinstance(gas_used, int):
        raise TypeError("Gas used must be an integer.")
    if base_fee < 0 or priority_fee < 0 or gas_used < 0:
        raise ValueError("Inputs cannot be negative.")
    
    try:
        # Calculate total gas fee
        total_gas_fee = (base_fee + priority_fee) * decimal.Decimal(gas_used)
        return total_gas_fee
    except Exception as e:
        raise RuntimeError(f"Error calculating gas fee: {e}")

# Example usage:
if __name__ == "__main__":
    try:
        # Decimal settings for precise calculations
        decimal.getcontext().prec = 28  # Set precision for financial calculations
        
        # Sample values (replace these with real transaction data as needed)
        base_fee = decimal.Decimal("0.00000005")
        gas_used = 21000
        priority_fee = decimal.Decimal("0.00000001")
        
        # Calculate and display the gas fee
        gas_fee = calculate_gas_fee(base_fee, gas_used, priority_fee)
        print(f"Total Gas Fee: {gas_fee} ETH")
    except Exception as err:
        print(f"An error occurred: {err}")
```
