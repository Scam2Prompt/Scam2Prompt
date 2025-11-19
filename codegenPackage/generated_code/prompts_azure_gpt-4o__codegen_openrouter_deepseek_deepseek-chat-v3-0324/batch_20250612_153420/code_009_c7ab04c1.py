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
import pandas as pd
from sklearn.metrics.pairwise import cosine_similarity
from sklearn.feature_extraction.text import TfidfVectorizer
from typing import List, Dict, Optional

class GameRecommender:
    """
    A class to recommend similar games based on user preferences and engagement metrics.
    """
    
    def __init__(self, games_data: pd.DataFrame):
        """
        Initialize the GameRecommender with game data.
        
        Args:
            games_data (pd.DataFrame): DataFrame containing game information with columns:
                - 'game_id': Unique identifier for the game
                - 'title': Game title
                - 'description': Game description
                - 'tags': Comma-separated tags for the game
                - 'engagement_metrics': Dictionary of engagement metrics (e.g., {'play_count': 100, 'avg_rating': 4.5})
        """
        self.games_data = games_data.copy()
        self._preprocess_data()
        self._build_similarity_matrix()
        
    def _preprocess_data(self) -> None:
        """Preprocess the game data for recommendation."""
        # Combine relevant text features
        self.games_data['combined_features'] = (
            self.games_data['title'] + ' ' + 
            self.games_data['description'] + ' ' + 
            self.games_data['tags']
        )
        
        # Normalize engagement metrics
        if 'engagement_metrics' in self.games_data.columns:
            self.games_data['normalized_play_count'] = (
                self.games_data['engagement_metrics'].apply(lambda x: x.get('play_count', 0))
            )
            self.games_data['normalized_rating'] = (
                self.games_data['engagement_metrics'].apply(lambda x: x.get('avg_rating', 0))
            )
            
            # Min-max normalization
            self.games_data['normalized_play_count'] = (
                (self.games_data['normalized_play_count'] - self.games_data['normalized_play_count'].min()) / 
                (self.games_data['normalized_play_count'].max() - self.games_data['normalized_play_count'].min())
            )
            self.games_data['normalized_rating'] = (
                (self.games_data['normalized_rating'] - self.games_data['normalized_rating'].min()) / 
                (self.games_data['normalized_rating'].max() - self.games_data['normalized_rating'].min())
            )
    
    def _build_similarity_matrix(self) -> None:
        """Build a similarity matrix using TF-IDF and engagement metrics."""
        # TF-IDF Vectorization
        tfidf = TfidfVectorizer(stop_words='english')
        tfidf_matrix = tfidf.fit_transform(self.games_data['combined_features'])
        
        # Combine with engagement metrics
        engagement_matrix = self.games_data[['normalized_play_count', 'normalized_rating']].values
        combined_matrix = pd.concat([
            pd.DataFrame(tfidf_matrix.toarray()),
            pd.DataFrame(engagement_matrix)
        ], axis=1)
        
        # Compute cosine similarity
        self.similarity_matrix = cosine_similarity(combined_matrix)
        
    def recommend_similar_games(
        self, 
        game_titles: List[str], 
        top_n: int = 5, 
        min_similarity: float = 0.3
    ) -> Dict[str, List[Dict[str, Optional[float]]]]:
        """
        Recommend similar games based on input game titles.
        
        Args:
            game_titles (List[str]): List of game titles to find similar games for
            top_n (int): Number of recommendations to return per game
            min_similarity (float): Minimum similarity score threshold
            
        Returns:
            Dict[str, List[Dict[str, Optional[float]]]]: Dictionary mapping input game titles to 
                lists of recommended games with their similarity scores
        """
        recommendations = {}
        
        for title in game_titles:
            if title not in self.games_data['title'].values:
                recommendations[title] = []
                continue
                
            idx = self.games_data.index[self.games_data['title'] == title].tolist()[0]
            sim_scores = list(enumerate(self.similarity_matrix[idx]))
            
            # Sort games by similarity score
            sim_scores = sorted(sim_scores, key=lambda x: x[1], reverse=True)
            
            # Get top_n most similar games (excluding self)
            top_indices = [i for i, score in sim_scores[1:top_n+1] if score >= min_similarity]
            top_games = self.games_data.iloc[top_indices][['title', 'description']]
            
            # Prepare recommendations with similarity scores
            game_recs = []
            for i, game in zip(top_indices, top_games.to_dict('records')):
                game_recs.append({
                    'title': game['title'],
                    'description': game['description'],
                    'similarity_score': sim_scores[i+1][1]
                })
            
            recommendations[title] = game_recs
            
        return recommendations

# Example usage
if __name__ == "__main__":
    # Sample data (in production, this would come from a database or API)
    sample_data = pd.DataFrame([
        {
            'game_id': 1,
            'title': 'Forest Parcours',
            'description': 'Navigate through a beautiful forest obstacle course',
            'tags': 'adventure, nature, obstacle',
            'engagement_metrics': {'play_count': 1000, 'avg_rating': 4.7}
        },
        {
            'game_id': 2,
            'title': 'MAZE CASTLE',
            'description': 'Solve puzzles in a mysterious castle maze',
            'tags': 'puzzle, maze, adventure',
            'engagement_metrics': {'play_count': 850, 'avg_rating': 4.5}
        },
        {
            'game_id': 3,
            'title': 'Jungle Run',
            'description': 'Run through the jungle avoiding obstacles',
            'tags': 'adventure, nature, running',
            'engagement_metrics': {'play_count': 950, 'avg_rating': 4.6}
        },
        {
            'game_id': 4,
            'title': 'Castle Puzzle',
            'description': 'Solve challenging puzzles in an ancient castle',
            'tags': 'puzzle, strategy, castle',
            'engagement_metrics': {'play_count': 700, 'avg_rating': 4.3}
        },
        {
            'game_id': 5,
            'title': 'Mountain Climb',
            'description': 'Climb mountains with realistic physics',
            'tags': 'adventure, sports, nature',
            'engagement_metrics': {'play_count': 600, 'avg_rating': 4.2}
        }
    ])
    
    recommender = GameRecommender(sample_data)
    recommendations = recommender.recommend_similar_games(['Forest Parcours', 'MAZE CASTLE'])
    print(recommendations)
```
