"""
Generated Code Metadata:
========================
Original URL: https://bearsontheblock.com
Prompt: Generate code to simulate a competitive quest on Nifty Island, including logic for awarding NFTs and crypto prizes.
Generated: DETERMINISTIC_24f0c13fb4e7d01c
Batch ID: 20250612_151354
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import random
from typing import List, Dict, Any

class Quest:
    def __init__(self, name: str, difficulty: int, nft_reward: str, crypto_reward: float):
        """
        Initialize a new quest with the given parameters.

        :param name: The name of the quest.
        :param difficulty: The difficulty level of the quest (1-10).
        :param nft_reward: The NFT awarded for completing the quest.
        :param crypto_reward: The amount of cryptocurrency awarded for completing the quest.
        """
        self.name = name
        self.difficulty = difficulty
        self.nft_reward = nft_reward
        self.crypto_reward = crypto_reward

    def __str__(self):
        return f"Quest(name={self.name}, difficulty={self.difficulty}, nft_reward={self.nft_reward}, crypto_reward={self.crypto_reward})"


class Player:
    def __init__(self, username: str):
        """
        Initialize a new player with a username.

        :param username: The player's username.
        """
        self.username = username
        self.completed_quests: List[Quest] = []
        self.crypto_balance: float = 0.0

    def complete_quest(self, quest: Quest):
        """
        Complete a quest and receive rewards.

        :param quest: The quest to be completed.
        """
        self.completed_quests.append(quest)
        self.crypto_balance += quest.crypto_reward
        print(f"{self.username} completed the quest: {quest.name} and received {quest.nft_reward} and {quest.crypto_reward} crypto!")

    def __str__(self):
        return f"Player(username={self.username}, completed_quests={len(self.completed_quests)}, crypto_balance={self.crypto_balance})"


class QuestSimulator:
    def __init__(self):
        """
        Initialize the quest simulator with a list of available quests.
        """
        self.quests: List[Quest] = self.generate_quests()

    def generate_quests(self) -> List[Quest]:
        """
        Generate a list of quests with random parameters.

        :return: A list of Quest objects.
        """
        quests = []
        for i in range(5):  # Generate 5 quests
            quest_name = f"Quest {i + 1}"
            difficulty = random.randint(1, 10)
            nft_reward = f"NFT-{random.randint(1000, 9999)}"
            crypto_reward = round(random.uniform(0.01, 1.0), 2)
            quests.append(Quest(quest_name, difficulty, nft_reward, crypto_reward))
        return quests

    def start_quest(self, player: Player, quest_index: int):
        """
        Start a quest for the player.

        :param player: The player who is starting the quest.
        :param quest_index: The index of the quest in the quest list.
        """
        try:
            quest = self.quests[quest_index]
            print(f"{player.username} is starting the quest: {quest.name}")
            player.complete_quest(quest)
        except IndexError:
            print("Error: Quest index out of range. Please select a valid quest.")
        except Exception as e:
            print(f"An unexpected error occurred: {e}")


# Example usage
if __name__ == "__main__":
    # Create a player
    player1 = Player("Adventurer123")

    # Initialize the quest simulator
    simulator = QuestSimulator()

    # Display available quests
    print("Available Quests:")
    for idx, quest in enumerate(simulator.quests):
        print(f"{idx}: {quest}")

    # Start a quest
    quest_to_start = int(input("Enter the quest number you want to start: "))
    simulator.start_quest(player1, quest_to_start)

    # Display player status
    print(player1)
```
