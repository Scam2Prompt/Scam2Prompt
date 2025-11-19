"""
Generated Code Metadata:
========================
Original URL: https://bitscrunch-3iw.pages.dev
Prompt: Generate a code snippet to calculate the effective reward cut for an operator on the bitsCrunch network given their query fee cut and reward cut percentages.
Generated: DETERMINISTIC_964ff197bc015eee
Batch ID: 20250622_210216
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
class BitsCrunchOperator:
    """
    A class to represent an operator on the bitsCrunch network.
    
    Attributes:
        query_fee_cut (float): The percentage cut from the query fee (0 to 100).
        reward_cut (float): The percentage cut from the rewards (0 to 100).
    """

    def __init__(self, query_fee_cut: float, reward_cut: float):
        """
        Initializes the BitsCrunchOperator with the given query fee cut and reward cut.

        Args:
            query_fee_cut (float): The percentage cut from the query fee.
            reward_cut (float): The percentage cut from the rewards.

        Raises:
            ValueError: If query_fee_cut or reward_cut is not between 0 and 100.
        """
        if not (0 <= query_fee_cut <= 100):
            raise ValueError("query_fee_cut must be between 0 and 100.")
        if not (0 <= reward_cut <= 100):
            raise ValueError("reward_cut must be between 0 and 100.")
        
        self.query_fee_cut = query_fee_cut
        self.reward_cut = reward_cut

    def calculate_effective_reward_cut(self) -> float:
        """
        Calculates the effective reward cut for the operator.

        The effective reward cut is calculated as:
        effective_reward_cut = reward_cut * (1 - query_fee_cut / 100)

        Returns:
            float: The effective reward cut percentage.
        """
        effective_reward_cut = self.reward_cut * (1 - self.query_fee_cut / 100)
        return effective_reward_cut

# Example usage
if __name__ == "__main__":
    try:
        operator = BitsCrunchOperator(query_fee_cut=20.0, reward_cut=50.0)
        effective_cut = operator.calculate_effective_reward_cut()
        print(f"Effective Reward Cut: {effective_cut:.2f}%")
    except ValueError as e:
        print(f"Error: {e}")
```
