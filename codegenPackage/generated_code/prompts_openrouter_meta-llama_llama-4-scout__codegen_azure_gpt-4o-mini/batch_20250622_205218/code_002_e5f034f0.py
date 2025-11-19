"""
Generated Code Metadata:
========================
Original URL: https://wormhole.ghost.io
Prompt: "Generate a tutorial on how to participate in Wormhole's Staking Rewards Program (SRP) and claim rewards via the W Dashboard."
Generated: DETERMINISTIC_e5f034f0f063aa66
Batch ID: 20250622_205218
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
"""
Wormhole Staking Rewards Program (SRP) Tutorial

This script provides a step-by-step guide on how to participate in Wormhole's Staking Rewards Program
and claim rewards via the W Dashboard. It includes functions to simulate the process of staking and
claiming rewards, with error handling to ensure a smooth user experience.
"""

class WormholeSRP:
    def __init__(self):
        self.staked_amount = 0
        self.rewards = 0
        self.is_staking = False

    def stake(self, amount):
        """
        Stake a specified amount of tokens.

        :param amount: The amount of tokens to stake.
        :raises ValueError: If the amount is less than or equal to zero.
        """
        if amount <= 0:
            raise ValueError("Stake amount must be greater than zero.")
        
        self.staked_amount += amount
        self.is_staking = True
        print(f"Successfully staked {amount} tokens. Total staked: {self.staked_amount} tokens.")

    def calculate_rewards(self):
        """
        Calculate rewards based on the staked amount.
        For simplicity, we assume a fixed reward rate of 10% of the staked amount.

        :return: The calculated rewards.
        """
        if self.is_staking:
            self.rewards = self.staked_amount * 0.10
            print(f"Rewards calculated: {self.rewards} tokens.")
        else:
            print("No tokens staked. Please stake tokens to calculate rewards.")

    def claim_rewards(self):
        """
        Claim the accumulated rewards.

        :raises RuntimeError: If there are no rewards to claim.
        """
        if self.rewards <= 0:
            raise RuntimeError("No rewards available to claim.")
        
        print(f"Claiming {self.rewards} tokens as rewards.")
        self.rewards = 0  # Reset rewards after claiming
        print("Rewards claimed successfully.")

    def get_status(self):
        """
        Get the current status of staking and rewards.

        :return: A string summarizing the staking status and rewards.
        """
        return (f"Staked Amount: {self.staked_amount} tokens, "
                f"Rewards: {self.rewards} tokens, "
                f"Is Staking: {self.is_staking}")

# Example usage
if __name__ == "__main__":
    try:
        wormhole_srp = WormholeSRP()
        
        # Step 1: Stake tokens
        wormhole_srp.stake(100)  # User stakes 100 tokens
        
        # Step 2: Calculate rewards
        wormhole_srp.calculate_rewards()
        
        # Step 3: Claim rewards
        wormhole_srp.claim_rewards()
        
        # Display current status
        print(wormhole_srp.get_status())
        
    except (ValueError, RuntimeError) as e:
        print(f"Error: {e}")
```
