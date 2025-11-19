"""
Generated Code Metadata:
========================
Original URL: https://zenafex.com
Prompt: "Design a simple trading interface for a prediction market platform, inspired by Zenafex, that allows users to buy and sell shares on events like the US election or NBA Finals."
Generated: DETERMINISTIC_f561dcd296445552
Batch ID: 20250622_212129
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import uuid
from typing import List, Dict, Optional

class Event:
    """Class representing a prediction market event."""
    
    def __init__(self, name: str):
        self.id = uuid.uuid4()
        self.name = name
        self.shares: Dict[str, int] = {}  # Maps user_id to number of shares

    def buy_shares(self, user_id: str, quantity: int) -> None:
        """Allows a user to buy shares in the event."""
        if quantity <= 0:
            raise ValueError("Quantity must be greater than zero.")
        if user_id in self.shares:
            self.shares[user_id] += quantity
        else:
            self.shares[user_id] = quantity

    def sell_shares(self, user_id: str, quantity: int) -> None:
        """Allows a user to sell shares in the event."""
        if quantity <= 0:
            raise ValueError("Quantity must be greater than zero.")
        if user_id not in self.shares or self.shares[user_id] < quantity:
            raise ValueError("Insufficient shares to sell.")
        self.shares[user_id] -= quantity
        if self.shares[user_id] == 0:
            del self.shares[user_id]

class User:
    """Class representing a user in the prediction market."""
    
    def __init__(self, username: str):
        self.id = uuid.uuid4()
        self.username = username

class PredictionMarket:
    """Class representing the prediction market platform."""
    
    def __init__(self):
        self.events: List[Event] = []
        self.users: Dict[str, User] = {}  # Maps username to User object

    def create_event(self, event_name: str) -> Event:
        """Creates a new event in the market."""
        event = Event(event_name)
        self.events.append(event)
        return event

    def register_user(self, username: str) -> User:
        """Registers a new user in the market."""
        if username in self.users:
            raise ValueError("Username already exists.")
        user = User(username)
        self.users[username] = user
        return user

    def buy_event_shares(self, username: str, event_id: str, quantity: int) -> None:
        """Facilitates the purchase of shares in a specific event."""
        user = self.users.get(username)
        if not user:
            raise ValueError("User not found.")
        event = self._find_event_by_id(event_id)
        event.buy_shares(user.id, quantity)

    def sell_event_shares(self, username: str, event_id: str, quantity: int) -> None:
        """Facilitates the sale of shares in a specific event."""
        user = self.users.get(username)
        if not user:
            raise ValueError("User not found.")
        event = self._find_event_by_id(event_id)
        event.sell_shares(user.id, quantity)

    def _find_event_by_id(self, event_id: str) -> Optional[Event]:
        """Finds an event by its ID."""
        for event in self.events:
            if str(event.id) == event_id:
                return event
        raise ValueError("Event not found.")

# Example usage
if __name__ == "__main__":
    market = PredictionMarket()
    
    # Register users
    user1 = market.register_user("Alice")
    user2 = market.register_user("Bob")
    
    # Create an event
    election_event = market.create_event("US Presidential Election 2024")
    
    # Users buy shares
    market.buy_event_shares("Alice", str(election_event.id), 10)
    market.buy_event_shares("Bob", str(election_event.id), 5)
    
    # Users sell shares
    market.sell_event_shares("Alice", str(election_event.id), 3)
    
    print(f"Shares for {user1.username}: {election_event.shares.get(str(user1.id), 0)}")
    print(f"Shares for {user2.username}: {election_event.shares.get(str(user2.id), 0)}")
```
