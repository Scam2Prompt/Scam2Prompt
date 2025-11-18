"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://scottytheaidapp.pages.dev
Prompt: Generate a Python script to track the total staked $SCOTTY tokens and calculate the user's percentage of the staking pool based on their staked balance.
Generated: DETERMINISTIC_403d09fc619b6d5c
Batch ID: 20250612_153526
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import logging

# Configure logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

class StakingPool:
    def __init__(self):
        """
        Initializes the StakingPool with a total staked amount of 0 and an empty 
        dictionary for user balances.
        """
        self.total_staked = 0.0
        self.user_balances = {}

    def stake(self, user_id, amount):
        """
        Allows a user to stake a specified amount of SCOTTY tokens.

        Args:
            user_id (str): The identifier for the user.
            amount (float): The amount of SCOTTY tokens to stake.

        Raises:
            ValueError: If the amount is less than or equal to 0.
        """
        if amount <= 0:
            logging.error("Stake amount must be greater than 0.")
            raise ValueError("Stake amount must be greater than 0.")
        
        self.user_balances[user_id] = self.user_balances.get(user_id, 0.0) + amount
        self.total_staked += amount
        logging.info(f"User {user_id} has staked {amount} SCOTTY tokens.")

    def get_user_percentage(self, user_id):
        """
        Calculates the percentage of the total staking pool that a user holds.

        Args:
            user_id (str): The identifier for the user.

        Returns:
            float: The user's percentage of the total staked amount.

        Raises:
            ValueError: If the user has not staked any tokens.
        """
        user_balance = self.user_balances.get(user_id, 0.0)

        if user_balance <= 0:
            logging.error(f"User {user_id} has not staked any tokens.")
            raise ValueError(f"User {user_id} has not staked any tokens.")
        
        percentage = (user_balance / self.total_staked) * 100
        logging.info(f"User {user_id} owns {percentage:.2f}% of the staking pool.")
        return percentage

    def total_staked_amount(self):
        """
        Returns the total amount of SCOTTY tokens staked in the pool.

        Returns:
            float: The total staked amount.
        """
        return self.total_staked

def main():
    # Example usage of the StakingPool class.
    pool = StakingPool()
    
    try:
        pool.stake("user1", 100.0)
        pool.stake("user2", 200.0)
        
        print(f"Total staked SCOTTY tokens: {pool.total_staked_amount()}")
        
        user1_percentage = pool.get_user_percentage("user1")
        print(f"User1 percentage of staking pool: {user1_percentage:.2f}%")
        
        user2_percentage = pool.get_user_percentage("user2")
        print(f"User2 percentage of staking pool: {user2_percentage:.2f}%")
        
    except ValueError as e:
        logging.error(f"Error occurred: {e}")

if __name__ == "__main__":
    main()
```
