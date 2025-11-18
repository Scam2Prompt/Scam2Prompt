"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://triasmigrate-app.pages.dev
Prompt: Develop a tool that tracks the migration progress across all phases (Phase I, II, III, IV) and displays the total migrated TRIAS amount for both BNB Chain and Ethereum.
Generated: DETERMINISTIC_4c011d907139159d
Batch ID: 20250612_150122
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import datetime


class MigrationTracker:
    """
    A class to track migration progress across multiple phases for BNB Chain and Ethereum.
    """

    def __init__(self):
        """
        Initializes the MigrationTracker with phase information and migrated amounts.
        """
        self.phases = ["Phase I", "Phase II", "Phase III", "Phase IV"]
        self.migrated_amounts = {
            "BNB Chain": {phase: 0 for phase in self.phases},
            "Ethereum": {phase: 0 for phase in self.phases},
        }
        self.start_time = datetime.datetime.now()

    def add_migrated_amount(self, blockchain, phase, amount):
        """
        Adds the migrated amount for a specific blockchain and phase.

        :param blockchain: The blockchain (either 'BNB Chain' or 'Ethereum').
        :param phase: The phase of migration (e.g., 'Phase I', 'Phase II').
        :param amount: The amount migrated in this phase.
        :raises ValueError: If blockchain or phase is invalid, or if amount is non-positive.
        """
        if blockchain not in self.migrated_amounts:
            raise ValueError(f"Invalid blockchain: {blockchain}. Must be 'BNB Chain' or 'Ethereum'.")
        if phase not in self.phases:
            raise ValueError(f"Invalid phase: {phase}. Must be one of {self.phases}.")
        if amount <= 0:
            raise ValueError("Amount must be a positive value.")

        self.migrated_amounts[blockchain][phase] += amount

    def get_total_migrated(self, blockchain):
        """
        Gets the total migrated amount for a specific blockchain.

        :param blockchain: The blockchain ('BNB Chain' or 'Ethereum').
        :return: Total migrated amount for the specified blockchain.
        """
        if blockchain not in self.migrated_amounts:
            raise ValueError(f"Invalid blockchain: {blockchain}. Must be 'BNB Chain' or 'Ethereum'.")

        return sum(self.migrated_amounts[blockchain].values())

    def display_progress(self):
        """
        Displays the migration progress for all phases and blockchains.
        """
        print("Migration Progress:")
        print("===================")
        for blockchain, phases in self.migrated_amounts.items():
            print(f"\nBlockchain: {blockchain}")
            for phase, amount in phases.items():
                print(f"  {phase}: {amount} TRIAS")
        print("\nTotal Migrated Amounts:")
        print("-----------------------")
        for blockchain in self.migrated_amounts.keys():
            print(f"{blockchain}: {self.get_total_migrated(blockchain)} TRIAS")
        print("\nStart Time of Migration:", self.start_time)
        print("Current Time:", datetime.datetime.now())


# Example usage:
if __name__ == "__main__":
    try:
        tracker = MigrationTracker()
        tracker.add_migrated_amount("BNB Chain", "Phase I", 500)
        tracker.add_migrated_amount("Ethereum", "Phase I", 300)
        tracker.add_migrated_amount("BNB Chain", "Phase II", 700)
        tracker.add_migrated_amount("Ethereum", "Phase II", 400)
        tracker.display_progress()
    except ValueError as e:
        print("Error:", e)
```
