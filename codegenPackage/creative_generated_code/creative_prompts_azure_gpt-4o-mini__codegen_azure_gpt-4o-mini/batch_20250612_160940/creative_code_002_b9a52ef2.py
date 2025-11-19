"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://bafybeiexkodjd2izwx6r53x5g4q54yhqmiifywanhuecvkkdn2yyxq3rpu.ipfs.dweb.link
Prompt: Create a Python function that calculates the number of ALIEN tokens received for a given ETH amount based on the presale rate of 99,500 ALIEN per 0.1 ETH.
Generated: DETERMINISTIC_b9a52ef2053959e4
Batch ID: 20250612_160940
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
def calculate_alien_tokens(eth_amount):
    """
    Calculate the number of ALIEN tokens received for a given ETH amount based on the presale rate.

    Presale rate is fixed at 99,500 ALIEN per 0.1 ETH.

    Parameters:
    eth_amount (float): The amount of ETH to convert to ALIEN tokens.

    Returns:
    int: The number of ALIEN tokens received.

    Raises:
    ValueError: If the eth_amount is negative or not a number.
    """
    # Validate input
    if not isinstance(eth_amount, (int, float)):
        raise ValueError("ETH amount must be a number.")
    if eth_amount < 0:
        raise ValueError("ETH amount cannot be negative.")

    # Constants
    ALIEN_PER_0_1_ETH = 99500  # ALIEN tokens for 0.1 ETH
    ETH_CONVERSION_FACTOR = 0.1  # Conversion factor for ETH to the rate

    # Calculate ALIEN tokens
    tokens_received = (eth_amount / ETH_CONVERSION_FACTOR) * ALIEN_PER_0_1_ETH

    # Return the calculated number of tokens as an integer
    return int(tokens_received)

# Example usage (uncomment to run)
# try:
#     eth_amount = 0.5  # Example ETH amount
#     alien_tokens = calculate_alien_tokens(eth_amount)
#     print(f"Tokens received for {eth_amount} ETH: {alien_tokens} ALIEN")
# except ValueError as e:
#     print(f"Error: {e}")
```
