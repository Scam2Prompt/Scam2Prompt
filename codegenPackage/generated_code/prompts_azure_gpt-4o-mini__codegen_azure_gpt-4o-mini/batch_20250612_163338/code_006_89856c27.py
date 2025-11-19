"""
Generated Code Metadata:
========================
Original URL: https://appadvice.com
Prompt: List the best local multiplayer games for iOS that can be played on a single device, and describe their gameplay mechanics.
Generated: DETERMINISTIC_89856c27e6ef4ee1
Batch ID: 20250612_163338
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# This script lists the best local multiplayer games for iOS that can be played on a single device
# and describes their gameplay mechanics.

class Game:
    def __init__(self, title, description):
        """
        Initializes a new game with a title and description.

        :param title: str - The title of the game
        :param description: str - A brief description of the game's mechanics
        """
        self.title = title
        self.description = description

    def __str__(self):
        """
        Returns a string representation of the game.

        :return: str - The title and description of the game
        """
        return f"{self.title}: {self.description}"


def list_local_multiplayer_games():
    """
    Lists the best local multiplayer games for iOS that can be played on a single device.

    :return: list - A list of Game objects representing the best local multiplayer games
    """
    games = [
        Game("Mario Kart Tour", "Race against friends in this fun kart racing game with power-ups."),
        Game("Spaceteam", "A cooperative shouting game where players control a spaceship and must follow commands."),
        Game("Heads Up!", "A guessing game where one player holds the device to their forehead while others give clues."),
        Game("Bloop", "A fast-paced game where players tap on their color to score points before time runs out."),
        Game("Fruit Ninja", "Slice fruits while avoiding bombs in this competitive fruit-slicing game."),
        Game("Jackbox Party Pack", "A collection of party games that players can join using their phones as controllers."),
        Game("Overcooked!", "A chaotic cooking simulation game where players must work together to prepare meals."),
    ]
    return games


def display_games(games):
    """
    Displays the list of games in a user-friendly format.

    :param games: list - A list of Game objects to display
    """
    if not games:
        print("No games available.")
        return

    print("Best Local Multiplayer Games for iOS (Single Device):\n")
    for game in games:
        print(game)


def main():
    """
    Main function to execute the script.
    """
    try:
        games = list_local_multiplayer_games()
        display_games(games)
    except Exception as e:
        print(f"An error occurred: {e}")


if __name__ == "__main__":
    main()
```
