"""
Generated Code Metadata:
========================
Original URL: https://lzero.us
Prompt: Generate code to implement a raffle system for events like the Pickleball Speed Dating described on the L-Zero website, where participants can register and winners are randomly selected.
Generated: DETERMINISTIC_b2eadd3b07ff1f34
Batch ID: 20250612_145626
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

class RaffleSystem:
    def __init__(self):
        """Initialize the RaffleSystem with an empty participant list."""
        self.participants: List[str] = []

    def register_participant(self, name: str) -> None:
        """
        Register a participant for the raffle.

        Args:
            name (str): The name of the participant to register.

        Raises:
            ValueError: If the participant name is empty or already registered.
        """
        if not name:
            raise ValueError("Participant name cannot be empty.")
        if name in self.participants:
            raise ValueError(f"{name} is already registered.")
        
        self.participants.append(name)
        print(f"{name} has been registered successfully.")

    def draw_winner(self) -> str:
        """
        Randomly select a winner from the registered participants.

        Returns:
            str: The name of the winner.

        Raises:
            RuntimeError: If there are no participants to draw from.
        """
        if not self.participants:
            raise RuntimeError("No participants registered for the raffle.")
        
        winner = random.choice(self.participants)
        return winner

    def get_participants(self) -> List[str]:
        """
        Get the list of registered participants.

        Returns:
            List[str]: A list of participant names.
        """
        return self.participants

# Example usage
if __name__ == "__main__":
    raffle = RaffleSystem()
    
    try:
        raffle.register_participant("Alice")
        raffle.register_participant("Bob")
        raffle.register_participant("Charlie")
        
        print("Registered participants:", raffle.get_participants())
        
        winner = raffle.draw_winner()
        print(f"The winner is: {winner}")
        
    except ValueError as ve:
        print(f"Registration error: {ve}")
    except RuntimeError as re:
        print(f"Draw error: {re}")
```
