"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://olas-network.pages.dev
Prompt: How can developers earn rewards for contributing service code to the Olas protocol, and what does the staking model look like?
Generated: DETERMINISTIC_8de0471f56daea51
Batch ID: 20250612_160940
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
class OlasProtocol:
    """
    A class to represent the Olas protocol for developers to contribute service code
    and earn rewards through a staking model.
    """
    
    def __init__(self):
        """Initialize the OlasProtocol with an empty list of contributions and a reward pool."""
        self.contributions = []
        self.reward_pool = 10000  # Total rewards available for distribution
        self.developer_stakes = {}  # Dictionary to track developer stakes

    def contribute(self, developer_id, contribution):
        """
        Allow a developer to contribute service code to the Olas protocol.

        Args:
            developer_id (str): Unique identifier for the developer.
            contribution (str): Description of the service code contributed.

        Raises:
            ValueError: If the contribution is empty or the developer_id is invalid.
        """
        if not contribution or not developer_id:
            raise ValueError("Contribution or developer ID cannot be empty.")

        self.contributions.append((developer_id, contribution))
        print(f"Developer {developer_id} contributed: {contribution}")

    def stake(self, developer_id, amount):
        """
        Allow a developer to stake a certain amount to earn rewards.

        Args:
            developer_id (str): Unique identifier for the developer.
            amount (float): Amount of stake.

        Raises:
            ValueError: If the stake amount is less than or equal to zero.
        """
        if amount <= 0:
            raise ValueError("Stake amount must be greater than zero.")

        if developer_id in self.developer_stakes:
            self.developer_stakes[developer_id] += amount
        else:
            self.developer_stakes[developer_id] = amount

        print(f"Developer {developer_id} staked: {amount}")

    def distribute_rewards(self):
        """
        Distribute rewards to developers based on their stakes relative to the total stakes.

        Raises:
            RuntimeError: If no contributions are made.
        """
        if not self.contributions:
            raise RuntimeError("No contributions have been made to distribute rewards.")

        total_stake = sum(self.developer_stakes.values())
        if total_stake == 0:
            print("No stakes found. No rewards will be distributed.")
            return

        for developer_id, stake in self.developer_stakes.items():
            reward = (stake / total_stake) * self.reward_pool
            print(f"Developer {developer_id} receives reward: {reward:.2f}")

        # Resetting the reward pool for the next distribution cycle
        self.reward_pool = 10000  # Resetting for the next period
        self.developer_stakes.clear()  # Clear stakes after distribution

# Example usage
if __name__ == "__main__":
    protocol = OlasProtocol()

    # Developers contribute code
    protocol.contribute("dev1", "Implemented a new authentication service.")
    protocol.contribute("dev2", "Added a caching service for better performance.")

    # Developers stake their contributions
    protocol.stake("dev1", 150)
    protocol.stake("dev2", 250)

    # Distribute rewards based on stakes
    protocol.distribute_rewards()
```
