"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://delegationonbeam.com
Prompt: How can I implement a delegation system for Beam Nodes to secure the Beam Network and earn rewards?
Generated: DETERMINISTIC_46f8051922ee8701
Batch ID: 20250612_161356
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
class BeamNode:
    """
    A class to represent a Beam Node in the Beam Network.
    Each node can delegate resources to validators and earn rewards.
    """

    def __init__(self, node_id, node_address):
        """
        Initializes a BeamNode instance.
        
        :param node_id: Unique identifier for the node
        :param node_address: Network address of the node
        """
        self.node_id = node_id
        self.node_address = node_address
        self.delegations = {}
        self.total_rewards = 0

    def delegate(self, validator_id, amount):
        """
        Delegates resources to a specified validator.
        
        :param validator_id: Unique identifier for the validator
        :param amount: Amount of resources to delegate
        :raises ValueError: If the amount is non-positive
        """
        if amount <= 0:
            raise ValueError("Delegated amount must be positive.")
        
        if validator_id in self.delegations:
            self.delegations[validator_id] += amount
        else:
            self.delegations[validator_id] = amount

        print(f"Delegated {amount} to validator {validator_id}.")

    def collect_rewards(self, validator_id, reward_amount):
        """
        Collects rewards from the specified validator.
        
        :param validator_id: Unique identifier for the validator
        :param reward_amount: Amount of rewards to collect
        :raises ValueError: If the reward amount is non-positive
        """
        if reward_amount <= 0:
            raise ValueError("Reward amount must be positive.")
        
        self.total_rewards += reward_amount
        print(f"Collected {reward_amount} rewards from validator {validator_id}.")

    def get_delegations(self):
        """
        Returns the current delegations of the node.
        
        :return: Dictionary of delegations
        """
        return self.delegations

    def get_total_rewards(self):
        """
        Returns the total rewards collected by the node.
        
        :return: Total rewards
        """
        return self.total_rewards


# Example usage
if __name__ == "__main__":
    try:
        # Creating a Beam Node
        node = BeamNode(node_id="node_1", node_address="192.168.1.1")

        # Delegating resources to validators
        node.delegate(validator_id="validator_1", amount=100)
        node.delegate(validator_id="validator_2", amount=50)

        # Collecting rewards from validators
        node.collect_rewards(validator_id="validator_1", reward_amount=10)

        # Displaying current delegations and total rewards
        print("Current Delegations:", node.get_delegations())
        print("Total Rewards:", node.get_total_rewards())
    
    except ValueError as e:
        print(f"Error: {e}")
```
