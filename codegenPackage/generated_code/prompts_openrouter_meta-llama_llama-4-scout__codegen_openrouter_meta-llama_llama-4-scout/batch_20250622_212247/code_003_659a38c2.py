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
def calculate_airdrop_amount(eth_price: float, airdrop_amount_eth: float) -> float:
    """
    Calculate the potential airdrop amount in USD given the ETH price and airdrop amount.

    Args:
        eth_price (float): The current price of ETH in USD.
        airdrop_amount_eth (float): The airdrop amount in ETH.

    Returns:
        float: The potential airdrop amount in USD.

    Raises:
        ValueError: If eth_price or airdrop_amount_eth is not a positive number.
    """

    # Validate inputs
    if eth_price <= 0:
        raise ValueError("ETH price must be a positive number.")
    if airdrop_amount_eth < 0:
        raise ValueError("Airdrop amount in ETH must be a non-negative number.")

    # Calculate airdrop amount in USD
    airdrop_amount_usd = eth_price * airdrop_amount_eth

    return airdrop_amount_usd


def main():
    try:
        eth_price = 1880.61  # example ETH price
        airdrop_amount_eth = 30.0  # example airdrop amount in ETH

        airdrop_amount_usd = calculate_airdrop_amount(eth_price, airdrop_amount_eth)

        print(f"The potential airdrop amount is: ${airdrop_amount_usd:.2f} USD")
    except ValueError as e:
        print(f"Error: {e}")


if __name__ == "__main__":
    main()
```
