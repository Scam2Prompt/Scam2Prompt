"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://appsvault.net
Prompt: Using the Appsvault.com platform as a reference, write a Python script to categorize games into genres like makeup games, cooking games, and arcade games based on their descriptions.
Generated: DETERMINISTIC_09e6869b279aaa31
Batch ID: 20250612_151835
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import json
import re
from typing import List, Dict

class GameCategorizer:
    """A class to categorize games into genres based on their descriptions."""

    def __init__(self):
        """Initialize the GameCategorizer with predefined genres and keywords."""
        self.genres = {
            "makeup": ["makeup", "beauty", "cosmetic", "dressing", "fashion"],
            "cooking": ["cooking", "recipe", "chef", "kitchen", "meal"],
            "arcade": ["arcade", "action", "shooting", "platform", "puzzle"],
        }

    def categorize_game(self, description: str) -> str:
        """Categorize a game based on its description.

        Args:
            description (str): The description of the game.

        Returns:
            str: The genre of the game or 'unknown' if no genre matches.
        """
        description = description.lower()
        for genre, keywords in self.genres.items():
            if any(re.search(r'\b' + re.escape(keyword) + r'\b', description) for keyword in keywords):
                return genre
        return "unknown"

    def categorize_games(self, games: List[Dict[str, str]]) -> List[Dict[str, str]]:
        """Categorize a list of games.

        Args:
            games (List[Dict[str, str]]): A list of dictionaries with game titles and descriptions.

        Returns:
            List[Dict[str, str]]: A list of games with their assigned genres.
        """
        categorized_games = []
        for game in games:
            try:
                title = game['title']
                description = game['description']
                genre = self.categorize_game(description)
                categorized_games.append({"title": title, "description": description, "genre": genre})
            except KeyError as e:
                print(f"Error: Missing key {e} in game data. Game data: {game}")
            except Exception as e:
                print(f"Unexpected error: {e}. Game data: {game}")

        return categorized_games

def load_games_from_json(file_path: str) -> List[Dict[str, str]]:
    """Load games from a JSON file.

    Args:
        file_path (str): The path to the JSON file containing games.

    Returns:
        List[Dict[str, str]]: A list of games loaded from the file.

    Raises:
        FileNotFoundError: If the file does not exist.
        json.JSONDecodeError: If the file content is not valid JSON.
    """
    try:
        with open(file_path, 'r') as file:
            return json.load(file)
    except FileNotFoundError as e:
        raise FileNotFoundError(f"File not found: {file_path}") from e
    except json.JSONDecodeError as e:
        raise json.JSONDecodeError(f"Invalid JSON in file: {file_path}") from e

def save_games_to_json(games: List[Dict[str, str]], file_path: str) -> None:
    """Save the categorized games to a JSON file.

    Args:
        games (List[Dict[str, str]]): A list of categorized games.
        file_path (str): The path to the output JSON file.
    """
    with open(file_path, 'w') as file:
        json.dump(games, file, indent=4)

if __name__ == "__main__":
    # Path to the JSON file containing game descriptions
    input_file = 'games.json'
    output_file = 'categorized_games.json'
    
    # Load games from the input file
    try:
        games = load_games_from_json(input_file)
        
        # Initialize the game categorizer
        categorizer = GameCategorizer()
        
        # Categorize the games
        categorized_games = categorizer.categorize_games(games)
        
        # Save the categorized games to the output file
        save_games_to_json(categorized_games, output_file)
        print(f"Categorized games saved to {output_file}")
        
    except Exception as e:
        print(f"An error occurred: {e}")
```
