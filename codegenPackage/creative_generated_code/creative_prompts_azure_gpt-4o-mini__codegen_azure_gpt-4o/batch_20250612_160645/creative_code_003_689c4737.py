"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://claims-runecoinio.pages.dev
Prompt: Generate a code snippet that simulates the mining of runes using activated RSICs and their corresponding allocation types.
Generated: DETERMINISTIC_689c4737e0ce10e0
Batch ID: 20250612_160645
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import random

# Define constants for RSIC types and allocation types
RSIC_TYPES = ["Fire", "Water", "Earth", "Air"]
ALLOCATION_TYPES = ["Standard", "Precision", "Balanced"]

class RuneMiningSimulator:
    """
    A simulator for mining runes using activated RSICs and their corresponding allocation types.
    """

    def __init__(self):
        """
        Initialize the simulator with available RSICs and allocation types.
        """
        self.rsics = RSIC_TYPES
        self.allocations = ALLOCATION_TYPES

    def activate_rsic(self, rsic_type):
        """
        Activates a given RSIC type for rune mining.

        Args:
            rsic_type (str): The RSIC type to activate.

        Returns:
            bool: True if activation is successful, False otherwise.
        """
        if rsic_type not in self.rsics:
            print(f"Error: RSIC type '{rsic_type}' is invalid.")
            return False
        print(f"RSIC '{rsic_type}' activated successfully.")
        return True

    def mine_rune(self, rsic_type, allocation_type):
        """
        Simulates mining a rune using an activated RSIC and allocation type.

        Args:
            rsic_type (str): The activated RSIC type.
            allocation_type (str): The allocation type for mining.

        Returns:
            dict: A dictionary containing mined rune details.
        """
        if rsic_type not in self.rsics:
            raise ValueError(f"RSIC type '{rsic_type}' is invalid.")
        if allocation_type not in self.allocations:
            raise ValueError(f"Allocation type '{allocation_type}' is invalid.")

        # Simulate rune mining outcome
        mined_rune = {
            'rsic_type': rsic_type,
            'allocation_type': allocation_type,
            'rune_name': f"{rsic_type} Rune",
            'quantity': random.randint(1, 10),
            'quality': random.choice(["Low", "Medium", "High"])
        }
        return mined_rune

def main():
    """
    Main function to demonstrate the rune mining simulation.
    """
    simulator = RuneMiningSimulator()

    # Activate an RSIC
    rsic_type = "Fire"
    if not simulator.activate_rsic(rsic_type):
        return

    # Simulate rune mining
    allocation_type = "Precision"
    try:
        mined_rune = simulator.mine_rune(rsic_type, allocation_type)
        print("Rune Mining Result:")
        for key, value in mined_rune.items():
            print(f"  {key}: {value}")
    except ValueError as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    main()
```
