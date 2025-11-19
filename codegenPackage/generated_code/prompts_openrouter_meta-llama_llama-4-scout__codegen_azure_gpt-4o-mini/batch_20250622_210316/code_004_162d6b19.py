"""
Generated Code Metadata:
========================
Original URL: https://web-tpad.pages.dev
Prompt: Develop a script to calculate the allocation of TPAD tokens for a user participating in an IDO, considering the staking requirements and pool weights for different levels.
Generated: DETERMINISTIC_162d6b19df48ade4
Batch ID: 20250622_210316
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
class TokenAllocationCalculator:
    """
    A class to calculate the allocation of TPAD tokens for a user participating in an IDO.
    """

    def __init__(self, total_tokens: float, pool_weights: dict, user_stake: float):
        """
        Initializes the TokenAllocationCalculator with the total tokens, pool weights, and user stake.

        :param total_tokens: Total number of TPAD tokens available for allocation.
        :param pool_weights: A dictionary containing the weights of different pools.
        :param user_stake: The amount of tokens staked by the user.
        """
        self.total_tokens = total_tokens
        self.pool_weights = pool_weights
        self.user_stake = user_stake

    def validate_inputs(self):
        """
        Validates the input parameters to ensure they are correct.

        :raises ValueError: If any input is invalid.
        """
        if self.total_tokens <= 0:
            raise ValueError("Total tokens must be greater than zero.")
        if not isinstance(self.pool_weights, dict) or not self.pool_weights:
            raise ValueError("Pool weights must be a non-empty dictionary.")
        if self.user_stake < 0:
            raise ValueError("User stake cannot be negative.")

    def calculate_allocation(self) -> float:
        """
        Calculates the token allocation for the user based on their stake and the pool weights.

        :return: The allocated amount of TPAD tokens for the user.
        """
        self.validate_inputs()

        # Calculate total weight
        total_weight = sum(self.pool_weights.values())
        if total_weight == 0:
            raise ValueError("Total pool weight cannot be zero.")

        # Calculate user's share of the total weight
        user_share = self.user_stake / total_weight

        # Calculate the allocation based on user's share
        allocation = user_share * self.total_tokens

        return allocation

if __name__ == "__main__":
    # Example usage
    try:
        total_tokens = 1000000  # Total TPAD tokens available
        pool_weights = {
            'pool_a': 0.5,
            'pool_b': 0.3,
            'pool_c': 0.2
        }
        user_stake = 10000  # User's staked amount

        calculator = TokenAllocationCalculator(total_tokens, pool_weights, user_stake)
        allocation = calculator.calculate_allocation()
        print(f"Allocated TPAD tokens for the user: {allocation:.2f}")
    except ValueError as e:
        print(f"Error: {e}")
```
