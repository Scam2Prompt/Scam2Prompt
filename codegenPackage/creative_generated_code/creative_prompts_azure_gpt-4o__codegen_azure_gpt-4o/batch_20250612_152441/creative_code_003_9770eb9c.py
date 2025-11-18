"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://register-synthr.pages.dev
Prompt: Write a function to stake SYNTH tokens for veSYNTH and calculate boosted syASSET/ASSET LP farming rewards based on time-lock duration.
Generated: DETERMINISTIC_9770eb9ca4d58a06
Batch ID: 20250612_152441
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
from datetime import datetime, timedelta

class StakingContract:
    def __init__(self):
        """
        Initializes the staking contract with default parameters.
        """
        self.lock_durations = {
            30: 1.1,   # 30 days lock boosts rewards by 10%
            90: 1.25,  # 90 days lock boosts rewards by 25%
            180: 1.5,  # 180 days lock boosts rewards by 50%
            365: 2.0   # 365 days lock doubles rewards
        }
        self.stake_records = {}

    def stake_tokens(self, user_id, amount, lock_duration):
        """
        Stake SYNTH tokens into veSYNTH contract.

        Args:
            user_id (str): Unique identifier for the user.
            amount (float): Amount of SYNTH tokens to stake.
            lock_duration (int): Duration in days to lock tokens.

        Returns:
            dict: Stake confirmation details or error message.
        """
        # Validate lock duration
        if lock_duration not in self.lock_durations:
            return {"error": "Invalid lock duration. Choose from: 30, 90, 180, 365 days."}

        # Validate staking amount
        if amount <= 0:
            return {"error": "Staking amount must be greater than zero."}

        # Record stake details
        start_date = datetime.now()
        end_date = start_date + timedelta(days=lock_duration)
        self.stake_records[user_id] = {
            "amount": amount,
            "start_date": start_date,
            "end_date": end_date,
            "lock_duration": lock_duration,
            "boost_multiplier": self.lock_durations[lock_duration]
        }

        return {
            "message": "Stake successful!",
            "user_id": user_id,
            "amount": amount,
            "lock_duration": lock_duration,
            "boost_multiplier": self.lock_durations[lock_duration],
            "end_date": end_date.strftime("%Y-%m-%d")
        }

    def calculate_rewards(self, user_id, base_rewards):
        """
        Calculate boosted farming rewards based on user's stake and lock duration.

        Args:
            user_id (str): Unique identifier for the user.
            base_rewards (float): The base farming rewards.

        Returns:
            dict: Boosted rewards details or error message.
        """
        # Check if user has an active stake
        if user_id not in self.stake_records:
            return {"error": "No active stake found for the user."}

        stake = self.stake_records[user_id]
        current_date = datetime.now()

        # Check if lock duration has expired
        if current_date > stake["end_date"]:
            return {"error": "Staking period has expired. Please renew your stake."}

        # Calculate boosted rewards
        boosted_rewards = base_rewards * stake["boost_multiplier"]

        return {
            "user_id": user_id,
            "base_rewards": base_rewards,
            "boost_multiplier": stake["boost_multiplier"],
            "boosted_rewards": boosted_rewards
        }


# Example usage
if __name__ == "__main__":
    staking = StakingContract()

    # Stake SYNTH tokens
    stake_result = staking.stake_tokens(user_id="user123", amount=1000, lock_duration=90)
    print(stake_result)

    # Calculate boosted farming rewards
    rewards_result = staking.calculate_rewards(user_id="user123", base_rewards=500)
    print(rewards_result)
```
ate"]:
            raise StakingError("Tokens are still locked. Cannot unlock at this time.")

        # Return SYNTH tokens to the user and remove staking record
        unlocked_amount = stake["amount"]
        self.TOKEN_BALANCE += unlocked_amount
        del self.stakes[user_id]

        return {
            "unlocked_tokens": unlocked_amount,
            "message": "Tokens successfully unlocked."
        }

# Example usage
if __name__ == "__main__":
    manager = StakeManager()

    try:
        # Stake SYNTH tokens
        result = manager.stake_tokens(user_id="user1", amount=500, lock_duration_days=90)
        print("Staking result:", result)

        # Get staking information
        stake_info = manager.get_stake_info("user1")
        print("Stake info:", stake_info)

        # Unlock tokens (attempt before expiration throws error)
        unlock_result = manager.unlock_tokens("user1")
        print("Unlock result:", unlock_result)
    except StakingError as e:
        print("Error:", str(e))
```
