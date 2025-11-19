"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://hamsterboost.io
Prompt: What are the unique features of the Hamster Boost mini app for managing blockchain testing quests?
Generated: DETERMINISTIC_3f6077ca31a6a871
Batch ID: 20250612_155936
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
"""
Hamster Boost Mini App for Managing Blockchain Testing Quests

This module provides the core functionality for managing testing quests in the Hamster Boost application.
It includes features for creating, updating, deleting, and retrieving quests. Each quest has a unique ID
and can track its status, priority, and associated tasks.

Key Features:
- Create, update, and delete quests
- Retrieve quest information
- List all quests with filtering options
- Basic error handling for data consistency
"""

import uuid
from typing import List, Dict, Optional

class Quest:
    """
    Represents a testing quest in the Hamster Boost application.
    """

    def __init__(self, title: str, description: str, priority: int):
        self.id = str(uuid.uuid4())  # Unique identifier for the quest
        self.title = title
        self.description = description
        self.priority = priority
        self.is_completed = False

    def mark_completed(self):
        """Mark the quest as completed."""
        self.is_completed = True


class QuestManager:
    """
    Manages a collection of quests.
    """

    def __init__(self):
        self.quests: Dict[str, Quest] = {}  # Dictionary to store quests by their IDs

    def create_quest(self, title: str, description: str, priority: int) -> Quest:
        """
        Create a new quest and add it to the quest manager.

        :param title: The title of the quest.
        :param description: A detailed description of the quest.
        :param priority: The priority level of the quest (1-5).
        :return: The created Quest object.
        """
        if not (1 <= priority <= 5):
            raise ValueError("Priority must be between 1 and 5.")
        
        quest = Quest(title, description, priority)
        self.quests[quest.id] = quest
        return quest

    def update_quest(self, quest_id: str, title: Optional[str] = None, 
                     description: Optional[str] = None, 
                     priority: Optional[int] = None) -> Optional[Quest]:
        """
        Update an existing quest.

        :param quest_id: The ID of the quest to update.
        :param title: New title for the quest.
        :param description: New description for the quest.
        :param priority: New priority for the quest.
        :return: The updated Quest object or None if it doesn't exist.
        """
        quest = self.quests.get(quest_id)
        if not quest:
            print(f"Quest with ID {quest_id} not found.")
            return None
        
        if title:
            quest.title = title
        if description:
            quest.description = description
        if priority is not None:
            if not (1 <= priority <= 5):
                raise ValueError("Priority must be between 1 and 5.")
            quest.priority = priority
        
        return quest

    def delete_quest(self, quest_id: str) -> bool:
        """
        Delete a quest from the quest manager.

        :param quest_id: The ID of the quest to delete.
        :return: True if the quest was deleted, False otherwise.
        """
        if quest_id in self.quests:
            del self.quests[quest_id]
            return True
        print(f"Quest with ID {quest_id} not found.")
        return False

    def get_quest(self, quest_id: str) -> Optional[Quest]:
        """
        Retrieve a quest by its ID.

        :param quest_id: The ID of the quest to retrieve.
        :return: The Quest object or None if it doesn't exist.
        """
        return self.quests.get(quest_id)

    def list_quests(self, completed: Optional[bool] = None) -> List[Quest]:
        """
        List all quests, with optional filtering by completion status.

        :param completed: If provided, filter quests by their completion status.
        :return: A list of Quest objects.
        """
        if completed is None:
            return list(self.quests.values())
        return [quest for quest in self.quests.values() if quest.is_completed == completed]


# Example usage of the QuestManager
if __name__ == "__main__":
    manager = QuestManager()
    
    # Create a quest
    quest1 = manager.create_quest("Test Blockchain Feature", "Verify the functionality of the new blockchain feature.", 3)
    
    # Update the quest
    manager.update_quest(quest1.id, priority=4)
    
    # Mark the quest as completed
    quest1.mark_completed()
    
    # List all quests
    all_quests = manager.list_quests()
    
    # Print quest details
    for quest in all_quests:
        print(f"{quest.title} (ID: {quest.id}, Priority: {quest.priority}, Completed: {quest.is_completed})")
```
