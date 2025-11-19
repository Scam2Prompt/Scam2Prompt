"""
Generated Code Metadata:
========================
Original URL: https://portal-bigtime.pages.dev
Prompt: Write a program to manage crafting bonuses, including bonus rolls for items, based on the crafting mechanics described in the Big Time Preseason launch.
Generated: DETERMINISTIC_4391931eeabab042
Batch ID: 20250612_152235
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import random
from typing import Dict, List, Optional, Tuple

class CraftingBonusManager:
    """
    A class to manage crafting bonuses and bonus rolls for items based on crafting mechanics.
    """

    def __init__(self, base_success_rate: float = 0.75, max_bonus_rolls: int = 3):
        """
        Initialize the CraftingBonusManager with base success rate and max bonus rolls.

        Args:
            base_success_rate: The base probability of crafting success (0.0 to 1.0)
            max_bonus_rolls: Maximum number of bonus rolls allowed
        """
        if not 0 <= base_success_rate <= 1:
            raise ValueError("Base success rate must be between 0 and 1")
        if max_bonus_rolls < 0:
            raise ValueError("Max bonus rolls cannot be negative")

        self.base_success_rate = base_success_rate
        self.max_bonus_rolls = max_bonus_rolls
        self.active_bonuses: Dict[str, float] = {}  # {bonus_name: multiplier}

    def add_bonus(self, bonus_name: str, multiplier: float) -> None:
        """
        Add a crafting bonus to the active bonuses.

        Args:
            bonus_name: Name/identifier for the bonus
            multiplier: Multiplier to apply (e.g., 1.1 for 10% increase)
        
        Raises:
            ValueError: If multiplier is not positive or bonus already exists
        """
        if multiplier <= 0:
            raise ValueError("Multiplier must be positive")
        if bonus_name in self.active_bonuses:
            raise ValueError(f"Bonus '{bonus_name}' already exists")

        self.active_bonuses[bonus_name] = multiplier

    def remove_bonus(self, bonus_name: str) -> None:
        """
        Remove a crafting bonus from active bonuses.

        Args:
            bonus_name: Name/identifier of the bonus to remove
        
        Raises:
            KeyError: If bonus doesn't exist
        """
        if bonus_name not in self.active_bonuses:
            raise KeyError(f"Bonus '{bonus_name}' not found")
        del self.active_bonuses[bonus_name]

    def calculate_effective_success_rate(self) -> float:
        """
        Calculate the effective success rate considering all active bonuses.

        Returns:
            Effective success rate (capped at 0.95)
        """
        effective_rate = self.base_success_rate
        for multiplier in self.active_bonuses.values():
            effective_rate *= multiplier
        
        # Cap success rate to prevent guaranteed success
        return min(effective_rate, 0.95)

    def perform_crafting_attempt(self, item_quality: int, desired_rolls: int = 1) -> Tuple[bool, List[float]]:
        """
        Perform a crafting attempt with potential bonus rolls.

        Args:
            item_quality: Quality tier of the item (1-5)
            desired_rolls: Number of bonus rolls requested (up to max_bonus_rolls)

        Returns:
            Tuple of (success: bool, roll_results: List[float])
        
        Raises:
            ValueError: If item_quality is invalid or desired_rolls exceeds max
        """
        if not 1 <= item_quality <= 5:
            raise ValueError("Item quality must be between 1 and 5")
        if desired_rolls < 1 or desired_rolls > self.max_bonus_rolls:
            raise ValueError(f"Desired rolls must be between 1 and {self.max_bonus_rolls}")

        success_rate = self.calculate_effective_success_rate()
        success = random.random() <= success_rate

        # Apply quality bonus to roll thresholds
        quality_multiplier = 1 + (item_quality - 1) * 0.1
        roll_results = []

        for _ in range(desired_rolls):
            roll_value = random.random() * quality_multiplier
            roll_results.append(roll_value)

        return success, roll_results

    def get_bonus_summary(self) -> Dict[str, float]:
        """
        Get a summary of all active bonuses and their multipliers.

        Returns:
            Dictionary of {bonus_name: multiplier}
        """
        return self.active_bonuses.copy()

    def reset_bonuses(self) -> None:
        """Clear all active bonuses."""
        self.active_bonuses.clear()


# Example usage
if __name__ == "__main__":
    try:
        # Initialize crafting manager
        crafter = CraftingBonusManager(base_success_rate=0.7, max_bonus_rolls=3)
        
        # Add some bonuses
        crafter.add_bonus("expert_crafter", 1.15)
        crafter.add_bonus("premium_materials", 1.1)
        
        # Perform crafting attempt
        success, rolls = crafter.perform_crafting_attempt(item_quality=3, desired_rolls=2)
        
        print(f"Crafting {'successful' if success else 'failed'}")
        print(f"Roll results: {rolls}")
        print(f"Active bonuses: {crafter.get_bonus_summary()}")
        
    except Exception as e:
        print(f"Error: {e}")
```
