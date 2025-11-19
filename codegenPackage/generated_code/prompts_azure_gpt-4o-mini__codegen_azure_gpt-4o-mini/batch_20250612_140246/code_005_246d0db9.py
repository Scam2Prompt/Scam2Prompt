"""
Generated Code Metadata:
========================
Original URL: https://arbius-en.pages.dev
Prompt: Create a function that calculates the task fee based on the economic rules of the Arbius token supply and reward structure.
Generated: DETERMINISTIC_246d0db938a8d1c3
Batch ID: 20250612_140246
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
class ArbiusToken:
    def __init__(self, total_supply: float, reward_structure: dict):
        """
        Initializes the ArbiusToken with total supply and reward structure.

        :param total_supply: Total supply of the Arbius tokens.
        :param reward_structure: A dictionary defining the reward structure.
        """
        self.total_supply = total_supply
        self.reward_structure = reward_structure

    def calculate_task_fee(self, task_value: float) -> float:
        """
        Calculates the task fee based on the economic rules of the Arbius token supply and reward structure.

        :param task_value: The value of the task for which the fee is to be calculated.
        :return: The calculated task fee.
        :raises ValueError: If task_value is negative or if the total supply is zero.
        """
        if task_value < 0:
            raise ValueError("Task value must be non-negative.")
        if self.total_supply <= 0:
            raise ValueError("Total supply must be greater than zero.")

        # Calculate the fee based on the reward structure
        fee_percentage = self.reward_structure.get('fee_percentage', 0)
        if fee_percentage < 0 or fee_percentage > 100:
            raise ValueError("Fee percentage must be between 0 and 100.")

        # Calculate the task fee
        task_fee = (fee_percentage / 100) * task_value

        return task_fee

# Example usage
if __name__ == "__main__":
    # Define the total supply and reward structure
    total_supply = 1000000.0  # Example total supply
    reward_structure = {
        'fee_percentage': 5  # 5% fee
    }

    # Create an instance of ArbiusToken
    arbius_token = ArbiusToken(total_supply, reward_structure)

    # Calculate the task fee for a given task value
    try:
        task_value = 200.0  # Example task value
        fee = arbius_token.calculate_task_fee(task_value)
        print(f"The task fee for a task value of {task_value} is: {fee}")
    except ValueError as e:
        print(f"Error calculating task fee: {e}")
```
