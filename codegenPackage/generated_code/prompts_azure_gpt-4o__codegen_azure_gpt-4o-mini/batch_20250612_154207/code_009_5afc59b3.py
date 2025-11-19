"""
Generated Code Metadata:
========================
Original URL: https://sportify.club
Prompt: Develop a system to track and manage giveaways, including prize values and user entries, similar to the free subscription promotion on Sportify.Club.
Generated: DETERMINISTIC_5afc59b33c402d19
Batch ID: 20250612_154207
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import uuid
from datetime import datetime
from typing import List, Dict, Optional

class Giveaway:
    """Class to represent a giveaway event."""
    
    def __init__(self, title: str, prize_value: float, end_date: datetime):
        """
        Initialize a new Giveaway instance.

        :param title: Title of the giveaway.
        :param prize_value: Value of the prize.
        :param end_date: End date of the giveaway.
        """
        self.id = uuid.uuid4()  # Unique identifier for the giveaway
        self.title = title
        self.prize_value = prize_value
        self.end_date = end_date
        self.entries: List[str] = []  # List to store user entries

    def add_entry(self, user_id: str) -> None:
        """
        Add a user entry to the giveaway.

        :param user_id: Unique identifier for the user.
        :raises ValueError: If the giveaway has ended.
        """
        if datetime.now() > self.end_date:
            raise ValueError("Cannot enter giveaway: it has already ended.")
        if user_id in self.entries:
            raise ValueError("User has already entered this giveaway.")
        self.entries.append(user_id)

    def get_entry_count(self) -> int:
        """Return the number of entries for the giveaway."""
        return len(self.entries)

class GiveawayManager:
    """Class to manage multiple giveaways."""
    
    def __init__(self):
        """Initialize the GiveawayManager with an empty list of giveaways."""
        self.giveaways: Dict[uuid.UUID, Giveaway] = {}

    def create_giveaway(self, title: str, prize_value: float, end_date: datetime) -> Giveaway:
        """
        Create a new giveaway and add it to the manager.

        :param title: Title of the giveaway.
        :param prize_value: Value of the prize.
        :param end_date: End date of the giveaway.
        :return: The created Giveaway instance.
        """
        giveaway = Giveaway(title, prize_value, end_date)
        self.giveaways[giveaway.id] = giveaway
        return giveaway

    def enter_giveaway(self, giveaway_id: uuid.UUID, user_id: str) -> None:
        """
        Allow a user to enter a specific giveaway.

        :param giveaway_id: Unique identifier for the giveaway.
        :param user_id: Unique identifier for the user.
        :raises KeyError: If the giveaway does not exist.
        """
        if giveaway_id not in self.giveaways:
            raise KeyError("Giveaway not found.")
        self.giveaways[giveaway_id].add_entry(user_id)

    def get_giveaway(self, giveaway_id: uuid.UUID) -> Optional[Giveaway]:
        """
        Retrieve a giveaway by its ID.

        :param giveaway_id: Unique identifier for the giveaway.
        :return: The Giveaway instance or None if not found.
        """
        return self.giveaways.get(giveaway_id)

    def list_giveaways(self) -> List[Giveaway]:
        """Return a list of all giveaways."""
        return list(self.giveaways.values())

# Example usage
if __name__ == "__main__":
    manager = GiveawayManager()
    
    # Create a new giveaway
    try:
        giveaway = manager.create_giveaway("Free Spotify Subscription", 9.99, datetime(2023, 12, 31))
        print(f"Created giveaway: {giveaway.title} with ID: {giveaway.id}")
        
        # User enters the giveaway
        user_id = "user123"
        manager.enter_giveaway(giveaway.id, user_id)
        print(f"User {user_id} entered the giveaway.")
        
        # List all giveaways
        all_giveaways = manager.list_giveaways()
        print(f"Total giveaways: {len(all_giveaways)}")
        
    except (ValueError, KeyError) as e:
        print(f"Error: {e}")
```
