"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://inqubeta-im.pages.dev
Prompt: Create a script to track the rewards earned from staking $QUBE tokens on InQubeta.
Generated: DETERMINISTIC_8dd81fe58784eebf
Batch ID: 20250612_164305
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

Here is the requested code in Python:

```python
import time
import logging
from typing import Dict

# Setup logging configuration
logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s"
)

class StakingContract:
    def __init__(self, token_symbol: str, annual_reward_rate: float):
        """
        Initializes the staking contract.

        :param token_symbol: Symbol of the token being staked (e.g., $QUBE).
        :param annual_reward_rate: Annual reward rate (e.g., 0.10 for 10% APR).
        """
        self.token_symbol = token_symbol
        self.annual_reward_rate = annual_reward_rate
        self.stakers: Dict[str, Dict[str, float]] = {}

    def stake_tokens(self, user: str, amount: float):
        """
        Allows a user to stake tokens.

        :param user: Identifier for the user (e.g., wallet address).
        :param amount: Number of tokens to stake.
        """
        if amount <= 0:
            raise ValueError("Stake amount must be greater than zero.")

        if user not in self.stakers:
            self.stakers[user] = {"amount_staked": 0, "start_time": time.time()}

        self.stakers[user]["amount_staked"] += amount
        self.stakers[user]["start_time"] = time.time()  # Reset staking start time
        logging.info(f"User '{user}' staked {amount} {self.token_symbol} tokens.")

    def calculate_rewards(self, user: str) -> float:
        """
        Calculates the rewards earned by a staker.

        :param user: Identifier for the user.
        :return: The rewards earned.
        """
        if user not in self.stakers:
            raise ValueError("User has not staked any tokens.")

        staker_data = self.stakers[user]
        amount_staked = staker_data["amount_staked"]
        start_time = staker_data["start_time"]

        # Calculate the staking duration in seconds
        staking_duration = time.time() - start_time

        # Convert annual reward rate to per-second rate
        per_second_reward_rate = self.annual_reward_rate / (365 * 24 * 60 * 60)

        # Calculate rewards
        rewards = amount_staked * staking_duration * per_second_reward_rate
        return rewards

    def withdraw_rewards(self, user: str) -> float:
        """
        Allows a user to withdraw their earned rewards.

        :param user: Identifier for the user.
        :return: The amount of rewards withdrawn.
        """
        rewards = self.calculate_rewards(user)
        self.stakers[user]["start_time"] = time.time()  # Reset staking start time
        logging.info(f"User '{user}' withdrew {rewards:.6f} {self.token_symbol} tokens as rewards.")
        return rewards


# Example usage of the script
if __name__ == "__main__":
    try:
        # Initialize staking contract with $QUBE token and 10% annual reward rate
        staking_contract = StakingContract(token_symbol="$QUBE", annual_reward_rate=0.10)

        # User stakes tokens
        staking_contract.stake_tokens(user="0x1234abcd", amount=1000)

        # Simulate some time passing
        time.sleep(5)  # Wait for 5 seconds

        # Calculate and display rewards
        user_rewards = staking_contract.calculate_rewards(user="0x1234abcd")
        print(f"Rewards earned: {user_rewards:.6f} $QUBE")

        # User withdraws rewards
        withdrawn_rewards = staking_contract.withdraw_rewards(user="0x1234abcd")
        print(f"Withdrawn rewards: {withdrawn_rewards:.6f} $QUBE")

    except Exception as e:
        logging.error(f"An error occurred: {e}")
```

This script is designed to track staking rewards for $QUBE tokens. It includes methods for staking tokens, calculating rewards, and withdrawing rewards, with proper error handling and logging.
