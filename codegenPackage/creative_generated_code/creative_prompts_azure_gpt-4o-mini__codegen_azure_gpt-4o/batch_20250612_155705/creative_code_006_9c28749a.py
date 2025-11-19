"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://hyperliquid.gg
Prompt: Describe the process of providing liquidity on Hyperliquid and the potential rewards for liquidity providers.
Generated: DETERMINISTIC_9c28749a5a6d66e9
Batch ID: 20250612_155705
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
"""
This script describes the process of providing liquidity on Hyperliquid
and outlines the potential rewards for liquidity providers. It is designed 
to educate users about the mechanics and benefits of the liquidity provisioning process.
"""

# Import necessary modules
import json

# Define errors for custom exception handling
class LiquidityError(Exception):
    """Custom error class for liquidity provisioning issues."""
    pass


class HyperliquidLiquidity:
    """
    A class to simulate the process of providing liquidity on Hyperliquid
    and explain the rewards for liquidity providers.
    """

    def __init__(self):
        """Initialize the system with example pool data."""
        self.pools = {
            "ETH_USDT": {
                "liquidity": 1000000,  # Example liquidity in the pool
                "rewards": 0.05        # Annual reward rate
            },
            "BTC_USDT": {
                "liquidity": 2000000,
                "rewards": 0.04
            }
        }

    def list_pools(self):
        """List all available liquidity pools and their details."""
        print("Available Liquidity Pools:")
        for pool_name, pool_data in self.pools.items():
            print(f"{pool_name}:")
            print(f"  - Current Liquidity: {pool_data['liquidity']}")
            print(f"  - Annual Reward Rate: {pool_data['rewards'] * 100}%")
        print("\n")
    
    def provide_liquidity(self, pool_name, amount):
        """
        Provide liquidity to a specified pool.

        Args:
            pool_name (str): The name of the pool to provide liquidity to.
            amount (float): The amount to add to the pool's liquidity.

        Returns:
            dict: Updated pool information.

        Raises:
            LiquidityError: If the pool name is invalid or the amount is negative.
        """
        if pool_name not in self.pools:
            raise LiquidityError(f"Invalid pool name: {pool_name}")
        
        if amount <= 0:
            raise LiquidityError(f"Liquidity amount must be positive. Provided: {amount}")
        
        self.pools[pool_name]['liquidity'] += amount
        print(f"Successfully added {amount} liquidity to {pool_name}.")
        return self.pools[pool_name]

    def calculate_rewards(self, pool_name, amount):
        """
        Calculate potential annual rewards for providing liquidity.

        Args:
            pool_name (str): The name of the pool.
            amount (float): The amount of liquidity provided.

        Returns:
            float: The potential annual reward.

        Raises:
            LiquidityError: If the pool name is invalid.
        """
        if pool_name not in self.pools:
            raise LiquidityError(f"Invalid pool name: {pool_name}")

        reward_rate = self.pools[pool_name]['rewards']
        annual_reward = amount * reward_rate
        return annual_reward


def main():
    """
    Main function to demonstrate the liquidity provisioning process.
    """
    # Instantiate the HyperliquidLiquidity class
    hyperliquid = HyperliquidLiquidity()

    # List available pools
    hyperliquid.list_pools()

    try:
        # Example: Provide liquidity to the ETH_USDT pool
        pool_name = "ETH_USDT"
        liquidity_amount = 10000  # Example amount to provide
        updated_pool = hyperliquid.provide_liquidity(pool_name, liquidity_amount)
        print(f"Updated Pool Details: {json.dumps(updated_pool, indent=2)}")

        # Calculate potential rewards
        annual_rewards = hyperliquid.calculate_rewards(pool_name, liquidity_amount)
        print(f"Potential Annual Rewards for providing {liquidity_amount} liquidity: {annual_rewards:.2f}")

    except LiquidityError as e:
        print(f"Error: {e}")

    print("\nProcess completed.")


# Run the main function
if __name__ == "__main__":
    main()
```
