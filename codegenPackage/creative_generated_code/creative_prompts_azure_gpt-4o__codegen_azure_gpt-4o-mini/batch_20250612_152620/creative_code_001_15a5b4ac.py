"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://bitscrunch-3iw.pages.dev
Prompt: Generate code to calculate the total rewards earned by delegators across all operators in the BitsCrunch Network using the provided data structure.
Generated: DETERMINISTIC_15a5b4aca9c3841d
Batch ID: 20250612_152620
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
from typing import List, Dict

class Delegator:
    """
    Class representing a delegator in the BitsCrunch Network.

    Attributes:
        name (str): The name of the delegator.
        rewards (float): The total rewards earned by the delegator.
    """
    def __init__(self, name: str, rewards: float):
        self.name = name
        self.rewards = rewards

    def __repr__(self):
        return f"Delegator(name={self.name}, rewards={self.rewards})"


class Operator:
    """
    Class representing an operator in the BitsCrunch Network.

    Attributes:
        name (str): The name of the operator.
        delegators (List[Delegator]): A list of delegators associated with the operator.
    """
    def __init__(self, name: str):
        self.name = name
        self.delegators: List[Delegator] = []

    def add_delegator(self, delegator: Delegator):
        """Adds a delegator to the operator's list of delegators."""
        self.delegators.append(delegator)

    def total_rewards(self) -> float:
        """
        Calculates the total rewards earned by all delegators for this operator.

        Returns:
            float: The total rewards earned by the operator's delegators.
        """
        total = sum(delegator.rewards for delegator in self.delegators)
        return total


def calculate_total_rewards(operators: List[Operator]) -> float:
    """
    Calculates the total rewards earned by all delegators across all operators.

    Args:
        operators (List[Operator]): A list of operators in the BitsCrunch Network.

    Returns:
        float: The total rewards earned by all delegators.
    """
    total_rewards = 0.0
    for operator in operators:
        operator_rewards = operator.total_rewards()
        print(f"Operator: {operator.name}, Delegator Rewards: {operator_rewards}")
        total_rewards += operator_rewards

    return total_rewards


# Example usage:
if __name__ == "__main__":
    # Create some operators
    operator1 = Operator("Operator1")
    operator2 = Operator("Operator2")

    # Create and add delegators for operator1
    operator1.add_delegator(Delegator("DelegatorA", 100.0))
    operator1.add_delegator(Delegator("DelegatorB", 200.0))

    # Create and add delegators for operator2
    operator2.add_delegator(Delegator("DelegatorC", 150.0))
    operator2.add_delegator(Delegator("DelegatorD", 250.0))

    # List of operators
    operators = [operator1, operator2]

    # Calculate total rewards
    total_rewards = calculate_total_rewards(operators)
    print(f"Total Rewards Earned by Delegators: {total_rewards}")
```
