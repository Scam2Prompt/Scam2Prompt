"""
Generated Code Metadata:
========================
Original URL: https://shibuswap.github.io
Prompt: Create a liquidity pool similar to ShibaSwap's DIG, and write a Python code snippet to calculate the SSLP tokens and rewards distribution.
Generated: DETERMINISTIC_fe5f40ed8f730a6a
Batch ID: 20250622_211156
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
class LiquidityPool:
    def __init__(self):
        # Initialize the liquidity pool with empty balances and total supply
        self.total_supply = 0
        self.liquidity_providers = {}
        self.rewards_distribution = {}

    def add_liquidity(self, provider, amount):
        """
        Add liquidity to the pool for a specific provider.
        
        :param provider: The address of the liquidity provider
        :param amount: The amount of liquidity being added
        """
        if amount <= 0:
            raise ValueError("Amount must be greater than zero.")
        
        # Update the provider's balance and total supply
        if provider in self.liquidity_providers:
            self.liquidity_providers[provider] += amount
        else:
            self.liquidity_providers[provider] = amount
        
        self.total_supply += amount

    def calculate_sslp_tokens(self, provider):
        """
        Calculate the SSLP tokens for a specific provider based on their liquidity contribution.
        
        :param provider: The address of the liquidity provider
        :return: The number of SSLP tokens for the provider
        """
        if provider not in self.liquidity_providers:
            raise ValueError("Provider has no liquidity in the pool.")
        
        provider_amount = self.liquidity_providers[provider]
        sslp_tokens = (provider_amount / self.total_supply) * 100  # Example calculation
        return sslp_tokens

    def distribute_rewards(self, total_rewards):
        """
        Distribute rewards to liquidity providers based on their share of the total supply.
        
        :param total_rewards: The total rewards to be distributed
        """
        if total_rewards <= 0:
            raise ValueError("Total rewards must be greater than zero.")
        
        for provider, amount in self.liquidity_providers.items():
            share = amount / self.total_supply
            rewards = share * total_rewards
            if provider in self.rewards_distribution:
                self.rewards_distribution[provider] += rewards
            else:
                self.rewards_distribution[provider] = rewards

    def get_provider_rewards(self, provider):
        """
        Get the total rewards for a specific provider.
        
        :param provider: The address of the liquidity provider
        :return: The total rewards for the provider
        """
        return self.rewards_distribution.get(provider, 0)

# Example usage
if __name__ == "__main__":
    pool = LiquidityPool()
    
    # Adding liquidity
    pool.add_liquidity("provider1", 100)
    pool.add_liquidity("provider2", 200)
    
    # Calculating SSLP tokens
    sslp_tokens_provider1 = pool.calculate_sslp_tokens("provider1")
    print(f"SSLP tokens for provider1: {sslp_tokens_provider1}")
    
    # Distributing rewards
    pool.distribute_rewards(300)
    
    # Getting provider rewards
    rewards_provider1 = pool.get_provider_rewards("provider1")
    print(f"Rewards for provider1: {rewards_provider1}")
```
