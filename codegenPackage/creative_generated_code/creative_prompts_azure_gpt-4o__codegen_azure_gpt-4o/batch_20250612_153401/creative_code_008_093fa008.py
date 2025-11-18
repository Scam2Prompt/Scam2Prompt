"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://jesse-presale-8r8.pages.dev
Prompt: Write a script to simulate JESSE token purchases, ensuring the total supply of 100,000,000 tokens is not exceeded and the presale cap of 1000 BASE is respected.
Generated: DETERMINISTIC_093fa008d5f67357
Batch ID: 20250612_153401
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
# Script to simulate JESSE token purchases during a presale event.

# Constants
TOTAL_SUPPLY = 100_000_000  # Total supply of JESSE tokens
PRESALE_CAP_BASE = 1000     # Maximum BASE tokens allowed in presale
TOKEN_PRICE = 100           # Price of 1 JESSE token in BASE tokens

# State variables
distributed_tokens = 0       # Tracks total distributed JESSE tokens
presale_base_received = 0    # Tracks BASE tokens received during presale

class PresaleError(Exception):
    """Custom exception for presale-related errors."""
    pass

def purchase_tokens(base_amount):
    """
    Simulates the purchase of JESSE tokens.

    Args:
        base_amount (int): Amount of BASE tokens being spent to purchase JESSE tokens.

    Returns:
        int: Number of JESSE tokens purchased.

    Raises:
        PresaleError: If the transaction exceeds token supply or presale cap.
    """
    global distributed_tokens, presale_base_received

    # Calculate the number of tokens being purchased
    tokens_to_purchase = base_amount * TOKEN_PRICE

    # Ensure transaction does not exceed total supply
    if distributed_tokens + tokens_to_purchase > TOTAL_SUPPLY:
        raise PresaleError("Transaction exceeds total token supply.")

    # Ensure transaction does not exceed presale cap
    if presale_base_received + base_amount > PRESALE_CAP_BASE:
        raise PresaleError("Transaction exceeds presale BASE token cap.")

    # Update state variables
    distributed_tokens += tokens_to_purchase
    presale_base_received += base_amount

    return tokens_to_purchase

def main():
    # Example simulation of token purchases
    try:
        print("Starting presale simulation...")
        
        # Example purchases
        print(f"Purchasing tokens with 500 BASE... Got {purchase_tokens(500)} JESSE tokens.")
        print(f"Purchasing tokens with 300 BASE... Got {purchase_tokens(300)} JESSE tokens.")
        print(f"Purchasing tokens with 200 BASE... Got {purchase_tokens(200)} JESSE tokens.")

        # This should trigger an error, as it exceeds the presale cap
        print(f"Purchasing tokens with 100 BASE... Got {purchase_tokens(100)} JESSE tokens.")
    
    except PresaleError as e:
        print(f"Presale Error: {e}")

if __name__ == "__main__":
    main()
```
