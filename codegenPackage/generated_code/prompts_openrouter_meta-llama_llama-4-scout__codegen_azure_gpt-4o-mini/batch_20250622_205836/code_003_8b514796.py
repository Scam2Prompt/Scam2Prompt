"""
Generated Code Metadata:
========================
Original URL: https://stargate-dwg.pages.dev
Prompt: Generate a code example for calculating voting power on Stargate based on locked STG tokens and average lock time.
Generated: DETERMINISTIC_8b514796c49f795e
Batch ID: 20250622_205836
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
class VotingPowerCalculator:
    """
    A class to calculate voting power based on locked STG tokens and average lock time.
    """

    def __init__(self, locked_tokens: float, average_lock_time: float):
        """
        Initializes the VotingPowerCalculator with locked tokens and average lock time.

        :param locked_tokens: The amount of STG tokens locked.
        :param average_lock_time: The average lock time in days.
        """
        if locked_tokens < 0:
            raise ValueError("Locked tokens cannot be negative.")
        if average_lock_time < 0:
            raise ValueError("Average lock time cannot be negative.")

        self.locked_tokens = locked_tokens
        self.average_lock_time = average_lock_time

    def calculate_voting_power(self) -> float:
        """
        Calculates the voting power based on locked tokens and average lock time.

        :return: The calculated voting power.
        """
        # Define a constant for the voting power multiplier
        VOTING_POWER_MULTIPLIER = 1.5

        # Calculate voting power
        voting_power = self.locked_tokens * (self.average_lock_time ** 0.5) * VOTING_POWER_MULTIPLIER

        return voting_power

def main():
    """
    Main function to demonstrate the VotingPowerCalculator.
    """
    try:
        # Example values for locked tokens and average lock time
        locked_tokens = 1000.0  # Example: 1000 STG tokens locked
        average_lock_time = 30.0  # Example: average lock time of 30 days

        # Create an instance of the VotingPowerCalculator
        calculator = VotingPowerCalculator(locked_tokens, average_lock_time)

        # Calculate and print the voting power
        voting_power = calculator.calculate_voting_power()
        print(f"Voting Power: {voting_power:.2f}")

    except ValueError as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    main()
```
