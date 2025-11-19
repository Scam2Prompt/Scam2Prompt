"""
Generated Code Metadata:
========================
Original URL: https://bitscrunch-3iw.pages.dev
Prompt: Generate code to calculate the total rewards earned by delegators across all operators in the BitsCrunch Network using the provided data structure.
Generated: DETERMINISTIC_15a5b4aca9c3841d
Batch ID: 20250612_152620
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
from typing import List, Dict, Union

class Operator:
    def __init__(self, operator_id: str, total_rewards: float, delegators: List[Dict[str, Union[str, float]]]):
        """
        Represents an operator in the BitsCrunch Network.
        
        Args:
            operator_id: Unique identifier for the operator
            total_rewards: Total rewards earned by the operator
            delegators: List of delegators with their details
        """
        self.operator_id = operator_id
        self.total_rewards = total_rewards
        self.delegators = delegators

class RewardCalculator:
    @staticmethod
    def calculate_total_delegator_rewards(operators: List[Operator]) -> float:
        """
        Calculate the total rewards earned by all delegators across all operators.
        
        Args:
            operators: List of Operator objects
            
        Returns:
            Total rewards earned by all delegators as float
            
        Raises:
            ValueError: If operators list is empty or contains invalid data
        """
        if not operators:
            raise ValueError("Operators list cannot be empty")
            
        total_delegator_rewards = 0.0
        
        for operator in operators:
            if not isinstance(operator, Operator):
                raise ValueError("Invalid operator object in list")
                
            for delegator in operator.delegators:
                try:
                    reward = float(delegator.get('reward', 0))
                    total_delegator_rewards += reward
                except (ValueError, TypeError) as e:
                    raise ValueError(f"Invalid reward value for delegator: {e}")
                    
        return round(total_delegator_rewards, 2)

# Example usage
if __name__ == "__main__":
    # Sample data
    operators = [
        Operator(
            operator_id="op1",
            total_rewards=1000.0,
            delegators=[
                {"address": "addr1", "stake": 500.0, "reward": 200.0},
                {"address": "addr2", "stake": 300.0, "reward": 120.0}
            ]
        ),
        Operator(
            operator_id="op2",
            total_rewards=800.0,
            delegators=[
                {"address": "addr3", "stake": 400.0, "reward": 160.0},
                {"address": "addr4", "stake": 200.0, "reward": 80.0}
            ]
        )
    ]
    
    try:
        total_rewards = RewardCalculator.calculate_total_delegator_rewards(operators)
        print(f"Total delegator rewards: {total_rewards}")
    except ValueError as e:
        print(f"Error calculating rewards: {e}")
```
