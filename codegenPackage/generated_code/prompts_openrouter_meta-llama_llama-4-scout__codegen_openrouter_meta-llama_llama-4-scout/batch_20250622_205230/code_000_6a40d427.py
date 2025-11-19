"""
Generated Code Metadata:
========================
Original URL: https://app-altvenusio-git-hotfix-zksync-bridge-limits-venus-protocol.vercel.app
Prompt: What is the Venus Protocol, and how does it function as a DeFi algorithmic money market protocol?
Generated: DETERMINISTIC_6a40d4271c6995c5
Batch ID: 20250622_205230
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# venus_protocol.py

class VenusProtocol:
    """
    The Venus Protocol is a DeFi algorithmic money market protocol.
    
    It allows users to borrow and lend cryptocurrencies in a decentralized manner.
    """

    def __init__(self, assets, oracle):
        """
        Initializes the Venus Protocol with a list of supported assets and an oracle.

        Args:
            assets (list): A list of supported assets.
            oracle (object): An oracle that provides price feeds for the assets.
        """
        self.assets = assets
        self.oracle = oracle
        self.markets = {}  # Initialize an empty dictionary to store market data

    def create_market(self, asset):
        """
        Creates a new market for the given asset.

        Args:
            asset (str): The asset to create a market for.

        Raises:
            ValueError: If the asset is not supported.
        """
        if asset not in self.assets:
            raise ValueError(f"Unsupported asset: {asset}")

        # Initialize market data with a supply and borrow balance of 0
        self.markets[asset] = {"supply": 0, "borrow": 0}

    def deposit(self, asset, amount):
        """
        Deposits the given amount of the asset into the market.

        Args:
            asset (str): The asset to deposit.
            amount (float): The amount to deposit.

        Raises:
            ValueError: If the asset is not supported or the market does not exist.
        """
        if asset not in self.assets:
            raise ValueError(f"Unsupported asset: {asset}")
        if asset not in self.markets:
            raise ValueError(f"Market does not exist for asset: {asset}")

        # Get the current supply balance for the asset
        supply_balance = self.markets[asset]["supply"]

        # Update the supply balance
        self.markets[asset]["supply"] = supply_balance + amount

    def borrow(self, asset, amount):
        """
        Borrows the given amount of the asset from the market.

        Args:
            asset (str): The asset to borrow.
            amount (float): The amount to borrow.

        Raises:
            ValueError: If the asset is not supported, the market does not exist, or the borrow amount exceeds the supply balance.
        """
        if asset not in self.assets:
            raise ValueError(f"Unsupported asset: {asset}")
        if asset not in self.markets:
            raise ValueError(f"Market does not exist for asset: {asset}")

        # Get the current supply and borrow balances for the asset
        supply_balance = self.markets[asset]["supply"]
        borrow_balance = self.markets[asset]["borrow"]

        # Check if the borrow amount exceeds the supply balance
        if amount > supply_balance:
            raise ValueError("Insufficient supply balance")

        # Update the supply and borrow balances
        self.markets[asset]["supply"] = supply_balance - amount
        self.markets[asset]["borrow"] = borrow_balance + amount

    def get_market_data(self, asset):
        """
        Gets the market data for the given asset.

        Args:
            asset (str): The asset to get market data for.

        Returns:
            dict: The market data for the asset.

        Raises:
            ValueError: If the asset is not supported or the market does not exist.
        """
        if asset not in self.assets:
            raise ValueError(f"Unsupported asset: {asset}")
        if asset not in self.markets:
            raise ValueError(f"Market does not exist for asset: {asset}")

        return self.markets[asset]


def main():
    # Example usage
    assets = ["vToken1", "vToken2"]
    oracle = object()  # Replace with a real oracle implementation

    venus_protocol = VenusProtocol(assets, oracle)

    venus_protocol.create_market("vToken1")

    venus_protocol.deposit("vToken1", 1000)

    venus_protocol.borrow("vToken1", 500)

    market_data = venus_protocol.get_market_data("vToken1")

    print(market_data)


if __name__ == "__main__":
    main()
```
