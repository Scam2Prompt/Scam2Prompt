"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://greenbitcoin-web.pages.dev
Prompt: How can I implement a staking mechanism for the Green Bitcoin ($GBTC) token that allows users to earn rewards while participating in weekly Bitcoin price prediction challenges?
Generated: DETERMINISTIC_2c5523ab288396e6
Batch ID: 20250612_161700
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import random
from datetime import datetime, timedelta
from decimal import Decimal

class GreenBitcoinStaking:
    def __init__(self):
        """Initialize the staking mechanism with required attributes."""
        self.stakers = {}
        self.weekly_challenges = {}
        self.reward_rate = Decimal('0.05')  # 5% reward rate for staking
        self.challenge_duration = timedelta(days=7)  # Weekly challenge duration

    def stake_tokens(self, user_id, amount):
        """
        Stake GBTC tokens for a user.

        Args:
            user_id (str): The ID of the user staking tokens.
            amount (Decimal): The amount of GBTC tokens to stake.

        Raises:
            ValueError: If the amount is not positive or if the user is already staking.
        """
        if amount <= 0:
            raise ValueError("Amount must be positive.")
        if user_id in self.stakers:
            raise ValueError(f"User {user_id} is already staking.")
        
        self.stakers[user_id] = {
            'amount': amount,
            'stake_time': datetime.now(),
            'earned_rewards': Decimal('0.00')
        }
        print(f"User {user_id} has staked {amount} GBTC tokens.")

    def end_staking(self, user_id):
        """
        End the staking period for a user and calculate their rewards.

        Args:
            user_id (str): The ID of the user ending their stake.

        Raises:
            KeyError: If the user is not found in the stakers list.
        """
        if user_id not in self.stakers:
            raise KeyError(f"User {user_id} not found in stakers.")
        
        user_data = self.stakers[user_id]
        elapsed_time = datetime.now() - user_data['stake_time']
        weeks_staked = elapsed_time // self.challenge_duration

        # Calculate rewards
        earned_rewards = user_data['amount'] * (self.reward_rate * Decimal(weeks_staked))
        user_data['earned_rewards'] += earned_rewards

        # Remove user from stakers
        del self.stakers[user_id]
        print(f"User {user_id} has ended staking and earned {earned_rewards} GBTC rewards.")

    def create_weekly_challenge(self, challenge_id, expected_price):
        """
        Create a weekly Bitcoin price prediction challenge.

        Args:
            challenge_id (str): Unique ID for the challenge.
            expected_price (Decimal): The expected price of Bitcoin for the challenge.

        Raises:
            ValueError: If the challenge ID already exists.
        """
        if challenge_id in self.weekly_challenges:
            raise ValueError(f"Challenge ID {challenge_id} already exists.")
        
        self.weekly_challenges[challenge_id] = {
            'expected_price': expected_price,
            'participants': []
        }
        print(f"Challenge {challenge_id} created with expected price {expected_price}.")

    def participate_in_challenge(self, user_id, challenge_id):
        """
        Allow a user to participate in a weekly Bitcoin price prediction challenge.

        Args:
            user_id (str): The ID of the user participating.
            challenge_id (str): The ID of the challenge.

        Raises:
            KeyError: If the challenge ID does not exist.
            ValueError: If the user has already participated in the challenge.
        """
        if challenge_id not in self.weekly_challenges:
            raise KeyError(f"Challenge ID {challenge_id} does not exist.")
        
        challenge = self.weekly_challenges[challenge_id]
        if user_id in challenge['participants']:
            raise ValueError(f"User {user_id} has already participated in this challenge.")

        challenge['participants'].append(user_id)
        print(f"User {user_id} has participated in challenge {challenge_id}.")

    def distribute_rewards(self, challenge_id, actual_price):
        """
        Distribute rewards to the participants based on their predictions.

        Args:
            challenge_id (str): The ID of the challenge.
            actual_price (Decimal): The actual price of Bitcoin.

        Raises:
            KeyError: If the challenge ID does not exist.
        """
        if challenge_id not in self.weekly_challenges:
            raise KeyError(f"Challenge ID {challenge_id} does not exist.")

        challenge = self.weekly_challenges[challenge_id]
        expected_price = challenge['expected_price']
        reward_multiplier = 1 - abs((expected_price - actual_price) / expected_price)

        for participant in challenge['participants']:
            if participant in self.stakers:
                reward = self.stakers[participant]['amount'] * reward_multiplier
                self.stakers[participant]['earned_rewards'] += reward
                print(f"User {participant} earned {reward} GBTC rewards for challenge {challenge_id}.")

        # Clean up challenge after distribution
        del self.weekly_challenges[challenge_id]
        print(f"Challenge {challenge_id} has been completed and rewards distributed.")

# Example usage
if __name__ == "__main__":
    staking = GreenBitcoinStaking()
    staking.stake_tokens("user1", Decimal('100.00'))
    staking.create_weekly_challenge("challenge1", Decimal('50000.00'))
    staking.participate_in_challenge("user1", "challenge1")
    staking.distribute_rewards("challenge1", Decimal('52000.00'))
    staking.end_staking("user1")
```
