"""
Generated Code Metadata:
========================
Original URL: https://wienerdog-addtoken.pages.dev
Prompt: Explain the tokenomics of WienerAI, including the distribution of $WAI tokens and the benefits of staking, and provide a sample code snippet for calculating staking rewards.
Generated: DETERMINISTIC_ae11d7f8ddbe39cb
Batch ID: 20250622_204722
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
class WienerAI:
    def __init__(self, total_supply: float, staking_rewards_rate: float):
        """
        Initialize the WienerAI tokenomics model.

        :param total_supply: Total supply of $WAI tokens.
        :param staking_rewards_rate: Annual staking rewards rate (as a decimal).
        """
        self.total_supply = total_supply
        self.staking_rewards_rate = staking_rewards_rate

    def calculate_staking_rewards(self, staked_amount: float, staking_duration: int) -> float:
        """
        Calculate the staking rewards based on the staked amount and duration.

        :param staked_amount: Amount of $WAI tokens staked.
        :param staking_duration: Duration of staking in days.
        :return: Calculated staking rewards.
        """
        if staked_amount < 0:
            raise ValueError("Staked amount must be non-negative.")
        if staking_duration < 0:
            raise ValueError("Staking duration must be non-negative.")

        # Calculate the annual rewards based on the staking rewards rate
        annual_rewards = staked_amount * self.staking_rewards_rate
        
        # Calculate daily rewards
        daily_rewards = annual_rewards / 365
        
        # Calculate total rewards for the given staking duration
        total_rewards = daily_rewards * staking_duration
        
        return total_rewards

# Example usage
if __name__ == "__main__":
    try:
        # Initialize the WienerAI tokenomics with a total supply of 1,000,000 $WAI and a 10% staking rewards rate
        wiener_ai = WienerAI(total_supply=1_000_000, staking_rewards_rate=0.10)

        # Calculate staking rewards for staking 1000 $WAI for 30 days
        staked_amount = 1000
        staking_duration = 30
        rewards = wiener_ai.calculate_staking_rewards(staked_amount, staking_duration)

        print(f"Staking rewards for {staked_amount} $WAI over {staking_duration} days: {rewards:.2f} $WAI")
    except ValueError as e:
        print(f"Error: {e}")
```
