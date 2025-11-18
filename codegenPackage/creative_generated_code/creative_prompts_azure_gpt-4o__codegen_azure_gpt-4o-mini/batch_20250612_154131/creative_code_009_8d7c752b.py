"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://unstaked-token.world
Prompt: Write a script to convert cryptocurrency amounts (e.g., ETH, BNB, USDT) into equivalent $UNSD tokens using the Stage 17 price ($0.01043).
Generated: DETERMINISTIC_8d7c752b348d27a3
Batch ID: 20250612_154131
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
# cryptocurrency_to_unsd_converter.py

class CryptocurrencyConverter:
    """
    A class to convert various cryptocurrencies to $UNSD tokens based on a fixed price.
    """

    def __init__(self, unsd_price: float):
        """
        Initializes the converter with the given price of $UNSD.

        Args:
            unsd_price (float): The price of one $UNSD token.
        """
        if unsd_price <= 0:
            raise ValueError("The price of $UNSD must be greater than zero.")
        self.unsd_price = unsd_price

    def convert_to_unsd(self, crypto_amount: float, crypto_to_usd_price: float) -> float:
        """
        Converts a given cryptocurrency amount to equivalent $UNSD tokens.

        Args:
            crypto_amount (float): The amount of cryptocurrency to convert.
            crypto_to_usd_price (float): The price of the cryptocurrency in USD.

        Returns:
            float: The equivalent amount of $UNSD tokens.

        Raises:
            ValueError: If the cryptocurrency amount or the price is negative.
        """
        if crypto_amount < 0:
            raise ValueError("Cryptocurrency amount cannot be negative.")
        if crypto_to_usd_price <= 0:
            raise ValueError("Cryptocurrency price must be greater than zero.")
        
        # Calculate the equivalent USD amount
        usd_amount = crypto_amount * crypto_to_usd_price
        
        # Calculate and return the equivalent $UNSD tokens
        unsd_tokens = usd_amount / self.unsd_price
        return unsd_tokens


def main():
    # Price of $UNSD
    unsd_price = 0.01043
    
    # Instantiate the converter
    converter = CryptocurrencyConverter(unsd_price)

    try:
        # Example conversion amounts and prices
        eth_amount = 1.0  # 1 ETH
        eth_to_usd_price = 2000.0  # Price of ETH in USD
        
        # Convert ETH to $UNSD
        unsd_from_eth = converter.convert_to_unsd(eth_amount, eth_to_usd_price)
        print(f"{eth_amount} ETH is equivalent to {unsd_from_eth:.2f} $UNSD tokens.")

        bnb_amount = 2.0  # 2 BNB
        bnb_to_usd_price = 300.0  # Price of BNB in USD
        
        # Convert BNB to $UNSD
        unsd_from_bnb = converter.convert_to_unsd(bnb_amount, bnb_to_usd_price)
        print(f"{bnb_amount} BNB is equivalent to {unsd_from_bnb:.2f} $UNSD tokens.")

        usdt_amount = 50.0  # 50 USDT
        usdt_to_usd_price = 1.0  # Price of USDT in USD
        
        # Convert USDT to $UNSD
        unsd_from_usdt = converter.convert_to_unsd(usdt_amount, usdt_to_usd_price)
        print(f"{usdt_amount} USDT is equivalent to {unsd_from_usdt:.2f} $UNSD tokens.")
    
    except ValueError as e:
        print(f"Error: {e}")


if __name__ == "__main__":
    main()
```
