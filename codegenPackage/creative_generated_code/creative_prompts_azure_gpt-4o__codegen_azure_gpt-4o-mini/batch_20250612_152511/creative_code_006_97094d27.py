"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://portal-coln.pages.dev
Prompt: Using the $PORTAL token pre-sale details, write a Python script to calculate the number of tokens a user would receive for purchasing 3 ETH at the rate of 1 ETH = 19,000 $PORTAL.
Generated: DETERMINISTIC_97094d27cf9a987e
Batch ID: 20250612_152511
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
# portal_token_calculator.py

def calculate_tokens(purchase_amount_eth, eth_to_portal_rate):
    """
    Calculate the number of $PORTAL tokens received for a given amount of ETH.

    Parameters:
    purchase_amount_eth (float): The amount of ETH to be used for purchasing tokens.
    eth_to_portal_rate (float): The conversion rate from ETH to $PORTAL tokens.

    Returns:
    float: The number of $PORTAL tokens received.
    """
    if purchase_amount_eth < 0:
        raise ValueError("Purchase amount cannot be negative.")
    if eth_to_portal_rate <= 0:
        raise ValueError("ETH to $PORTAL rate must be greater than zero.")

    # Calculate the number of $PORTAL tokens
    portal_tokens = purchase_amount_eth * eth_to_portal_rate
    return portal_tokens

def main():
    """
    Main function to execute the token calculation for a purchase of 3 ETH.
    """
    # User input for the ETH amount and the conversion rate
    purchase_amount_eth = 3  # Amount of ETH to purchase
    eth_to_portal_rate = 19000  # Conversion rate: 1 ETH = 19,000 $PORTAL

    try:
        # Calculate the tokens
        tokens_received = calculate_tokens(purchase_amount_eth, eth_to_portal_rate)
        print(f"For purchasing {purchase_amount_eth} ETH, you will receive {tokens_received} $PORTAL tokens.")
    except ValueError as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    main()
```
