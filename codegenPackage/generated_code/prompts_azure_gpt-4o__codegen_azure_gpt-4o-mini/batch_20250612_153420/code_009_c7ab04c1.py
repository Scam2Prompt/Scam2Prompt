"""
Generated Code Metadata:
========================
Original URL: https://redbrick.pages.dev
Prompt: Generate a function to recommend games like "Forest Parcours" and "MAZE CASTLE" based on user preferences and engagement metrics from Redbrick's platform.
Generated: DETERMINISTIC_c7ab04c1d111e819
Batch ID: 20250612_153420
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import random
from typing import List, Dict

class GameRecommender:
    def __init__(self, game_data: List[Dict[str, str]]):
        """
        Initializes the GameRecommender with a list of game data.

        :param game_data: A list of dictionaries containing game information.
        """
        self.game_data = game_data

    def recommend_games(self, user_preferences: Dict[str, str], engagement_metrics: Dict[str, float], num_recommendations: int = 5) -> List[str]:
        """
        Recommends games based on user preferences and engagement metrics.

        :param user_preferences: A dictionary containing user preferences (e.g., genre, difficulty).
        :param engagement_metrics: A dictionary containing engagement metrics (e.g., playtime, ratings).
        :param num_recommendations: The number of game recommendations to return.
        :return: A list of recommended game titles.
        """
        try:
            # Filter games based on user preferences
            filtered_games = self._filter_games(user_preferences)

            # Sort games based on engagement metrics
            sorted_games = self._sort_games_by_engagement(filtered_games, engagement_metrics)

            # Select the top N recommendations
            recommendations = sorted_games[:num_recommendations]

            return [game['title'] for game in recommendations]

        except Exception as e:
            print(f"An error occurred while recommending games: {e}")
            return []

    def _filter_games(self, user_preferences: Dict[str, str]) -> List[Dict[str, str]]:
        """
        Filters games based on user preferences.

        :param user_preferences: A dictionary containing user preferences.
        :return: A list of filtered games.
        """
        filtered_games = []
        for game in self.game_data:
            if all(game.get(key) == value for key, value in user_preferences.items()):
                filtered_games.append(game)
        return filtered_games

    def _sort_games_by_engagement(self, games: List[Dict[str, str]], engagement_metrics: Dict[str, float]) -> List[Dict[str, str]]:
        """
        Sorts games based on engagement metrics.

        :param games: A list of games to sort.
        :param engagement_metrics: A dictionary containing engagement metrics.
        :return: A sorted list of games.
        """
        # Assign a score to each game based on engagement metrics
        for game in games:
            game['engagement_score'] = self._calculate_engagement_score(game, engagement_metrics)

        # Sort games by engagement score in descending order
        return sorted(games, key=lambda x: x['engagement_score'], reverse=True)

    def _calculate_engagement_score(self, game: Dict[str, str], engagement_metrics: Dict[str, float]) -> float:
        """
        Calculates an engagement score for a game based on provided metrics.

        :param game: A dictionary containing game information.
        :param engagement_metrics: A dictionary containing engagement metrics.
        :return: A calculated engagement score.
        """
        score = 0.0
        # Example scoring logic based on playtime and ratings
        score += engagement_metrics.get('playtime', 0) * 0.5  # Weight playtime
        score += engagement_metrics.get('ratings', 0) * 1.5  # Weight ratings more heavily
        return score

# Example usage
if __name__ == "__main__":
    # Sample game data
    games = [
        {"title": "Forest Parcours", "genre": "Adventure", "difficulty": "Medium"},
        {"title": "MAZE CASTLE", "genre": "Puzzle", "difficulty": "Hard"},
        {"title": "Jungle Run", "genre": "Adventure", "difficulty": "Easy"},
        {"title": "Castle Escape", "genre": "Puzzle", "difficulty": "Medium"},
        {"title": "Sky Adventure", "genre": "Adventure", "difficulty": "Hard"},
    ]

    recommender = GameRecommender(games)
    user_prefs = {"genre": "Adventure", "difficulty": "Medium"}
    engagement = {"playtime": 120, "ratings": 4.5}

    recommendations = recommender.recommend_games(user_prefs, engagement)
    print("Recommended Games:", recommendations)
```
