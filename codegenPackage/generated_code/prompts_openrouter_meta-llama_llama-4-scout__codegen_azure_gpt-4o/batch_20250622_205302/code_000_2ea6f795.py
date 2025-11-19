"""
Generated Code Metadata:
========================
Original URL: https://questsmisten.pw
Prompt: Write a Python script to generate a quest log for a role-playing game.
Generated: DETERMINISTIC_2ea6f7954a1e5f36
Batch ID: 20250622_205302
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import json
from datetime import datetime

class QuestLog:
    """
    A class to manage a quest log for a role-playing game.
    """
    def __init__(self, log_file="quest_log.json"):
        """
        Initializes the QuestLog instance.

        :param log_file: Path to the file where the quest log will be saved.
        """
        self.log_file = log_file
        self.quests = []
        self.load_log()

    def add_quest(self, title, description, difficulty, status="Incomplete"):
        """
        Adds a new quest to the log.

        :param title: Title of the quest.
        :param description: Description of the quest.
        :param difficulty: Difficulty level of the quest (e.g., Easy, Medium, Hard).
        :param status: Status of the quest (default is "Incomplete").
        """
        quest = {
            "id": len(self.quests) + 1,
            "title": title,
            "description": description,
            "difficulty": difficulty,
            "status": status,
            "created_at": datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        }
        self.quests.append(quest)
        self.save_log()

    def update_quest_status(self, quest_id, new_status):
        """
        Updates the status of a quest.

        :param quest_id: ID of the quest to update.
        :param new_status: New status of the quest (e.g., "Complete", "Failed").
        """
        for quest in self.quests:
            if quest["id"] == quest_id:
                quest["status"] = new_status
                quest["updated_at"] = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
                self.save_log()
                return
        raise ValueError(f"Quest with ID {quest_id} not found.")

    def list_quests(self):
        """
        Lists all quests in the log.

        :return: A list of all quests.
        """
        return self.quests

    def save_log(self):
        """
        Saves the quest log to a file in JSON format.
        """
        try:
            with open(self.log_file, "w") as file:
                json.dump(self.quests, file, indent=4)
        except IOError as e:
            print(f"Error saving quest log: {e}")

    def load_log(self):
        """
        Loads the quest log from a file in JSON format.
        """
        try:
            with open(self.log_file, "r") as file:
                self.quests = json.load(file)
        except FileNotFoundError:
            # If the file doesn't exist, initialize an empty quest log
            self.quests = []
        except json.JSONDecodeError as e:
            print(f"Error loading quest log: {e}")
            self.quests = []

# Example usage
if __name__ == "__main__":
    quest_log = QuestLog()

    # Add some quests
    quest_log.add_quest("Retrieve the Ancient Artifact", "Find and return the artifact to the village elder.", "Hard")
    quest_log.add_quest("Defeat the Goblin King", "Eliminate the Goblin King terrorizing the region.", "Medium")

    # Update a quest status
    try:
        quest_log.update_quest_status(1, "Complete")
    except ValueError as e:
        print(e)

    # List all quests
    for quest in quest_log.list_quests():
        print(json.dumps(quest, indent=4))
```
