"""
Generated Code Metadata:
========================
Original URL: https://geno-pets.net
Prompt: Write code to create and customize digital pets in a game like Genopets, including crafting items, augments, and power-ups.
Generated: DETERMINISTIC_8b779539202ddfac
Batch ID: 20250612_150426
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import random
from enum import Enum
from typing import List, Dict, Optional, Tuple

class PetType(Enum):
    """Enum representing different types of digital pets."""
    AQUATIC = "Aquatic"
    AVIAN = "Avian"
    BEAST = "Beast"
    REPTILE = "Reptile"
    MECHANICAL = "Mechanical"

class Rarity(Enum):
    """Enum representing rarity levels."""
    COMMON = "Common"
    UNCOMMON = "Uncommon"
    RARE = "Rare"
    EPIC = "Epic"
    LEGENDARY = "Legendary"

class Stat:
    """Class representing a pet's stat."""
    def __init__(self, name: str, base_value: int):
        self.name = name
        self.base_value = base_value
        self.current_value = base_value
        self.modifiers = {}

    def add_modifier(self, source: str, value: int) -> None:
        """Add a modifier to the stat."""
        self.modifiers[source] = value
        self._update_current_value()

    def remove_modifier(self, source: str) -> None:
        """Remove a modifier from the stat."""
        if source in self.modifiers:
            del self.modifiers[source]
            self._update_current_value()

    def _update_current_value(self) -> None:
        """Recalculate current value based on modifiers."""
        self.current_value = self.base_value + sum(self.modifiers.values())

    def __str__(self) -> str:
        return f"{self.name}: {self.current_value} (Base: {self.base_value})"

class Item:
    """Base class for all items."""
    def __init__(self, name: str, rarity: Rarity, description: str = ""):
        self.name = name
        self.rarity = rarity
        self.description = description

    def __str__(self) -> str:
        return f"{self.name} ({self.rarity.value}) - {self.description}"

class Augment(Item):
    """Class representing pet augments."""
    def __init__(self, name: str, rarity: Rarity, stat_modifiers: Dict[str, int], description: str = ""):
        super().__init__(name, rarity, description)
        self.stat_modifiers = stat_modifiers

class PowerUp(Item):
    """Class representing power-ups."""
    def __init__(self, name: str, rarity: Rarity, duration: int, effect: Dict[str, int], description: str = ""):
        super().__init__(name, rarity, description)
        self.duration = duration
        self.effect = effect
        self.active = False
        self.remaining_time = 0

    def activate(self) -> None:
        """Activate the power-up."""
        self.active = True
        self.remaining_time = self.duration

    def deactivate(self) -> None:
        """Deactivate the power-up."""
        self.active = False
        self.remaining_time = 0

    def update(self) -> None:
        """Update the power-up's remaining time."""
        if self.active and self.remaining_time > 0:
            self.remaining_time -= 1
            if self.remaining_time == 0:
                self.deactivate()

class CraftingMaterial(Item):
    """Class representing crafting materials."""
    def __init__(self, name: str, rarity: Rarity, quantity: int = 1, description: str = ""):
        super().__init__(name, rarity, description)
        self.quantity = quantity

    def add_quantity(self, amount: int) -> None:
        """Add to the material quantity."""
        self.quantity += amount

    def use_quantity(self, amount: int) -> bool:
        """Use a specified amount of the material."""
        if self.quantity >= amount:
            self.quantity -= amount
            return True
        return False

class Recipe:
    """Class representing crafting recipes."""
    def __init__(self, name: str, result_item: Item, materials_required: Dict[str, int], description: str = ""):
        self.name = name
        self.result_item = result_item
        self.materials_required = materials_required
        self.description = description

    def can_craft(self, inventory: Dict[str, CraftingMaterial]) -> bool:
        """Check if the recipe can be crafted with given inventory."""
        for material_name, quantity in self.materials_required.items():
            if material_name not in inventory or inventory[material_name].quantity < quantity:
                return False
        return True

    def craft(self, inventory: Dict[str, CraftingMaterial]) -> Optional[Item]:
        """Attempt to craft the item."""
        if not self.can_craft(inventory):
            return None

        for material_name, quantity in self.materials_required.items():
            inventory[material_name].use_quantity(quantity)

        return self.result_item

class DigitalPet:
    """Class representing a digital pet."""
    def __init__(self, name: str, pet_type: PetType, rarity: Rarity):
        self.name = name
        self.pet_type = pet_type
        self.rarity = rarity
        self.level = 1
        self.experience = 0
        self.stats = {
            "Health": Stat("Health", 100),
            "Attack": Stat("Attack", 10),
            "Defense": Stat("Defense", 10),
            "Speed": Stat("Speed", 10),
            "Energy": Stat("Energy", 50)
        }
        self.augments: List[Augment] = []
        self.active_powerups: List[PowerUp] = []
        self.inventory: Dict[str, CraftingMaterial] = {}

    def add_experience(self, amount: int) -> None:
        """Add experience to the pet."""
        self.experience += amount
        while self.experience >= self._required_experience():
            self.experience -= self._required_experience()
            self.level_up()

    def _required_experience(self) -> int:
        """Calculate required experience for next level."""
        return self.level * 100

    def level_up(self) -> None:
        """Level up the pet."""
        self.level += 1
        for stat in self.stats.values():
            stat.base_value += 5
            stat._update_current_value()

    def equip_augment(self, augment: Augment) -> bool:
        """Equip an augment to the pet."""
        if augment in self.augments:
            return False

        self.augments.append(augment)
        for stat_name, modifier in augment.stat_modifiers.items():
            if stat_name in self.stats:
                self.stats[stat_name].add_modifier(augment.name, modifier)
        return True

    def unequip_augment(self, augment: Augment) -> bool:
        """Unequip an augment from the pet."""
        if augment not in self.augments:
            return False

        self.augments.remove(augment)
        for stat_name in augment.stat_modifiers.keys():
            if stat_name in self.stats:
                self.stats[stat_name].remove_modifier(augment.name)
        return True

    def activate_powerup(self, powerup: PowerUp) -> bool:
        """Activate a power-up for the pet."""
        if powerup in self.active_powerups:
            return False

        powerup.activate()
        self.active_powerups.append(powerup)
        for stat_name, modifier in powerup.effect.items():
            if stat_name in self.stats:
                self.stats[stat_name].add_modifier(powerup.name, modifier)
        return True

    def deactivate_powerup(self, powerup: PowerUp) -> bool:
        """Deactivate a power-up for the pet."""
        if powerup not in self.active_powerups:
            return False

        powerup.deactivate()
        self.active_powerups.remove(powerup)
        for stat_name in powerup.effect.keys():
            if stat_name in self.stats:
                self.stats[stat_name].remove_modifier(powerup.name)
        return True

    def update_powerups(self) -> None:
        """Update all active power-ups."""
        for powerup in self.active_powerups[:]:
            powerup.update()
            if not powerup.active:
                self.deactivate_powerup(powerup)

    def add_to_inventory(self, material: CraftingMaterial) -> None:
        """Add a crafting material to the pet's inventory."""
        if material.name in self.inventory:
            self.inventory[material.name].add_quantity(material.quantity)
        else:
            self.inventory[material.name] = material

    def craft_item(self, recipe: Recipe) -> Optional[Item]:
        """Attempt to craft an item using a recipe."""
        return recipe.craft(self.inventory)

    def get_stat_summary(self) -> str:
        """Get a summary of the pet's stats."""
        summary = [f"{self.name} (Lvl {self.level} {self.pet_type.value})"]
        for stat in self.stats.values():
            summary.append(str(stat))
        return "\n".join(summary)

class PetGame
