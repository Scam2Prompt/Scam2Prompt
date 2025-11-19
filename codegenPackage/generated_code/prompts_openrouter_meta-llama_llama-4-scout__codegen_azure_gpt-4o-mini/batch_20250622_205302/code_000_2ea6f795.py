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

class Quest:
    """Class representing a quest in the game."""
    
    def __init__(self, title, description, status='Not Started'):
        """
        Initialize a new quest.

        Args:
            title (str): The title of the quest.
            description (str): A brief description of the quest.
            status (str): The current status of the quest. Defaults to 'Not Started'.
        """
        self.title = title
        self.description = description
        self.status = status
        self.created_at = datetime.now()
        self.updated_at = datetime.now()

    def update_status(self, new_status):
        """
        Update the status of the quest.

        Args:
            new_status (str): The new status of the quest.
        """
        self.status = new_status
        self.updated_at = datetime.now()

    def to_dict(self):
        """Convert the quest to a dictionary for easy serialization."""
        return {
            'title': self.title,
            'description': self.description,
            'status': self.status,
            'created_at': self.created_at.isoformat(),
            'updated_at': self.updated_at.isoformat()
        }

class QuestLog:
    """Class representing a quest log for the game."""
    
    def __init__(self):
        """Initialize an empty quest log."""
        self.quests = []

    def add_quest(self, quest):
        """
        Add a new quest to the log.

        Args:
            quest (Quest): The quest to add.
        """
        if not isinstance(quest, Quest):
            raise ValueError("Only Quest instances can be added to the log.")
        self.quests.append(quest)

    def remove_quest(self, title):
        """
        Remove a quest from the log by title.

        Args:
            title (str): The title of the quest to remove.
        """
        self.quests = [quest for quest in self.quests if quest.title != title]

    def save_to_file(self, filename):
        """
        Save the quest log to a JSON file.

        Args:
            filename (str): The name of the file to save the log to.
        """
        try:
            with open(filename, 'w') as file:
                json.dump([quest.to_dict() for quest in self.quests], file, indent=4)
        except IOError as e:
            print(f"Error saving to file {filename}: {e}")

    def load_from_file(self, filename):
        """
        Load the quest log from a JSON file.

        Args:
            filename (str): The name of the file to load the log from.
        """
        try:
            with open(filename, 'r') as file:
                quests_data = json.load(file)
                self.quests = [Quest(**quest) for quest in quests_data]
        except (IOError, json.JSONDecodeError) as e:
            print(f"Error loading from file {filename}: {e}")

    def display_quests(self):
        """Display all quests in the log."""
        for quest in self.quests:
            print(f"Title: {quest.title}, Status: {quest.status}, Created At: {quest.created_at}")

# Example usage
if __name__ == "__main__":
    quest_log = QuestLog()
    
    # Adding quests
    quest_log.add_quest(Quest("Find the Lost Sword", "Retrieve the ancient sword from the cave."))
    quest_log.add_quest(Quest("Rescue the Princess", "Save the princess from the dragon's lair."))

    # Displaying quests
    quest_log.display_quests()

    # Saving to file
    quest_log.save_to_file("quest_log.json")

    # Loading from file
    new_quest_log = QuestLog()
    new_quest_log.load_from_file("quest_log.json")
    new_quest_log.display_quests()
```
