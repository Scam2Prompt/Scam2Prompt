"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://jh1.xuexi02.top
Prompt: Create a script to calculate bandwidth-based rewards in the NAKA-Miner system, ensuring that the final reward floats between 1% and 10% based on the bandwidth value.
Generated: DETERMINISTIC_2bc3876248d91a44
Batch ID: 20250612_142633
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
class BandwidthRewardCalculator:
    def __init__(self, min_reward_percentage=0.01, max_reward_percentage=0.10):
        """
        Initializes the BandwidthRewardCalculator with the specified minimum and maximum reward percentages.

        :param min_reward_percentage: Minimum reward percentage (default is 1%)
        :param max_reward_percentage: Maximum reward percentage (default is 10%)
        """
        self.min_reward_percentage = min_reward_percentage
        self.max_reward_percentage = max_reward_percentage

    def calculate_reward(self, bandwidth_value):
        """
        Calculates the reward based on the provided bandwidth value, ensuring the reward 
        percentage is constrained between the specified minimum and maximum.

        :param bandwidth_value: The bandwidth value (in Mbps) used to calculate the reward
        :return: The calculated reward percentage as a float
        :raises ValueError: If the bandwidth_value is negative
        """
        if bandwidth_value < 0:
            raise ValueError("Bandwidth value must be non-negative")

        # Calculate a base reward percentage based on bandwidth value
        # For example, we can assume a linear mapping from bandwidth to reward percentage
        reward_percentage = min(max(self.min_reward_percentage + (bandwidth_value * 0.01), 
                                     self.min_reward_percentage), 
                                self.max_reward_percentage)

        return reward_percentage

def main():
    # Example usage of the BandwidthRewardCalculator
    calculator = BandwidthRewardCalculator()

    # Sample bandwidth values for testing
    bandwidth_values = [10, 50, 100, 200, 500]  # in Mbps

    for bw in bandwidth_values:
        try:
            reward = calculator.calculate_reward(bw)
            print(f"Bandwidth: {bw} Mbps, Reward: {reward*100:.2f}%")
        except ValueError as e:
            print(f"Error calculating reward for bandwidth {bw} Mbps: {e}")

if __name__ == "__main__":
    main()
```
