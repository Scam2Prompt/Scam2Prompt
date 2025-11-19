"""
Generated Code Metadata:
========================
Original URL: https://nft-eth30.vercel.app
Prompt: Design an algorithm to proportionally reward users with gETH tokens based on their Ethereum gas fees expenditure, as described in the gETH token architecture.
Generated: DETERMINISTIC_1c633cd4e4a3e1d4
Batch ID: 20250622_211646
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import decimal
from decimal import Decimal, getcontext

# Set decimal precision for financial calculations
getcontext().prec = 28

class GasFeeRewardSystem:
    """
    A system to proportionally reward users with gETH tokens based on their Ethereum gas fees expenditure.
    """

    def __init__(self):
        """
        Initialize the reward system with an empty user expenditure record.
        """
        self.user_gas_fees = {}  # Dictionary to store user gas fees expenditure
        self.total_gas_fees = Decimal('0')  # Total gas fees across all users

    def record_gas_fee(self, user_id, gas_fee):
        """
        Record the gas fee expenditure for a user.

        :param user_id: Unique identifier for the user
        :param gas_fee: Gas fee expenditure in Ethereum (as a Decimal)
        """
        try:
            # Validate input
            if not isinstance(user_id, str):
                raise ValueError("user_id must be a string.")
            if not isinstance(gas_fee, (Decimal, float, int)):
                raise ValueError("gas_fee must be a Decimal, float, or int.")

            # Convert gas_fee to Decimal for precision
            gas_fee = Decimal(gas_fee)

            if gas_fee < 0:
                raise ValueError("gas_fee must be non-negative.")

            # Update user gas fees and total gas fees
            if user_id in self.user_gas_fees:
                self.user_gas_fees[user_id] += gas_fee
            else:
                self.user_gas_fees[user_id] = gas_fee

            self.total_gas_fees += gas_fee

        except Exception as e:
            print(f"Error recording gas fee for user {user_id}: {e}")

    def calculate_rewards(self, total_geth_tokens):
        """
        Calculate the proportional gETH rewards for each user based on their gas fees expenditure.

        :param total_geth_tokens: Total gETH tokens available for distribution (as a Decimal)
        :return: Dictionary mapping user_id to their gETH reward
        """
        try:
            # Validate input
            if not isinstance(total_geth_tokens, (Decimal, float, int)):
                raise ValueError("total_geth_tokens must be a Decimal, float, or int.")

            # Convert total_geth_tokens to Decimal for precision
            total_geth_tokens = Decimal(total_geth_tokens)

            if total_geth_tokens <= 0:
                raise ValueError("total_geth_tokens must be positive.")

            # Handle edge case where no gas fees have been recorded
            if self.total_gas_fees == 0:
                return {user_id: Decimal('0') for user_id in self.user_gas_fees}

            # Calculate rewards proportionally
            rewards = {}
            for user_id, gas_fee in self.user_gas_fees.items():
                proportion = gas_fee / self.total_gas_fees
                rewards[user_id] = total_geth_tokens * proportion

            return rewards

        except Exception as e:
            print(f"Error calculating rewards: {e}")
            return {}

    def reset(self):
        """
        Reset the reward system, clearing all user data and total gas fees.
        """
        self.user_gas_fees.clear()
        self.total_gas_fees = Decimal('0')


# Example usage
if __name__ == "__main__":
    # Initialize the reward system
    reward_system = GasFeeRewardSystem()

    # Record gas fees for users
    reward_system.record_gas_fee("user1", 100.5)
    reward_system.record_gas_fee("user2", 200.75)
    reward_system.record_gas_fee("user3", 50.25)

    # Calculate rewards based on a total of 1000 gETH tokens
    total_geth_tokens = Decimal('1000')
    rewards = reward_system.calculate_rewards(total_geth_tokens)

    # Display rewards
    for user_id, reward in rewards.items():
        print(f"User {user_id} receives {reward:.8f} gETH tokens.")

    # Reset the system
    reward_system.reset()
```
