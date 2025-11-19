"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://hamsterkom-com.pages.dev
Prompt: Create a function that tracks user progress through quests and upgrades in a game, inspired by the mechanics of Hamster Kombat.
Generated: DETERMINISTIC_18858ee35e0ec5b5
Batch ID: 20250612_155131
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
class Quest:
    """Represents a quest in the game."""
    def __init__(self, quest_id, name, description):
        self.quest_id = quest_id
        self.name = name
        self.description = description
        self.is_completed = False

    def complete(self):
        """Marks the quest as completed."""
        self.is_completed = True


class Upgrade:
    """Represents an upgrade in the game."""
    def __init__(self, upgrade_id, name, description):
        self.upgrade_id = upgrade_id
        self.name = name
        self.description = description
        self.is_applied = False

    def apply(self):
        """Applies the upgrade."""
        self.is_applied = True


class UserProgress:
    """Tracks user progress through quests and upgrades."""
    def __init__(self, user_id):
        self.user_id = user_id
        self.quests = {}
        self.upgrades = {}

    def add_quest(self, quest: Quest):
        """Adds a quest to the user's progress."""
        if quest.quest_id in self.quests:
            raise ValueError(f"Quest ID {quest.quest_id} already exists.")
        self.quests[quest.quest_id] = quest

    def complete_quest(self, quest_id):
        """Marks a quest as completed."""
        if quest_id not in self.quests:
            raise ValueError(f"Quest ID {quest_id} not found.")
        self.quests[quest_id].complete()

    def add_upgrade(self, upgrade: Upgrade):
        """Adds an upgrade to the user's progress."""
        if upgrade.upgrade_id in self.upgrades:
            raise ValueError(f"Upgrade ID {upgrade.upgrade_id} already exists.")
        self.upgrades[upgrade.upgrade_id] = upgrade

    def apply_upgrade(self, upgrade_id):
        """Applies an upgrade to the user."""
        if upgrade_id not in self.upgrades:
            raise ValueError(f"Upgrade ID {upgrade_id} not found.")
        self.upgrades[upgrade_id].apply()

    def get_progress_summary(self):
        """Returns a summary of quests and upgrades."""
        completed_quests = [quest.name for quest in self.quests.values() if quest.is_completed]
        applied_upgrades = [upgrade.name for upgrade in self.upgrades.values() if upgrade.is_applied]

        return {
            "completed_quests": completed_quests,
            "applied_upgrades": applied_upgrades
        }


# Example usage
if __name__ == "__main__":
    try:
        user_progress = UserProgress(user_id="player1")

        # Adding quests
        quest1 = Quest(quest_id=1, name="Quest of the Brave", description="Defeat the dragon.")
        user_progress.add_quest(quest1)

        # Completing a quest
        user_progress.complete_quest(1)

        # Adding upgrades
        upgrade1 = Upgrade(upgrade_id=1, name="Sword of Valor", description="Increase attack power.")
        user_progress.add_upgrade(upgrade1)

        # Applying an upgrade
        user_progress.apply_upgrade(1)

        # Get progress summary
        summary = user_progress.get_progress_summary()
        print(summary)

    except ValueError as e:
        print(f"Error: {e}")
```
