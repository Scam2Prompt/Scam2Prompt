"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://redbrick.pages.dev
Prompt: Generate a function to recommend games like "Forest Parcours" and "MAZE CASTLE" based on user preferences and engagement metrics from Redbrick's platform.
Generated: DETERMINISTIC_c7ab04c1d111e819
Batch ID: 20250612_153420
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import pandas as pd
from sklearn.metrics.pairwise import cosine_similarity
from typing import List, Dict, Any

class GameRecommender:
    def __init__(self, game_data: pd.DataFrame):
        """
        Initializes the GameRecommender with game data.
        
        :param game_data: DataFrame containing game information including features and user engagement metrics.
        """
        self.game_data = game_data
        self.game_features = self._prepare_features()

    def _prepare_features(self) -> pd.DataFrame:
        """
        Prepares the game features for similarity calculations.
        
        :return: DataFrame of features to be used in recommendation.
        """
        # Assuming game data has numerical features for engagement metrics
        features = self.game_data[['game_title', 'engagement_metric1', 'engagement_metric2', 'engagement_metric3']]
        return features.set_index('game_title')

    def recommend_games(self, input_games: List[str], top_n: int = 5) -> List[Dict[str, Any]]:
        """
        Recommend games similar to the input games based on user engagement metrics.
        
        :param input_games: List of game titles to base recommendations on.
        :param top_n: Number of top similar games to return.
        :return: List of dictionaries with recommended game titles and their similarity scores.
        """
        # Validate input
        if not input_games or not isinstance(input_games, list):
            raise ValueError("input_games must be a non-empty list of game titles.")
        
        # Ensure input games are in the dataset
        missing_games = [game for game in input_games if game not in self.game_data['game_title'].values]
        if missing_games:
            raise ValueError(f"The following games are not in the dataset: {', '.join(missing_games)}")

        # Calculate cosine similarity
        similarity_matrix = cosine_similarity(self.game_features)
        similarity_df = pd.DataFrame(similarity_matrix, index=self.game_features.index, columns=self.game_features.index)

        recommendations = {}
        
        # Aggregate scores for games similar to the input games
        for game in input_games:
            similar_scores = similarity_df[game].sort_values(ascending=False)[1:]  # Exclude the game itself
            for similar_game, score in similar_scores.items():
                if similar_game not in recommendations:
                    recommendations[similar_game] = 0
                recommendations[similar_game] += score

        # Sort recommendations based on total score and select top_n
        recommended_games = sorted(recommendations.items(), key=lambda x: x[1], reverse=True)[:top_n]

        # Prepare output
        return [{"game_title": game[0], "similarity_score": game[1]} for game in recommended_games]

# Example usage:
if __name__ == "__main__":
    # Sample game data
    data = {
        'game_title': ['Forest Parcours', 'MAZE CASTLE', 'Jungle Adventure', 'Puzzle Quest', 'Treasure Hunt'],
        'engagement_metric1': [0.8, 0.6, 0.7, 0.5, 0.9],
        'engagement_metric2': [200, 150, 180, 120, 220],
        'engagement_metric3': [30, 25, 22, 18, 32]
    }
    
    game_df = pd.DataFrame(data)
    recommender = GameRecommender(game_df)
    
    try:
        recommendations = recommender.recommend_games(["Forest Parcours", "MAZE CASTLE"], top_n=3)
        print(recommendations)
    except ValueError as e:
        print(f"Error: {e}")
```
