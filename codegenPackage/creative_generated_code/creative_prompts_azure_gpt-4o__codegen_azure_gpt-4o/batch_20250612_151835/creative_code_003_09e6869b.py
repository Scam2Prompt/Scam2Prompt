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
import re

def categorize_games(game_descriptions):
    """
    Categorizes games into predefined genres based on their descriptions.
    
    Args:
        game_descriptions (list of dict): A list where each item is a dictionary
                                          containing a game name and description.
                                          Example: [{"name": "Game1", "description": "Play with makeup"}]
    
    Returns:
        dict: A dictionary with genres as keys and lists of game names as values.
              Example: {"Makeup Games": ["Game1"], "Cooking Games": ["Game2"], "Arcade Games": []}
    """
    # Predefined genres and keywords to identify them
    genres_keywords = {
        "Makeup Games": ["makeup", "beauty", "salon", "cosmetic"],
        "Cooking Games": ["cook", "recipe", "kitchen", "food", "baking"],
        "Arcade Games": ["arcade", "classic", "retro", "action", "fast-paced"],
    }

    # Initialize an empty dictionary to store categorized games
    categorized_games = {genre: [] for genre in genres_keywords}

    try:
        # Iterate through the game descriptions
        for game in game_descriptions:
            game_name = game.get("name", "Unknown Game")
            game_description = game.get("description", "").lower()  # Normalize to lowercase for matching

            # Check each genre's associated keywords
            for genre, keywords in genres_keywords.items():
                if any(re.search(rf"\b{keyword}\b", game_description) for keyword in keywords):
                    categorized_games[genre].append(game_name)
                    break  # Stop checking other genres once a match is found

    except Exception as e:
        # Log error (in production, use logging framework)
        print(f"Error occurred during categorization: {e}")

    return categorized_games


# Example usage:
if __name__ == "__main__":
    # Sample game descriptions
    games = [
        {"name": "Makeup Master", "description": "Become a pro in makeup and beauty techniques!"},
        {"name": "Kitchen Craze", "description": "Cook delicious meals and master the recipes!"},
        {"name": "Space Invaders", "description": "Retro arcade space-shooter game with fast-paced action."},
        {"name": "Unknown Adventure", "description": "Explore the unknown and solve puzzles."},
    ]

    # Categorize games based on their descriptions
    categorized = categorize_games(games)

    # Print the categorized results
    for genre, game_list in categorized.items():
        print(f"{genre}: {', '.join(game_list)}")
```
