"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://lzero.us
Prompt: Generate code to implement a raffle system for events like the Pickleball Speed Dating described on the L-Zero website, where participants can register and winners are randomly selected.
Generated: DETERMINISTIC_b2eadd3b07ff1f34
Batch ID: 20250612_145626
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import random

class Raffle:
    def __init__(self):
        """Initialize an empty list of participants."""
        self.participants = []

    def register_participant(self, name):
        """
        Register a participant for the raffle.
        
        Parameters:
            name (str): The name of the participant.
        
        Raises:
            ValueError: If the participant name is empty or already registered.
        """
        if not name:
            raise ValueError("Participant name cannot be empty.")
        if name in self.participants:
            raise ValueError(f"{name} is already registered.")
        
        self.participants.append(name)
        print(f"{name} has been registered for the raffle.")

    def draw_winner(self):
        """
        Select a random winner from the registered participants.
        
        Returns:
            str: The name of the winner.
        
        Raises:
            RuntimeError: If no participants are registered.
        """
        if not self.participants:
            raise RuntimeError("No participants registered for the raffle.")
        
        winner = random.choice(self.participants)
        return winner

    def list_participants(self):
        """
        List all registered participants.
        
        Returns:
            list: The list of participant names.
        """
        return self.participants

# Example usage
if __name__ == "__main__":
    raffle = Raffle()
    
    # Register participants
    try:
        raffle.register_participant("Alice")
        raffle.register_participant("Bob")
        raffle.register_participant("Charlie")
        
        # Attempt to register a duplicate participant
        raffle.register_participant("Alice")  # This should raise an error
    except ValueError as e:
        print(f"Error: {e}")
    
    # List participants
    print("Registered participants:", raffle.list_participants())
    
    # Draw a winner
    try:
        winner = raffle.draw_winner()
        print(f"The winner is: {winner}")
    except RuntimeError as e:
        print(f"Error: {e}")
```
