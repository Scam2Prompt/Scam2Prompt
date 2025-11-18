"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://decentralizedtoolz.pages.dev
Prompt: Write code to troubleshoot staking and unstaking issues, including rewards retrieval, based on the "Staking / Unstaking" section of the Node Rectification Tool.
Generated: DETERMINISTIC_ceb7af93fdc9d5c1
Batch ID: 20250612_150237
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import logging

class StakingManager:
    def __init__(self, staking_service):
        """
        Initializes the StakingManager with a given staking service.
        
        :param staking_service: An instance of a service that manages staking operations.
        """
        self.staking_service = staking_service
        logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

    def stake(self, user_id, amount):
        """
        Stakes an amount for a given user.
        
        :param user_id: The ID of the user staking the amount.
        :param amount: The amount to stake.
        :raises ValueError: If the amount is non-positive.
        :raises Exception: If an error occurs during the staking process.
        """
        if amount <= 0:
            raise ValueError("Staking amount must be greater than zero.")
        
        try:
            logging.info(f"User {user_id} is attempting to stake {amount}.")
            result = self.staking_service.stake(user_id, amount)
            logging.info(f"Stake successful for user {user_id}: {result}")
        except Exception as e:
            logging.error(f"Error while staking for user {user_id}: {e}")
            raise

    def unstake(self, user_id, amount):
        """
        Unstakes an amount for a given user.
        
        :param user_id: The ID of the user unstaking the amount.
        :param amount: The amount to unstake.
        :raises ValueError: If the amount is non-positive.
        :raises Exception: If an error occurs during the unstaking process.
        """
        if amount <= 0:
            raise ValueError("Unstaking amount must be greater than zero.")
        
        try:
            logging.info(f"User {user_id} is attempting to unstake {amount}.")
            result = self.staking_service.unstake(user_id, amount)
            logging.info(f"Unstake successful for user {user_id}: {result}")
        except Exception as e:
            logging.error(f"Error while unstaking for user {user_id}: {e}")
            raise

    def retrieve_rewards(self, user_id):
        """
        Retrieves rewards for a given user.
        
        :param user_id: The ID of the user for whom to retrieve rewards.
        :raises Exception: If an error occurs during the rewards retrieval process.
        """
        try:
            logging.info(f"User {user_id} is attempting to retrieve rewards.")
            rewards = self.staking_service.get_rewards(user_id)
            logging.info(f"Rewards retrieval successful for user {user_id}: {rewards}")
            return rewards
        except Exception as e:
            logging.error(f"Error while retrieving rewards for user {user_id}: {e}")
            raise

# Example staking service implementation
class MockStakingService:
    def stake(self, user_id, amount):
        # Simulate a successful staking operation
        return {"user_id": user_id, "amount": amount, "status": "staked"}

    def unstake(self, user_id, amount):
        # Simulate a successful unstaking operation
        return {"user_id": user_id, "amount": amount, "status": "unstaked"}

    def get_rewards(self, user_id):
        # Simulate rewards retrieval
        return {"user_id": user_id, "rewards": 100}

# Example usage
if __name__ == "__main__":
    service = MockStakingService()
    manager = StakingManager(service)

    try:
        manager.stake("user123", 50)
        manager.unstake("user123", 20)
        rewards = manager.retrieve_rewards("user123")
        print(f"User rewards: {rewards}")
    except Exception as e:
        logging.error(f"An error occurred: {e}")
```
