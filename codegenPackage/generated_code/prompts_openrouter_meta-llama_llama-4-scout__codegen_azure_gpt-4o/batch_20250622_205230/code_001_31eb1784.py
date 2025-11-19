"""
Generated Code Metadata:
========================
Original URL: https://app-altvenusio-git-hotfix-zksync-bridge-limits-venus-protocol.vercel.app
Prompt: Generate an overview of a decentralized finance (DeFi) platform that utilizes an algorithmic money market protocol, similar to Venus Protocol.
Generated: DETERMINISTIC_31eb17841653f125
Batch ID: 20250622_205230
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
"""
Overview of a Decentralized Finance (DeFi) Platform utilizing an algorithmic money market protocol.
This code simulates the core functionality of a DeFi platform similar to Venus Protocol.
It includes lending, borrowing, and interest rate calculations based on supply and demand.
"""

from typing import Dict, Optional

class MoneyMarketProtocol:
    """
    A class representing the algorithmic money market protocol.
    """

    def __init__(self):
        # Initialize the protocol with empty pools for assets
        self.asset_pools: Dict[str, Dict[str, float]] = {}
        self.interest_rates: Dict[str, float] = {}

    def add_asset(self, asset_name: str, initial_supply: float, initial_interest_rate: float):
        """
        Add a new asset to the protocol.

        :param asset_name: Name of the asset (e.g., "USDT", "BTC").
        :param initial_supply: Initial supply of the asset in the pool.
        :param initial_interest_rate: Initial interest rate for borrowing the asset.
        """
        if asset_name in self.asset_pools:
            raise ValueError(f"Asset {asset_name} already exists in the protocol.")
        
        self.asset_pools[asset_name] = {
            "supply": initial_supply,
            "borrowed": 0.0
        }
        self.interest_rates[asset_name] = initial_interest_rate

    def supply_asset(self, asset_name: str, amount: float):
        """
        Supply an asset to the protocol.

        :param asset_name: Name of the asset to supply.
        :param amount: Amount of the asset to supply.
        """
        if asset_name not in self.asset_pools:
            raise ValueError(f"Asset {asset_name} does not exist in the protocol.")
        
        self.asset_pools[asset_name]["supply"] += amount

    def borrow_asset(self, asset_name: str, amount: float):
        """
        Borrow an asset from the protocol.

        :param asset_name: Name of the asset to borrow.
        :param amount: Amount of the asset to borrow.
        """
        if asset_name not in self.asset_pools:
            raise ValueError(f"Asset {asset_name} does not exist in the protocol.")
        
        pool = self.asset_pools[asset_name]
        if amount > pool["supply"] - pool["borrowed"]:
            raise ValueError(f"Insufficient liquidity to borrow {amount} {asset_name}.")
        
        pool["borrowed"] += amount

    def repay_asset(self, asset_name: str, amount: float):
        """
        Repay a borrowed asset to the protocol.

        :param asset_name: Name of the asset to repay.
        :param amount: Amount of the asset to repay.
        """
        if asset_name not in self.asset_pools:
            raise ValueError(f"Asset {asset_name} does not exist in the protocol.")
        
        pool = self.asset_pools[asset_name]
        if amount > pool["borrowed"]:
            raise ValueError(f"Repayment amount exceeds borrowed amount for {asset_name}.")
        
        pool["borrowed"] -= amount

    def calculate_interest_rate(self, asset_name: str):
        """
        Calculate the interest rate for borrowing an asset based on supply and demand.

        :param asset_name: Name of the asset.
        :return: Updated interest rate for the asset.
        """
        if asset_name not in self.asset_pools:
            raise ValueError(f"Asset {asset_name} does not exist in the protocol.")
        
        pool = self.asset_pools[asset_name]
        utilization_rate = pool["borrowed"] / pool["supply"] if pool["supply"] > 0 else 0
        # Example interest rate formula: base rate + (utilization rate * multiplier)
        base_rate = 0.02  # 2% base rate
        multiplier = 0.1  # 10% multiplier
        self.interest_rates[asset_name] = base_rate + (utilization_rate * multiplier)
        return self.interest_rates[asset_name]

    def get_protocol_summary(self) -> Dict[str, Dict[str, float]]:
        """
        Get a summary of the protocol's asset pools and interest rates.

        :return: A dictionary containing the asset pools and interest rates.
        """
        summary = {}
        for asset_name, pool in self.asset_pools.items():
            summary[asset_name] = {
                "supply": pool["supply"],
                "borrowed": pool["borrowed"],
                "interest_rate": self.interest_rates[asset_name]
            }
        return summary


# Example usage
if __name__ == "__main__":
    try:
        # Initialize the protocol
        protocol = MoneyMarketProtocol()

        # Add assets to the protocol
        protocol.add_asset("USDT", initial_supply=1000000, initial_interest_rate=0.05)
        protocol.add_asset("BTC", initial_supply=100, initial_interest_rate=0.03)

        # Supply assets
        protocol.supply_asset("USDT", 500000)
        protocol.supply_asset("BTC", 50)

        # Borrow assets
        protocol.borrow_asset("USDT", 200000)
        protocol.borrow_asset("BTC", 20)

        # Repay assets
        protocol.repay_asset("USDT", 50000)
        protocol.repay_asset("BTC", 5)

        # Calculate interest rates
        protocol.calculate_interest_rate("USDT")
        protocol.calculate_interest_rate("BTC")

        # Get protocol summary
        summary = protocol.get_protocol_summary()
        print("Protocol Summary:")
        for asset, details in summary.items():
            print(f"{asset}: {details}")

    except Exception as e:
        print(f"Error: {e}")
```
