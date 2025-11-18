"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://yfyuyyufy.pages.dev
Prompt: Write a script to calculate the rewards for EarthNode operators based on network transaction volume, using the tokenomics model described in the World Mobile Token documentation.
Generated: DETERMINISTIC_635a0491c5623325
Batch ID: 20250612_150012
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import logging

# Configure logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

class EarthNodeRewardCalculator:
    """
    A class to calculate rewards for EarthNode operators based on network transaction volume
    and tokenomics model described in the World Mobile Token documentation.
    """
    def __init__(self, total_transaction_volume, reward_pool_percentage, earth_nodes_count):
        """
        Initializes the calculator with necessary parameters.

        :param total_transaction_volume: The total transaction volume (in tokens) for the network.
        :param reward_pool_percentage: Percentage of transaction volume allocated to the reward pool.
        :param earth_nodes_count: Number of active EarthNode operators.
        """
        self.total_transaction_volume = total_transaction_volume
        self.reward_pool_percentage = reward_pool_percentage
        self.earth_nodes_count = earth_nodes_count

    def calculate_rewards_per_node(self):
        """
        Calculates the reward for each EarthNode operator.

        :return: Reward per EarthNode operator (in tokens).
        """
        try:
            # Validate input
            if self.total_transaction_volume < 0 or self.reward_pool_percentage < 0 or self.earth_nodes_count <= 0:
                raise ValueError("Input values must be positive, and EarthNode count must be greater than zero.")

            # Calculate reward pool size
            reward_pool = self.total_transaction_volume * (self.reward_pool_percentage / 100)

            # Calculate reward per EarthNode
            reward_per_node = reward_pool / self.earth_nodes_count

            return reward_per_node
        except Exception as e:
            logging.error(f"Error calculating rewards: {e}")
            raise

def main():
    """
    Main function to execute the reward calculation.
    """
    try:
        # Input parameters
        total_transaction_volume = float(input("Enter total transaction volume (in tokens): "))
        reward_pool_percentage = float(input("Enter reward pool percentage (%): "))
        earth_nodes_count = int(input("Enter number of EarthNode operators: "))

        # Create calculator instance
        calculator = EarthNodeRewardCalculator(total_transaction_volume, reward_pool_percentage, earth_nodes_count)

        # Calculate rewards
        rewards_per_node = calculator.calculate_rewards_per_node()
        logging.info(f"Rewards per EarthNode operator: {rewards_per_node:.2f} tokens")
    except Exception as e:
        logging.error(f"An error occurred during execution: {e}")

# Entry point
if __name__ == "__main__":
    main()
```
