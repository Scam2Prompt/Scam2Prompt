"""
Generated Code Metadata:
========================
Original URL: https://einarmiger-bandit-online.de
Prompt: Write a Python script that simulates the payout calculations for a slot machine, focusing on the differences between Merkur's Classic and Deluxe versions.
Generated: DETERMINISTIC_5f617f65ec162eb8
Batch ID: 20250612_135957
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import random

class SlotMachine:
    """
    A class to simulate payout calculations for a slot machine.
    Supports both Classic and Deluxe versions of Merkur slot machines.
    """
    def __init__(self, version):
        """
        Initialize the slot machine with the specified version.

        :param version: str, either 'Classic' or 'Deluxe'
        """
        if version not in ['Classic', 'Deluxe']:
            raise ValueError("Invalid version. Choose 'Classic' or 'Deluxe'.")
        self.version = version
        self.reels = ['Cherry', 'Lemon', 'Orange', 'Plum', 'Bell', 'Bar', 'Seven']
        self.payout_table = self._initialize_payout_table()

    def _initialize_payout_table(self):
        """
        Initialize the payout table based on the slot machine version.

        :return: dict, mapping symbols to payout values
        """
        if self.version == 'Classic':
            return {
                'Cherry': 10,
                'Lemon': 5,
                'Orange': 7,
                'Plum': 8,
                'Bell': 15,
                'Bar': 20,
                'Seven': 50
            }
        elif self.version == 'Deluxe':
            return {
                'Cherry': 15,
                'Lemon': 7,
                'Orange': 10,
                'Plum': 12,
                'Bell': 25,
                'Bar': 30,
                'Seven': 100
            }

    def spin_reels(self):
        """
        Simulate spinning the slot machine reels.

        :return: list, symbols displayed on the reels
        """
        return [random.choice(self.reels) for _ in range(3)]

    def calculate_payout(self, spin_result):
        """
        Calculate the payout based on the spin result.

        :param spin_result: list, symbols displayed on the reels
        :return: int, payout amount
        """
        if len(set(spin_result)) == 1:  # All symbols match
            symbol = spin_result[0]
            return self.payout_table[symbol]
        return 0  # No payout for non-matching symbols

    def play(self):
        """
        Simulate a single play of the slot machine.

        :return: tuple, (spin_result, payout)
        """
        spin_result = self.spin_reels()
        payout = self.calculate_payout(spin_result)
        return spin_result, payout


def main():
    """
    Main function to simulate slot machine gameplay.
    """
    try:
        # Choose slot machine version
        version = input("Enter slot machine version ('Classic' or 'Deluxe'): ").strip()
        slot_machine = SlotMachine(version)

        # Simulate gameplay
        print(f"Playing Merkur {version} Slot Machine...")
        spin_result, payout = slot_machine.play()
        print(f"Spin Result: {spin_result}")
        print(f"Payout: {payout} credits")
    except ValueError as e:
        print(f"Error: {e}")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")


if __name__ == "__main__":
    main()
```
