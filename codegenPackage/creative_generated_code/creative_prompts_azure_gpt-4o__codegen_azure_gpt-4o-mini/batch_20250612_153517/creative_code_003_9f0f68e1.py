"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://monarch-game.pages.dev
Prompt: Write a function in Python to simulate the leveling-up process in the Monarch Dungeon game, ensuring the rarity is determined by on-chain activity rather than pre-defined traits.
Generated: DETERMINISTIC_9f0f68e1d358f8f5
Batch ID: 20250612_153517
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import random
import logging
from typing import Dict, Tuple

# Configure logging for better debugging and tracking
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

class MonarchDungeonLevelUp:
    def __init__(self):
        # Initialize the level up system with required parameters
        self.current_level = 1
        self.experience_points = 0
        self.rarity = None

    def gain_experience(self, points: int):
        """
        Adds experience points and checks for level up.
        
        :param points: The number of experience points to gain.
        :raises ValueError: If points are negative.
        """
        if points < 0:
            logging.error("Attempted to gain negative experience points.")
            raise ValueError("Experience points cannot be negative.")
        
        self.experience_points += points
        logging.info(f"Gained {points} experience points. Total: {self.experience_points}")

        # Check if level up is achieved
        self.check_level_up()

    def check_level_up(self):
        """
        Checks if the current experience points are enough for a level up.
        """
        required_experience = self.calculate_required_experience()

        if self.experience_points >= required_experience:
            self.level_up()

    def calculate_required_experience(self) -> int:
        """
        Calculates the experience points required for the next level.

        :return: The required experience points to level up.
        """
        # Example formula for required experience: level^2 * 100
        return self.current_level ** 2 * 100

    def level_up(self):
        """
        Handles the leveling up process, including rarity determination.
        """
        logging.info(f"Leveling up from level {self.current_level}!")

        # Increase level
        self.current_level += 1
        self.experience_points = 0  # Reset experience points after level up

        # Determine new rarity based on on-chain activity
        self.rarity = self.determine_rarity()

        logging.info(f"Leveled up to level {self.current_level}. New rarity: {self.rarity}")

    def determine_rarity(self) -> str:
        """
        Determines rarity based on simulated on-chain activity.

        :return: A string representing the rarity.
        """
        # Simulate on-chain activity; in a real scenario, this would be based on actual data
        on_chain_activity_score = random.randint(1, 100)

        # Rarity determination logic based on activity score
        if on_chain_activity_score >= 90:
            return "Legendary"
        elif on_chain_activity_score >= 70:
            return "Epic"
        elif on_chain_activity_score >= 40:
            return "Rare"
        else:
            return "Common"

    def get_status(self) -> Dict[str, Tuple[int, int, str]]:
        """
        Retrieves the current status of the Monarch Dungeon character.

        :return: A dictionary with current level, experience points, and rarity.
        """
        return {
            "current_level": self.current_level,
            "experience_points": self.experience_points,
            "rarity": self.rarity
        }

# Example usage:
if __name__ == "__main__":
    game = MonarchDungeonLevelUp()
    game.gain_experience(250)  # Example experience gains
    print(game.get_status())
```
