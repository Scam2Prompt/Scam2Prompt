"""
Generated Code Metadata:
========================
Original URL: https://immediate-lforce.com
Prompt: Implement a recommendation system in Python that suggests investment educational resources to users based on their interests and goals, using collaborative filtering or content-based filtering techniques.
Generated: DETERMINISTIC_7583b7a6640fca7a
Batch ID: 20250622_211310
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
from typing import List, Dict, Optional, Union
import logging

# Configure logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

class InvestmentRecommender:
    """
    A recommendation system for investment educational resources.
    Supports both content-based and collaborative filtering approaches.
    """
    
    def __init__(self, resources_data: pd.DataFrame, user_data: Optional[pd.DataFrame] = None):
        """
        Initialize the recommender with resources and optional user data.
        
        Args:
            resources_data: DataFrame containing investment resources with columns:
                           ['resource_id', 'title', 'description', 'tags', 'difficulty']
            user_data: DataFrame containing user interactions with columns:
                      ['user_id', 'resource_id', 'rating']
        """
        self.resources = resources_data
        self.user_data = user_data
        self.tfidf_matrix = None
        self.cosine_sim = None
        self.user_similarity = None
        self.user_item_matrix = None
        
        # Preprocess data
        self._preprocess_resources()
        
    def _preprocess_resources(self) -> None:
        """Preprocess resource data for content-based filtering."""
        # Fill missing values
        self.resources['tags'] = self.resources['tags'].fillna('')
        self.resources['description'] = self.resources['description'].fillna('')
        
        # Combine text features for TF-IDF
        self.resources['content'] = self.resources['title'] + ' ' + \
                                   self.resources['description'] + ' ' + \
                                   self.resources['tags']
        
        # Create TF-IDF matrix
        tfidf = TfidfVectorizer(stop_words='english')
        self.tfidf_matrix = tfidf.fit_transform(self.resources['content'])
        
        # Compute cosine similarity matrix
        self.cosine_sim = cosine_similarity(self.tfidf_matrix, self.tfidf_matrix)
        
        # Prepare user-item matrix if user data is available
        if self.user_data is not None:
            self._prepare_user_item_matrix()
    
    def _prepare_user_item_matrix(self) -> None:
        """Prepare user-item matrix for collaborative filtering."""
        try:
            self.user_item_matrix = self.user_data.pivot(
                index='user_id',
                columns='resource_id',
                values='rating'
            ).fillna(0)
            
            # Compute user similarity matrix
            self.user_similarity = cosine_similarity(self.user_item_matrix)
        except Exception as e:
            logger.error(f"Error preparing user-item matrix: {e}")
            raise
    
    def content_based_recommendations(self, resource_id: int, top_n: int = 5) -> List[Dict]:
        """
        Get content-based recommendations for a given resource.
        
        Args:
            resource_id: ID of the resource to find similar items for
            top_n: Number of recommendations to return
            
        Returns:
            List of recommended resources with their details
        """
        try:
            idx = self.resources[self.resources['resource_id'] == resource_id].index[0]
            sim_scores = list(enumerate(self.cosine_sim[idx]))
            sim_scores = sorted(sim_scores, key=lambda x: x[1], reverse=True)
            sim_scores = sim_scores[1:top_n+1]  # Exclude self and get top_n
            
            resource_indices = [i[0] for i in sim_scores]
            recommendations = self.resources.iloc[resource_indices].to_dict('records')
            
            return recommendations
        except Exception as e:
            logger.error(f"Error in content-based recommendations: {e}")
            return []
    
    def collaborative_filtering_recommendations(self, user_id: int, top_n: int = 5) -> List[Dict]:
        """
        Get collaborative filtering recommendations for a given user.
        
        Args:
            user_id: ID of the user to recommend for
            top_n: Number of recommendations to return
            
        Returns:
            List of recommended resources with their details
        """
        if self.user_data is None:
            logger.warning("No user data available for collaborative filtering")
            return []
            
        try:
            # Get the user's index
            user_idx = self.user_item_matrix.index.get_loc(user_id)
            
            # Get similar users
            similar_users = list(enumerate(self.user_similarity[user_idx]))
            similar_users = sorted(similar_users, key=lambda x: x[1], reverse=True)
            similar_users = similar_users[1:6]  # Top 5 similar users
            
            # Get resources rated by similar users
            similar_users_indices = [u[0] for u in similar_users]
            similar_users_ratings = self.user_item_matrix.iloc[similar_users_indices]
            
            # Calculate weighted average of ratings
            weighted_ratings = np.zeros(self.user_item_matrix.shape[1])
            total_similarity = 0
            
            for idx, similarity in similar_users:
                weighted_ratings += similarity * self.user_item_matrix.iloc[idx]
                total_similarity += similarity
            
            if total_similarity > 0:
                weighted_ratings /= total_similarity
            
            # Get top rated unseen resources
            user_rated = set(self.user_data[self.user_data['user_id'] == user_id]['resource_id'])
            resource_ids = self.user_item_matrix.columns
            
            recommendations = []
            for i, rating in enumerate(weighted_ratings):
                resource_id = resource_ids[i]
                if resource_id not in user_rated and rating > 0:
                    resource_info = self.resources[self.resources['resource_id'] == resource_id].iloc[0]
                    recommendations.append((resource_info, rating))
            
            # Sort by rating and get top_n
            recommendations.sort(key=lambda x: x[1], reverse=True)
            recommendations = [r[0].to_dict() for r in recommendations[:top_n]]
            
            return recommendations
        except Exception as e:
            logger.error(f"Error in collaborative filtering recommendations: {e}")
            return []
    
    def hybrid_recommendations(self, user_id: Optional[int], resource_id: Optional[int], top_n: int = 5) -> List[Dict]:
        """
        Get hybrid recommendations combining content-based and collaborative filtering.
        
        Args:
            user_id: ID of the user (optional)
            resource_id: ID of the resource (optional)
            top_n: Number of recommendations to return
            
        Returns:
            List of recommended resources with their details
        """
        try:
            content_rec = []
            collab_rec = []
            
            if resource_id is not None:
                content_rec = self.content_based_recommendations(resource_id, top_n)
            
            if user_id is not None and self.user_data is not None:
                collab_rec = self.collaborative_filtering_recommendations(user_id, top_n)
            
            # Combine and deduplicate recommendations
            all_rec = content_rec + collab_rec
            seen = set()
            unique_rec = []
            
            for rec in all_rec:
                rec_id = rec['resource_id']
                if rec_id not in seen:
                    seen.add(rec_id)
                    unique_rec.append(rec)
            
            return unique_rec[:top_n]
        except Exception as e:
            logger.error(f"Error in hybrid recommendations: {e}")
            return []

# Example usage
if __name__ == "__main__":
    # Sample data
    resources = pd.DataFrame({
        'resource_id': [1, 2, 3, 4, 5],
        'title': [
            'Stock Market Basics',
            'Advanced Portfolio Theory',
            'Real Estate Investing 101',
            'Cryptocurrency Fundamentals',
            'Value Investing Principles'
        ],
        'description': [
            'Learn the basics of stock market investing',
            'Advanced techniques for portfolio management',
            'Introduction to real estate investment strategies',
            'Understanding blockchain and crypto assets',
            'Fundamentals of value investing approach'
        ],
        'tags': [
            'stocks, beginner',
            'portfolio, advanced',
            'real estate, beginner',
            'crypto, blockchain',
            'stocks, value'
        ],
        'difficulty': ['beginner', 'advanced', 'beginner', 'intermediate', 'intermediate']
    })
    
    user_interactions = pd.DataFrame({
        'user_id': [101, 101, 101, 102, 102, 103, 103, 103],
        'resource_id': [1, 2, 3, 1, 4, 2, 3, 5],
        'rating': [5, 4, 3, 4, 5, 3, 4, 5]
    })
    
    # Initialize recommender
    recommender = InvestmentRecommender(resources, user_interactions)
    
    # Get recommendations
    print("Content-based recommendations for resource 1:")
    print(recommender.content_based_recommendations(1))
    
    print("\nCollaborative filtering recommendations for user 101:")
    print(recommender
