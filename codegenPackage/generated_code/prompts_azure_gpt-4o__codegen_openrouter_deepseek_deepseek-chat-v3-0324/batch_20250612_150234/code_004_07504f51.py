"""
Generated Code Metadata:
========================
Original URL: https://as-media.rs
Prompt: Suggest a library or framework for building a music recommendation system similar to Radio S's personalized playlist feature, including genres like "Latino," "Folk Lounge," and "Pop Ballads."
Generated: DETERMINISTIC_07504f51bd4bcded
Batch ID: 20250612_150234
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# music_recommendation_system.py

import numpy as np
import pandas as pd
from sklearn.neighbors import NearestNeighbors
from sklearn.preprocessing import StandardScaler
from sklearn.pipeline import Pipeline
from sklearn.decomposition import PCA
from scipy.sparse import csr_matrix
import joblib
import os
from typing import List, Dict, Optional

class MusicRecommendationSystem:
    """
    A music recommendation system using collaborative filtering and content-based filtering.
    Handles genres like 'Latino', 'Folk Lounge', 'Pop Ballads' and provides personalized recommendations.
    """
    
    def __init__(self, model_path: str = None):
        """
        Initialize the recommendation system.
        
        Args:
            model_path: Path to load a pre-trained model. If None, initializes a new model.
        """
        self.model = None
        self.scaler = StandardScaler()
        self.pca = PCA(n_components=0.95)
        self.user_item_matrix = None
        self.song_features = None
        self.song_ids = None
        
        if model_path and os.path.exists(model_path):
            self.load_model(model_path)
    
    def preprocess_data(self, user_data: pd.DataFrame, song_data: pd.DataFrame) -> None:
        """
        Preprocess user listening history and song features.
        
        Args:
            user_data: DataFrame with columns ['user_id', 'song_id', 'play_count']
            song_data: DataFrame with columns ['song_id', 'features', 'genres']
        """
        # Create user-item matrix
        self.user_item_matrix = user_data.pivot(
            index='user_id',
            columns='song_id',
            values='play_count'
        ).fillna(0)
        
        # Convert to sparse matrix
        self.user_item_matrix = csr_matrix(self.user_item_matrix.values)
        
        # Process song features
        self.song_ids = song_data['song_id'].values
        self.song_features = np.array(song_data['features'].tolist())
        
        # Normalize features
        self.song_features = self.scaler.fit_transform(self.song_features)
        self.song_features = self.pca.fit_transform(self.song_features)
    
    def train_model(self, n_neighbors: int = 20, metric: str = 'cosine') -> None:
        """
        Train the recommendation model using KNN.
        
        Args:
            n_neighbors: Number of neighbors to consider
            metric: Distance metric to use
        """
        self.model = NearestNeighbors(
            n_neighbors=n_neighbors,
            metric=metric,
            algorithm='auto'
        )
        self.model.fit(self.song_features)
    
    def recommend_songs(
        self,
        user_history: List[str],
        n_recommendations: int = 10,
        genre_filter: Optional[List[str]] = None
    ) -> List[Dict]:
        """
        Generate song recommendations for a user.
        
        Args:
            user_history: List of song IDs the user has listened to
            n_recommendations: Number of recommendations to return
            genre_filter: Optional list of genres to filter by
            
        Returns:
            List of recommended songs with their details
        """
        if not self.model:
            raise ValueError("Model not trained. Call train_model() first.")
        
        # Get indices of user's songs in our dataset
        user_song_indices = [np.where(self.song_ids == sid)[0][0] for sid in user_history]
        
        # Get average features of user's songs
        user_profile = np.mean(self.song_features[user_song_indices], axis=0)
        
        # Find nearest neighbors
        distances, indices = self.model.kneighbors([user_profile], n_neighbors=n_recommendations)
        
        # Get recommended song IDs
        recommended_song_ids = [self.song_ids[i] for i in indices[0]]
        
        # Filter by genre if specified
        if genre_filter:
            # This would require additional genre data in the song_data DataFrame
            pass
        
        # In a real implementation, you would return song details here
        return [{"song_id": sid, "distance": float(dist)} 
                for sid, dist in zip(recommended_song_ids, distances[0])]
    
    def save_model(self, path: str) -> None:
        """
        Save the trained model to disk.
        
        Args:
            path: Path to save the model
        """
        joblib.dump({
            'model': self.model,
            'scaler': self.scaler,
            'pca': self.pca,
            'user_item_matrix': self.user_item_matrix,
            'song_features': self.song_features,
            'song_ids': self.song_ids
        }, path)
    
    def load_model(self, path: str) -> None:
        """
        Load a trained model from disk.
        
        Args:
            path: Path to load the model from
        """
        data = joblib.load(path)
        self.model = data['model']
        self.scaler = data['scaler']
        self.pca = data['pca']
        self.user_item_matrix = data['user_item_matrix']
        self.song_features = data['song_features']
        self.song_ids = data['song_ids']

# Example usage
if __name__ == "__main__":
    # Mock data - in a real system this would come from a database
    user_data = pd.DataFrame({
        'user_id': ['u1', 'u1', 'u2', 'u2', 'u2'],
        'song_id': ['s1', 's2', 's1', 's3', 's4'],
        'play_count': [5, 3, 2, 1, 4]
    })
    
    song_data = pd.DataFrame({
        'song_id': ['s1', 's2', 's3', 's4', 's5'],
        'features': [
            [0.8, 0.2, 0.5],  # Latino
            [0.1, 0.9, 0.3],  # Folk Lounge
            [0.7, 0.3, 0.6],  # Latino
            [0.2, 0.8, 0.4],  # Pop Ballads
            [0.5, 0.5, 0.5]   # Mixed
        ],
        'genres': [
            ['Latino'],
            ['Folk Lounge'],
            ['Latino'],
            ['Pop Ballads'],
            ['Latino', 'Pop Ballads']
        ]
    })
    
    # Initialize and train the system
    recommender = MusicRecommendationSystem()
    recommender.preprocess_data(user_data, song_data)
    recommender.train_model()
    
    # Get recommendations for a user
    recommendations = recommender.recommend_songs(
        user_history=['s1', 's2'],
        n_recommendations=3,
        genre_filter=['Latino', 'Pop Ballads']
    )
    
    print("Recommended songs:", recommendations)
    
    # Save the model for later use
    recommender.save_model('music_recommender_model.joblib')
```
