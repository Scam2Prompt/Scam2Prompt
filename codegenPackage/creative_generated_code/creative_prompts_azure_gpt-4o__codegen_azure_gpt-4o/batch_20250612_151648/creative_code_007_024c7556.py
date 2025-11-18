"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://blockchainbets-app.pages.dev
Prompt: Create a Python script to track and display the user's claimable rewards in $BCB, $ETH, and $USDT on the BCB Staking v2 platform, ensuring accurate calculations based on staking duration.
Generated: DETERMINISTIC_024c7556fe790508
Batch ID: 20250612_151648
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import time
import json

class RewardTracker:
    def __init__(self):
        """
        Initializes the reward tracker with token reward rates per second.
        These rates represent rewards in $BCB, $ETH, and $USDT.
        """
        self.reward_rates = {
            "BCB": 0.0001,  # Reward rate per second in $BCB
            "ETH": 0.00005,  # Reward rate per second in $ETH
            "USDT": 0.0002   # Reward rate per second in $USDT
        }
        self.staking_start_time = None
        self.rewards_claimed = {"BCB": 0.0, "ETH": 0.0, "USDT": 0.0}

    def start_staking(self):
        """
        Starts the staking process by noting the current timestamp.
        """
        self.staking_start_time = time.time()
        print("Staking started!")

    def calculate_rewards(self):
        """
        Calculates the claimable rewards based on staking duration.
        Returns a dictionary containing the claimable rewards for each token.
        """
        if self.staking_start_time is None:
            raise RuntimeError("Staking has not started yet.")

        # Calculate staking duration in seconds
        staking_duration = time.time() - self.staking_start_time

        # Calculate rewards for each token
        rewards = {token: rate * staking_duration for token, rate in self.reward_rates.items()}
        return rewards

    def claim_rewards(self):
        """
        Claims the current reward and resets the staking start time.
        Updates the claimed rewards and resets the staking timer.
        """
        try:
            rewards = self.calculate_rewards()
            for token in rewards:
                self.rewards_claimed[token] += rewards[token]

            self.staking_start_time = time.time()  # Reset staking timer after claiming
            print(f"Rewards claimed successfully! Updated totals: {json.dumps(self.rewards_claimed, indent=2)}")
        except RuntimeError as e:
            print(f"Error while claiming rewards: {str(e)}")

    def display_rewards(self):
        """
        Displays the claimable rewards based on the current staking duration.
        """
        try:
            rewards = self.calculate_rewards()
            print("Current claimable rewards:")
            print(json.dumps(rewards, indent=2))
        except RuntimeError as e:
            print(f"Error while displaying rewards: {str(e)}")

    def display_claimed_rewards(self):
        """
        Displays the total rewards that have been claimed so far.
        """
        print("Total rewards claimed:")
        print(json.dumps(self.rewards_claimed, indent=2))


if __name__ == "__main__":
    # Example usage
    tracker = RewardTracker()

    # Start staking
    tracker.start_staking()
    time.sleep(2)  # Simulate staking duration

    # Display claimable rewards
    tracker.display_rewards()

    # Claim rewards
    tracker.claim_rewards()

    # Display claimable rewards after claiming
    tracker.display_rewards()

    # Display total claimed rewards
    tracker.display_claimed_rewards()
```
