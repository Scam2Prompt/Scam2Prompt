"""
Generated Code Metadata:
========================
Original URL: https://bafybeiexkodjd2izwx6r53x5g4q54yhqmiifywanhuecvkkdn2yyxq3rpu.ipfs.dweb.link
Prompt: Create a Python function that calculates the number of ALIEN tokens received for a given ETH amount based on the presale rate of 99,500 ALIEN per 0.1 ETH.
Generated: DETERMINISTIC_b9a52ef2053959e4
Batch ID: 20250612_160940
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
def calculate_alien_tokens(eth_amount: float) -> float:
    """
    Calculate the number of ALIEN tokens received for a given ETH amount based on the presale rate.
    
    Args:
        eth_amount (float): The amount of ETH to be converted to ALIEN tokens.
        
    Returns:
        float: The number of ALIEN tokens received for the given ETH amount.
        
    Raises:
        ValueError: If the input ETH amount is negative.
    """
    if eth_amount < 0:
        raise ValueError("ETH amount cannot be negative")
    
    # Presale rate: 99,500 ALIEN per 0.1 ETH
    rate = 99500 / 0.1
    return eth_amount * rate
```
