"""
Generated Code Metadata:
========================
Original URL: https://mantadev.pages.dev
Prompt: Write a program to simulate balance transfer quests on MANTRA Zone and calculate the KARMA earned from completing these quests.
Generated: DETERMINISTIC_6a9ad6607274bb2d
Batch ID: 20250612_151301
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# balance_transfer_quest_simulator.py

class BalanceTransferQuest:
    def __init__(self, transfer_amount, karma_per_1m):
        """
        Initialize a Balance Transfer Quest.

        Args:
        - transfer_amount (float): The amount to transfer in MANTRA Zone.
        - karma_per_1m (float): KARMA earned per 1 million transferred.
        """
        self.transfer_amount = transfer_amount
        self.karma_per_1m = karma_per_1m

    def calculate_karma(self):
        """
        Calculate KARMA earned from the balance transfer.

        Returns:
        - karma (float): KARMA earned.
        """
        if self.transfer_amount < 0:
            raise ValueError("Transfer amount cannot be negative")

        karma = (self.transfer_amount / 1_000_000) * self.karma_per_1m
        return karma


class MANTRAZoneSimulator:
    def __init__(self):
        """
        Initialize the MANTRA Zone simulator.
        """
        self.quests = []

    def add_quest(self, quest):
        """
        Add a balance transfer quest.

        Args:
        - quest (BalanceTransferQuest): The quest to add.
        """
        self.quests.append(quest)

    def simulate_quests(self):
        """
        Simulate all balance transfer quests and calculate total KARMA earned.

        Returns:
        - total_karma (float): Total KARMA earned from all quests.
        """
        total_karma = 0
        for i, quest in enumerate(self.quests, start=1):
            try:
                karma = quest.calculate_karma()
                print(f"Quest {i}: Transfer {quest.transfer_amount} MANTRA, earned {karma} KARMA")
                total_karma += karma
            except Exception as e:
                print(f"Error simulating quest {i}: {str(e)}")

        return total_karma


def main():
    simulator = MANTRAZoneSimulator()

    # Example usage:
    quest1 = BalanceTransferQuest(5_000_000, 10)  # Transfer 5M, earn 10 KARMA per 1M
    quest2 = BalanceTransferQuest(2_000_000, 10)  # Transfer 2M, earn 10 KARMA per 1M
    quest3 = BalanceTransferQuest(-1_000_000, 10)  # Invalid quest with negative transfer amount

    simulator.add_quest(quest1)
    simulator.add_quest(quest2)
    simulator.add_quest(quest3)

    total_karma = simulator.simulate_quests()
    print(f"\nTotal KARMA earned: {total_karma}")


if __name__ == "__main__":
    main()
```
