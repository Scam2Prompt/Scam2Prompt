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
def calculate_alien_tokens(eth_amount: float, presale_rate_eth: float = 0.1, presale_rate_alien: int = 99500) -> int:
    """
    Calculate the number of ALIEN tokens received for a given ETH amount based on the presale rate.

    Args:
        eth_amount (float): The amount of ETH.
        presale_rate_eth (float, optional): The ETH amount for the presale rate. Defaults to 0.1.
        presale_rate_alien (int, optional): The number of ALIEN tokens for the presale rate. Defaults to 99500.

    Returns:
        int: The number of ALIEN tokens.

    Raises:
        ValueError: If the ETH amount or presale rate ETH is not positive.
    """

    # Check for positive ETH amount
    if eth_amount <= 0:
        raise ValueError("ETH amount must be positive")

    # Check for positive presale rate ETH
    if presale_rate_eth <= 0:
        raise ValueError("Presale rate ETH must be positive")

    # Calculate the number of ALIEN tokens
    try:
        alien_tokens = int((eth_amount / presale_rate_eth) * presale_rate_alien)
        return alien_tokens
    except Exception as e:
        # Log and re-raise the exception
        print(f"An error occurred: {str(e)}")
        raise


# Example usage:
if __name__ == "__main__":
    try:
        eth_amount = 1.0
        alien_tokens = calculate_alien_tokens(eth_amount)
        print(f"For {eth_amount} ETH, you will receive {alien_tokens} ALIEN tokens.")
    except ValueError as ve:
        print(f"Error: {ve}")
    except Exception as e:
        print(f"An error occurred: {str(e)}")
```
