"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://thenafl.org
Prompt: Write code to simulate yield farming strategies using THENA FI's ve-token mechanisms and calculate optimized earnings for liquidity providers.
Generated: DETERMINISTIC_e1766108391efc98
Batch ID: 20250612_154902
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import pandas as pd
from typing import List, Dict

class YieldFarmingSimulator:
    def __init__(self, liquidity_providers: List[Dict], reward_rate: float):
        """
        Initializes the YieldFarmingSimulator with a list of liquidity providers and a reward rate.
        
        :param liquidity_providers: A list of dictionaries containing information about each provider.
        :param reward_rate: The annual reward rate for liquidity providers (in decimal).
        """
        self.liquidity_providers = liquidity_providers
        self.reward_rate = reward_rate

    def calculate_rewards(self, amount: float, duration: int) -> float:
        """
        Calculate the rewards for a given amount of liquidity provided over a certain duration.
        
        :param amount: The amount of liquidity provided by the provider.
        :param duration: The duration of the liquidity provision in days.
        :return: The total rewards earned.
        """
        if amount < 0 or duration < 0:
            raise ValueError("Amount and duration must be non-negative.")

        # Calculate daily rewards and then total rewards for the given duration
        daily_reward = amount * self.reward_rate / 365
        total_rewards = daily_reward * duration
        return total_rewards

    def simulate(self) -> pd.DataFrame:
        """
        Simulates yield farming strategies for all liquidity providers and returns a DataFrame with results.
        
        :return: A DataFrame containing liquidity provider information and their calculated rewards.
        """
        results = []
        for provider in self.liquidity_providers:
            try:
                provider_rewards = self.calculate_rewards(provider['amount'], provider['duration'])
                results.append({
                    'provider': provider['name'],
                    'amount': provider['amount'],
                    'duration': provider['duration'],
                    'rewards': provider_rewards
                })
            except Exception as e:
                # Log error for individual provider but continue processing others
                results.append({
                    'provider': provider['name'],
                    'error': str(e)
                })

        # Convert results into a DataFrame for better visualization
        return pd.DataFrame(results)


# Example usage:
if __name__ == "__main__":
    # Define liquidity providers with their amounts and duration
    liquidity_providers = [
        {'name': 'Provider A', 'amount': 1000, 'duration': 30},
        {'name': 'Provider B', 'amount': 2000, 'duration': 60},
        {'name': 'Provider C', 'amount': -500, 'duration': 20}  # This will cause an error
    ]

    # Define an annual reward rate
    reward_rate = 0.1  # 10% annual reward rate

    # Initialize the simulator
    simulator = YieldFarmingSimulator(liquidity_providers, reward_rate)

    # Run the simulation
    results_df = simulator.simulate()

    # Output the results
    print(results_df)
```
