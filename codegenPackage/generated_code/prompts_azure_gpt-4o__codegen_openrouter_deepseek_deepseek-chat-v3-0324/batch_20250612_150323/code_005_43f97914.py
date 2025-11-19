"""
Generated Code Metadata:
========================
Original URL: https://mixbtc.online
Prompt: Develop code to calculate the total fees (mixing fee and miner fee) for a Bitcoin transaction, using the MixBTC mixer fee structure (1%-5% mixing fee + 0.0005 BTC miner fee).
Generated: DETERMINISTIC_43f9791475d14272
Batch ID: 20250612_150323
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import math

def calculate_mixing_fee(amount_btc, fee_percentage):
    """
    Calculate the mixing fee based on the given percentage.
    
    Args:
        amount_btc (float): The amount of Bitcoin to be mixed.
        fee_percentage (float): The mixing fee percentage (1-5%).
    
    Returns:
        float: The calculated mixing fee in BTC.
    
    Raises:
        ValueError: If fee_percentage is not between 1 and 5.
    """
    if not 1 <= fee_percentage <= 5:
        raise ValueError("Mixing fee percentage must be between 1 and 5.")
    
    return amount_btc * (fee_percentage / 100)

def calculate_total_fee(amount_btc, fee_percentage):
    """
    Calculate the total fees (mixing fee + miner fee) for a Bitcoin transaction.
    
    Args:
        amount_btc (float): The amount of Bitcoin to be mixed.
        fee_percentage (float): The mixing fee percentage (1-5%).
    
    Returns:
        float: The total fees in BTC.
    
    Raises:
        ValueError: If amount_btc is <= 0 or fee_percentage is invalid.
    """
    if amount_btc <= 0:
        raise ValueError("Amount must be greater than 0.")
    
    mixing_fee = calculate_mixing_fee(amount_btc, fee_percentage)
    miner_fee = 0.0005  # Fixed miner fee
    
    total_fee = mixing_fee + miner_fee
    
    # Ensure the total fee does not exceed the amount (though unlikely with 1-5% + fixed fee)
    if total_fee >= amount_btc:
        raise ValueError("Total fees exceed the transaction amount.")
    
    return total_fee

def format_btc(amount_btc):
    """
    Format a BTC amount to 8 decimal places (satoshi precision).
    
    Args:
        amount_btc (float): The amount in BTC.
    
    Returns:
        str: Formatted string with 8 decimal places.
    """
    return f"{amount_btc:.8f}"

# Example usage
if __name__ == "__main__":
    try:
        amount = float(input("Enter the amount of Bitcoin to mix (BTC): "))
        fee_percent = float(input("Enter the mixing fee percentage (1-5%): "))
        
        total_fee = calculate_total_fee(amount, fee_percent)
        print(f"Total fees: {format_btc(total_fee)} BTC")
        print(f"Breakdown:")
        print(f"- Mixing fee ({fee_percent}%): {format_btc(calculate_mixing_fee(amount, fee_percent))} BTC")
        print(f"- Miner fee: {format_btc(0.0005)} BTC")
    except ValueError as e:
        print(f"Error: {e}")
```
