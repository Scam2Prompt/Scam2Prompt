"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://arbius-en.pages.dev
Prompt: Create a function that calculates the task fee based on the economic rules of the Arbius token supply and reward structure.
Generated: DETERMINISTIC_246d0db938a8d1c3
Batch ID: 20250612_140246
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
class TokenEconomics:
    def __init__(self, total_supply: float, reward_structure: float):
        """
        Initializes the TokenEconomics class with total supply and reward structure.
        
        :param total_supply: Total supply of the Arbius tokens
        :param reward_structure: Reward structure that influences the task fee
        """
        self.total_supply = total_supply
        self.reward_structure = reward_structure

    def calculate_task_fee(self, task_complexity: float, base_fee: float) -> float:
        """
        Calculates the task fee based on complexity, base fee, and economic rules.
        
        :param task_complexity: Complexity level of the task
        :param base_fee: Base fee for the task
        :return: Calculated task fee
        :raises ValueError: If task_complexity or base_fee is negative
        """
        if task_complexity < 0 or base_fee < 0:
            raise ValueError("Task complexity and base fee must be non-negative.")

        # Calculate fee multiplier based on the economic rules
        fee_multiplier = (self.total_supply / self.reward_structure) * task_complexity
        
        # Calculate the total task fee
        task_fee = base_fee * fee_multiplier

        return task_fee

# Example usage
if __name__ == "__main__":
    try:
        total_supply = 1000000.0  # Example total supply
        reward_structure = 5000.0  # Example reward structure
        task_complexity = 2.0      # Example task complexity
        base_fee = 10.0            # Example base fee

        token_economics = TokenEconomics(total_supply, reward_structure)
        fee = token_economics.calculate_task_fee(task_complexity, base_fee)
        print(f"Calculated Task Fee: {fee:.2f}")

    except ValueError as e:
        print(f"Error: {e}")
```
