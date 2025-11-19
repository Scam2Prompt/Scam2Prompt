"""
Generated Code Metadata:
========================
Original URL: https://anonymixer.xyz
Prompt: Create a function that calculates service fees for mixing Bitcoin based on the fee range (1-2%) provided by Anonymixer. Include upfront fee display functionality before initiating transactions.
Generated: DETERMINISTIC_92e5d245fae72e99
Batch ID: 20250612_155115
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import math

def calculate_service_fee(bitcoin_amount: float, fee_percentage: float) -> float:
    """
    Calculate the service fee for mixing Bitcoin based on the provided fee percentage.
    
    Args:
        bitcoin_amount (float): The amount of Bitcoin to be mixed.
        fee_percentage (float): The fee percentage (1-2%) for the mixing service.
        
    Returns:
        float: The calculated service fee in Bitcoin.
        
    Raises:
        ValueError: If bitcoin_amount is negative or fee_percentage is outside 1-2% range.
    """
    if bitcoin_amount < 0:
        raise ValueError("Bitcoin amount cannot be negative.")
    if fee_percentage < 1 or fee_percentage > 2:
        raise ValueError("Fee percentage must be between 1% and 2%.")
    
    fee = (bitcoin_amount * fee_percentage) / 100
    return round(fee, 8)  # Round to 8 decimal places (standard Bitcoin precision)

def display_upfront_fee(bitcoin_amount: float, fee_percentage: float) -> None:
    """
    Display the upfront fee information before initiating the transaction.
    
    Args:
        bitcoin_amount (float): The amount of Bitcoin to be mixed.
        fee_percentage (float): The fee percentage (1-2%) for the mixing service.
        
    Raises:
        ValueError: If bitcoin_amount is negative or fee_percentage is outside 1-2% range.
    """
    try:
        fee = calculate_service_fee(bitcoin_amount, fee_percentage)
        print("\n--- Upfront Fee Information ---")
        print(f"Bitcoin Amount: {bitcoin_amount:.8f} BTC")
        print(f"Fee Percentage: {fee_percentage}%")
        print(f"Service Fee: {fee:.8f} BTC")
        print(f"Amount After Fee: {(bitcoin_amount - fee):.8f} BTC")
        print("------------------------------\n")
    except ValueError as e:
        print(f"Error: {e}")

# Example usage
if __name__ == "__main__":
    try:
        bitcoin_amount = float(input("Enter Bitcoin amount to mix (BTC): "))
        fee_percentage = float(input("Enter fee percentage (1-2%): "))
        display_upfront_fee(bitcoin_amount, fee_percentage)
    except ValueError:
        print("Error: Invalid input. Please enter numeric values.")
```
