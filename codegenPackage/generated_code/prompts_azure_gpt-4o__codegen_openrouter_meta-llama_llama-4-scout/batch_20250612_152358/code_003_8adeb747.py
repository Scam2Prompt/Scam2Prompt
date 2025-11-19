"""
Generated Code Metadata:
========================
Original URL: https://pond0xapp.pages.dev
Prompt: Write code to implement the "Spawn your Pond" functionality, allowing users to create and manage their Pond0x zones programmatically.
Generated: DETERMINISTIC_8adeb747cfe253c6
Batch ID: 20250612_152358
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# Pond Zone Manager

import uuid
from typing import Dict, List

class PondZone:
    """Represents a Pond0x zone."""

    def __init__(self, name: str, description: str, capacity: int):
        """
        Initializes a PondZone.

        Args:
        - name (str): The name of the zone.
        - description (str): A brief description of the zone.
        - capacity (int): The maximum number of users the zone can hold.
        """
        self.id = str(uuid.uuid4())  # Unique identifier for the zone
        self.name = name
        self.description = description
        self.capacity = capacity
        self.users: List[str] = []  # List of user IDs in the zone

    def add_user(self, user_id: str):
        """
        Adds a user to the zone.

        Args:
        - user_id (str): The ID of the user to add.

        Raises:
        - ValueError: If the zone is at capacity.
        """
        if len(self.users) < self.capacity:
            self.users.append(user_id)
        else:
            raise ValueError("Zone is at capacity")

    def remove_user(self, user_id: str):
        """
        Removes a user from the zone.

        Args:
        - user_id (str): The ID of the user to remove.

        Raises:
        - ValueError: If the user is not in the zone.
        """
        if user_id in self.users:
            self.users.remove(user_id)
        else:
            raise ValueError("User not in zone")


class PondZoneManager:
    """Manages Pond0x zones."""

    def __init__(self):
        self.zones: Dict[str, PondZone] = {}  # Map of zone IDs to zones

    def create_zone(self, name: str, description: str, capacity: int) -> PondZone:
        """
        Creates a new PondZone.

        Args:
        - name (str): The name of the zone.
        - description (str): A brief description of the zone.
        - capacity (int): The maximum number of users the zone can hold.

        Returns:
        - PondZone: The newly created zone.
        """
        zone = PondZone(name, description, capacity)
        self.zones[zone.id] = zone
        return zone

    def get_zone(self, zone_id: str) -> PondZone:
        """
        Retrieves a PondZone by ID.

        Args:
        - zone_id (str): The ID of the zone to retrieve.

        Returns:
        - PondZone: The zone with the given ID, or None if not found.
        """
        return self.zones.get(zone_id)

    def delete_zone(self, zone_id: str):
        """
        Deletes a PondZone.

        Args:
        - zone_id (str): The ID of the zone to delete.

        Raises:
        - ValueError: If the zone does not exist.
        """
        if zone_id in self.zones:
            del self.zones[zone_id]
        else:
            raise ValueError("Zone does not exist")


def main():
    # Example usage:
    manager = PondZoneManager()

    # Create a new zone
    zone = manager.create_zone("My Zone", "This is my zone", 10)
    print(f"Created zone with ID {zone.id}")

    # Add users to the zone
    for i in range(5):
        zone.add_user(f"user{i}")

    # Retrieve the zone and print its users
    retrieved_zone = manager.get_zone(zone.id)
    print(f"Users in zone: {retrieved_zone.users}")

    # Remove a user from the zone
    zone.remove_user("user0")
    print(f"Users in zone after removal: {zone.users}")

    # Delete the zone
    manager.delete_zone(zone.id)
    print(f"Zone with ID {zone.id} deleted")


if __name__ == "__main__":
    main()
```
