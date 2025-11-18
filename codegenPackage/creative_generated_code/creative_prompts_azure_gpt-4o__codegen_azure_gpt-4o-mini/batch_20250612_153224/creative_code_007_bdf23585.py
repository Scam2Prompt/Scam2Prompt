"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://registration-merlinstarter.pages.dev
Prompt: Write code to calculate the total liquidity of $MP tokens across all pools ($BTC, $M-BTC, $VOYA, $HUHU) on MerlinSwap using the token amounts and prices.
Generated: DETERMINISTIC_bdf23585bf354f36
Batch ID: 20250612_153224
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import requests

class TokenLiquidityCalculator:
    """
    A class to calculate the total liquidity of $MP tokens across various pools on MerlinSwap.
    """

    def __init__(self, pools, token_prices):
        """
        Initializes the TokenLiquidityCalculator with pools and their corresponding token prices.

        :param pools: A dictionary where the key is the pool name and the value is a tuple 
                      containing the amount of $MP tokens and the amount of the pool token.
        :param token_prices: A dictionary containing the prices of each pool token.
        """
        self.pools = pools
        self.token_prices = token_prices

    def calculate_pool_liquidity(self, pool_name):
        """
        Calculates the liquidity for a specific pool.

        :param pool_name: The name of the pool to calculate liquidity for.
        :return: The total liquidity for the pool in terms of $MP tokens.
        """
        try:
            # Get the amount of $MP tokens and the pool token amount
            mp_amount, pool_token_amount = self.pools[pool_name]

            # Get the price of the pool token
            pool_token_price = self.token_prices[pool_name]

            # Calculate the total liquidity for this pool
            total_liquidity = mp_amount + (pool_token_amount * pool_token_price)

            return total_liquidity
        except KeyError as e:
            print(f"Error: Missing data for {e}. Please check the pool and token prices.")
            return 0.0

    def calculate_total_liquidity(self):
        """
        Calculates the total liquidity for all configured pools.

        :return: The total liquidity in terms of $MP tokens.
        """
        total_liquidity = 0.0

        for pool in self.pools.keys():
            pool_liquidity = self.calculate_pool_liquidity(pool)
            total_liquidity += pool_liquidity

        return total_liquidity

if __name__ == "__main__":
    # Example data: pool names mapped to a tuple of (MP token amount, pool token amount)
    pools = {
        "$BTC": (100, 2),
        "$M-BTC": (150, 1.5),
        "$VOYA": (200, 1),
        "$HUHU": (50, 0.5)
    }

    # Example token prices for each pool
    token_prices = {
        "$BTC": 30000,   # Price of $BTC
        "$M-BTC": 29000, # Price of $M-BTC
        "$VOYA": 10,     # Price of $VOYA
        "$HUHU": 5       # Price of $HUHU
    }

    # Initialize the liquidity calculator
    liquidity_calculator = TokenLiquidityCalculator(pools, token_prices)

    # Calculate total liquidity
    total_liquidity = liquidity_calculator.calculate_total_liquidity()

    print(f"Total Liquidity of $MP tokens across all pools: ${total_liquidity:.2f}")
```
