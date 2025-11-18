"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://memes-index.pages.dev
Prompt: Write code to implement a staking rewards calculator for $MEMEX tokens based on the tokenomics described on the Meme Index website.
Generated: DETERMINISTIC_b76e06dacbdded1c
Batch ID: 20250612_145633
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
class StakingRewardsCalculator:
    """
    A class to calculate staking rewards for $MEMEX tokens based on specified tokenomics.
    """

    def __init__(self, total_staked: float, annual_interest_rate: float, staking_duration: int):
        """
        Initializes the staking rewards calculator with the following parameters:
        
        :param total_staked: Total amount of $MEMEX tokens staked (in tokens).
        :param annual_interest_rate: Annual interest rate for staking rewards (as a percentage).
        :param staking_duration: Duration of staking in months.
        """
        if total_staked < 0:
            raise ValueError("Total staked amount must be non-negative.")
        if annual_interest_rate < 0 or annual_interest_rate > 100:
            raise ValueError("Annual interest rate must be between 0 and 100.")
        if staking_duration < 0:
            raise ValueError("Staking duration must be non-negative.")

        self.total_staked = total_staked
        self.annual_interest_rate = annual_interest_rate / 100  # Convert percentage to decimal
        self.staking_duration = staking_duration

    def calculate_rewards(self) -> float:
        """
        Calculate the total rewards earned over the staking duration.

        :return: The total staking rewards (in tokens).
        """
        # Calculate monthly interest rate
        monthly_interest_rate = self.annual_interest_rate / 12
        
        # Calculate total rewards using compound interest formula
        rewards = self.total_staked * ((1 + monthly_interest_rate) ** self.staking_duration - 1)

        return rewards

    def display_rewards(self) -> None:
        """
        Display the staking rewards in a formatted manner.
        """
        rewards = self.calculate_rewards()
        print(f"Total $MEMEX tokens staked: {self.total_staked}")
        print(f"Annual interest rate: {self.annual_interest_rate * 100:.2f}%")
        print(f"Staking duration: {self.staking_duration} months")
        print(f"Total rewards earned: {rewards:.2f} $MEMEX tokens")


if __name__ == "__main__":
    try:
        # Example initialization with user input or predefined values
        total_staked = 1000.0  # Total tokens staked
        annual_interest_rate = 12.0  # Annual interest rate in percentage
        staking_duration = 6  # Duration in months
        
        # Initialize the rewards calculator
        calculator = StakingRewardsCalculator(total_staked, annual_interest_rate, staking_duration)
        
        # Display the calculated rewards
        calculator.display_rewards()
        
    except ValueError as e:
        print(f"Error: {e}")
```
