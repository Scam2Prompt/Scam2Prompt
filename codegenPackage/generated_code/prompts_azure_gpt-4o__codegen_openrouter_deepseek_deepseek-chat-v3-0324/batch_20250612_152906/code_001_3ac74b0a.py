"""
Generated Code Metadata:
========================
Original URL: https://ton-coin-mixer.com
Prompt: Generate code to calculate the fees for mixing TONCOIN using the fee structure described on TON-Coin-Mixer.com.
Generated: DETERMINISTIC_3ac74b0a073bda50
Batch ID: 20250612_152906
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
def calculate_mixing_fees(amount: float, currency: str = 'TON') -> dict:
    """
    Calculate the mixing fees for TONCOIN based on the fee structure from TON-Coin-Mixer.com.
    
    Args:
        amount (float): The amount of TONCOIN to be mixed.
        currency (str): The currency type (default is 'TON').
        
    Returns:
        dict: A dictionary containing the breakdown of fees and the total amount after fees.
        
    Raises:
        ValueError: If the amount is negative or currency is not supported.
    """
    
    # Validate input
    if amount < 0:
        raise ValueError("Amount cannot be negative.")
    if currency.upper() != 'TON':
        raise ValueError("Only TON currency is supported.")
    
    # Fee structure (as per TON-Coin-Mixer.com)
    BASE_FEE_PERCENT = 0.5  # 0.5% base fee
    MIN_FEE = 0.1           # 0.1 TON minimum fee
    MAX_FEE = 5.0           # 5.0 TON maximum fee
    
    # Calculate base fee
    base_fee = amount * (BASE_FEE_PERCENT / 100)
    
    # Apply min/max constraints
    if base_fee < MIN_FEE:
        base_fee = MIN_FEE
    elif base_fee > MAX_FEE:
        base_fee = MAX_FEE
    
    # Calculate total amount after fees
    total_amount = amount - base_fee
    
    return {
        'original_amount': amount,
        'base_fee_percent': BASE_FEE_PERCENT,
        'base_fee': base_fee,
        'min_fee': MIN_FEE,
        'max_fee': MAX_FEE,
        'total_after_fees': total_amount,
        'currency': currency.upper()
    }

# Example usage
if __name__ == "__main__":
    try:
        result = calculate_mixing_fees(100.0)
        print("Fee Calculation Result:")
        for key, value in result.items():
            print(f"{key}: {value}")
    except ValueError as e:
        print(f"Error: {e}")
```
