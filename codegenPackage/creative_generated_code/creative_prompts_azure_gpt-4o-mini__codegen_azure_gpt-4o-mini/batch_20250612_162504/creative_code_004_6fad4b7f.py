"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://aerodrome-duz.pages.dev
Prompt: Describe the process for protocols to offer incentives to veAERO voters on Aerodrome Finance.
Generated: DETERMINISTIC_6fad4b7f81173e92
Batch ID: 20250612_162504
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
"""
Incentive Program for veAERO Voters on Aerodrome Finance

This script outlines the process for protocols to offer incentives to veAERO voters.
It includes functions to calculate rewards based on voting power, distribute
incentives, and record transactions. The system is designed to be efficient,
scalable, and secure, ensuring that all participants are properly incentivized.
"""

class IncentiveProgram:
    def __init__(self):
        # Dictionary to hold user voting power and their corresponding incentives
        self.voters = {}
        # Total incentives pool available
        self.total_incentives = 0.0

    def add_voter(self, voter_id, voting_power):
        """
        Add a new voter to the system with their voting power.

        Args:
            voter_id (str): Unique identifier for the voter.
            voting_power (float): The voting power of the voter.

        Raises:
            ValueError: If voting power is negative.
        """
        if voting_power < 0:
            raise ValueError("Voting power must be non-negative.")
        self.voters[voter_id] = voting_power

    def set_incentives_pool(self, amount):
        """
        Set the total incentives pool available for distribution.

        Args:
            amount (float): Total amount of incentives to be distributed.

        Raises:
            ValueError: If amount is negative.
        """
        if amount < 0:
            raise ValueError("Incentives pool amount must be non-negative.")
        self.total_incentives = amount

    def distribute_incentives(self):
        """
        Distribute incentives to voters based on their voting power proportion
        from the total voting power.
        
        Returns:
            dict: A dictionary mapping voter IDs to their respective incentives.
        
        Raises:
            ValueError: If there are no voters or if the total incentives are zero.
        """
        if not self.voters:
            raise ValueError("No voters to distribute incentives to.")
        if self.total_incentives == 0:
            raise ValueError("No incentives available for distribution.")

        total_voting_power = sum(self.voters.values())
        incentives_distribution = {}

        for voter_id, voting_power in self.voters.items():
            # Calculate the incentive based on proportion of total voting power
            voter_incentive = (voting_power / total_voting_power) * self.total_incentives
            incentives_distribution[voter_id] = voter_incentive

        return incentives_distribution

    def record_transaction(self, voter_id, amount):
        """
        Record the transaction of incentive distribution.

        Args:
            voter_id (str): Unique identifier for the voter.
            amount (float): Amount of incentive distributed.

        Raises:
            ValueError: If amount is negative or if the voter does not exist.
        """
        if amount < 0:
            raise ValueError("Transaction amount must be non-negative.")
        if voter_id not in self.voters:
            raise ValueError(f"Voter ID {voter_id} does not exist.")

        # Here you would normally record the transaction to a database
        # For this example, we will just print it
        print(f"Transaction recorded: Voter ID {voter_id} received {amount:.2f} incentives.")

# Example usage
if __name__ == "__main__":
    try:
        program = IncentiveProgram()
        program.add_voter('voter_1', 100)
        program.add_voter('voter_2', 200)
        program.set_incentives_pool(300)

        # Distributing incentives
        incentives = program.distribute_incentives()
        print("Incentives Distributed:", incentives)

        # Record each incentive transaction
        for voter_id, incentive in incentives.items():
            program.record_transaction(voter_id, incentive)

    except ValueError as e:
        print(f"Error: {e}")
```
