"""
Generated Code Metadata:
========================
Original URL: https://pepeunchained-es.web.app
Prompt: Design a staking rewards system for $PEPU tokens on Pepe Unchained, taking into account the double staking rewards and 100x faster transaction processing compared to Ethereum.
Generated: DETERMINISTIC_5ec4d1e453cd2c03
Batch ID: 20250622_205901
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import time
from decimal import Decimal

class StakingRewardsSystem:
    """
    A staking rewards system for $PEPU tokens on Pepe Unchained.
    This system supports double staking rewards and faster transaction processing.
    """

    def __init__(self, reward_rate_per_second: Decimal, double_staking_multiplier: Decimal):
        """
        Initialize the staking rewards system.

        :param reward_rate_per_second: Base reward rate per second for staking.
        :param double_staking_multiplier: Multiplier for double staking rewards.
        """
        self.reward_rate_per_second = reward_rate_per_second
        self.double_staking_multiplier = double_staking_multiplier
        self.stakers = {}  # Dictionary to store staker information

    def stake_tokens(self, user_id: str, amount: Decimal, double_staking: bool = False):
        """
        Stake $PEPU tokens for a user.

        :param user_id: Unique identifier for the user.
        :param amount: Amount of $PEPU tokens to stake.
        :param double_staking: Whether the user opts for double staking rewards.
        """
        if amount <= 0:
            raise ValueError("Stake amount must be greater than zero.")

        current_time = time.time()
        if user_id in self.stakers:
            # Calculate pending rewards before updating stake
            self.stakers[user_id]['pending_rewards'] += self.calculate_rewards(user_id)
            self.stakers[user_id]['last_stake_time'] = current_time
            self.stakers[user_id]['staked_amount'] += amount
            self.stakers[user_id]['double_staking'] = double_staking
        else:
            # New staker
            self.stakers[user_id] = {
                'staked_amount': amount,
                'last_stake_time': current_time,
                'pending_rewards': Decimal(0),
                'double_staking': double_staking
            }

    def calculate_rewards(self, user_id: str) -> Decimal:
        """
        Calculate the rewards for a staker.

        :param user_id: Unique identifier for the user.
        :return: Calculated rewards.
        """
        if user_id not in self.stakers:
            raise ValueError("User not found in staking system.")

        staker = self.stakers[user_id]
        elapsed_time = Decimal(time.time() - staker['last_stake_time'])
        base_rewards = elapsed_time * self.reward_rate_per_second * staker['staked_amount']

        if staker['double_staking']:
            return base_rewards * self.double_staking_multiplier
        return base_rewards

    def claim_rewards(self, user_id: str) -> Decimal:
        """
        Claim staking rewards for a user.

        :param user_id: Unique identifier for the user.
        :return: Total claimed rewards.
        """
        if user_id not in self.stakers:
            raise ValueError("User not found in staking system.")

        # Calculate total rewards (pending + new rewards)
        staker = self.stakers[user_id]
        total_rewards = staker['pending_rewards'] + self.calculate_rewards(user_id)

        # Reset pending rewards and update last stake time
        staker['pending_rewards'] = Decimal(0)
        staker['last_stake_time'] = time.time()

        return total_rewards

    def unstake_tokens(self, user_id: str) -> Decimal:
        """
        Unstake $PEPU tokens for a user and claim rewards.

        :param user_id: Unique identifier for the user.
        :return: Total claimed rewards upon unstaking.
        """
        if user_id not in self.stakers:
            raise ValueError("User not found in staking system.")

        # Claim rewards before unstaking
        total_rewards = self.claim_rewards(user_id)

        # Remove staker from the system
        staked_amount = self.stakers[user_id]['staked_amount']
        del self.stakers[user_id]

        return staked_amount, total_rewards

    def get_staker_info(self, user_id: str) -> dict:
        """
        Get staking information for a user.

        :param user_id: Unique identifier for the user.
        :return: Staker information.
        """
        if user_id not in self.stakers:
            raise ValueError("User not found in staking system.")

        staker = self.stakers[user_id]
        return {
            'staked_amount': staker['staked_amount'],
            'pending_rewards': staker['pending_rewards'] + self.calculate_rewards(user_id),
            'double_staking': staker['double_staking']
        }


# Example usage
if __name__ == "__main__":
    # Initialize the staking rewards system
    reward_rate = Decimal("0.0001")  # Example reward rate per second
    double_staking_multiplier = Decimal("2")  # Double staking multiplier
    staking_system = StakingRewardsSystem(reward_rate, double_staking_multiplier)

    # Stake tokens
    staking_system.stake_tokens("user1", Decimal("100"), double_staking=True)

    # Simulate time passing
    time.sleep(2)  # Wait for 2 seconds

    # Claim rewards
    rewards = staking_system.claim_rewards("user1")
    print(f"Rewards claimed: {rewards}")

    # Unstake tokens
    staked_amount, total_rewards = staking_system.unstake_tokens("user1")
    print(f"Unstaked amount: {staked_amount}, Total rewards: {total_rewards}")
```
