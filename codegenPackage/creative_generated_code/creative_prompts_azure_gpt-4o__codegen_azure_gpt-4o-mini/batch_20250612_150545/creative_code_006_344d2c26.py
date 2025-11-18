"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://tsr-dao.web.app
Prompt: Write a program to calculate rewards in $TNSR tokens based on trading activity on Tensor and display the results in a user-friendly format.
Generated: DETERMINISTIC_344d2c2679d00f76
Batch ID: 20250612_150545
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import json
from typing import List, Dict

# Define a class to handle the reward calculation
class TNSRRewardCalculator:
    def __init__(self, trading_data: List[Dict[str, float]], reward_rate: float):
        """
        Initializes the TNSRRewardCalculator with trading data and a reward rate.

        :param trading_data: A list of dictionaries containing trading activity.
                             Each dictionary should have 'trade_volume' and 'trade_count'.
        :param reward_rate: The reward rate per unit of trade volume (in TNSR tokens).
        """
        self.trading_data = trading_data
        self.reward_rate = reward_rate

    def calculate_rewards(self) -> float:
        """
        Calculates total rewards based on trading activity.

        :return: Total rewards in TNSR tokens.
        """
        total_rewards = 0.0
        
        # Calculate rewards based on trading activity
        for trade in self.trading_data:
            try:
                trade_volume = trade.get('trade_volume', 0)
                trade_count = trade.get('trade_count', 0)

                # Validate trade data
                if trade_volume < 0 or trade_count < 0:
                    raise ValueError("Trade volume and trade count must be non-negative.")

                # Calculate rewards for the trade
                rewards = trade_volume * self.reward_rate
                total_rewards += rewards

            except Exception as e:
                print(f"Error processing trade data {trade}: {e}")

        return total_rewards

    def display_results(self, total_rewards: float) -> None:
        """
        Displays the calculated rewards in a user-friendly format.

        :param total_rewards: Total rewards in TNSR tokens.
        """
        print(f"Total Rewards Earned in TNSR tokens: ${total_rewards:.2f}")

def main():
    # Example trading data (could be fetched from an API or a database)
    trading_data = [
        {"trade_volume": 1000.0, "trade_count": 10},
        {"trade_volume": 1500.0, "trade_count": 5},
        {"trade_volume": 800.0, "trade_count": 8}
    ]

    # Define the reward rate (for example, 0.01 TNSR per unit of volume)
    reward_rate = 0.01

    # Initialize the reward calculator
    reward_calculator = TNSRRewardCalculator(trading_data, reward_rate)

    # Calculate total rewards
    total_rewards = reward_calculator.calculate_rewards()

    # Display the results
    reward_calculator.display_results(total_rewards)

if __name__ == "__main__":
    main()
```
