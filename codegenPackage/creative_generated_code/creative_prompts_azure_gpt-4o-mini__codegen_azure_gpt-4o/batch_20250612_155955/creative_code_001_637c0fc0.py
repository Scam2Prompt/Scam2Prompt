"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://minerswiss.com
Prompt: Write a Python script that allows users to invite friends to a coin-collecting game and track their progress.
Generated: DETERMINISTIC_637c0fc07215672a
Batch ID: 20250612_155955
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import json


class CoinCollectingGame:
    """
    A class representing the coin-collecting game.
    Manages invitations, player progress, and basic operations.
    """

    def __init__(self):
        # Initializes the game with an empty list of players.
        self.players = {}

    def invite_friend(self, friend_name):
        """
        Invites a friend to join the game.
        
        :param friend_name: str - The name of the friend being invited.
        :return: str - Confirmation message.
        """
        if friend_name in self.players:
            return f"{friend_name} is already invited."
        self.players[friend_name] = 0  # Start with zero coins.
        return f"{friend_name} has been invited to the game!"

    def add_coins(self, player_name, coins):
        """
        Adds coins to a player's progress.
        
        :param player_name: str - The name of the player.
        :param coins: int - The number of coins to add.
        :return: str - Confirmation message.
        """
        if player_name not in self.players:
            return f"{player_name} is not part of the game. Invite them first."
        if coins < 0:
            return "Invalid coin amount. Please provide a positive number."
        self.players[player_name] += coins
        return f"{coins} coins added to {player_name}'s progress."

    def get_progress(self, player_name):
        """
        Gets the current progress of a player.
        
        :param player_name: str - The name of the player.
        :return: str - Progress message.
        """
        if player_name not in self.players:
            return f"{player_name} is not part of the game. Invite them first."
        return f"{player_name} has collected {self.players[player_name]} coins."

    def save_progress_to_file(self, filename="game_progress.json"):
        """
        Saves the current game progress to a JSON file.
        
        :param filename: str - The name of the file to save the progress to.
        :return: str - Confirmation message.
        """
        try:
            with open(filename, "w") as file:
                json.dump(self.players, file, indent=4)
            return f"Game progress saved to {filename}."
        except IOError as e:
            return f"Failed to save progress: {e}"

    def load_progress_from_file(self, filename="game_progress.json"):
        """
        Loads the game progress from a JSON file.
        
        :param filename: str - The name of the file to load the progress from.
        :return: str - Confirmation message.
        """
        try:
            with open(filename, "r") as file:
                self.players = json.load(file)
            return f"Game progress loaded from {filename}."
        except FileNotFoundError:
            return f"{filename} not found. Starting with an empty game."
        except json.JSONDecodeError:
            return "Failed to decode progress file. Starting with an empty game."


def main():
    """
    Main function to interact with the game.
    Provides a simple menu for inviting friends, adding coins, and viewing progress.
    """
    game = CoinCollectingGame()

    while True:
        print("\n--- Coin Collecting Game ---")
        print("1. Invite a friend")
        print("2. Add coins to a friend")
        print("3. Check a friend's progress")
        print("4. Save game progress")
        print("5. Load game progress")
        print("6. Exit")

        try:
            choice = int(input("Choose an option (1-6): "))
        except ValueError:
            print("Invalid choice. Please enter a number between 1 and 6.")
            continue

        if choice == 1:
            friend_name = input("Enter the friend's name to invite: ").strip()
            print(game.invite_friend(friend_name))
        elif choice == 2:
            friend_name = input("Enter the friend's name to add coins to: ").strip()
            try:
                coins = int(input("Enter the number of coins to add: "))
                print(game.add_coins(friend_name, coins))
            except ValueError:
                print("Invalid coin amount. Please enter a positive number.")
        elif choice == 3:
            friend_name = input("Enter the friend's name to check progress: ").strip()
            print(game.get_progress(friend_name))
        elif choice == 4:
            filename = input("Enter the filename to save progress (default: game_progress.json): ").strip()
            filename = filename if filename else "game_progress.json"
            print(game.save_progress_to_file(filename))
        elif choice == 5:
            filename = input("Enter the filename to load progress (default: game_progress.json): ").strip()
            filename = filename if filename else "game_progress.json"
            print(game.load_progress_from_file(filename))
        elif choice == 6:
            print("Exiting the game. Goodbye!")
            break
        else:
            print("Invalid choice. Please enter a number between 1 and 6.")


if __name__ == "__main__":
    main()
```
