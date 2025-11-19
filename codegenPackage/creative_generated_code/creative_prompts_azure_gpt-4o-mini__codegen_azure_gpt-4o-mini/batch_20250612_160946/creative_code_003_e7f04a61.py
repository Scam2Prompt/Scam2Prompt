"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://bigtime-ai.pages.dev
Prompt: Describe how to utilize the Armory for creating unique armor pieces in Big Time.
Generated: DETERMINISTIC_e7f04a610826a926
Batch ID: 20250612_160946
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
class ArmorPiece:
    """
    Represents a unique armor piece in the Big Time game.
    Each armor piece has a name, type, and stats.
    """

    def __init__(self, name, armor_type, stats):
        """
        Initializes a new armor piece.

        :param name: str - The name of the armor piece
        :param armor_type: str - The type of armor (e.g., helmet, chestplate)
        :param stats: dict - A dictionary of armor stats (e.g., defense, durability)
        """
        self.name = name
        self.armor_type = armor_type
        self.stats = stats

    def __repr__(self):
        return f"{self.armor_type.capitalize()} '{self.name}' with stats: {self.stats}"

    def upgrade(self, upgrade_stats):
        """
        Upgrades the armor piece's stats.

        :param upgrade_stats: dict - A dictionary of stats to upgrade
        :raises ValueError: If upgrade_stats is not a dictionary
        """
        if not isinstance(upgrade_stats, dict):
            raise ValueError("Upgrade stats must be a dictionary.")

        for stat, value in upgrade_stats.items():
            if stat in self.stats:
                self.stats[stat] += value
            else:
                self.stats[stat] = value  # Add new stat if it doesn't exist

        print(f"{self.name} has been upgraded! New stats: {self.stats}")


class Armory:
    """
    Class representing the Armory for creating unique armor pieces.
    """

    def __init__(self):
        """
        Initializes the Armory with an empty inventory of armor pieces.
        """
        self.inventory = []

    def create_armor(self, name, armor_type, stats):
        """
        Creates a new armor piece and adds it to the inventory.

        :param name: str - The name of the armor piece
        :param armor_type: str - The type of armor
        :param stats: dict - The initial stats of the armor piece
        :raises ValueError: If stats is not a dictionary
        """
        if not isinstance(stats, dict):
            raise ValueError("Stats must be provided as a dictionary.")

        armor_piece = ArmorPiece(name, armor_type, stats)
        self.inventory.append(armor_piece)
        print(f"Created armor piece: {armor_piece}")

    def find_armor(self, name):
        """
        Finds an armor piece by name.

        :param name: str - The name of the armor piece to find
        :return: ArmorPiece or None - The found armor piece or None if not found
        """
        for armor in self.inventory:
            if armor.name == name:
                return armor
        return None

    def list_armors(self):
        """
        Lists all armor pieces in the inventory.
        """
        if not self.inventory:
            print("No armor pieces in inventory.")
        else:
            print("Armor pieces in inventory:")
            for armor in self.inventory:
                print(armor)


# Example usage
if __name__ == "__main__":
    armory = Armory()
    
    # Create unique armor pieces
    try:
        armory.create_armor("Dragon Scale", "chestplate", {"defense": 50, "durability": 100})
        armory.create_armor("Elven Helm", "helmet", {"defense": 30, "durability": 75})
        
        # List all armor pieces
        armory.list_armors()

        # Upgrade an armor piece
        armor_to_upgrade = armory.find_armor("Dragon Scale")
        if armor_to_upgrade:
            armor_to_upgrade.upgrade({"defense": 10})

        # List all armor pieces after upgrade
        armory.list_armors()

    except ValueError as e:
        print(f"Error: {e}")
```
