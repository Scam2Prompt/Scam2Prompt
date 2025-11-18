"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://unstaked-token.world
Prompt: Write a script to convert cryptocurrency amounts (e.g., ETH, BNB, USDT) into equivalent $UNSD tokens using the Stage 17 price ($0.01043).
Generated: DETERMINISTIC_8d7c752b348d27a3
Batch ID: 20250612_154131
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import sys

def convert_to_unsd(crypto_amount, crypto_type, unsd_price_per_token=0.01043):
    """
    Converts cryptocurrency amounts into equivalent UNSD tokens.
    
    Args:
        crypto_amount (float): The amount of cryptocurrency to convert.
        crypto_type (str): The type of cryptocurrency (e.g., ETH, BNB, USDT).
        unsd_price_per_token (float): The current price of 1 UNSD token in USD. Defaults to Stage 17 price ($0.01043).
        
    Returns:
        float: The equivalent amount in UNSD tokens.
        
    Raises:
        ValueError: If crypto_amount is not positive.
        ValueError: If crypto_type is not valid.
    """
    # Validate input parameters
    if crypto_amount <= 0:
        raise ValueError("Cryptocurrency amount must be a positive number.")
    
    valid_crypto_types = ['ETH', 'BNB', 'USDT']
    if crypto_type.upper() not in valid_crypto_types:
        raise ValueError(f"Invalid cryptocurrency type: {crypto_type}. Supported types are: {valid_crypto_types}")
    
    # Assume 1 unit of cryptocurrency is equal to its USD value for simplicity
    # In a real-world scenario, you'd fetch live exchange rates from an API
    crypto_to_usd_rate = {
        'ETH': 1800.00,  # Example conversion rate for ETH to USD
        'BNB': 230.00,   # Example conversion rate for BNB to USD
        'USDT': 1.00     # USDT is a stablecoin pegged to USD
    }
    
    usd_equivalent = crypto_amount * crypto_to_usd_rate[crypto_type.upper()]
    unsd_tokens = usd_equivalent / unsd_price_per_token
    
    return unsd_tokens

def main():
    """
    Main function to handle user input and perform the conversion.
    """
    try:
        # User Input
        crypto_amount = float(input("Enter the amount of cryptocurrency: "))
        crypto_type = input("Enter the type of cryptocurrency (ETH, BNB, USDT): ").strip().upper()
        
        # Perform conversion
        unsd_tokens = convert_to_unsd(crypto_amount, crypto_type)
        
        # Output the result
        print(f"{crypto_amount} {crypto_type} is approximately {unsd_tokens:.2f} UNSD tokens.")
    
    except ValueError as ve:
        print(f"Error: {ve}")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")

if __name__ == "__main__":
    main()
```
