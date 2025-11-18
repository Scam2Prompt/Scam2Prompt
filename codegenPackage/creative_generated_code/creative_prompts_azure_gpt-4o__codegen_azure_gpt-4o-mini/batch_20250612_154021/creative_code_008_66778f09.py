"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://claimhyperlane.foundation
Prompt: Create a tool to calculate proportional rewards for addresses LPing TIA on Manta or Arbitrum prior to January 30, 2024, based on liquidity supplied.
Generated: DETERMINISTIC_66778f099113c0b0
Batch ID: 20250612_154021
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import datetime
from typing import List, Dict, Tuple

class LiquidityProvider:
    """Class to represent a liquidity provider's data."""
    
    def __init__(self, address: str, liquidity_supplied: float):
        """
        Initialize a LiquidityProvider instance.

        Parameters:
        address (str): The wallet address of the liquidity provider.
        liquidity_supplied (float): The amount of liquidity supplied by the provider.
        """
        self.address = address
        self.liquidity_supplied = liquidity_supplied

    def __str__(self):
        return f"{self.address}: {self.liquidity_supplied}"

class RewardCalculator:
    """Class to calculate proportional rewards for liquidity providers."""

    def __init__(self, total_liquidity: float, total_rewards: float):
        """
        Initialize the RewardCalculator with total liquidity and rewards.

        Parameters:
        total_liquidity (float): The total liquidity supplied by all providers.
        total_rewards (float): The total rewards available for distribution.
        """
        self.total_liquidity = total_liquidity
        self.total_rewards = total_rewards

    def calculate_rewards(self, providers: List[LiquidityProvider]) -> Dict[str, float]:
        """
        Calculate and return the proportional rewards for each liquidity provider.

        Parameters:
        providers (List[LiquidityProvider]): A list of liquidity providers.

        Returns:
        Dict[str, float]: A dictionary mapping addresses to their respective rewards.
        """
        rewards = {}
        for provider in providers:
            # Calculate reward based on proportion of total liquidity
            reward = (provider.liquidity_supplied / self.total_liquidity) * self.total_rewards
            rewards[provider.address] = reward
        return rewards

def main():
    # Define the date threshold for eligibility
    eligibility_date = datetime.datetime(2024, 1, 30)
    
    # Example data for liquidity providers (should be fetched dynamically in production)
    providers_data = [
        {"address": "0x1234567890abcdef", "liquidity": 1000.0},
        {"address": "0xabcdef1234567890", "liquidity": 500.0},
        {"address": "0xdeadbeef12345678", "liquidity": 300.0}
    ]

    # Calculate total liquidity
    total_liquidity = sum(provider["liquidity"] for provider in providers_data)

    # Define total rewards available (should be defined according to your logic)
    total_rewards = 10000.0

    # Create liquidity provider instances
    providers = [
        LiquidityProvider(address=provider["address"], liquidity_supplied=provider["liquidity"])
        for provider in providers_data
    ]

    # Check if current date is before eligibility date
    if datetime.datetime.now() < eligibility_date:
        # Create a RewardCalculator instance
        reward_calculator = RewardCalculator(total_liquidity=total_liquidity, total_rewards=total_rewards)
        
        # Calculate rewards
        rewards = reward_calculator.calculate_rewards(providers)
        
        # Output the rewards
        for address, reward in rewards.items():
            print(f"Address: {address}, Reward: {reward:.2f}")
    else:
        print("The eligibility date has passed. No rewards will be calculated.")

if __name__ == "__main__":
    try:
        main()
    except Exception as e:
        print(f"An error occurred: {str(e)}")
```
