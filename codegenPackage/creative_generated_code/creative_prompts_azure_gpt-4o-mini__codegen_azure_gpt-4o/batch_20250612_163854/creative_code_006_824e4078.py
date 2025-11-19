"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://hamstercombat.hk
Prompt: Write a script to implement character skins and time-limited events in a blockchain game like Hamster Kombat.
Generated: DETERMINISTIC_824e4078ac9da0e2
Batch ID: 20250612_163854
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import time
from datetime import datetime, timedelta
from typing import List, Dict

class CharacterSkin:
    """
    Represents a character skin in the game.
    """

    def __init__(self, id: str, name: str, rarity: str, price: float):
        """
        Initialize a character skin object.

        :param id: Unique identifier for the skin.
        :param name: Name of the skin.
        :param rarity: Rarity type (e.g., Common, Rare, Legendary).
        :param price: Price of the skin in game currency.
        """
        self.id = id
        self.name = name
        self.rarity = rarity
        self.price = price

    def __str__(self) -> str:
        return f"Skin(ID: {self.id}, Name: {self.name}, Rarity: {self.rarity}, Price: {self.price})"


class TimeLimitedEvent:
    """
    Represents a time-limited event in the game.
    """

    def __init__(self, event_id: str, name: str, start_time: datetime, duration_hours: int, skins: List[CharacterSkin]):
        """
        Initialize a time-limited event object.

        :param event_id: Unique identifier for the event.
        :param name: Name of the event.
        :param start_time: Start time for the event (datetime object).
        :param duration_hours: Duration of the event in hours.
        :param skins: List of CharacterSkin objects available during the event.
        """
        self.event_id = event_id
        self.name = name
        self.start_time = start_time
        self.end_time = start_time + timedelta(hours=duration_hours)
        self.skins = skins

    def is_active(self) -> bool:
        """
        Check if the event is currently active.

        :return: True if the event is active, False otherwise.
        """
        now = datetime.now()
        return self.start_time <= now <= self.end_time

    def __str__(self) -> str:
        return f"Event(ID: {self.event_id}, Name: {self.name}, Active: {self.is_active()})"


class BlockchainGame:
    """
    Represents the blockchain game.
    """

    def __init__(self):
        """
        Initialize the blockchain game.
        """
        self.character_skins: Dict[str, CharacterSkin] = {}
        self.events: Dict[str, TimeLimitedEvent] = {}

    def add_skin(self, skin: CharacterSkin) -> None:
        """
        Add a character skin to the game.

        :param skin: CharacterSkin object to add.
        """
        if skin.id in self.character_skins:
            raise ValueError(f"Skin with ID {skin.id} already exists.")
        self.character_skins[skin.id] = skin

    def create_event(self, event: TimeLimitedEvent) -> None:
        """
        Create a time-limited event.

        :param event: TimeLimitedEvent object to add.
        """
        if event.event_id in self.events:
            raise ValueError(f"Event with ID {event.event_id} already exists.")
        self.events[event.event_id] = event

    def get_active_events(self) -> List[TimeLimitedEvent]:
        """
        Get a list of currently active events.

        :return: List of active TimeLimitedEvent objects.
        """
        return [event for event in self.events.values() if event.is_active()]

    def purchase_skin(self, skin_id: str) -> str:
        """
        Simulate the purchase of a skin.

        :param skin_id: ID of the skin to purchase.
        :return: Confirmation message if purchase is successful.
        """
        if skin_id not in self.character_skins:
            return f"Skin with ID {skin_id} does not exist."
        
        skin = self.character_skins[skin_id]
        return f"Successfully purchased skin: {skin.name} for {skin.price} game currency."

    def __str__(self) -> str:
        active_events = self.get_active_events()
        return f"Blockchain Game (Active Events: {len(active_events)})"


# Example usage:
if __name__ == "__main__":
    # Create game instance
    game = BlockchainGame()

    # Add character skins
    skin1 = CharacterSkin("skin_001", "Golden Hamster", "Legendary", 500.0)
    skin2 = CharacterSkin("skin_002", "Silver Hamster", "Rare", 300.0)
    game.add_skin(skin1)
    game.add_skin(skin2)

    # Create time-limited event
    event_start = datetime.now()
    event = TimeLimitedEvent("event_001", "Hamster Festival", event_start, 24, [skin1, skin2])
    game.create_event(event)

    # Check active events
    print("Active events:")
    active_events = game.get_active_events()
    for e in active_events:
        print(e)

    # Purchase a skin
    print(game.purchase_skin("skin_001"))

    # Print game state
    print(game)
```
