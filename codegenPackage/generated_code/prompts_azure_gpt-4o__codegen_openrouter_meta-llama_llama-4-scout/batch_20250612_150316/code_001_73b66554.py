"""
Generated Code Metadata:
========================
Original URL: https://bigtimecodes.pages.dev
Prompt: Generate code to simulate crafting weapons and armor cosmetics in Big Time using $BIGTIME tokens and materials, including functionality for upgrading items through the Forge and Armory.
Generated: DETERMINISTIC_73b665545a32727c
Batch ID: 20250612_150316
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# big_time_crafting_simulator.py

class BigTimeToken:
    """Represents a $BIGTIME token."""
    def __init__(self, amount=0):
        self.amount = amount

    def __str__(self):
        return f"${self.amount} BIGTIME"


class Material:
    """Represents a material used for crafting."""
    def __init__(self, name, quantity=0):
        self.name = name
        self.quantity = quantity

    def __str__(self):
        return f"{self.name} x{self.quantity}"


class CosmeticItem:
    """Represents a cosmetic item (weapon or armor)."""
    def __init__(self, name, rarity, level=1):
        self.name = name
        self.rarity = rarity
        self.level = level

    def __str__(self):
        return f"{self.name} ({self.rarity}, Level {self.level})"


class Forge:
    """Simulates the Forge for upgrading items."""
    def __init__(self):
        self.upgrade_cost = {
            "material": Material("Rare Material", 10),
            "token": BigTimeToken(100)
        }

    def upgrade_item(self, item, bigtime_token, material):
        """Upgrades an item using $BIGTIME tokens and materials."""
        if bigtime_token.amount < self.upgrade_cost["token"].amount:
            raise ValueError("Insufficient $BIGTIME tokens")
        if material.quantity < self.upgrade_cost["material"].quantity:
            raise ValueError("Insufficient materials")

        bigtime_token.amount -= self.upgrade_cost["token"].amount
        material.quantity -= self.upgrade_cost["material"].quantity
        item.level += 1

        return item


class Armory:
    """Simulates the Armory for crafting items."""
    def __init__(self):
        self.crafting_cost = {
            "weapon": {
                "material": Material("Common Material", 5),
                "token": BigTimeToken(50)
            },
            "armor": {
                "material": Material("Uncommon Material", 10),
                "token": BigTimeToken(100)
            }
        }

    def craft_item(self, item_type, bigtime_token, material):
        """Crafts a new item using $BIGTIME tokens and materials."""
        if item_type not in ["weapon", "armor"]:
            raise ValueError("Invalid item type")

        if bigtime_token.amount < self.crafting_cost[item_type]["token"].amount:
            raise ValueError("Insufficient $BIGTIME tokens")
        if material.quantity < self.crafting_cost[item_type]["material"].quantity:
            raise ValueError("Insufficient materials")

        bigtime_token.amount -= self.crafting_cost[item_type]["token"].amount
        material.quantity -= self.crafting_cost[item_type]["material"].quantity

        if item_type == "weapon":
            return CosmeticItem("New Weapon", "Common")
        elif item_type == "armor":
            return CosmeticItem("New Armor", "Uncommon")


def main():
    # Initialize $BIGTIME tokens and materials
    bigtime_token = BigTimeToken(1000)
    material = Material("Common Material", 100)

    # Initialize Forge and Armory
    forge = Forge()
    armory = Armory()

    # Craft a new weapon
    new_weapon = armory.craft_item("weapon", bigtime_token, material)
    print(f"Crafted: {new_weapon}")

    # Upgrade the weapon
    upgraded_weapon = forge.upgrade_item(new_weapon, bigtime_token, material)
    print(f"Upgraded: {upgraded_weapon}")

    # Print remaining $BIGTIME tokens and materials
    print(f"Remaining $BIGTIME tokens: {bigtime_token}")
    print(f"Remaining materials: {material}")


if __name__ == "__main__":
    main()
```
