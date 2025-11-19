"""
Generated Code Metadata:
========================
Original URL: https://bafybeihdjl7xixuxxuxsexbtlzb37crgafyrxd5652yvkz4aokv7np4uty.ipfs.dweb.link
Prompt: Write a function that calculates MOR rewards based on the usage and impact of contributed work in the Morpheus ecosystem.
Generated: DETERMINISTIC_32bd7cf212091f63
Batch ID: 20250622_205751
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
class MorpheusRewardCalculator:
    """
    A class to calculate MOR rewards based on the usage and impact of contributed work
    in the Morpheus ecosystem.
    """

    def __init__(self, base_reward: float = 10.0):
        """
        Initializes the reward calculator with a base reward.

        :param base_reward: The base reward amount for contributions.
        """
        if base_reward < 0:
            raise ValueError("Base reward must be a non-negative value.")
        self.base_reward = base_reward

    def calculate_reward(self, usage: float, impact: float) -> float:
        """
        Calculates the MOR reward based on usage and impact.

        :param usage: The usage metric of the contribution (should be non-negative).
        :param impact: The impact metric of the contribution (should be non-negative).
        :return: The calculated MOR reward.
        :raises ValueError: If usage or impact is negative.
        """
        if usage < 0 or impact < 0:
            raise ValueError("Usage and impact must be non-negative values.")

        # Calculate reward based on usage and impact
        reward = self.base_reward * (1 + usage * 0.1 + impact * 0.2)
        return round(reward, 2)  # Round to 2 decimal places for currency format

    def display_reward(self, usage: float, impact: float) -> None:
        """
        Displays the calculated MOR reward.

        :param usage: The usage metric of the contribution.
        :param impact: The impact metric of the contribution.
        """
        try:
            reward = self.calculate_reward(usage, impact)
            print(f"The calculated MOR reward for usage {usage} and impact {impact} is: {reward}")
        except ValueError as e:
            print(f"Error calculating reward: {e}")


# Example usage
if __name__ == "__main__":
    calculator = MorpheusRewardCalculator(base_reward=15.0)
    calculator.display_reward(usage=5, impact=10)  # Example values for usage and impact
```
