"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://thorchain-cu5.pages.dev
Prompt: How does THORChain ensure low-risk liquidity for Savers, and what mechanisms are in place to prevent impermanent loss?
Generated: DETERMINISTIC_cba688e136666d7d
Batch ID: 20250612_161353
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
class THORChainLiquidity:
    """
    A class to represent the liquidity mechanisms of THORChain,
    particularly how it ensures low-risk liquidity for Savers and 
    prevents impermanent loss.
    """

    def __init__(self):
        """
        Initializes the THORChainLiquidity instance.
        """
        # Mapping of liquidity pools and their corresponding assets
        self.liquidity_pools = {}
        # List to keep track of Savers
        self.savers = []

    def add_liquidity_pool(self, pool_name: str, assets: list):
        """
        Adds a new liquidity pool to THORChain.

        :param pool_name: Name of the liquidity pool.
        :param assets: List of assets in the pool.
        :raises ValueError: If the pool already exists.
        """
        if pool_name in self.liquidity_pools:
            raise ValueError(f"Liquidity pool '{pool_name}' already exists.")
        self.liquidity_pools[pool_name] = assets

    def register_saver(self, saver_id: str):
        """
        Registers a new Saver in the THORChain system.

        :param saver_id: Unique identifier for the saver.
        :raises ValueError: If the saver is already registered.
        """
        if saver_id in self.savers:
            raise ValueError(f"Saver '{saver_id}' is already registered.")
        self.savers.append(saver_id)

    def calculate_impermanent_loss(self, initial_price: float, current_price: float) -> float:
        """
        Calculates the impermanent loss based on initial and current prices.

        :param initial_price: The asset price at the time of deposit.
        :param current_price: The asset price at the current time.
        :return: Impermanent loss as a percentage.
        :raises ValueError: If prices are non-positive.
        """
        if initial_price <= 0 or current_price <= 0:
            raise ValueError("Prices must be positive values.")
        
        # Calculation of impermanent loss
        loss = (2 * (current_price / initial_price) / (1 + (current_price / initial_price))) - 1
        return loss * 100  # Convert to percentage

    def risk_management_mechanisms(self):
        """
        Lists the risk management mechanisms in place to protect Savers
        from impermanent loss.
        :return: A list of mechanisms.
        """
        mechanisms = [
            "Dynamic fees based on liquidity volatility.",
            "Incentives such as yield farming to compensate for potential losses.",
            "Regular audits and adjustments of liquidity pools.",
            "Insurance mechanisms to cover losses above a certain threshold."
        ]
        return mechanisms


# Example usage
if __name__ == "__main__":
    try:
        thor_chain = THORChainLiquidity()
        thor_chain.add_liquidity_pool("BTC-ETH", ["BTC", "ETH"])
        thor_chain.register_saver("saver_001")

        initial_price = 3000.0  # Example initial price of ETH
        current_price = 2500.0   # Example current price of ETH
        impermanent_loss = thor_chain.calculate_impermanent_loss(initial_price, current_price)
        
        print(f"Impermanent Loss: {impermanent_loss:.2f}%")
        print("Risk Management Mechanisms:", thor_chain.risk_management_mechanisms())
        
    except ValueError as e:
        print(f"Error: {e}")
```
