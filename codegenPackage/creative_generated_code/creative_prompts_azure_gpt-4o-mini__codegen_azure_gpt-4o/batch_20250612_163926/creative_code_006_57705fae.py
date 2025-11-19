"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://hamsbat.com
Prompt: How can I create special cards and airdrop tasks for a game based on the roadmap of Hamster Kombat?
Generated: DETERMINISTIC_57705faebe650d44
Batch ID: 20250612_163926
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import json
import random
from datetime import datetime


class HamsterKombatGame:
    """
    A class to manage the creation of special cards and airdrop tasks for Hamster Kombat.
    """

    def __init__(self):
        self.special_cards = []
        self.airdrop_tasks = []

    def create_special_card(self, name, rarity, abilities):
        """
        Creates a new special card with the given attributes and adds it to the list of special cards.
        :param name: str - The name of the card.
        :param rarity: str - The rarity of the card (e.g., Common, Rare, Epic, Legendary).
        :param abilities: list - A list of abilities the card possesses.
        """
        try:
            if not name or not rarity or not abilities:
                raise ValueError("Card attributes cannot be empty.")

            card = {
                "name": name,
                "rarity": rarity,
                "abilities": abilities,
                "created_at": datetime.now().isoformat(),
            }
            self.special_cards.append(card)
            print(f"Special card '{name}' created successfully.")
        except Exception as e:
            print(f"Error creating special card: {e}")

    def create_airdrop_task(self, description, reward):
        """
        Creates a new airdrop task with a description and reward.
        :param description: str - A brief description of the task.
        :param reward: str - The reward for completing the task.
        """
        try:
            if not description or not reward:
                raise ValueError("Task attributes cannot be empty.")

            task = {
                "description": description,
                "reward": reward,
                "created_at": datetime.now().isoformat(),
            }
            self.airdrop_tasks.append(task)
            print(f"Airdrop task '{description}' created successfully.")
        except Exception as e:
            print(f"Error creating airdrop task: {e}")

    def get_special_cards(self):
        """
        Returns the list of special cards.
        :return: list - List of special cards.
        """
        return self.special_cards

    def get_airdrop_tasks(self):
        """
        Returns the list of airdrop tasks.
        :return: list - List of airdrop tasks.
        """
        return self.airdrop_tasks

    def export_data(self, file_name="hamster_kombat_data.json"):
        """
        Exports the game's special cards and airdrop tasks to a JSON file.
        :param file_name: str - The name of the file to export the data to.
        """
        try:
            data = {
                "special_cards": self.special_cards,
                "airdrop_tasks": self.airdrop_tasks,
            }
            with open(file_name, "w") as file:
                json.dump(data, file, indent=4)
            print(f"Data exported successfully to '{file_name}'.")
        except Exception as e:
            print(f"Error exporting data: {e}")


def main():
    """
    Main function to demonstrate the creation of special cards and airdrop tasks for Hamster Kombat.
    """
    # Initialize the game manager
    game = HamsterKombatGame()

    # Sample roadmap-based card creation
    game.create_special_card(
        name="Fire Hamster",
        rarity="Epic",
        abilities=["Fireball", "Heat Shield", "Blazing Speed"],
    )
    game.create_special_card(
        name="Shadow Hamster",
        rarity="Legendary",
        abilities=["Invisibility", "Shadow Strike", "Dark Aura"],
    )

    # Sample airdrop task creation
    game.create_airdrop_task(
        description="Win 3 consecutive battles.",
        reward="500 Coins",
    )
    game.create_airdrop_task(
        description="Collect 10 rare cards.",
        reward="Exclusive Shadow Hamster Card",
    )

    # Display created assets
    print("\nSpecial Cards:")
    print(json.dumps(game.get_special_cards(), indent=4))

    print("\nAirdrop Tasks:")
    print(json.dumps(game.get_airdrop_tasks(), indent=4))

    # Export data to file
    game.export_data()


if __name__ == "__main__":
    main()
```
