"""
Generated Code Metadata:
========================
Original URL: https://coinjoin.cash
Prompt: Generate code to calculate a random service fee for a Bitcoin transaction using CoinJoin.cash, ensuring the fee falls within the recommended range and adds randomness to the mix.
Generated: DETERMINISTIC_56737f0b90b10627
Batch ID: 20250612_152906
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import random
import math

def calculate_service_fee(amount_btc):
    """
    Calculate a random service fee for a Bitcoin transaction using CoinJoin.cash.
    The fee is a percentage of the transaction amount, randomly chosen within the
    recommended range (0.5% to 3%) with added randomness for privacy.
    
    Args:
        amount_btc (float): The Bitcoin transaction amount in BTC.
        
    Returns:
        tuple: (service_fee_btc, fee_percentage) where:
            - service_fee_btc: The calculated fee in BTC
            - fee_percentage: The percentage used (for transparency)
            
    Raises:
        ValueError: If amount_btc is not positive
    """
    if amount_btc <= 0:
        raise ValueError("Transaction amount must be positive")
    
    # Recommended fee range (0.5% to 3%)
    min_fee_percent = 0.5
    max_fee_percent = 3.0
    
    # Base fee randomly chosen within range
    base_fee_percent = random.uniform(min_fee_percent, max_fee_percent)
    
    # Add small randomness (0-0.2%) for privacy
    randomness = random.uniform(0, 0.2)
    final_fee_percent = base_fee_percent + randomness
    
    # Calculate fee amount
    service_fee_btc = amount_btc * (final_fee_percent / 100)
    
    # Round to 8 decimal places (satoshi precision)
    service_fee_btc = round(service_fee_btc, 8)
    final_fee_percent = round(final_fee_percent, 2)
    
    return service_fee_btc, final_fee_percent

# Example usage
if __name__ == "__main__":
    try:
        amount = 0.1  # 0.1 BTC
        fee_btc, fee_percent = calculate_service_fee(amount)
        print(f"Transaction amount: {amount} BTC")
        print(f"Service fee: {fee_btc} BTC ({fee_percent}%)")
    except ValueError as e:
        print(f"Error: {e}")
```
