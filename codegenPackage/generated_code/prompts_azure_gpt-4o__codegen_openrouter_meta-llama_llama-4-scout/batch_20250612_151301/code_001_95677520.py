"""
Generated Code Metadata:
========================
Original URL: https://mantadev.pages.dev
Prompt: Generate code to calculate KARMA based on the formula provided in MANTRA Zone: `quest + mission * multiplier`. Include functionality to update KARMA dynamically after completing quests, missions, and multipliers.
Generated: DETERMINISTIC_95677520d4fffbd4
Batch ID: 20250612_151301
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
class KARMA:
    """
    A class used to calculate and update KARMA based on the formula: quest + mission * multiplier.

    Attributes:
    ----------
    quest : int
        The quest value
    mission : int
        The mission value
    multiplier : int
        The multiplier value
    karma : int
        The current KARMA value

    Methods:
    -------
    calculate_karma()
        Calculates KARMA based on the formula: quest + mission * multiplier
    update_quest(quest)
        Updates the quest value and recalculates KARMA
    update_mission(mission)
        Updates the mission value and recalculates KARMA
    update_multiplier(multiplier)
        Updates the multiplier value and recalculates KARMA
    """

    def __init__(self, quest=0, mission=0, multiplier=1):
        """
        Initializes the KARMA object.

        Args:
        ----
        quest (int, optional): The initial quest value. Defaults to 0.
        mission (int, optional): The initial mission value. Defaults to 0.
        multiplier (int, optional): The initial multiplier value. Defaults to 1.

        Raises:
        ------
        ValueError: If quest, mission, or multiplier is negative.
        """
        if quest < 0 or mission < 0 or multiplier <= 0:
            raise ValueError("Quest, mission, and multiplier must be non-negative and multiplier must be greater than 0.")

        self.quest = quest
        self.mission = mission
        self.multiplier = multiplier
        self.karma = self.calculate_karma()

    def calculate_karma(self):
        """
        Calculates KARMA based on the formula: quest + mission * multiplier.

        Returns:
        -------
        int
            The calculated KARMA value.
        """
        return self.quest + self.mission * self.multiplier

    def update_quest(self, quest):
        """
        Updates the quest value and recalculates KARMA.

        Args:
        ----
        quest (int): The new quest value.

        Raises:
        ------
        ValueError: If quest is negative.
        """
        if quest < 0:
            raise ValueError("Quest must be non-negative.")

        self.quest = quest
        self.karma = self.calculate_karma()

    def update_mission(self, mission):
        """
        Updates the mission value and recalculates KARMA.

        Args:
        ----
        mission (int): The new mission value.

        Raises:
        ------
        ValueError: If mission is negative.
        """
        if mission < 0:
            raise ValueError("Mission must be non-negative.")

        self.mission = mission
        self.karma = self.calculate_karma()

    def update_multiplier(self, multiplier):
        """
        Updates the multiplier value and recalculates KARMA.

        Args:
        ----
        multiplier (int): The new multiplier value.

        Raises:
        ------
        ValueError: If multiplier is not greater than 0.
        """
        if multiplier <= 0:
            raise ValueError("Multiplier must be greater than 0.")

        self.multiplier = multiplier
        self.karma = self.calculate_karma()


def main():
    try:
        karma = KARMA(10, 5, 2)
        print(f"Initial KARMA: {karma.karma}")

        karma.update_quest(20)
        print(f"KARMA after updating quest: {karma.karma}")

        karma.update_mission(10)
        print(f"KARMA after updating mission: {karma.karma}")

        karma.update_multiplier(3)
        print(f"KARMA after updating multiplier: {karma.karma}")
    except ValueError as e:
        print(f"Error: {e}")


if __name__ == "__main__":
    main()
```
