"""
Generated Code Metadata:
========================
Original URL: https://moontropica-rewards.web.app
Prompt: Develop a quest and challenge system for a game like Moon Tropica, with rewards and XP progression for players.
Generated: DETERMINISTIC_39d61b3a6c31c7e0
Batch ID: 20250622_205039
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import random

class Quest:
    """
    Represents a quest in the game.
    """
    def __init__(self, name, description, difficulty, reward, xp):
        """
        Initializes a new quest.

        :param name: Name of the quest
        :param description: Description of the quest
        :param difficulty: Difficulty level of the quest (Easy, Medium, Hard)
        :param reward: Reward for completing the quest
        :param xp: XP gained upon completion
        """
        self.name = name
        self.description = description
        self.difficulty = difficulty
        self.reward = reward
        self.xp = xp
        self.completed = False

    def complete_quest(self):
        """
        Marks the quest as completed.
        """
        if not self.completed:
            self.completed = True
            return self.reward, self.xp
        else:
            raise ValueError("Quest already completed.")

class Player:
    """
    Represents a player in the game.
    """
    def __init__(self, name):
        """
        Initializes a new player.

        :param name: Name of the player
        """
        self.name = name
        self.level = 1
        self.xp = 0
        self.inventory = []

    def add_xp(self, xp):
        """
        Adds XP to the player and handles level progression.

        :param xp: XP to add
        """
        self.xp += xp
        while self.xp >= self.xp_to_next_level():
            self.level_up()

    def xp_to_next_level(self):
        """
        Calculates the XP required to reach the next level.

        :return: XP required for the next level
        """
        return self.level * 100

    def level_up(self):
        """
        Levels up the player.
        """
        self.level += 1
        self.xp -= self.xp_to_next_level()
        print(f"{self.name} leveled up! Now at level {self.level}.")

    def add_reward(self, reward):
        """
        Adds a reward to the player's inventory.

        :param reward: Reward to add
        """
        self.inventory.append(reward)

class Game:
    """
    Represents the game system.
    """
    def __init__(self):
        """
        Initializes the game system.
        """
        self.players = {}
        self.quests = []

    def add_player(self, player_name):
        """
        Adds a new player to the game.

        :param player_name: Name of the player
        """
        if player_name in self.players:
            raise ValueError("Player already exists.")
        self.players[player_name] = Player(player_name)

    def add_quest(self, name, description, difficulty, reward, xp):
        """
        Adds a new quest to the game.

        :param name: Name of the quest
        :param description: Description of the quest
        :param difficulty: Difficulty level of the quest
        :param reward: Reward for completing the quest
        :param xp: XP gained upon completion
        """
        self.quests.append(Quest(name, description, difficulty, reward, xp))

    def assign_quest_to_player(self, player_name):
        """
        Assigns a random quest to a player.

        :param player_name: Name of the player
        """
        if player_name not in self.players:
            raise ValueError("Player not found.")
        if not self.quests:
            raise ValueError("No quests available.")
        quest = random.choice(self.quests)
        print(f"Assigned quest '{quest.name}' to player '{player_name}'.")
        return quest

    def complete_quest(self, player_name, quest):
        """
        Completes a quest for a player.

        :param player_name: Name of the player
        :param quest: Quest to complete
        """
        if player_name not in self.players:
            raise ValueError("Player not found.")
        player = self.players[player_name]
        try:
            reward, xp = quest.complete_quest()
            player.add_reward(reward)
            player.add_xp(xp)
            print(f"Player '{player_name}' completed quest '{quest.name}' and earned {xp} XP and reward: {reward}.")
        except ValueError as e:
            print(e)

# Example usage
if __name__ == "__main__":
    game = Game()

    # Add players
    game.add_player("Alice")
    game.add_player("Bob")

    # Add quests
    game.add_quest("Find the Lost Artifact", "Locate the ancient artifact in the forest.", "Medium", "Golden Sword", 150)
    game.add_quest("Defeat the Dragon", "Slay the dragon terrorizing the village.", "Hard", "Dragon Shield", 300)
    game.add_quest("Gather Herbs", "Collect 10 healing herbs from the meadow.", "Easy", "Healing Potion", 50)

    # Assign and complete quests
    quest_for_alice = game.assign_quest_to_player("Alice")
    game.complete_quest("Alice", quest_for_alice)

    quest_for_bob = game.assign_quest_to_player("Bob")
    game.complete_quest("Bob", quest_for_bob)
```
