"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://claimgift-z164.web.app
Prompt: Describe the process of becoming a Node Operator for Lido and the benefits associated with it.
Generated: DETERMINISTIC_f0750ab459ac968d
Batch ID: 20250612_162504
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
class NodeOperator:
    """
    A class to represent a Node Operator for Lido.
    
    Attributes
    ----------
    operator_id : str
        Unique identifier for the node operator
    operator_name : str
        Name of the node operator
    staked_eth : float
        Amount of ETH staked by the operator
    rewards : float
        Total rewards earned by the operator
    """

    def __init__(self, operator_id: str, operator_name: str):
        """
        Initializes a new Node Operator with the given ID and name.
        
        Parameters
        ----------
        operator_id : str
            The unique identifier for the node operator.
        operator_name : str
            The name of the node operator.
        """
        self.operator_id = operator_id
        self.operator_name = operator_name
        self.staked_eth = 0.0
        self.rewards = 0.0

    def stake_eth(self, amount: float):
        """
        Staking ETH with the node operator.
        
        Parameters
        ----------
        amount : float
            The amount of ETH to stake.
        
        Raises
        ------
        ValueError
            If the amount is negative or zero.
        """
        if amount <= 0:
            raise ValueError("Amount to stake must be greater than zero.")
        
        self.staked_eth += amount
        print(f"{amount} ETH staked successfully. Total staked: {self.staked_eth} ETH.")

    def receive_rewards(self, amount: float):
        """
        Receive rewards for the node operator.
        
        Parameters
        ----------
        amount : float
            The amount of rewards to receive.
        
        Raises
        ------
        ValueError
            If the amount is negative or zero.
        """
        if amount <= 0:
            raise ValueError("Reward amount must be greater than zero.")
        
        self.rewards += amount
        print(f"Received {amount} rewards successfully. Total rewards: {self.rewards}.")

    def get_summary(self):
        """
        Returns a summary of the node operator's status.
        
        Returns
        -------
        str
            A summary string containing the operator's ID, name, staked ETH, and rewards.
        """
        return (f"Node Operator ID: {self.operator_id}\n"
                f"Operator Name: {self.operator_name}\n"
                f"Staked ETH: {self.staked_eth}\n"
                f"Total Rewards: {self.rewards}")

# Example Usage
if __name__ == "__main__":
    try:
        # Creating a new node operator
        lido_node = NodeOperator("Lido123", "Lido Node Operator")

        # Staking ETH
        lido_node.stake_eth(10.0)
        
        # Receiving rewards
        lido_node.receive_rewards(0.5)

        # Getting summary
        print(lido_node.get_summary())
    
    except ValueError as e:
        print(f"Error: {e}")
```
