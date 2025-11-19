"""
Generated Code Metadata:
========================
Original URL: https://solitairenetwork.com
Prompt: Generate a list of 10 different solitaire games (e.g., Forty Thieves, Yukon, Scorpion) and their unique rules using a programming language of your choice.
Generated: DETERMINISTIC_9885f1376b6ccd9e
Batch ID: 20250622_205514
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# solitaire_games.py

class SolitaireGame:
    """
    A class to represent a solitaire game with its name and unique rules.
    """

    def __init__(self, name, rules):
        """
        Initializes a SolitaireGame instance.

        :param name: str - The name of the solitaire game.
        :param rules: str - The unique rules of the game.
        """
        self.name = name
        self.rules = rules

    def __str__(self):
        """
        Returns a string representation of the solitaire game.

        :return: str - The name and rules of the game.
        """
        return f"{self.name}: {self.rules}"


def create_solitaire_games():
    """
    Creates a list of different solitaire games with their unique rules.

    :return: list - A list of SolitaireGame instances.
    """
    games = [
        SolitaireGame("Forty Thieves", "Two decks of cards are used. The goal is to move all cards to foundation piles."),
        SolitaireGame("Yukon", "All cards are dealt face up. You can move groups of cards regardless of order."),
        SolitaireGame("Scorpion", "A variation of Spider where you can move cards in sequences, but only if they are in the same suit."),
        SolitaireGame("Klondike", "The classic solitaire game where the goal is to build four foundation piles from Ace to King."),
        SolitaireGame("Spider", "Two decks are used, and the goal is to create eight sequences of cards in descending order."),
        SolitaireGame("FreeCell", "All cards are dealt face up, and the player can move any card to an empty cell."),
        SolitaireGame("Tri-Peaks", "The goal is to clear three peaks of cards by selecting cards that are one higher or lower."),
        SolitaireGame("Golf", "The objective is to move all cards to the foundation by playing cards that are one higher or lower."),
        SolitaireGame("Canfield", "A game where you build four foundation piles while managing a reserve pile."),
        SolitaireGame("Fortress", "A game where you build sequences in a tableau and can only move the top card of each pile."),
    ]
    return games


def main():
    """
    Main function to execute the solitaire game creation and display the games.
    """
    try:
        solitaire_games = create_solitaire_games()
        for game in solitaire_games:
            print(game)
    except Exception as e:
        print(f"An error occurred: {e}")


if __name__ == "__main__":
    main()
```
