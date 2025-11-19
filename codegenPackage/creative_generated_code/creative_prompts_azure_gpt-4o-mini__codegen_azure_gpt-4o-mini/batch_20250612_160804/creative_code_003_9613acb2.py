"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://dappadapp.pages.dev
Prompt: Describe the unique staking and distribution methodology used by Dappad to ensure fair fundraising participation.
Generated: DETERMINISTIC_9613acb2568c55ca
Batch ID: 20250612_160804
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
class DappadStaking:
    """
    A class to represent Dappad's unique staking and distribution methodology 
    for fair fundraising participation.

    Attributes:
        total_funds (float): Total funds raised through staking.
        stakers (dict): A dictionary to keep track of each staker's stake.
        max_stake (float): Maximum amount a single participant can stake.
        min_stake (float): Minimum amount a single participant must stake.
    """

    def __init__(self, min_stake: float, max_stake: float):
        """
        Initializes the DappadStaking class with minimum and maximum stake limits.

        Args:
            min_stake (float): Minimum required stake for participation.
            max_stake (float): Maximum allowed stake for a single participant.
        """
        self.total_funds = 0.0
        self.stakers = {}
        self.min_stake = min_stake
        self.max_stake = max_stake

    def stake(self, participant_id: str, amount: float) -> None:
        """
        Allows participants to stake funds.

        Args:
            participant_id (str): Unique identifier for the participant.
            amount (float): The amount to stake.

        Raises:
            ValueError: If the stake amount is not within the allowed range.
            KeyError: If the participant ID is already staked.
        """
        if amount < self.min_stake or amount > self.max_stake:
            raise ValueError(f"Stake amount must be between {self.min_stake} and {self.max_stake}.")
        
        if participant_id in self.stakers:
            raise KeyError(f"Participant {participant_id} has already staked.")

        self.stakers[participant_id] = amount
        self.total_funds += amount
        print(f"Participant {participant_id} staked {amount}. Total funds: {self.total_funds}")

    def distribute_rewards(self) -> dict:
        """
        Distributes rewards to participants based on their stake proportion.

        Returns:
            dict: A dictionary with participant IDs and their respective rewards.
        
        Raises:
            ValueError: If there are no funds available to distribute.
        """
        if self.total_funds == 0:
            raise ValueError("No funds available for distribution.")

        rewards = {}
        for participant_id, stake in self.stakers.items():
            reward = stake / self.total_funds * 100  # Example reward calculation
            rewards[participant_id] = reward
            print(f"Participant {participant_id} receives a reward of {reward:.2f}%")

        return rewards

    def get_staker_info(self, participant_id: str) -> float:
        """
        Retrieves the stake of a particular participant.

        Args:
            participant_id (str): Unique identifier for the participant.

        Returns:
            float: The amount staked by the participant.

        Raises:
            KeyError: If the participant ID does not exist.
        """
        try:
            return self.stakers[participant_id]
        except KeyError:
            raise KeyError(f"Participant {participant_id} has not staked any funds.")

# Example usage:
if __name__ == "__main__":
    try:
        dappad = DappadStaking(min_stake=10.0, max_stake=1000.0)
        dappad.stake("user1", 500.0)
        dappad.stake("user2", 300.0)
        rewards = dappad.distribute_rewards()
        print("Rewards distribution:", rewards)
    except (ValueError, KeyError) as e:
        print(f"Error: {e}")
```
