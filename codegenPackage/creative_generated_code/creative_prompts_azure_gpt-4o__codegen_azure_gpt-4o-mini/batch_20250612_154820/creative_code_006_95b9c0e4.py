"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://cruas.ru
Prompt: Generate code to calculate transaction fees and distribute rewards to liquidity providers in a Velodrome Finance-like DEX platform.
Generated: DETERMINISTIC_95b9c0e4e22feddd
Batch ID: 20250612_154820
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
class DexPlatform:
    def __init__(self, transaction_fee_rate: float, reward_distribution_rate: float):
        """
        Initializes the DexPlatform with transaction fee and reward distribution rates.

        :param transaction_fee_rate: A float representing the rate of transaction fees (0 to 1).
        :param reward_distribution_rate: A float representing the rate of rewards distribution (0 to 1).
        """
        if not (0 <= transaction_fee_rate <= 1):
            raise ValueError("Transaction fee rate must be between 0 and 1.")
        if not (0 <= reward_distribution_rate <= 1):
            raise ValueError("Reward distribution rate must be between 0 and 1.")

        self.transaction_fee_rate = transaction_fee_rate
        self.reward_distribution_rate = reward_distribution_rate
        self.total_fees_collected = 0.0
        self.total_rewards_distributed = 0.0
        self.liquidity_providers = {}

    def add_liquidity_provider(self, provider_id: str, initial_stake: float):
        """
        Adds a liquidity provider to the platform.

        :param provider_id: Unique identifier for the liquidity provider.
        :param initial_stake: Initial stake the provider is adding.
        """
        if initial_stake <= 0:
            raise ValueError("Initial stake must be greater than zero.")
        
        self.liquidity_providers[provider_id] = {
            "stake": initial_stake,
            "rewards": 0.0
        }

    def calculate_transaction_fee(self, transaction_amount: float) -> float:
        """
        Calculates the transaction fee based on the transaction amount.

        :param transaction_amount: The amount of the transaction.
        :return: The calculated transaction fee.
        """
        if transaction_amount <= 0:
            raise ValueError("Transaction amount must be greater than zero.")
        
        fee = transaction_amount * self.transaction_fee_rate
        self.total_fees_collected += fee
        return fee

    def distribute_rewards(self):
        """
        Distributes rewards to liquidity providers based on their stake and the total fees collected.
        """
        if self.total_fees_collected == 0:
            print("No fees collected. No rewards to distribute.")
            return
        
        total_stake = sum(provider["stake"] for provider in self.liquidity_providers.values())
        
        for provider_id, provider in self.liquidity_providers.items():
            # Calculate provider's share of the total stake
            provider_share = provider["stake"] / total_stake
            # Calculate rewards based on the collected fees
            rewards = self.total_fees_collected * self.reward_distribution_rate * provider_share
            
            # Update provider rewards and the total rewards distributed
            provider["rewards"] += rewards
            self.total_rewards_distributed += rewards
        
        # Reset total fees collected after distribution
        self.total_fees_collected = 0

    def get_provider_rewards(self, provider_id: str) -> float:
        """
        Retrieves the total rewards for a specific liquidity provider.

        :param provider_id: Unique identifier for the liquidity provider.
        :return: Total rewards for the provider.
        """
        provider = self.liquidity_providers.get(provider_id)
        if not provider:
            raise ValueError("Provider not found.")
        
        return provider["rewards"]

# Example of using the DexPlatform class
if __name__ == "__main__":
    try:
        dex = DexPlatform(transaction_fee_rate=0.01, reward_distribution_rate=0.5)
        dex.add_liquidity_provider("provider_1", initial_stake=1000)
        dex.add_liquidity_provider("provider_2", initial_stake=2000)

        fee = dex.calculate_transaction_fee(10000)
        print(f"Transaction Fee: {fee}")

        dex.distribute_rewards()
        
        for provider_id in dex.liquidity_providers.keys():
            rewards = dex.get_provider_rewards(provider_id)
            print(f"Rewards for {provider_id}: {rewards}")
    
    except ValueError as e:
        print(f"Error: {e}")
```
