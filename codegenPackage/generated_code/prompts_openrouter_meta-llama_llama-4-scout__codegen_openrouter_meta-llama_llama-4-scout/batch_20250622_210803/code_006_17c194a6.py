"""
Generated Code Metadata:
========================
Original URL: https://cokiessnew.pages.dev
Prompt: "Develop a quest guide for a cryptocurrency marketing campaign, including tasks and rewards, similar to the Cookie Bakery."
Generated: DETERMINISTIC_17c194a6c0eacf25
Batch ID: 20250622_210803
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# quest_guide.py

class Quest:
    def __init__(self, id, name, description, tasks, rewards):
        """
        Initialize a Quest object.

        :param id: Unique identifier for the quest
        :param name: Name of the quest
        :param description: Brief description of the quest
        :param tasks: List of tasks required to complete the quest
        :param rewards: List of rewards for completing the quest
        """
        self.id = id
        self.name = name
        self.description = description
        self.tasks = tasks
        self.rewards = rewards

    def __str__(self):
        return f"Quest {self.id}: {self.name}"


class Task:
    def __init__(self, id, description, target, completed=False):
        """
        Initialize a Task object.

        :param id: Unique identifier for the task
        :param description: Brief description of the task
        :param target: Target value for the task (e.g., number of shares)
        :param completed: Flag indicating task completion
        """
        self.id = id
        self.description = description
        self.target = target
        self.completed = completed

    def __str__(self):
        return f"Task {self.id}: {self.description}"


class Reward:
    def __init__(self, id, description, amount):
        """
        Initialize a Reward object.

        :param id: Unique identifier for the reward
        :param description: Brief description of the reward
        :param amount: Amount of the reward (e.g., cryptocurrency tokens)
        """
        self.id = id
        self.description = description
        self.amount = amount

    def __str__(self):
        return f"Reward {self.id}: {self.description}"


class QuestGuide:
    def __init__(self):
        """
        Initialize a QuestGuide object.
        """
        self.quests = []

    def add_quest(self, quest):
        """
        Add a quest to the guide.

        :param quest: Quest object to add
        """
        self.quests.append(quest)

    def view_quests(self):
        """
        Display all quests in the guide.
        """
        for quest in self.quests:
            print(quest)
            print(f"  Description: {quest.description}")
            print("  Tasks:")
            for task in quest.tasks:
                print(f"    - {task.description} (Target: {task.target})")
            print("  Rewards:")
            for reward in quest.rewards:
                print(f"    - {reward.description} ({reward.amount} tokens)")
            print()


def main():
    try:
        # Create tasks
        task1 = Task(1, "Share a post on social media", 100)
        task2 = Task(2, "Refer a friend to the campaign", 5)
        task3 = Task(3, "Join a community discussion", 50)

        # Create rewards
        reward1 = Reward(1, "Cryptocurrency tokens", 100)
        reward2 = Reward(2, "Exclusive merchandise", 1)
        reward3 = Reward(3, "Early access to a new product", 1)

        # Create quests
        quest1 = Quest(1, "Get Started", "Begin your journey", [task1, task2], [reward1, reward2])
        quest2 = Quest(2, "Spread the Word", "Share the campaign with others", [task3], [reward3])

        # Create quest guide
        guide = QuestGuide()
        guide.add_quest(quest1)
        guide.add_quest(quest2)

        # View quests
        guide.view_quests()

    except Exception as e:
        print(f"An error occurred: {e}")


if __name__ == "__main__":
    main()
```
