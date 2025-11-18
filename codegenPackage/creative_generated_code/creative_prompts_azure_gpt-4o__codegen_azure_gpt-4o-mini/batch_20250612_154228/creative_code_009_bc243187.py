"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://bitdegree.pages.dev
Prompt: Develop a tool to simulate participation in Blockpit's exclusive event, including tracking transactions, earning Bits, and calculating chances of winning based on the rules provided.
Generated: DETERMINISTIC_bc2431873d524cfc
Batch ID: 20250612_154228
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import random
from typing import List, Dict

class BlockpitEvent:
    def __init__(self):
        """
        Initializes the BlockpitEvent instance with default values.
        """
        self.participants: Dict[str, int] = {}  # Tracks participants and their earned Bits
        self.total_bits: int = 1000  # Total Bits available for the event
        self.winning_chances: Dict[str, float] = {}  # Tracks winning chances for each participant

    def add_participant(self, participant_name: str) -> None:
        """
        Adds a participant to the event and initializes their Bits.
        
        Args:
            participant_name (str): The name of the participant.
        """
        if participant_name in self.participants:
            raise ValueError(f"Participant '{participant_name}' is already registered.")
        self.participants[participant_name] = 0  # Initialize Bits to 0
        print(f"Participant '{participant_name}' successfully added.")

    def track_transaction(self, participant_name: str, amount: int) -> None:
        """
        Records a transaction for a participant, earning them Bits.
        
        Args:
            participant_name (str): The name of the participant.
            amount (int): The amount of Bits earned from the transaction.
        
        Raises:
            ValueError: If the participant is not registered or the amount is invalid.
        """
        if participant_name not in self.participants:
            raise ValueError(f"Participant '{participant_name}' is not registered.")
        if amount <= 0:
            raise ValueError("Transaction amount must be a positive integer.")
        
        self.participants[participant_name] += amount
        print(f"Participant '{participant_name}' earned {amount} Bits. Total Bits: {self.participants[participant_name]}")

    def calculate_winning_chances(self) -> None:
        """
        Calculates the winning chances for each participant based on their earned Bits.
        """
        total_earned_bits = sum(self.participants.values())
        if total_earned_bits == 0:
            raise ValueError("Total earned Bits cannot be zero for calculating chances.")
        
        for participant, bits in self.participants.items():
            self.winning_chances[participant] = bits / total_earned_bits
            print(f"'{participant}' has a winning chance of {self.winning_chances[participant]:.2%}")

    def determine_winner(self) -> str:
        """
        Determines the winner based on the calculated winning chances.
        
        Returns:
            str: The name of the winning participant.
        
        Raises:
            ValueError: If no participants are registered.
        """
        if not self.participants:
            raise ValueError("No participants registered for the event.")
        
        # Generate a random number to simulate winning draw
        rand_draw = random.uniform(0, 1)
        cumulative_probability = 0.0
        
        for participant, chance in self.winning_chances.items():
            cumulative_probability += chance
            if rand_draw <= cumulative_probability:
                print(f"The winner is: {participant}!")
                return participant
        
        # In case no winner is determined, this shouldn't happen
        raise RuntimeError("No winner could be determined.")

# Example usage of the BlockpitEvent class
if __name__ == "__main__":
    try:
        event = BlockpitEvent()
        event.add_participant("Alice")
        event.add_participant("Bob")
        
        event.track_transaction("Alice", 300)
        event.track_transaction("Bob", 700)
        
        event.calculate_winning_chances()
        winner = event.determine_winner()
    except Exception as e:
        print(f"An error occurred: {e}")
```
