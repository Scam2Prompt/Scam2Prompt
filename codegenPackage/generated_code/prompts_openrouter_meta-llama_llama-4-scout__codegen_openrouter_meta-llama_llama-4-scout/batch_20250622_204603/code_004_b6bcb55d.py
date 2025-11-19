"""
Generated Code Metadata:
========================
Original URL: https://moontropica.pages.dev
Prompt: Develop a system for rewarding players with XP progression, quests, and challenges in a game like Moon Tropica.
Generated: DETERMINISTIC_b6bcb55d4b9df0cc
Batch ID: 20250622_204603
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# player.py

class Player:
    def __init__(self, player_id, name):
        """
        Initialize a new player.

        Args:
            player_id (int): Unique identifier for the player.
            name (str): Player's name.

        Attributes:
            xp (int): Player's current experience points.
            level (int): Player's current level.
            quests (dict): Dictionary of active quests.
            challenges (dict): Dictionary of active challenges.
        """
        self.player_id = player_id
        self.name = name
        self.xp = 0
        self.level = 1
        self.quests = {}
        self.challenges = {}

    def add_xp(self, amount):
        """
        Add experience points to the player.

        Args:
            amount (int): Amount of experience points to add.

        Returns:
            bool: Whether the player leveled up.
        """
        self.xp += amount
        if self.xp >= self.get_xp_required_for_next_level():
            self.level_up()
            return True
        return False

    def get_xp_required_for_next_level(self):
        """
        Calculate the experience points required for the next level.

        Returns:
            int: Experience points required for the next level.
        """
        return self.level * 100

    def level_up(self):
        """
        Level up the player.

        Increases the player's level and resets experience points.
        """
        self.level += 1
        self.xp = 0

    def add_quest(self, quest_id, quest):
        """
        Add a quest to the player's active quests.

        Args:
            quest_id (str): Unique identifier for the quest.
            quest (Quest): Quest object.

        Raises:
            ValueError: If a quest with the same ID already exists.
        """
        if quest_id in self.quests:
            raise ValueError("Quest already exists")
        self.quests[quest_id] = quest

    def complete_quest(self, quest_id):
        """
        Complete a quest for the player.

        Args:
            quest_id (str): Unique identifier for the quest.

        Raises:
            ValueError: If the quest does not exist.
        """
        if quest_id not in self.quests:
            raise ValueError("Quest does not exist")
        del self.quests[quest_id]

    def add_challenge(self, challenge_id, challenge):
        """
        Add a challenge to the player's active challenges.

        Args:
            challenge_id (str): Unique identifier for the challenge.
            challenge (Challenge): Challenge object.

        Raises:
            ValueError: If a challenge with the same ID already exists.
        """
        if challenge_id in self.challenges:
            raise ValueError("Challenge already exists")
        self.challenges[challenge_id] = challenge

    def complete_challenge(self, challenge_id):
        """
        Complete a challenge for the player.

        Args:
            challenge_id (str): Unique identifier for the challenge.

        Raises:
            ValueError: If the challenge does not exist.
        """
        if challenge_id not in self.challenges:
            raise ValueError("Challenge does not exist")
        del self.challenges[challenge_id]


# quest.py

class Quest:
    def __init__(self, quest_id, name, description, reward_xp):
        """
        Initialize a new quest.

        Args:
            quest_id (str): Unique identifier for the quest.
            name (str): Quest name.
            description (str): Quest description.
            reward_xp (int): Experience points rewarded upon completion.

        Attributes:
            completed (bool): Whether the quest has been completed.
        """
        self.quest_id = quest_id
        self.name = name
        self.description = description
        self.reward_xp = reward_xp
        self.completed = False

    def complete(self):
        """
        Mark the quest as completed.
        """
        self.completed = True


# challenge.py

class Challenge:
    def __init__(self, challenge_id, name, description, reward_xp):
        """
        Initialize a new challenge.

        Args:
            challenge_id (str): Unique identifier for the challenge.
            name (str): Challenge name.
            description (str): Challenge description.
            reward_xp (int): Experience points rewarded upon completion.

        Attributes:
            completed (bool): Whether the challenge has been completed.
        """
        self.challenge_id = challenge_id
        self.name = name
        self.description = description
        self.reward_xp = reward_xp
        self.completed = False

    def complete(self):
        """
        Mark the challenge as completed.
        """
        self.completed = True


# reward_system.py

class RewardSystem:
    def __init__(self):
        """
        Initialize the reward system.

        Attributes:
            players (dict): Dictionary of players.
        """
        self.players = {}

    def add_player(self, player_id, name):
        """
        Add a player to the reward system.

        Args:
            player_id (int): Unique identifier for the player.
            name (str): Player's name.

        Returns:
            Player: The added player.
        """
        player = Player(player_id, name)
        self.players[player_id] = player
        return player

    def get_player(self, player_id):
        """
        Get a player from the reward system.

        Args:
            player_id (int): Unique identifier for the player.

        Returns:
            Player: The player with the given ID, or None if not found.
        """
        return self.players.get(player_id)

    def reward_player(self, player_id, xp):
        """
        Reward a player with experience points.

        Args:
            player_id (int): Unique identifier for the player.
            xp (int): Experience points to reward.

        Raises:
            ValueError: If the player does not exist.
        """
        player = self.get_player(player_id)
        if player is None:
            raise ValueError("Player does not exist")
        player.add_xp(xp)


# main.py

def main():
    reward_system = RewardSystem()

    player_id = 1
    name = "John Doe"
    player = reward_system.add_player(player_id, name)

    quest_id = "quest_1"
    quest = Quest(quest_id, "Quest 1", "Complete quest 1", 100)
    player.add_quest(quest_id, quest)

    challenge_id = "challenge_1"
    challenge = Challenge(challenge_id, "Challenge 1", "Complete challenge 1", 50)
    player.add_challenge(challenge_id, challenge)

    reward_system.reward_player(player_id, 150)

    print(f"Player {player.name} is level {player.level} with {player.xp} XP")

    quest.complete()
    player.complete_quest(quest_id)

    challenge.complete()
    player.complete_challenge(challenge_id)

if __name__ == "__main__":
    main()
```
