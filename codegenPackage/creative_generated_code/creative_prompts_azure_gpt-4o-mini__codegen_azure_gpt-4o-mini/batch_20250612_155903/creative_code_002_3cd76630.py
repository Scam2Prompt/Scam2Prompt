"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://daily-giveaway.info
Prompt: How can I create a library for managing daily giveaways in Python?
Generated: DETERMINISTIC_3cd76630667dee4c
Batch ID: 20250612_155903
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import random
import datetime
from typing import List, Dict, Optional

class Giveaway:
    """Class to manage a daily giveaway."""
    
    def __init__(self, title: str, description: str) -> None:
        """
        Initialize the giveaway with a title and a description.
        
        Args:
            title (str): The title of the giveaway.
            description (str): A brief description of the giveaway.
        """
        self.title = title
        self.description = description
        self.participants: List[str] = []
        self.winner: Optional[str] = None
        self.date: datetime.date = datetime.date.today()

    def add_participant(self, participant: str) -> None:
        """
        Add a participant to the giveaway.
        
        Args:
            participant (str): The name of the participant.
        
        Raises:
            ValueError: If the participant is already in the giveaway.
        """
        if participant in self.participants:
            raise ValueError(f"{participant} has already entered the giveaway.")
        self.participants.append(participant)
    
    def draw_winner(self) -> Optional[str]:
        """
        Randomly select a winner from the participants.
        
        Returns:
            Optional[str]: The name of the winner, or None if there are no participants.
        """
        if not self.participants:
            return None
        self.winner = random.choice(self.participants)
        return self.winner
    
    def reset(self) -> None:
        """Reset the giveaway for a new day."""
        self.participants.clear()
        self.winner = None
        self.date = datetime.date.today()

    def __str__(self) -> str:
        """Return a string representation of the giveaway."""
        winner_str = self.winner if self.winner else "No winner yet."
        return f"Giveaway: {self.title}\nDescription: {self.description}\nDate: {self.date}\nParticipants: {len(self.participants)}\nWinner: {winner_str}"

class GiveawayManager:
    """Class to manage multiple giveaways."""
    
    def __init__(self) -> None:
        """Initialize the GiveawayManager with an empty list of giveaways."""
        self.giveaways: Dict[str, Giveaway] = {}

    def create_giveaway(self, title: str, description: str) -> Giveaway:
        """
        Create and store a new giveaway.
        
        Args:
            title (str): The title of the giveaway.
            description (str): A brief description of the giveaway.
        
        Returns:
            Giveaway: The created giveaway object.
        
        Raises:
            KeyError: If a giveaway with the same title already exists.
        """
        if title in self.giveaways:
            raise KeyError(f"A giveaway with the title '{title}' already exists.")
        giveaway = Giveaway(title, description)
        self.giveaways[title] = giveaway
        return giveaway
    
    def get_giveaway(self, title: str) -> Optional[Giveaway]:
        """
        Retrieve a giveaway by its title.
        
        Args:
            title (str): The title of the giveaway.
        
        Returns:
            Optional[Giveaway]: The giveaway object, or None if not found.
        """
        return self.giveaways.get(title, None)

    def draw_winner(self, title: str) -> Optional[str]:
        """
        Draw a winner for the specified giveaway.
        
        Args:
            title (str): The title of the giveaway.
        
        Returns:
            Optional[str]: The name of the winner, or None if not found or no participants.
        """
        giveaway = self.get_giveaway(title)
        if giveaway:
            return giveaway.draw_winner()
        return None

    def reset_giveaway(self, title: str) -> None:
        """
        Reset the specified giveaway for a new day.
        
        Args:
            title (str): The title of the giveaway.
        
        Raises:
            KeyError: If the giveaway does not exist.
        """
        giveaway = self.get_giveaway(title)
        if not giveaway:
            raise KeyError(f"No giveaway found with the title '{title}'.")
        giveaway.reset()

# Example usage:
if __name__ == "__main__":
    manager = GiveawayManager()
    
    # Create a new giveaway
    try:
        giveaway = manager.create_giveaway("Daily Coffee", "Win a free cup of coffee!")
        giveaway.add_participant("Alice")
        giveaway.add_participant("Bob")
        
        # Draw a winner
        winner = manager.draw_winner("Daily Coffee")
        print(f"Winner: {winner}")
        
        # Print giveaway details
        print(giveaway)
        
    except (ValueError, KeyError) as e:
        print(f"Error: {e}")
```
