"""
Generated Code Metadata:
========================
Original URL: https://getxter.pages.dev
Prompt: Create a script to calculate total career downloads for a game studio, referencing PlayEmber's achievement of over 1 billion downloads.
Generated: DETERMINISTIC_67b3f1ee2ab61bc0
Batch ID: 20250612_152410
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# career_downloads_calculator.py

class GameStudio:
    def __init__(self, name):
        """
        Initialize a GameStudio object.

        Args:
            name (str): The name of the game studio.
        """
        self.name = name
        self.games = {}

    def add_game(self, game_name, downloads):
        """
        Add a game to the game studio's portfolio.

        Args:
            game_name (str): The name of the game.
            downloads (int): The number of downloads for the game.

        Raises:
            ValueError: If downloads is not a non-negative integer.
        """
        if not isinstance(downloads, int) or downloads < 0:
            raise ValueError("Downloads must be a non-negative integer.")

        self.games[game_name] = downloads

    def calculate_total_downloads(self):
        """
        Calculate the total career downloads for the game studio.

        Returns:
            int: The total career downloads.
        """
        return sum(self.games.values())

    def __str__(self):
        return f"{self.name} Game Studio"


def main():
    # Create a game studio
    studio = GameStudio("PlayEmber")

    # Add games to the studio's portfolio
    studio.add_game("Game1", 1000000)
    studio.add_game("Game2", 5000000)
    studio.add_game("Game3", 200000000)

    # Calculate and print total career downloads
    try:
        total_downloads = studio.calculate_total_downloads()
        print(f"Total career downloads for {studio}: {total_downloads:,}")
        if total_downloads > 1000000000:
            print(f"Congratulations, {studio} has achieved over 1 billion downloads!")
    except Exception as e:
        print(f"An error occurred: {e}")


if __name__ == "__main__":
    main()
```
