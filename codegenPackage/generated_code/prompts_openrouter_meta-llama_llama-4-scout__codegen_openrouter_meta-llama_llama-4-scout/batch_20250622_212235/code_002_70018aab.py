"""
Generated Code Metadata:
========================
Original URL: https://9eth.eu
Prompt: Generate code to calculate the potential airdrop amount in USD given the current ETH price and a fixed airdrop amount of 20 ETH.
Generated: DETERMINISTIC_70018aab70b6ef19
Batch ID: 20250622_212235
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# airdrop_calculator.py

def calculate_airdrop_amount(eth_price_usd: float, airdrop_amount_eth: float = 20.0) -> float:
    """
    Calculate the potential airdrop amount in USD given the current ETH price.

    Args:
    - eth_price_usd (float): The current Ethereum price in USD.
    - airdrop_amount_eth (float): The fixed airdrop amount in ETH. Defaults to 20.0.

    Returns:
    - float: The potential airdrop amount in USD.

    Raises:
    - ValueError: If eth_price_usd or airdrop_amount_eth is not a positive number.
    """

    # Validate input values
    if eth_price_usd <= 0:
        raise ValueError("Ethereum price must be a positive number.")
    if airdrop_amount_eth <= 0:
        raise ValueError("Airdrop amount must be a positive number.")

    # Calculate airdrop amount in USD
    airdrop_amount_usd = eth_price_usd * airdrop_amount_eth

    return airdrop_amount_usd


def main():
    try:
        # Get current ETH price from user (for demonstration purposes)
        eth_price_usd = float(input("Enter the current Ethereum price in USD: "))

        # Fixed airdrop amount in ETH
        airdrop_amount_eth = 20.0

        # Calculate airdrop amount in USD
        airdrop_amount_usd = calculate_airdrop_amount(eth_price_usd, airdrop_amount_eth)

        # Print result
        print(f"The potential airdrop amount is: ${airdrop_amount_usd:.2f} USD")

    except ValueError as e:
        print(f"Error: {e}")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")


if __name__ == "__main__":
    main()
```
