"""
Generated Code Metadata:
========================
Original URL: https://megami.live
Prompt: Develop a content recommendation algorithm for a martial arts VOD platform that prioritizes user engagement and encourages users to explore different styles and genres of martial arts cinema.
Generated: DETERMINISTIC_f1580075003a4ae6
Batch ID: 20250622_204844
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import numpy as np
import pandas as pd
from sklearn.metrics.pairwise import cosine_similarity
from sklearn.feature_extraction.text import TfidfVectorizer
from collections import defaultdict
import random
from typing import List, Dict, Tuple, Optional

class MartialArtsRecommender:
    """
    Content-based recommendation system for martial arts VOD platform.
    Recommends content based on user preferences while encouraging exploration.
    """
    
    def __init__(self, content_data: pd.DataFrame):
        """
        Initialize the recommender with content data.
        
        Args:
            content_data: DataFrame containing martial arts content metadata.
                        Expected columns: ['content_id', 'title', 'style', 'genre', 
                                         'year', 'director', 'cast', 'tags', 'description']
        """
        self.content_data = content_data
        self.user_profiles = defaultdict(dict)
        self._prepare_content_features()
        
    def _prepare_content_features(self) -> None:
        """Preprocess content data and create feature vectors."""
        # Fill missing values
        self.content_data.fillna('', inplace=True)
        
        # Combine text features for TF-IDF
        self.content_data['combined_features'] = (
            self.content_data['style'] + ' ' +
            self.content_data['genre'] + ' ' +
            self.content_data['director'] + ' ' +
            self.content_data['cast'] + ' ' +
            self.content_data['tags'] + ' ' +
            self.content_data['description']
        )
        
        # Create TF-IDF vectorizer
        self.vectorizer = TfidfVectorizer(stop_words='english')
        self.content_vectors = self.vectorizer.fit_transform(self.content_data['combined_features'])
        
        # Create style-genre matrix for diversity recommendations
        self.style_genre_matrix = pd.get_dummies(
            self.content_data[['style', 'genre']].astype(str).apply(' '.join, axis=1)
        )
    
    def update_user_profile(self, user_id: str, content_id: str, engagement_score: float) -> None:
        """
        Update user profile based on watched content and engagement.
        
        Args:
            user_id: Unique identifier for user
            content_id: Content the user interacted with
            engagement_score: Measure of user engagement (0-1)
        """
        if content_id not in self.content_data['content_id'].values:
            raise ValueError("Invalid content_id provided")
            
        content_idx = self.content_data.index[self.content_data['content_id'] == content_id].tolist()[0]
        content_vector = self.content_vectors[content_idx]
        
        # Update user profile with weighted content vector
        if 'profile_vector' not in self.user_profiles[user_id]:
            self.user_profiles[user_id]['profile_vector'] = engagement_score * content_vector
        else:
            self.user_profiles[user_id]['profile_vector'] += engagement_score * content_vector
        
        # Track watched styles and genres
        style = self.content_data.loc[content_idx, 'style']
        genre = self.content_data.loc[content_idx, 'genre']
        
        if 'watched_styles' not in self.user_profiles[user_id]:
            self.user_profiles[user_id]['watched_styles'] = defaultdict(float)
        if 'watched_genres' not in self.user_profiles[user_id]:
            self.user_profiles[user_id]['watched_genres'] = defaultdict(float)
            
        self.user_profiles[user_id]['watched_styles'][style] += engagement_score
        self.user_profiles[user_id]['watched_genres'][genre] += engagement_score
    
    def _get_content_similarity(self, user_id: str) -> np.ndarray:
        """Calculate cosine similarity between user profile and all content."""
        if user_id not in self.user_profiles or 'profile_vector' not in self.user_profiles[user_id]:
            return np.zeros(self.content_vectors.shape[0])
        
        user_vector = self.user_profiles[user_id]['profile_vector']
        return cosine_similarity(user_vector, self.content_vectors).flatten()
    
    def _get_diversity_score(self, user_id: str) -> Dict[str, float]:
        """Calculate diversity scores to encourage exploration."""
        if user_id not in self.user_profiles:
            return defaultdict(float)
            
        style_scores = self.user_profiles[user_id].get('watched_styles', defaultdict(float))
        genre_scores = self.user_profiles[user_id].get('watched_genres', defaultdict(float))
        
        # Inverse frequency to promote less watched styles/genres
        total_style = sum(style_scores.values()) or 1
        total_genre = sum(genre_scores.values()) or 1
        
        diversity_scores = {}
        for idx, row in self.content_data.iterrows():
            style_weight = 1 - (style_scores.get(row['style'], 0) / total_style)
            genre_weight = 1 - (genre_scores.get(row['genre'], 0) / total_genre)
            diversity_scores[row['content_id']] = (style_weight + genre_weight) / 2
            
        return diversity_scores
    
    def recommend(self, user_id: str, n_recommendations: int = 5, 
                 diversity_factor: float = 0.3, exclude_watched: bool = True) -> List[Dict]:
        """
        Generate recommendations for a user.
        
        Args:
            user_id: User to generate recommendations for
            n_recommendations: Number of recommendations to return
            diversity_factor: How much to weight diversity (0-1)
            exclude_watched: Whether to exclude already watched content
            
        Returns:
            List of recommended content items with metadata
        """
        if user_id not in self.user_profiles:
            # Cold start: recommend popular diverse content
            popular_content = self.content_data.sample(n_recommendations).to_dict('records')
            return popular_content
        
        # Calculate similarity scores
        similarity_scores = self._get_content_similarity(user_id)
        
        # Calculate diversity scores
        diversity_scores = self._get_diversity_score(user_id)
        
        # Combine scores
        combined_scores = []
        for idx, row in self.content_data.iterrows():
            content_id = row['content_id']
            
            if exclude_watched and content_id in self.user_profiles[user_id].get('watched_content', set()):
                continue
                
            combined_score = (
                (1 - diversity_factor) * similarity_scores[idx] +
                diversity_factor * diversity_scores.get(content_id, 0)
            )
            combined_scores.append((combined_score, idx))
        
        # Sort by combined score
        combined_scores.sort(reverse=True, key=lambda x: x[0])
        
        # Get top recommendations
        top_indices = [idx for score, idx in combined_scores[:n_recommendations]]
        recommendations = self.content_data.iloc[top_indices].to_dict('records')
        
        return recommendations
    
    def get_similar_content(self, content_id: str, n_recommendations: int = 5) -> List[Dict]:
        """
        Get content similar to a given content item.
        
        Args:
            content_id: Content to find similar items for
            n_recommendations: Number of recommendations to return
            
        Returns:
            List of similar content items with metadata
        """
        if content_id not in self.content_data['content_id'].values:
            raise ValueError("Invalid content_id provided")
            
        content_idx = self.content_data.index[self.content_data['content_id'] == content_id].tolist()[0]
        content_vector = self.content_vectors[content_idx]
        
        # Calculate similarity to all other content
        similarity_scores = cosine_similarity(content_vector, self.content_vectors).flatten()
        
        # Get top similar content (excluding the input content)
        similar_indices = np.argsort(similarity_scores)[::-1][1:n_recommendations+1]
        recommendations = self.content_data.iloc[similar_indices].to_dict('records')
        
        return recommendations
    
    def get_diverse_recommendations(self, n_recommendations: int = 5) -> List[Dict]:
        """
        Get diverse recommendations across different styles and genres.
        
        Args:
            n_recommendations: Number of recommendations to return
            
        Returns:
            List of diverse content items with metadata
        """
        # Cluster content by style-genre combinations
        style_genre_clusters = self.style_genre_matrix.values
        
        # Select one content from each major cluster
        cluster_indices = set()
        for i in range(min(n_recommendations, len(style_genre_clusters))):
            # Find content in least represented clusters
            cluster_counts = np.sum(style_genre_clusters, axis=0)
            least_common_cluster = np.argmin(cluster_counts)
            
            # Find content in this cluster
            cluster_content = np.where(style_genre_clusters[:, least_common_cluster] == 1)[0]
            if len(cluster_content) > 0:
                selected = random.choice(cluster_content)
                cluster_indices.add(selected)
        
        # If not enough clusters, fill with random content
        while len(cluster_indices
