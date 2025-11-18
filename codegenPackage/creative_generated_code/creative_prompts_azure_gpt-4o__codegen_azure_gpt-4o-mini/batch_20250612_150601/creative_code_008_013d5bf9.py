"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://nft-solaj.web.app
Prompt: Write code to implement a rewards system for NFT creators, similar to the "Rewards" feature mentioned on the Magic Eden Launchpad.
Generated: DETERMINISTIC_013d5bf998c0fbf7
Batch ID: 20250612_150601
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
# rewards_system.py

class NFTCreator:
    """
    Class to represent an NFT Creator in the rewards system.
    """

    def __init__(self, creator_id, name):
        """
        Initialize an NFT Creator with an ID and name.

        :param creator_id: Unique identifier for the creator
        :param name: The name of the NFT creator
        """
        self.creator_id = creator_id
        self.name = name
        self.total_rewards = 0.0

    def add_rewards(self, amount):
        """
        Add rewards to the creator's account.

        :param amount: The amount of rewards to add
        :raises ValueError: If the amount is negative
        """
        if amount < 0:
            raise ValueError("Amount must be non-negative")
        self.total_rewards += amount

    def get_rewards(self):
        """
        Get the total rewards of the creator.

        :return: Total rewards of the creator
        """
        return self.total_rewards


class RewardsSystem:
    """
    Class to manage the rewards system for NFT creators.
    """

    def __init__(self):
        """
        Initializes the rewards system with an empty creator registry.
        """
        self.creators = {}

    def register_creator(self, creator_id, name):
        """
        Register a new NFT creator in the system.

        :param creator_id: Unique identifier for the creator
        :param name: The name of the NFT creator
        :raises ValueError: If creator_id already exists
        """
        if creator_id in self.creators:
            raise ValueError(f"Creator ID {creator_id} is already registered.")
        self.creators[creator_id] = NFTCreator(creator_id, name)

    def allocate_rewards(self, creator_id, amount):
        """
        Allocate rewards to a specific NFT creator.

        :param creator_id: Unique identifier for the creator
        :param amount: The amount of rewards to allocate
        :raises ValueError: If the creator_id does not exist or amount is negative
        """
        if creator_id not in self.creators:
            raise ValueError(f"Creator ID {creator_id} not found.")
        self.creators[creator_id].add_rewards(amount)

    def get_creator_rewards(self, creator_id):
        """
        Retrieve the total rewards for a specific creator.

        :param creator_id: Unique identifier for the creator
        :return: Total rewards of the creator
        :raises ValueError: If the creator_id does not exist
        """
        if creator_id not in self.creators:
            raise ValueError(f"Creator ID {creator_id} not found.")
        return self.creators[creator_id].get_rewards()

    def report(self):
        """
        Generate a report of all creators and their total rewards.

        :return: A dictionary with creator IDs and their rewards
        """
        report_data = {}
        for creator_id, creator in self.creators.items():
            report_data[creator_id] = creator.get_rewards()
        return report_data


# Example usage:
if __name__ == "__main__":
    try:
        rewards_system = RewardsSystem()
        
        # Registering creators
        rewards_system.register_creator("creator1", "Alice")
        rewards_system.register_creator("creator2", "Bob")
        
        # Allocating rewards
        rewards_system.allocate_rewards("creator1", 100.0)
        rewards_system.allocate_rewards("creator2", 150.0)

        # Retrieving rewards
        print("Alice's Rewards:", rewards_system.get_creator_rewards("creator1"))
        print("Bob's Rewards:", rewards_system.get_creator_rewards("creator2"))

        # Reporting all creators' rewards
        print("Rewards Report:", rewards_system.report())
        
    except ValueError as e:
        print("Error:", e)
```
