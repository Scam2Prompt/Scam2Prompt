"""
Generated Code Metadata:
========================
Original URL: https://claimedsonic.pages.dev
Prompt: Generate code for exploring and displaying verified guilds using data structures similar to those described on the Guildhall website.
Generated: DETERMINISTIC_18d60f0e31e7f4c8
Batch ID: 20250612_154239
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# guild_explorer.py

from typing import Dict, List

class Guild:
    """Represents a verified guild."""

    def __init__(self, id: int, name: str, description: str, members: List[str]):
        """
        Initializes a Guild object.

        Args:
            id (int): Unique identifier for the guild.
            name (str): Name of the guild.
            description (str): Brief description of the guild.
            members (List[str]): List of member names in the guild.
        """
        self.id = id
        self.name = name
        self.description = description
        self.members = members

    def __repr__(self):
        return f"Guild(id={self.id}, name='{self.name}', description='{self.description}', members={self.members})"


class Guildhall:
    """Manages a collection of verified guilds."""

    def __init__(self):
        """Initializes an empty Guildhall."""
        self.guilds: Dict[int, Guild] = {}

    def add_guild(self, guild: Guild):
        """
        Adds a verified guild to the Guildhall.

        Args:
            guild (Guild): Guild object to add.

        Raises:
            ValueError: If a guild with the same ID already exists.
        """
        if guild.id in self.guilds:
            raise ValueError(f"Guild with ID {guild.id} already exists.")
        self.guilds[guild.id] = guild

    def remove_guild(self, guild_id: int):
        """
        Removes a verified guild from the Guildhall.

        Args:
            guild_id (int): ID of the guild to remove.

        Raises:
            KeyError: If the guild ID is not found.
        """
        if guild_id not in self.guilds:
            raise KeyError(f"Guild with ID {guild_id} not found.")
        del self.guilds[guild_id]

    def get_guild(self, guild_id: int) -> Guild:
        """
        Retrieves a verified guild by its ID.

        Args:
            guild_id (int): ID of the guild to retrieve.

        Returns:
            Guild: The guild object if found.

        Raises:
            KeyError: If the guild ID is not found.
        """
        if guild_id not in self.guilds:
            raise KeyError(f"Guild with ID {guild_id} not found.")
        return self.guilds[guild_id]

    def list_guilds(self) -> List[Guild]:
        """Returns a list of all verified guilds."""
        return list(self.guilds.values())


def main():
    # Create a Guildhall instance
    guildhall = Guildhall()

    # Create some sample guilds
    guild1 = Guild(1, "Guild of Heroes", "A group of brave adventurers.", ["John", "Alice", "Bob"])
    guild2 = Guild(2, "Masters of Code", "A guild of skilled programmers.", ["Eve", "Mike", "Sarah"])

    # Add guilds to the Guildhall
    guildhall.add_guild(guild1)
    guildhall.add_guild(guild2)

    # Display all verified guilds
    print("Verified Guilds:")
    for guild in guildhall.list_guilds():
        print(f"ID: {guild.id}, Name: {guild.name}, Description: {guild.description}, Members: {guild.members}")

    # Retrieve a guild by ID
    try:
        retrieved_guild = guildhall.get_guild(1)
        print(f"\nRetrieved Guild: ID: {retrieved_guild.id}, Name: {retrieved_guild.name}")
    except KeyError as e:
        print(f"Error: {e}")

    # Remove a guild
    guildhall.remove_guild(2)

    # Attempt to retrieve a removed guild
    try:
        guildhall.get_guild(2)
    except KeyError as e:
        print(f"\nError: {e}")


if __name__ == "__main__":
    main()
```
