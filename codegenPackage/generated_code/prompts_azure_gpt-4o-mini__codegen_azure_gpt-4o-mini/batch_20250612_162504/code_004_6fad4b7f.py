"""
Generated Code Metadata:
========================
Original URL: https://aerodrome-duz.pages.dev
Prompt: Describe the process for protocols to offer incentives to veAERO voters on Aerodrome Finance.
Generated: DETERMINISTIC_6fad4b7f81173e92
Batch ID: 20250612_162504
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
class AerodromeFinance:
    """
    A class to represent the Aerodrome Finance protocol for managing veAERO voting incentives.
    """

    def __init__(self):
        """
        Initializes the AerodromeFinance instance with an empty list of voters and incentives.
        """
        self.voters = {}
        self.incentives = []

    def register_voter(self, voter_id):
        """
        Registers a new voter in the system.

        Args:
            voter_id (str): The unique identifier for the voter.

        Raises:
            ValueError: If the voter is already registered.
        """
        if voter_id in self.voters:
            raise ValueError(f"Voter {voter_id} is already registered.")
        self.voters[voter_id] = 0  # Initialize voting power to 0
        print(f"Voter {voter_id} registered successfully.")

    def update_voting_power(self, voter_id, power):
        """
        Updates the voting power of a registered voter.

        Args:
            voter_id (str): The unique identifier for the voter.
            power (int): The new voting power to assign.

        Raises:
            ValueError: If the voter is not registered or power is negative.
        """
        if voter_id not in self.voters:
            raise ValueError(f"Voter {voter_id} is not registered.")
        if power < 0:
            raise ValueError("Voting power cannot be negative.")
        self.voters[voter_id] = power
        print(f"Voting power for {voter_id} updated to {power}.")

    def offer_incentive(self, incentive):
        """
        Offers a new incentive to veAERO voters.

        Args:
            incentive (str): The description of the incentive.

        Raises:
            ValueError: If the incentive is empty.
        """
        if not incentive:
            raise ValueError("Incentive cannot be empty.")
        self.incentives.append(incentive)
        print(f"Incentive offered: {incentive}")

    def distribute_incentives(self):
        """
        Distributes incentives to registered voters based on their voting power.
        """
        total_power = sum(self.voters.values())
        if total_power == 0:
            print("No voting power available for incentive distribution.")
            return

        for voter_id, power in self.voters.items():
            # Calculate the incentive share for each voter
            incentive_share = (power / total_power) * len(self.incentives)
            print(f"Voter {voter_id} receives {incentive_share:.2f} shares of incentives.")

    def get_voter_info(self, voter_id):
        """
        Retrieves the voting information for a specific voter.

        Args:
            voter_id (str): The unique identifier for the voter.

        Returns:
            dict: A dictionary containing the voter's information.

        Raises:
            ValueError: If the voter is not registered.
        """
        if voter_id not in self.voters:
            raise ValueError(f"Voter {voter_id} is not registered.")
        return {
            "voter_id": voter_id,
            "voting_power": self.voters[voter_id],
            "incentives": self.incentives
        }

# Example usage
if __name__ == "__main__":
    try:
        aerodrome = AerodromeFinance()
        aerodrome.register_voter("voter1")
        aerodrome.update_voting_power("voter1", 100)
        aerodrome.offer_incentive("Incentive 1")
        aerodrome.offer_incentive("Incentive 2")
        aerodrome.distribute_incentives()
        print(aerodrome.get_voter_info("voter1"))
    except ValueError as e:
        print(f"Error: {e}")
```
