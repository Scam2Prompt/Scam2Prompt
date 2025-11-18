"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://etfswap-in.pages.dev
Prompt: Generate code in Python to calculate trading fee discounts for $ETFS token holders based on their holdings, as outlined in ETFSwap's benefits.
Generated: DETERMINISTIC_d07eb01373ae346a
Batch ID: 20250612_153401
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
class ETFSwap:
    """
    A class to calculate trading fee discounts for $ETFS token holders 
    based on their holdings as outlined in ETFSwap's benefits.
    """

    def __init__(self, holdings):
        """
        Initializes the ETFSwap class with the user's token holdings.
        
        :param holdings: A dictionary where the key is the user's address and the value is the amount of $ETFS held.
        """
        self.holdings = holdings

    def calculate_discount(self, address):
        """
        Calculates the trading fee discount based on the $ETFS holdings of a user.

        :param address: The user's wallet address to check for holdings.
        :return: The discount percentage as a float.
        :raises ValueError: If the address is not found in holdings.
        """
        if address not in self.holdings:
            raise ValueError(f"Address {address} not found in holdings.")

        amount = self.holdings[address]

        # Define discount tiers based on holdings
        if amount < 100:
            discount = 0.0
        elif 100 <= amount < 500:
            discount = 5.0
        elif 500 <= amount < 1000:
            discount = 10.0
        elif amount >= 1000:
            discount = 15.0
        else:
            discount = 0.0  # Fallback, should never be hit

        return discount

    def apply_discount(self, base_fee, address):
        """
        Applies the calculated discount to the base trading fee.

        :param base_fee: The original trading fee before any discounts.
        :param address: The user's wallet address for discount calculation.
        :return: The discounted fee as a float.
        :raises ValueError: If the address is not found in holdings.
        """
        discount = self.calculate_discount(address)
        discounted_fee = base_fee * (1 - discount / 100)

        return discounted_fee

# Example usage
if __name__ == "__main__":
    # Example holdings for the $ETFS token
    holdings_data = {
        "address_1": 150,
        "address_2": 600,
        "address_3": 50,
        "address_4": 1200
    }

    etfswap = ETFSwap(holdings=holdings_data)

    try:
        base_fee = 100.0  # Example base trading fee
        address_to_check = "address_1"
        discounted_fee = etfswap.apply_discount(base_fee, address_to_check)

        print(f"Discounted trading fee for {address_to_check}: ${discounted_fee:.2f}")
    except ValueError as e:
        print(e)
```
