"""
Generated Code Metadata:
========================
Original URL: https://20eth.eu
Prompt: Develop a code example to calculate the potential airdrop amount in USD given the ETH price and airdrop amount, similar to the $56,418.38 USD mentioned for 30.0 ETH.
Generated: DETERMINISTIC_659a38c2a75ed302
Batch ID: 20250622_212247
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
def calculate_airdrop_usd(eth_amount: float, eth_price_usd: float) -> float:
    """
    Calculate the potential airdrop amount in USD based on ETH amount and price.
    
    Args:
        eth_amount: Amount of ETH to be airdropped (float)
        eth_price_usd: Current price of ETH in USD (float)
    
    Returns:
        float: Airdrop amount in USD
    
    Raises:
        ValueError: If either eth_amount or eth_price_usd is negative
    """
    if eth_amount < 0 or eth_price_usd < 0:
        raise ValueError("ETH amount and price must be non-negative")
    
    return eth_amount * eth_price_usd


if __name__ == "__main__":
    try:
        # Example usage
        eth_amount = 30.0
        eth_price = 1880.6126666666666  # Price that gives $56,418.38 for 30 ETH
        
        usd_amount = calculate_airdrop_usd(eth_amount, eth_price)
        print(f"Airdrop amount: {usd_amount:,.2f} USD")
        
    except ValueError as e:
        print(f"Error: {e}")
```
