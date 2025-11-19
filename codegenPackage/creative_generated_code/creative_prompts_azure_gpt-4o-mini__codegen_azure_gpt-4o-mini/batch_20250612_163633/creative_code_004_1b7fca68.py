"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://jellybabiesnft.web.app
Prompt: How can I develop a lottery system for NFTs akin to the Jellotto feature from the Jelly Babies NFT project?
Generated: DETERMINISTIC_1b7fca685e3785e7
Batch ID: 20250612_163633
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

class LotterySystem:
    def __init__(self):
        """Initialize the lottery system with an empty list of participants."""
        self.participants: List[str] = []
        self.winners: List[str] = []

    def enter_lottery(self, participant: str) -> None:
        """Add a participant to the lottery.

        Args:
            participant (str): The NFT owner's address or identifier.

        Raises:
            ValueError: If the participant is already entered in the lottery.
        """
        if participant in self.participants:
            raise ValueError("Participant has already entered the lottery.")
        self.participants.append(participant)

    def draw_winner(self, number_of_winners: int) -> List[str]:
        """Randomly select winners from the participants.

        Args:
            number_of_winners (int): The number of winners to draw.

        Returns:
            List[str]: A list of winners.

        Raises:
            ValueError: If the number of winners exceeds the number of participants.
        """
        if number_of_winners > len(self.participants):
            raise ValueError("Number of winners exceeds number of participants.")
        
        # Randomly select the specified number of winners
        self.winners = random.sample(self.participants, number_of_winners)
        return self.winners

    def reset_lottery(self) -> None:
        """Reset the lottery for a new round by clearing participants and winners."""
        self.participants.clear()
        self.winners.clear()

    def get_participants(self) -> List[str]:
        """Return the list of participants currently entered in the lottery.

        Returns:
            List[str]: Current participants.
        """
        return self.participants

    def get_winners(self) -> List[str]:
        """Return the list of winners from the latest draw.

        Returns:
            List[str]: Current winners.
        """
        return self.winners

# Example Usage
if __name__ == "__main__":
    # Create a lottery system instance
    lottery = LotterySystem()
    
    # Enter some participants
    try:
        lottery.enter_lottery("NFT_OWNER_1")
        lottery.enter_lottery("NFT_OWNER_2")
        lottery.enter_lottery("NFT_OWNER_3")
    except ValueError as ve:
        print(f"Error: {ve}")

    # Draw winners
    try:
        winners = lottery.draw_winner(2)
        print(f"Winners: {winners}")
    except ValueError as ve:
        print(f"Error: {ve}")

    # Reset for a new round
    lottery.reset_lottery()
    print("Lottery reset. Participants and winners cleared.")
```
