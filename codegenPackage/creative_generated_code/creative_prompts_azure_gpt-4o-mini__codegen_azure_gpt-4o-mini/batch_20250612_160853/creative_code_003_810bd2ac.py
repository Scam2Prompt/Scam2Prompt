"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://monprotocol-4yq.pages.dev
Prompt: Provide an example of how to implement a raffle system for distributing waitlist lots in a presale event.
Generated: DETERMINISTIC_810bd2aca10d3a46
Batch ID: 20250612_160853
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import random
from typing import List, Dict, Any

class RaffleSystem:
    def __init__(self):
        """Initialize the Raffle System with an empty list of participants."""
        self.participants: List[str] = []
        self.winners: List[str] = []

    def add_participant(self, participant: str) -> None:
        """
        Add a participant to the raffle.
        
        :param participant: The name of the participant to add.
        :raises ValueError: If the participant is already in the raffle.
        """
        if participant in self.participants:
            raise ValueError(f"Participant '{participant}' is already in the raffle.")
        self.participants.append(participant)

    def draw_winners(self, num_winners: int) -> List[str]:
        """
        Draw winners from the list of participants.
        
        :param num_winners: The number of winners to draw.
        :raises ValueError: If the number of winners exceeds the number of participants.
        :return: A list of winner names.
        """
        if num_winners > len(self.participants):
            raise ValueError("Number of winners exceeds number of participants.")
        
        self.winners = random.sample(self.participants, num_winners)
        return self.winners

    def get_winners(self) -> List[str]:
        """
        Get the list of winners.
        
        :return: A list of winner names.
        :raises RuntimeError: If no winners have been drawn yet.
        """
        if not self.winners:
            raise RuntimeError("No winners have been drawn yet.")
        return self.winners

    def reset_raffle(self) -> None:
        """Reset the raffle system by clearing the participants and winners."""
        self.participants.clear()
        self.winners.clear()

# Example usage
if __name__ == "__main__":
    raffle = RaffleSystem()

    # Add participants
    try:
        raffle.add_participant("Alice")
        raffle.add_participant("Bob")
        raffle.add_participant("Charlie")
        raffle.add_participant("David")
    except ValueError as e:
        print(e)

    # Draw winners
    try:
        winners = raffle.draw_winners(2)
        print("Winners drawn:", winners)
    except ValueError as e:
        print(e)

    # Retrieve winners
    try:
        winners_list = raffle.get_winners()
        print("Current winners:", winners_list)
    except RuntimeError as e:
        print(e)

    # Reset the raffle for the next event
    raffle.reset_raffle()
    print("Raffle has been reset.")
```
