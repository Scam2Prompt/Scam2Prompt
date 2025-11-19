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
    Calculate the number of ALIEN tokens received for a given ETH amount 
    based on the presale rate of 99,500 ALIEN per 0.1 ETH.

    :param eth_amount: float, The amount of ETH being exchanged for ALIEN tokens.
    :return: float, The number of ALIEN tokens received.
    :raises ValueError: If eth_amount is negative or zero.
    """

    # Presale rate constants
    RATE_ETH = 0.1  # Conversion rate basis (ETH)
    RATE_ALIEN = 99500  # Number of ALIEN tokens per 0.1 ETH

    # Validate input
    if eth_amount <= 0:
        raise ValueError("ETH amount must be greater than zero.")

    # Calculate ALIEN tokens
    alien_tokens = (eth_amount / RATE_ETH) * RATE_ALIEN

    return alien_tokens


# Example usage:
if __name__ == "__main__":
    try:
        eth_amount = float(input("Enter ETH amount: "))  # Get user input
        tokens_received = calculate_alien_tokens(eth_amount)
        print(f"You will receive {tokens_received:.2f} ALIEN tokens.")
    except ValueError as ve:
        print(f"Error: {ve}")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")
```
