"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://mantadev.pages.dev
Prompt: Generate code to calculate KARMA based on the formula provided in MANTRA Zone: `quest + mission * multiplier`. Include functionality to update KARMA dynamically after completing quests, missions, and multipliers.
Generated: DETERMINISTIC_95677520d4fffbd4
Batch ID: 20250612_151301
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
class KarmaCalculator:
    """
    A class to calculate and dynamically update KARMA based on the formula:
    KARMA = quest + (mission * multiplier)
    """

    def __init__(self):
        """
        Initializes the KarmaCalculator with default values for quest, mission, and multiplier.
        Sets the initial KARMA value to 0.
        """
        self.quest = 0
        self.mission = 0
        self.multiplier = 1
        self.karma = 0

    def update_values(self, quest: int = None, mission: int = None, multiplier: float = None):
        """
        Updates the quest, mission, and multiplier values dynamically.
        Recalculates KARMA after updating the values.

        Args:
            quest (int, optional): The new quest value. Defaults to None (no update).
            mission (int, optional): The new mission value. Defaults to None (no update).
            multiplier (float, optional): The new multiplier value. Defaults to None (no update).
        """
        if quest is not None:
            if quest < 0:
                raise ValueError("Quest value cannot be negative")
            self.quest = quest

        if mission is not None:
            if mission < 0:
                raise ValueError("Mission value cannot be negative")
            self.mission = mission

        if multiplier is not None:
            if multiplier < 0:
                raise ValueError("Multiplier value cannot be negative")
            self.multiplier = multiplier

        self.calculate_karma()

    def calculate_karma(self):
        """
        Calculates KARMA based on the formula:
        KARMA = quest + (mission * multiplier)
        """
        self.karma = self.quest + (self.mission * self.multiplier)

    def get_karma(self) -> float:
        """
        Returns the current KARMA value.

        Returns:
            float: The calculated KARMA value.
        """
        return self.karma


# Example Usage
if __name__ == "__main__":
    try:
        # Initialize the KarmaCalculator
        calculator = KarmaCalculator()

        # Update values
        calculator.update_values(quest=10, mission=5, multiplier=2.5)
        print("Updated KARMA:", calculator.get_karma())  # Output: 22.5

        # Update only the quest value
        calculator.update_values(quest=15)
        print("Updated KARMA after changing quest:", calculator.get_karma())  # Output: 27.5

        # Update mission and multiplier
        calculator.update_values(mission=4, multiplier=3)
        print("Updated KARMA after changing mission and multiplier:", calculator.get_karma())  # Output: 27.0

    except ValueError as e:
        print("Error:", e)
    except Exception as e:
        print("Unexpected error:", e)
```
