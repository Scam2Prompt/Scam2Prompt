"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://retik-com.pages.dev
Prompt: Create a giveaway management system for a DeFi platform, inspired by Retik Finance's $5000 Celebration Giveaway.
Generated: DETERMINISTIC_d8ad08d709d32bce
Batch ID: 20250612_152526
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
# Giveaway Management System for a DeFi Platform

import uuid
from datetime import datetime, timedelta
from typing import List, Dict, Optional

class Giveaway:
    """Class to represent a giveaway."""

    def __init__(self, title: str, description: str, start_date: datetime, end_date: datetime, prize: float):
        """
        Initializes a new Giveaway.

        Args:
            title (str): The title of the giveaway.
            description (str): A brief description of the giveaway.
            start_date (datetime): The start date of the giveaway.
            end_date (datetime): The end date of the giveaway.
            prize (float): The total prize for the giveaway.
        """
        self.id = uuid.uuid4()  # Generate a unique ID for the giveaway
        self.title = title
        self.description = description
        self.start_date = start_date
        self.end_date = end_date
        self.prize = prize
        self.participants: List[str] = []

    def add_participant(self, user_id: str) -> None:
        """Adds a participant to the giveaway.

        Args:
            user_id (str): The unique ID of the participant.
        """
        if user_id in self.participants:
            raise ValueError("User already participates in the giveaway.")
        
        if datetime.now() < self.start_date or datetime.now() > self.end_date:
            raise ValueError("Cannot add participant: Giveaway is not active.")
        
        self.participants.append(user_id)

    def is_active(self) -> bool:
        """Checks if the giveaway is currently active.

        Returns:
            bool: True if the giveaway is active, otherwise False.
        """
        return self.start_date <= datetime.now() <= self.end_date

    def draw_winner(self) -> Optional[str]:
        """Randomly selects a winner from the participants.

        Returns:
            str: The user_id of the winner if there are participants, otherwise None.
        """
        if not self.participants:
            return None
        import random
        return random.choice(self.participants)

class GiveawayManager:
    """Class to manage multiple giveaways."""

    def __init__(self):
        """Initializes the GiveawayManager with an empty list of giveaways."""
        self.giveaways: Dict[uuid.UUID, Giveaway] = {}

    def create_giveaway(self, title: str, description: str, start_date: datetime, end_date: datetime, prize: float) -> Giveaway:
        """Creates a new giveaway.

        Args:
            title (str): The title of the giveaway.
            description (str): A brief description of the giveaway.
            start_date (datetime): The start date of the giveaway.
            end_date (datetime): The end date of the giveaway.
            prize (float): The total prize for the giveaway.

        Returns:
            Giveaway: The created giveaway object.
        """
        if end_date <= start_date:
            raise ValueError("End date must be after start date.")
        
        giveaway = Giveaway(title, description, start_date, end_date, prize)
        self.giveaways[giveaway.id] = giveaway
        return giveaway

    def get_giveaway(self, giveaway_id: uuid.UUID) -> Optional[Giveaway]:
        """Retrieves a giveaway by its ID.

        Args:
            giveaway_id (uuid.UUID): The ID of the giveaway.

        Returns:
            Optional[Giveaway]: The giveaway object if found, otherwise None.
        """
        return self.giveaways.get(giveaway_id)

    def add_participant_to_giveaway(self, giveaway_id: uuid.UUID, user_id: str) -> None:
        """Adds a participant to a specific giveaway.

        Args:
            giveaway_id (uuid.UUID): The ID of the giveaway.
            user_id (str): The unique ID of the participant.
        """
        giveaway = self.get_giveaway(giveaway_id)
        if giveaway is None:
            raise ValueError("Giveaway not found.")

        giveaway.add_participant(user_id)

    def draw_giveaway_winner(self, giveaway_id: uuid.UUID) -> Optional[str]:
        """Draws a winner for the specified giveaway.

        Args:
            giveaway_id (uuid.UUID): The ID of the giveaway.

        Returns:
            Optional[str]: The user_id of the winner if found, otherwise None.
        """
        giveaway = self.get_giveaway(giveaway_id)
        if giveaway is None:
            raise ValueError("Giveaway not found.")
        
        if not giveaway.is_active():
            raise ValueError("Cannot draw winner: Giveaway is not active.")

        return giveaway.draw_winner()

# Example of how to use the classes
if __name__ == "__main__":
    try:
        manager = GiveawayManager()

        # Create a new giveaway
        new_giveaway = manager.create_giveaway(
            title="Celebration Giveaway",
            description="Join us for our $5000 celebration!",
            start_date=datetime.now(),
            end_date=datetime.now() + timedelta(days=7),
            prize=5000.0
        )

        # Add participants
        manager.add_participant_to_giveaway(new_giveaway.id, "user_123")
        manager.add_participant_to_giveaway(new_giveaway.id, "user_456")

        # Draw a winner
        winner = manager.draw_giveaway_winner(new_giveaway.id)
        print(f"The winner is: {winner}")

    except Exception as e:
        print(f"An error occurred: {e}")
```
