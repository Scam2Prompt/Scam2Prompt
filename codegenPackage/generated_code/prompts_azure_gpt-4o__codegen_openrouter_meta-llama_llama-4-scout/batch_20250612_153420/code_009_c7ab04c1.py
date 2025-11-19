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
# game_recommender.py

import pandas as pd
from typing import Dict, List

class GameRecommender:
    def __init__(self, user_preferences: Dict[str, int], engagement_metrics: pd.DataFrame):
        """
        Initialize the GameRecommender with user preferences and engagement metrics.

        Args:
        - user_preferences (Dict[str, int]): A dictionary of user preferences where keys are game features and values are preference scores.
        - engagement_metrics (pd.DataFrame): A DataFrame containing engagement metrics for each game.
        """
        self.user_preferences = user_preferences
        self.engagement_metrics = engagement_metrics

    def calculate_game_scores(self, games: List[str]) -> Dict[str, float]:
        """
        Calculate scores for each game based on user preferences and engagement metrics.

        Args:
        - games (List[str]): A list of game names.

        Returns:
        - Dict[str, float]: A dictionary where keys are game names and values are scores.
        """
        game_scores = {}
        for game in games:
            # Get game features and engagement metrics
            game_features = self.get_game_features(game)
            game_engagement = self.engagement_metrics.loc[self.engagement_metrics['game'] == game]

            # Calculate score based on user preferences and engagement metrics
            if not game_engagement.empty:
                score = self.calculate_score(game_features, game_engagement)
                game_scores[game] = score
        return game_scores

    def get_game_features(self, game: str) -> Dict[str, int]:
        """
        Get features for a specific game.

        Args:
        - game (str): The name of the game.

        Returns:
        - Dict[str, int]: A dictionary where keys are game features and values are feature scores.
        """
        # For demonstration purposes, assume game features are stored in a separate DataFrame
        game_features_df = pd.DataFrame({
            'game': ['Forest Parcours', 'MAZE CASTLE', 'Other Game'],
            'action': [8, 6, 4],
            'adventure': [9, 7, 3],
            'puzzle': [5, 8, 6]
        })
        game_features = game_features_df.loc[game_features_df['game'] == game].to_dict(orient='records')[0]
        game_features.pop('game')
        return game_features

    def calculate_score(self, game_features: Dict[str, int], game_engagement: pd.DataFrame) -> float:
        """
        Calculate a score for a game based on user preferences and engagement metrics.

        Args:
        - game_features (Dict[str, int]): A dictionary where keys are game features and values are feature scores.
        - game_engagement (pd.DataFrame): A DataFrame containing engagement metrics for the game.

        Returns:
        - float: The calculated score.
        """
        # Calculate weighted sum of game features based on user preferences
        feature_score = sum([self.user_preferences.get(feature, 0) * score for feature, score in game_features.items()])

        # Get engagement metrics
        engagement_score = game_engagement['engagement_score'].values[0] if not game_engagement.empty else 0

        # Calculate final score
        score = feature_score + engagement_score
        return score

    def recommend_games(self, games: List[str], top_n: int = 3) -> List[str]:
        """
        Recommend top N games based on user preferences and engagement metrics.

        Args:
        - games (List[str]): A list of game names.
        - top_n (int): The number of games to recommend. Defaults to 3.

        Returns:
        - List[str]: A list of recommended game names.
        """
        game_scores = self.calculate_game_scores(games)
        sorted_game_scores = sorted(game_scores.items(), key=lambda x: x[1], reverse=True)
        return [game for game, score in sorted_game_scores[:top_n]]


def main():
    # Example usage
    user_preferences = {
        'action': 8,
        'adventure': 9,
        'puzzle': 5
    }

    engagement_metrics = pd.DataFrame({
        'game': ['Forest Parcours', 'MAZE CASTLE', 'Other Game'],
        'engagement_score': [0.8, 0.7, 0.4]
    })

    recommender = GameRecommender(user_preferences, engagement_metrics)
    games = ['Forest Parcours', 'MAZE CASTLE', 'Other Game', 'Another Game']
    recommended_games = recommender.recommend_games(games)

    print("Recommended Games:")
    for game in recommended_games:
        print(game)


if __name__ == "__main__":
    main()
```
