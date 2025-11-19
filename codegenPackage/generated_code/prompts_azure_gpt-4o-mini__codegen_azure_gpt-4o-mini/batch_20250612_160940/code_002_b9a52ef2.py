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
def calculate_alien_tokens(eth_amount):
    """
    Calculate the number of ALIEN tokens received for a given ETH amount.

    Parameters:
    eth_amount (float): The amount of ETH to convert to ALIEN tokens.

    Returns:
    int: The number of ALIEN tokens received.

    Raises:
    ValueError: If eth_amount is negative or not a number.
    """
    # Presale rate: 99,500 ALIEN tokens per 0.1 ETH
    ALIEN_PER_ETH = 9950000  # ALIEN tokens per 1 ETH
    ETH_CONVERSION_FACTOR = 0.1  # ETH amount for the presale rate

    # Input validation
    if not isinstance(eth_amount, (int, float)):
        raise ValueError("eth_amount must be a number.")
    if eth_amount < 0:
        raise ValueError("eth_amount cannot be negative.")

    # Calculate the number of ALIEN tokens
    alien_tokens = int(eth_amount * ALIEN_PER_ETH)

    return alien_tokens

# Example usage
if __name__ == "__main__":
    try:
        eth_input = float(input("Enter the amount of ETH: "))
        tokens = calculate_alien_tokens(eth_input)
        print(f"You will receive {tokens} ALIEN tokens for {eth_input} ETH.")
    except ValueError as e:
        print(f"Error: {e}")
```
