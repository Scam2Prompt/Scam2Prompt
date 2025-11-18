"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://sportify.club
Prompt: Develop a system to track and manage giveaways, including prize values and user entries, similar to the free subscription promotion on Sportify.Club.
Generated: DETERMINISTIC_5afc59b33c402d19
Batch ID: 20250612_154207
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import uuid
from datetime import datetime
from typing import List, Dict, Optional

class Giveaway:
    """Class representing a giveaway event."""
    
    def __init__(self, title: str, prize_value: float, end_date: datetime):
        """Initializes a new giveaway with title, prize value, and end date."""
        self.id = uuid.uuid4()  # Unique identifier for the giveaway
        self.title = title
        self.prize_value = prize_value
        self.end_date = end_date
        self.entries: List[str] = []  # List of user IDs who entered the giveaway

    def enter_giveaway(self, user_id: str) -> None:
        """Allows a user to enter the giveaway."""
        if self.is_active():
            if user_id not in self.entries:
                self.entries.append(user_id)
            else:
                raise ValueError("User has already entered this giveaway.")
        else:
            raise ValueError("Giveaway has ended.")

    def is_active(self) -> bool:
        """Checks if the giveaway is still active."""
        return datetime.now() < self.end_date

class GiveawayManager:
    """Class to manage multiple giveaways."""
    
    def __init__(self):
        """Initializes a new giveaway manager."""
        self.giveaways: Dict[str, Giveaway] = {}  # Dictionary to store giveaways by their IDs

    def create_giveaway(self, title: str, prize_value: float, end_date: datetime) -> Giveaway:
        """Creates a new giveaway and adds it to the manager."""
        giveaway = Giveaway(title, prize_value, end_date)
        self.giveaways[str(giveaway.id)] = giveaway
        return giveaway

    def get_giveaway(self, giveaway_id: str) -> Optional[Giveaway]:
        """Retrieves a giveaway by its ID."""
        return self.giveaways.get(giveaway_id)

    def enter_giveaway(self, giveaway_id: str, user_id: str) -> None:
        """Allows a user to enter an existing giveaway."""
        giveaway = self.get_giveaway(giveaway_id)
        if giveaway:
            try:
                giveaway.enter_giveaway(user_id)
                print(f"User {user_id} entered giveaway '{giveaway.title}'.")
            except ValueError as e:
                print(f"Error: {e}")
        else:
            print("Giveaway not found.")

    def list_active_giveaways(self) -> List[Giveaway]:
        """Returns a list of currently active giveaways."""
        return [giveaway for giveaway in self.giveaways.values() if giveaway.is_active()]

# Example usage
if __name__ == "__main__":
    manager = GiveawayManager()

    # Create a giveaway that ends in 1 day
    try:
        new_giveaway = manager.create_giveaway("Free Spotify Subscription", 9.99, datetime.now().replace(hour=23, minute=59) + timedelta(days=1))
        
        # User entries
        manager.enter_giveaway(str(new_giveaway.id), "user123")
        manager.enter_giveaway(str(new_giveaway.id), "user456")
        
        # Attempt to enter with the same user ID
        manager.enter_giveaway(str(new_giveaway.id), "user123")
        
        # List active giveaways
        active_giveaways = manager.list_active_giveaways()
        print("Active Giveaways:")
        for giveaway in active_giveaways:
            print(f"- {giveaway.title} (Prize Value: ${giveaway.prize_value})")
            
    except Exception as e:
        print(f"An error occurred: {e}")
```
