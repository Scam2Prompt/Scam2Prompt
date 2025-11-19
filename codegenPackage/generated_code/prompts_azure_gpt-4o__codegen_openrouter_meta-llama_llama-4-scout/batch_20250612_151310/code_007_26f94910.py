"""
Generated Code Metadata:
========================
Original URL: https://ethena-a30.pages.dev
Prompt: Develop a tool to calculate the shard rewards for holding USDe YT or LP on Pendle, based on the shard earning rates provided by Ethena.
Generated: DETERMINISTIC_26f94910074d49ec
Batch ID: 20250612_151310
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# shard_rewards_calculator.py

from typing import Dict

class ShardRewardsCalculator:
    """
    Calculates shard rewards for holding USDe YT or LP on Pendle based on Ethena's shard earning rates.

    Attributes:
        ethna_shard_earning_rates (Dict): A dictionary containing Ethena's shard earning rates.
    """

    def __init__(self, ethna_shard_earning_rates: Dict):
        """
        Initializes the ShardRewardsCalculator with Ethena's shard earning rates.

        Args:
            ethna_shard_earning_rates (Dict): A dictionary containing Ethena's shard earning rates.
        """
        self.ethna_shard_earning_rates = ethna_shard_earning_rates

    def calculate_shard_rewards(self, holding_type: str, amount: float) -> float:
        """
        Calculates shard rewards based on the holding type and amount.

        Args:
            holding_type (str): The type of holding (USDe YT or LP).
            amount (float): The amount of holding.

        Returns:
            float: The calculated shard rewards.

        Raises:
            ValueError: If the holding type is not supported.
        """
        if holding_type not in ['USDe YT', 'LP']:
            raise ValueError("Unsupported holding type. Supported types are 'USDe YT' and 'LP'.")

        # Get the shard earning rate for the given holding type
        shard_earning_rate = self.ethna_shard_earning_rates.get(holding_type)

        if shard_earning_rate is None:
            raise ValueError(f"No shard earning rate found for {holding_type}")

        # Calculate shard rewards
        shard_rewards = amount * shard_earning_rate

        return shard_rewards


def main():
    # Example usage
    ethna_shard_earning_rates = {
        'USDe YT': 0.1,  # 10% APY
        'LP': 0.05       # 5% APY
    }

    calculator = ShardRewardsCalculator(ethna_shard_earning_rates)

    try:
        holding_type = 'USDe YT'
        amount = 1000.0
        shard_rewards = calculator.calculate_shard_rewards(holding_type, amount)
        print(f"Shard rewards for {holding_type} with amount {amount}: {shard_rewards}")

        holding_type = 'LP'
        amount = 500.0
        shard_rewards = calculator.calculate_shard_rewards(holding_type, amount)
        print(f"Shard rewards for {holding_type} with amount {amount}: {shard_rewards}")

    except ValueError as e:
        print(f"Error: {e}")


if __name__ == "__main__":
    main()
```
