"""
Generated Code Metadata:
========================
Original URL: https://app-virtuswap.pages.dev
Prompt: Write code to simulate a staking mechanism for a DeFi application, inspired by the Virtuswap staking functionality.
Generated: DETERMINISTIC_94bfced884177923
Batch ID: 20250612_152527
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# staking_mechanism.py

from datetime import datetime, timedelta
from typing import Dict

class StakingMechanism:
    """
    Simulates a staking mechanism for a DeFi application.
    """

    def __init__(self):
        # Initialize an empty dictionary to store staker information
        self.stakers: Dict[str, Staker] = {}

    def add_staker(self, staker_id: str, amount: float, duration: int):
        """
        Adds a new staker to the staking mechanism.

        Args:
        - staker_id (str): Unique identifier for the staker.
        - amount (float): The amount of tokens to stake.
        - duration (int): The staking duration in days.

        Raises:
        - ValueError: If the staker_id already exists or if the amount/duration is invalid.
        """
        if staker_id in self.stakers:
            raise ValueError("Staker ID already exists")

        if amount <= 0 or duration <= 0:
            raise ValueError("Invalid amount or duration")

        # Create a new Staker object and add it to the dictionary
        self.stakers[staker_id] = Staker(staker_id, amount, duration)

    def remove_staker(self, staker_id: str):
        """
        Removes a staker from the staking mechanism.

        Args:
        - staker_id (str): Unique identifier for the staker.

        Raises:
        - KeyError: If the staker_id does not exist.
        """
        if staker_id not in self.stakers:
            raise KeyError("Staker ID does not exist")

        # Remove the staker from the dictionary
        del self.stakers[staker_id]

    def get_staker_info(self, staker_id: str):
        """
        Retrieves information about a staker.

        Args:
        - staker_id (str): Unique identifier for the staker.

        Returns:
        - Staker: The Staker object associated with the staker_id.

        Raises:
        - KeyError: If the staker_id does not exist.
        """
        if staker_id not in self.stakers:
            raise KeyError("Staker ID does not exist")

        # Return the Staker object
        return self.stakers[staker_id]

    def stake(self, staker_id: str):
        """
        Simulates the staking process for a staker.

        Args:
        - staker_id (str): Unique identifier for the staker.

        Raises:
        - KeyError: If the staker_id does not exist.
        """
        if staker_id not in self.stakers:
            raise KeyError("Staker ID does not exist")

        # Get the Staker object
        staker = self.stakers[staker_id]

        # Update the staking status and end time
        staker.stake()

    def unstake(self, staker_id: str):
        """
        Simulates the unstaking process for a staker.

        Args:
        - staker_id (str): Unique identifier for the staker.

        Raises:
        - KeyError: If the staker_id does not exist.
        """
        if staker_id not in self.stakers:
            raise KeyError("Staker ID does not exist")

        # Get the Staker object
        staker = self.stakers[staker_id]

        # Update the staking status and end time
        staker.unstake()


class Staker:
    """
    Represents a staker in the staking mechanism.
    """

    def __init__(self, staker_id: str, amount: float, duration: int):
        # Initialize the staker's properties
        self.staker_id = staker_id
        self.amount = amount
        self.duration = duration
        self.start_time = None
        self.end_time = None
        self.staked = False

    def stake(self):
        """
        Simulates the staking process.
        """
        if not self.staked:
            # Update the staking status and start time
            self.staked = True
            self.start_time = datetime.now()
            self.end_time = self.start_time + timedelta(days=self.duration)
            print(f"Staker {self.staker_id} staked {self.amount} tokens for {self.duration} days.")

    def unstake(self):
        """
        Simulates the unstaking process.
        """
        if self.staked:
            # Check if the staking period has ended
            if datetime.now() >= self.end_time:
                # Update the staking status
                self.staked = False
                print(f"Staker {self.staker_id} unstaked {self.amount} tokens.")
            else:
                print(f"Staker {self.staker_id} cannot unstake yet. Staking period ends at {self.end_time}.")


def main():
    staking_mechanism = StakingMechanism()

    # Add stakers
    staking_mechanism.add_staker("staker1", 1000.0, 30)
    staking_mechanism.add_staker("staker2", 500.0, 60)

    # Stake
    staking_mechanism.stake("staker1")
    staking_mechanism.stake("staker2")

    # Get staker info
    staker = staking_mechanism.get_staker_info("staker1")
    print(f"Staker {staker.staker_id} - Amount: {staker.amount}, Duration: {staker.duration}, Staked: {staker.staked}")

    # Unstake
    staking_mechanism.unstake("staker1")

if __name__ == "__main__":
    main()
```
