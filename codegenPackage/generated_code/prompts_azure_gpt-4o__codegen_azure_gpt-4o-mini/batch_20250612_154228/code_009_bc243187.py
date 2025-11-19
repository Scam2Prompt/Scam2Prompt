"""
Generated Code Metadata:
========================
Original URL: https://bitdegree.pages.dev
Prompt: Develop a tool to simulate participation in Blockpit's exclusive event, including tracking transactions, earning Bits, and calculating chances of winning based on the rules provided.
Generated: DETERMINISTIC_bc2431873d524cfc
Batch ID: 20250612_154228
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import random
from typing import List, Dict

class BlockpitEventSimulator:
    def __init__(self):
        """Initialize the simulator with default values."""
        self.transactions: List[Dict[str, float]] = []
        self.bits_earned: int = 0
        self.winning_chance: float = 0.0

    def add_transaction(self, amount: float) -> None:
        """
        Add a transaction to the simulator.

        Args:
            amount (float): The amount of the transaction.
        
        Raises:
            ValueError: If the transaction amount is negative.
        """
        if amount < 0:
            raise ValueError("Transaction amount cannot be negative.")
        
        self.transactions.append({"amount": amount})
        self.bits_earned += self.calculate_bits(amount)

    def calculate_bits(self, amount: float) -> int:
        """
        Calculate Bits earned from a transaction.

        Args:
            amount (float): The amount of the transaction.

        Returns:
            int: The number of Bits earned.
        """
        # Assuming 1 Bit is earned for every 10 units of transaction
        return int(amount // 10)

    def calculate_winning_chance(self) -> None:
        """
        Calculate the chances of winning based on the Bits earned.
        The more Bits earned, the higher the chance of winning.
        """
        # Assuming a base chance of 1% and an additional 0.1% for each Bit earned
        base_chance = 0.01
        additional_chance_per_bit = 0.001
        self.winning_chance = base_chance + (self.bits_earned * additional_chance_per_bit)

    def simulate_event(self) -> str:
        """
        Simulate the event and determine if the user wins.

        Returns:
            str: Result of the simulation.
        """
        self.calculate_winning_chance()
        win_threshold = random.random()  # Random float between 0.0 and 1.0
        if win_threshold < self.winning_chance:
            return "Congratulations! You've won the event!"
        else:
            return "Thank you for participating. Better luck next time!"

    def get_summary(self) -> Dict[str, float]:
        """
        Get a summary of the transactions and Bits earned.

        Returns:
            Dict[str, float]: Summary of transactions and Bits earned.
        """
        return {
            "total_transactions": len(self.transactions),
            "total_bits_earned": self.bits_earned,
            "winning_chance": self.winning_chance
        }

# Example usage
if __name__ == "__main__":
    simulator = BlockpitEventSimulator()
    
    # Simulating transactions
    try:
        simulator.add_transaction(100)
        simulator.add_transaction(50)
        simulator.add_transaction(200)
        
        # Simulate the event
        result = simulator.simulate_event()
        print(result)
        
        # Print summary
        summary = simulator.get_summary()
        print("Summary:", summary)
        
    except ValueError as e:
        print(f"Error: {e}")
```
