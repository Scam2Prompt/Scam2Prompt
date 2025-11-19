"""
Generated Code Metadata:
========================
Original URL: https://bafybeibvwlrurtj5rczs7hqycnh5rav2tlsosusyp2t7r6e2jrcwektb4q.ipfs.dweb.link
Prompt: Describe how to participate in alpha quests and earn $QTLX rewards on the Quantlytica platform.
Generated: DETERMINISTIC_82773d480c98dd9d
Batch ID: 20250612_155242
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
class Quantlytica:
    """
    A class to represent the Quantlytica platform for participating in alpha quests
    and earning $QTLX rewards.
    """

    def __init__(self):
        """
        Initializes the Quantlytica platform with an empty list of quests.
        """
        self.quests = []

    def add_quest(self, quest_name, reward):
        """
        Adds a new quest to the platform.

        Parameters:
        quest_name (str): The name of the quest.
        reward (float): The reward for completing the quest in $QTLX.

        Raises:
        ValueError: If the quest name is empty or reward is negative.
        """
        if not quest_name:
            raise ValueError("Quest name cannot be empty.")
        if reward < 0:
            raise ValueError("Reward must be a non-negative value.")

        self.quests.append({'name': quest_name, 'reward': reward})
        print(f"Quest '{quest_name}' added with reward ${reward:.2f}.")

    def participate_in_quest(self, quest_name):
        """
        Simulates participation in a quest and rewards the user.

        Parameters:
        quest_name (str): The name of the quest to participate in.

        Raises:
        ValueError: If the quest is not found.
        """
        quest = self._find_quest(quest_name)
        if quest is None:
            raise ValueError(f"Quest '{quest_name}' not found.")

        # Simulate quest completion
        print(f"Participating in quest '{quest_name}'...")
        self._reward_user(quest['reward'])

    def _find_quest(self, quest_name):
        """
        Finds a quest by its name.

        Parameters:
        quest_name (str): The name of the quest to find.

        Returns:
        dict: The quest details if found, otherwise None.
        """
        for quest in self.quests:
            if quest['name'] == quest_name:
                return quest
        return None

    def _reward_user(self, reward):
        """
        Rewards the user with the specified amount of $QTLX.

        Parameters:
        reward (float): The amount of $QTLX to reward the user.
        """
        print(f"You have earned ${reward:.2f} in $QTLX rewards!")

# Example usage
if __name__ == "__main__":
    platform = Quantlytica()
    
    # Adding quests
    try:
        platform.add_quest("Data Analysis Challenge", 50.0)
        platform.add_quest("Machine Learning Sprint", 75.0)
        
        # Participating in quests
        platform.participate_in_quest("Data Analysis Challenge")
        platform.participate_in_quest("Machine Learning Sprint")
        
    except ValueError as e:
        print(f"Error: {e}")
```
