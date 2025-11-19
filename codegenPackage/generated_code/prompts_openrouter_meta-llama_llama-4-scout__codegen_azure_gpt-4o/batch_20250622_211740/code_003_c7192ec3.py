"""
Generated Code Metadata:
========================
Original URL: https://vatanplatform.site
Prompt: Design a loyalty program, similar to BaxBet's, that rewards users with cashback on losses and bonus rewards, using a Python programming language.
Generated: DETERMINISTIC_c7192ec33a49c04b
Batch ID: 20250622_211740
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import datetime
import logging

# Configure logging for error handling and debugging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

class LoyaltyProgram:
    """
    A class to represent a loyalty program that rewards users with cashback on losses
    and bonus rewards based on their activity.
    """
    def __init__(self, cashback_rate=0.05, bonus_threshold=1000, bonus_reward=50):
        """
        Initialize the loyalty program with default parameters.

        :param cashback_rate: Percentage of losses to be returned as cashback (default: 5%)
        :param bonus_threshold: Minimum amount spent to qualify for bonus rewards (default: $1000)
        :param bonus_reward: Bonus reward amount (default: $50)
        """
        self.cashback_rate = cashback_rate
        self.bonus_threshold = bonus_threshold
        self.bonus_reward = bonus_reward
        self.user_data = {}  # Store user data in the format {user_id: {'losses': float, 'spent': float}}

    def register_user(self, user_id):
        """
        Register a new user in the loyalty program.

        :param user_id: Unique identifier for the user
        """
        if user_id in self.user_data:
            logging.warning(f"User {user_id} is already registered.")
        else:
            self.user_data[user_id] = {'losses': 0.0, 'spent': 0.0}
            logging.info(f"User {user_id} successfully registered.")

    def record_transaction(self, user_id, amount, is_loss):
        """
        Record a transaction for a user.

        :param user_id: Unique identifier for the user
        :param amount: Transaction amount (positive value)
        :param is_loss: Boolean indicating whether the transaction is a loss
        """
        if user_id not in self.user_data:
            logging.error(f"User {user_id} is not registered.")
            raise ValueError("User not registered in the loyalty program.")

        if amount <= 0:
            logging.error("Transaction amount must be positive.")
            raise ValueError("Transaction amount must be positive.")

        self.user_data[user_id]['spent'] += amount
        if is_loss:
            self.user_data[user_id]['losses'] += amount
        logging.info(f"Transaction recorded for user {user_id}: Amount=${amount}, Loss={is_loss}")

    def calculate_cashback(self, user_id):
        """
        Calculate the cashback amount for a user based on their losses.

        :param user_id: Unique identifier for the user
        :return: Cashback amount
        """
        if user_id not in self.user_data:
            logging.error(f"User {user_id} is not registered.")
            raise ValueError("User not registered in the loyalty program.")

        losses = self.user_data[user_id]['losses']
        cashback = losses * self.cashback_rate
        logging.info(f"Cashback calculated for user {user_id}: ${cashback:.2f}")
        return cashback

    def check_bonus_eligibility(self, user_id):
        """
        Check if a user is eligible for a bonus reward.

        :param user_id: Unique identifier for the user
        :return: Boolean indicating bonus eligibility
        """
        if user_id not in self.user_data:
            logging.error(f"User {user_id} is not registered.")
            raise ValueError("User not registered in the loyalty program.")

        spent = self.user_data[user_id]['spent']
        is_eligible = spent >= self.bonus_threshold
        logging.info(f"Bonus eligibility for user {user_id}: {is_eligible}")
        return is_eligible

    def get_bonus_reward(self, user_id):
        """
        Get the bonus reward for a user if they are eligible.

        :param user_id: Unique identifier for the user
        :return: Bonus reward amount or 0 if not eligible
        """
        if self.check_bonus_eligibility(user_id):
            logging.info(f"User {user_id} received a bonus reward of ${self.bonus_reward}.")
            return self.bonus_reward
        else:
            logging.info(f"User {user_id} is not eligible for a bonus reward.")
            return 0

# Example usage
if __name__ == "__main__":
    program = LoyaltyProgram()

    # Register users
    program.register_user("user1")
    program.register_user("user2")

    # Record transactions
    program.record_transaction("user1", 500, is_loss=True)
    program.record_transaction("user1", 600, is_loss=False)
    program.record_transaction("user2", 1200, is_loss=True)

    # Calculate cashback
    print(f"User1 Cashback: ${program.calculate_cashback('user1'):.2f}")
    print(f"User2 Cashback: ${program.calculate_cashback('user2'):.2f}")

    # Check bonus eligibility and rewards
    print(f"User1 Bonus Reward: ${program.get_bonus_reward('user1')}")
    print(f"User2 Bonus Reward: ${program.get_bonus_reward('user2')}")
```
