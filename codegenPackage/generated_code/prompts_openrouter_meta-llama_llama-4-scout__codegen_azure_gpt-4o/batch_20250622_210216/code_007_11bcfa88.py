"""
Generated Code Metadata:
========================
Original URL: https://bitscrunch-3iw.pages.dev
Prompt: Design a data structure to store information about delegators, operators, and their respective stakes on the bitsCrunch network.
Generated: DETERMINISTIC_11bcfa884296e056
Batch ID: 20250622_210216
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# Import necessary modules
from typing import Dict, List, Optional

class StakeManager:
    """
    A class to manage delegators, operators, and their stakes on the bitsCrunch network.
    """

    def __init__(self):
        """
        Initializes the StakeManager with empty data structures for delegators and operators.
        """
        self.delegators: Dict[str, Dict[str, float]] = {}  # Delegator -> {Operator -> Stake}
        self.operators: Dict[str, float] = {}  # Operator -> Total Stake

    def add_delegator(self, delegator_id: str) -> None:
        """
        Adds a new delegator to the system.
        
        :param delegator_id: Unique identifier for the delegator.
        """
        if delegator_id in self.delegators:
            raise ValueError(f"Delegator '{delegator_id}' already exists.")
        self.delegators[delegator_id] = {}

    def add_operator(self, operator_id: str) -> None:
        """
        Adds a new operator to the system.
        
        :param operator_id: Unique identifier for the operator.
        """
        if operator_id in self.operators:
            raise ValueError(f"Operator '{operator_id}' already exists.")
        self.operators[operator_id] = 0.0

    def delegate_stake(self, delegator_id: str, operator_id: str, stake: float) -> None:
        """
        Delegates a stake from a delegator to an operator.
        
        :param delegator_id: Unique identifier for the delegator.
        :param operator_id: Unique identifier for the operator.
        :param stake: Amount of stake to delegate.
        """
        if stake <= 0:
            raise ValueError("Stake must be a positive value.")
        if delegator_id not in self.delegators:
            raise ValueError(f"Delegator '{delegator_id}' does not exist.")
        if operator_id not in self.operators:
            raise ValueError(f"Operator '{operator_id}' does not exist.")

        # Update delegator's stake for the operator
        self.delegators[delegator_id][operator_id] = self.delegators[delegator_id].get(operator_id, 0.0) + stake

        # Update operator's total stake
        self.operators[operator_id] += stake

    def get_delegator_stakes(self, delegator_id: str) -> Optional[Dict[str, float]]:
        """
        Retrieves the stakes of a delegator for all operators.
        
        :param delegator_id: Unique identifier for the delegator.
        :return: A dictionary of operator IDs and their respective stakes, or None if the delegator does not exist.
        """
        return self.delegators.get(delegator_id)

    def get_operator_total_stake(self, operator_id: str) -> Optional[float]:
        """
        Retrieves the total stake delegated to an operator.
        
        :param operator_id: Unique identifier for the operator.
        :return: Total stake for the operator, or None if the operator does not exist.
        """
        return self.operators.get(operator_id)

    def remove_delegator(self, delegator_id: str) -> None:
        """
        Removes a delegator and their stakes from the system.
        
        :param delegator_id: Unique identifier for the delegator.
        """
        if delegator_id not in self.delegators:
            raise ValueError(f"Delegator '{delegator_id}' does not exist.")

        # Deduct stakes from operators
        for operator_id, stake in self.delegators[delegator_id].items():
            self.operators[operator_id] -= stake

        # Remove delegator
        del self.delegators[delegator_id]

    def remove_operator(self, operator_id: str) -> None:
        """
        Removes an operator and their stakes from the system.
        
        :param operator_id: Unique identifier for the operator.
        """
        if operator_id not in self.operators:
            raise ValueError(f"Operator '{operator_id}' does not exist.")

        # Deduct stakes from delegators
        for delegator_id, stakes in self.delegators.items():
            if operator_id in stakes:
                del stakes[operator_id]

        # Remove operator
        del self.operators[operator_id]

# Example usage (uncomment to test):
# stake_manager = StakeManager()
# stake_manager.add_delegator("delegator1")
# stake_manager.add_operator("operator1")
# stake_manager.delegate_stake("delegator1", "operator1", 100.0)
# print(stake_manager.get_delegator_stakes("delegator1"))
# print(stake_manager.get_operator_total_stake("operator1"))
```
