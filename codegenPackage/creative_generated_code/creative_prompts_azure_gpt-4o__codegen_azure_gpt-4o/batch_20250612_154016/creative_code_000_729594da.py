"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://fun-virtuals-agent.pages.dev
Prompt: Write code to simulate a bonding curve for purchasing coins, as described on the Fun Virtuals Agent platform. Include steps for calculating market cap and liquidity deposit.
Generated: DETERMINISTIC_729594da4c58e088
Batch ID: 20250612_154016
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import math

class BondingCurve:
    """
    A class to simulate a bonding curve for purchasing coins.
    It calculates the coin price, market cap, and liquidity deposit.
    """

    def __init__(self, reserve_ratio: float, initial_supply: float, initial_liquidity: float):
        """
        Initialize the bonding curve with a reserve ratio, initial supply, and liquidity.

        :param reserve_ratio: The ratio of reserve to market cap. (0 < reserve_ratio < 1)
        :param initial_supply: Initial supply of coins (in units).
        :param initial_liquidity: Initial liquidity deposit (in currency units).
        """
        if not (0 < reserve_ratio < 1):
            raise ValueError("Reserve ratio must be between 0 and 1.")
        if initial_supply <= 0 or initial_liquidity <= 0:
            raise ValueError("Initial supply and liquidity must be greater than zero.")

        self.reserve_ratio = reserve_ratio
        self.supply = initial_supply
        self.liquidity = initial_liquidity

    def _calculate_price(self, supply: float) -> float:
        """
        Private method to calculate the price per coin.

        :param supply: Current supply of coins (units).
        :return: Price per coin (currency/unit).
        """
        return self.liquidity / (supply ** (1 / self.reserve_ratio))

    def purchase(self, investment: float) -> float:
        """
        Simulate purchasing coins by investing a certain amount.

        :param investment: Amount of currency to invest.
        :return: Number of coins purchased.
        """
        if investment <= 0:
            raise ValueError("Investment must be greater than zero.")

        new_liquidity = self.liquidity + investment
        new_supply = (new_liquidity * (self.reserve_ratio)) ** self.reserve_ratio
        coins_purchased = new_supply - self.supply

        # Update state of the curve after purchase
        self.liquidity = new_liquidity
        self.supply = new_supply

        return coins_purchased

    def calculate_market_cap(self) -> float:
        """
        Calculate the current market cap.

        :return: Market cap (currency units).
        """
        return self.supply * self._calculate_price(self.supply)

    def get_liquidity_deposit(self) -> float:
        """
        Get the current liquidity deposit.

        :return: Liquidity deposit (currency units).
        """
        return self.liquidity


# Example usage
if __name__ == "__main__":
    try:
        # Initialize the bonding curve with a reserve ratio of 0.5, initial supply of 1000, and liquidity of 5000
        curve = BondingCurve(reserve_ratio=0.5, initial_supply=1000, initial_liquidity=5000)

        # Simulate purchasing coins with an investment of 1000 currency units
        coins_purchased = curve.purchase(investment=1000)
        print(f"Coins purchased: {coins_purchased}")

        # Calculate market cap
        market_cap = curve.calculate_market_cap()
        print(f"Market Cap: {market_cap}")

        # Get liquidity deposit
        liquidity = curve.get_liquidity_deposit()
        print(f"Liquidity Deposit: {liquidity}")

    except Exception as e:
        print(f"Error: {str(e)}")
```
