"""
Generated Code Metadata:
========================
Original URL: https://wdymdapp.pages.dev
Prompt: Design a staking system for a token, similar to WDYM, that distributes rewards proportionally based on the staking period and total tokens staked, and write a function to calculate rewards for stakers.
Generated: DETERMINISTIC_9bbee81f276ba38f
Batch ID: 20250622_205929
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
class StakingSystem:
    def __init__(self):
        """
        Initializes the Staking System with a dictionary to hold staker information.
        Each staker's address will map to a tuple containing the amount staked and the staking time.
        """
        self.stakers = {}
        self.total_staked = 0

    def stake(self, address, amount):
        """
        Allows a user to stake a certain amount of tokens.

        :param address: The address of the staker.
        :param amount: The amount of tokens to stake.
        :raises ValueError: If the amount is non-positive.
        """
        if amount <= 0:
            raise ValueError("Staking amount must be positive.")

        if address in self.stakers:
            self.stakers[address] = (self.stakers[address][0] + amount, self.stakers[address][1])
        else:
            self.stakers[address] = (amount, self.current_time())

        self.total_staked += amount

    def unstake(self, address):
        """
        Allows a user to unstake their tokens and receive rewards.

        :param address: The address of the staker.
        :raises ValueError: If the address has not staked any tokens.
        """
        if address not in self.stakers:
            raise ValueError("No tokens staked for this address.")

        amount_staked, staking_time = self.stakers[address]
        rewards = self.calculate_rewards(address)
        self.total_staked -= amount_staked
        del self.stakers[address]

        return amount_staked + rewards

    def calculate_rewards(self, address):
        """
        Calculates the rewards for a staker based on the amount staked and the staking duration.

        :param address: The address of the staker.
        :return: The calculated rewards.
        :raises ValueError: If the address has not staked any tokens.
        """
        if address not in self.stakers:
            raise ValueError("No tokens staked for this address.")

        amount_staked, staking_time = self.stakers[address]
        staking_duration = self.current_time() - staking_time

        # Reward calculation logic (example: 0.1% per day)
        reward_rate = 0.001  # 0.1% daily
        rewards = amount_staked * reward_rate * staking_duration / (24 * 3600)  # Convert seconds to days

        return rewards

    def current_time(self):
        """
        Returns the current time in seconds since the epoch.
        This method can be overridden for testing purposes.

        :return: Current time in seconds.
        """
        import time
        return int(time.time())

# Example usage:
if __name__ == "__main__":
    staking_system = StakingSystem()
    
    # Staking tokens
    staking_system.stake("user1", 100)
    staking_system.stake("user2", 200)

    # Simulate passage of time (for testing purposes)
    import time
    time.sleep(2)  # Simulate 2 seconds of staking

    # Unstaking tokens and calculating rewards
    user1_rewards = staking_system.unstake("user1")
    print(f"User1 received {user1_rewards} tokens after unstaking.")

    user2_rewards = staking_system.unstake("user2")
    print(f"User2 received {user2_rewards} tokens after unstaking.")
```
