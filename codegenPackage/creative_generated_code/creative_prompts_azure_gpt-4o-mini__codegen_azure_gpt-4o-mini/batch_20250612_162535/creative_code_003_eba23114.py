"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://slo.finance
Prompt: Create a function that calculates the total value locked (TVL) in Silo Finance based on the provided APRs and total supplies of various markets.
Generated: DETERMINISTIC_eba23114d9362570
Batch ID: 20250612_162535
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
class Market:
    """
    Class representing a financial market with its total supply and APR.
    """
    
    def __init__(self, total_supply: float, apr: float):
        """
        Initializes a Market instance.

        :param total_supply: The total supply of the asset in the market.
        :param apr: The annual percentage rate for the market.
        """
        self.total_supply = total_supply
        self.apr = apr / 100  # Convert APR percentage to decimal

    def calculate_market_value(self) -> float:
        """
        Calculates the market value based on total supply and APR.

        :return: The calculated market value.
        """
        return self.total_supply * (1 + self.apr)


def calculate_tvl(markets: list) -> float:
    """
    Calculates the total value locked (TVL) across multiple markets.

    :param markets: A list of Market instances.
    :return: The total value locked in the markets.
    :raises ValueError: If the input list is empty or contains invalid Market instances.
    """
    if not markets:
        raise ValueError("The markets list cannot be empty.")

    total_tvl = 0.0

    for market in markets:
        if not isinstance(market, Market):
            raise ValueError("All items in the markets list must be instances of the Market class.")
        
        total_tvl += market.calculate_market_value()

    return total_tvl


# Example usage:
if __name__ == "__main__":
    try:
        market1 = Market(total_supply=1000000, apr=5.0)
        market2 = Market(total_supply=2000000, apr=3.5)
        market3 = Market(total_supply=1500000, apr=4.0)

        markets = [market1, market2, market3]
        total_value_locked = calculate_tvl(markets)
        print(f"Total Value Locked (TVL) in Silo Finance: ${total_value_locked:,.2f}")
    except ValueError as e:
        print(f"Error calculating TVL: {e}")
```
