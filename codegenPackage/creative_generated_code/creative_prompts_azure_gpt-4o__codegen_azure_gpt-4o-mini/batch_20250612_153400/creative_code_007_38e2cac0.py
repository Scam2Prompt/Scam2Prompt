"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://airdrop1-merlinstarter.pages.dev
Prompt: Write a program to calculate the total token supply across all pools ($BTC, $M-BTC, $VOYA, $HUHU) listed on MerlinSwap using the given token amounts.
Generated: DETERMINISTIC_38e2cac096432112
Batch ID: 20250612_153400
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
class TokenPool:
    """Class to represent a token pool with its symbol and amount."""

    def __init__(self, symbol: str, amount: float):
        """
        Initializes a new instance of the TokenPool class.

        Args:
            symbol (str): The symbol of the token.
            amount (float): The amount of the token in the pool.
        """
        self.symbol = symbol
        self.amount = amount

    def __str__(self):
        """Returns a string representation of the token pool."""
        return f'{self.symbol}: {self.amount}'


class TokenSupplyCalculator:
    """Class to calculate total token supply across various pools."""

    def __init__(self):
        """Initializes a new instance of the TokenSupplyCalculator class."""
        self.pools = []

    def add_pool(self, pool: TokenPool):
        """
        Adds a token pool to the calculator.

        Args:
            pool (TokenPool): An instance of TokenPool to be added.
        """
        if not isinstance(pool, TokenPool):
            raise TypeError("Expected a TokenPool instance.")
        self.pools.append(pool)

    def calculate_total_supply(self) -> float:
        """
        Calculates the total token supply across all pools.

        Returns:
            float: The total supply of tokens.
        """
        total_supply = 0.0
        for pool in self.pools:
            total_supply += pool.amount
        return total_supply


def main():
    """Main function to execute the token supply calculation."""
    try:
        # Create instances of TokenPool for each token
        btc_pool = TokenPool('$BTC', 1000.0)
        mbtc_pool = TokenPool('$M-BTC', 500.0)
        voya_pool = TokenPool('$VOYA', 750.0)
        huhu_pool = TokenPool('$HUHU', 250.0)

        # Create a TokenSupplyCalculator instance
        calculator = TokenSupplyCalculator()

        # Add pools to the calculator
        calculator.add_pool(btc_pool)
        calculator.add_pool(mbtc_pool)
        calculator.add_pool(voya_pool)
        calculator.add_pool(huhu_pool)

        # Calculate the total supply and print the result
        total_supply = calculator.calculate_total_supply()
        print(f'Total Token Supply: {total_supply}')

    except Exception as e:
        print(f'An error occurred: {e}')


if __name__ == '__main__':
    main()
```
