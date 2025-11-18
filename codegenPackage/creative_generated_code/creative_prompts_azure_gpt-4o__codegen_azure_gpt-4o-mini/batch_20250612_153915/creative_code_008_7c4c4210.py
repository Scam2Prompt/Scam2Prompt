"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://ton-448f1f.webflow.io
Prompt: Write a script to simulate the staking process for Airdrop Nodes and calculate expected rewards in $TONCAP tokens based on user input parameters.
Generated: DETERMINISTIC_7c4c4210f19a749c
Batch ID: 20250612_153915
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
class StakingSimulation:
    """
    A class to simulate the staking process for Airdrop Nodes and calculate
    expected rewards in $TONCAP tokens based on user input parameters.
    """

    def __init__(self, staking_amount, reward_rate, staking_duration):
        """
        Initializes the StakingSimulation with user-defined parameters.

        :param staking_amount: The amount of tokens to stake (in $TONCAP)
        :param reward_rate: The annual reward rate as a percentage (e.g., 5 for 5%)
        :param staking_duration: The duration of the stake in days
        """
        self.staking_amount = staking_amount
        self.reward_rate = reward_rate
        self.staking_duration = staking_duration

    def calculate_rewards(self):
        """
        Calculates the expected rewards based on the staking parameters.

        :return: The expected rewards in $TONCAP tokens
        """
        if self.staking_duration <= 0:
            raise ValueError("Staking duration must be greater than zero.")
        
        if self.reward_rate < 0:
            raise ValueError("Reward rate must be non-negative.")
        
        # Convert annual reward rate to daily rate
        daily_rate = self.reward_rate / 100 / 365
        
        # Calculate the total rewards
        rewards = self.staking_amount * daily_rate * self.staking_duration
        return rewards

    def display_rewards(self):
        """
        Displays the calculated rewards to the user.
        """
        try:
            rewards = self.calculate_rewards()
            print(f"Expected rewards for staking {self.staking_amount} $TONCAP "
                  f"for {self.staking_duration} days at a reward rate of "
                  f"{self.reward_rate}% is: {rewards:.2f} $TONCAP.")
        except ValueError as e:
            print(f"Error: {str(e)}")


if __name__ == "__main__":
    # Sample user input
    try:
        staking_amount = float(input("Enter staking amount in $TONCAP: "))
        reward_rate = float(input("Enter reward rate in percent: "))
        staking_duration = int(input("Enter staking duration in days: "))

        # Create StakingSimulation instance
        staking_simulation = StakingSimulation(staking_amount, reward_rate, staking_duration)
        
        # Display expected rewards
        staking_simulation.display_rewards()

    except ValueError as e:
        print(f"Invalid input: {str(e)}. Please enter numeric values only.")
```
