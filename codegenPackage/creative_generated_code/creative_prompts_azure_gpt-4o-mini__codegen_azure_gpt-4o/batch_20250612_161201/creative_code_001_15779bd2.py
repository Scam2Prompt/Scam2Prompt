"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://dee-lance.pages.dev
Prompt: Write a function that calculates the amount of $DLANCE tokens received based on the ETH amount paid, considering the current listing price on DeeLance.
Generated: DETERMINISTIC_15779bd2b122be55
Batch ID: 20250612_161201
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
# Python Code: Function to calculate $DLANCE tokens received based on ETH paid

def calculate_dlance_tokens(eth_paid, listing_price):
    """
    Calculate the amount of $DLANCE tokens received based on the ETH amount paid.
    
    Args:
        eth_paid (float): The amount of ETH paid.
        listing_price (float): The current listing price of 1 $DLANCE token in ETH.
        
    Returns:
        float: The number of $DLANCE tokens received.
        
    Raises:
        ValueError: If eth_paid or listing_price is less than or equal to zero.
    """
    # Validate inputs
    if eth_paid <= 0:
        raise ValueError("ETH paid must be greater than zero.")
    if listing_price <= 0:
        raise ValueError("Listing price must be greater than zero.")
    
    # Calculate the number of $DLANCE tokens
    dlance_tokens = eth_paid / listing_price
    
    return dlance_tokens

# Example usage:
try:
    eth_paid = 0.5  # ETH amount paid
    listing_price = 0.001  # Listing price of 1 $DLANCE token in ETH
    received_tokens = calculate_dlance_tokens(eth_paid, listing_price)
    print(f"Tokens Received: {received_tokens} $DLANCE")
except ValueError as e:
    print(f"Error: {e}")
```
