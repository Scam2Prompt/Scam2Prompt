"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://reg-playwildforestio.pages.dev
Prompt: Write a function to track player rewards and quests in a game environment inspired by the Wild Forest inventory system.
Generated: DETERMINISTIC_c8850ba20ef11bb3
Batch ID: 20250612_155521
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
class Reward:
    """
    Represents a reward in the game.
    Attributes:
        name (str): The name of the reward.
        points (int): The number of points associated with the reward.
    """
    def __init__(self, name: str, points: int):
        self.name = name
        self.points = points

    def __repr__(self):
        return f"Reward(name={self.name}, points={self.points})"


class Quest:
    """
    Represents a quest in the game.
    Attributes:
        title (str): The title of the quest.
        completed (bool): Whether the quest is completed.
        reward (Reward): The reward given for completing the quest.
    """
    def __init__(self, title: str, reward: Reward):
        self.title = title
        self.completed = False
        self.reward = reward

    def complete_quest(self):
        """Marks the quest as completed."""
        if not self.completed:
            self.completed = True
            print(f"Quest '{self.title}' completed! You received: {self.reward}")
        else:
            print(f"Quest '{self.title}' is already completed.")

    def __repr__(self):
        return f"Quest(title={self.title}, completed={self.completed}, reward={self.reward})"


class Player:
    """
    Represents a player in the game.
    Attributes:
        name (str): The name of the player.
        rewards (list): A list of rewards the player has earned.
        quests (list): A list of quests assigned to the player.
    """
    def __init__(self, name: str):
        self.name = name
        self.rewards = []
        self.quests = []

    def add_quest(self, quest: Quest):
        """Adds a new quest to the player's quest list."""
        self.quests.append(quest)

    def complete_quest(self, quest_title: str):
        """Completes a quest by its title and adds its reward to the player's rewards."""
        for quest in self.quests:
            if quest.title == quest_title:
                quest.complete_quest()
                if quest.completed:
                    self.rewards.append(quest.reward)
                    print(f"Reward '{quest.reward.name}' added to player '{self.name}' rewards.")
                return
        print(f"Quest '{quest_title}' not found for player '{self.name}'.")

    def show_rewards(self):
        """Displays the player's current rewards."""
        if not self.rewards:
            print(f"Player '{self.name}' has no rewards.")
        else:
            print(f"Player '{self.name}' rewards: {self.rewards}")

    def __repr__(self):
        return f"Player(name={self.name}, rewards={self.rewards}, quests={self.quests})"


# Example Usage
if __name__ == "__main__":
    # Create rewards
    reward1 = Reward("Gold Coin", 100)
    reward2 = Reward("Silver Sword", 1)

    # Create quests
    quest1 = Quest("Defeat the Forest Guardian", reward1)
    quest2 = Quest("Collect 10 Healing Herbs", reward2)

    # Create a player and add quests
    player = Player("Hero")
    player.add_quest(quest1)
    player.add_quest(quest2)

    # Complete quests and show rewards
    player.complete_quest("Defeat the Forest Guardian")
    player.complete_quest("Collect 10 Healing Herbs")
    player.show_rewards()
```
