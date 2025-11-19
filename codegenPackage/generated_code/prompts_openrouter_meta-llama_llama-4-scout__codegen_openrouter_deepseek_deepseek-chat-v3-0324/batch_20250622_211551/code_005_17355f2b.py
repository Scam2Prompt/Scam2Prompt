"""
Generated Code Metadata:
========================
Original URL: https://lidofi.us.com
Prompt: Design a system to implement a recommendation engine for WW88, suggesting games, sports, or betting options to users based on their preferences, betting history, and demographics.
Generated: DETERMINISTIC_17355f2bfd131f63
Batch ID: 20250622_211551
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity
from sklearn.preprocessing import MinMaxScaler
from sklearn.cluster import KMeans
import numpy as np
import logging
from typing import List, Dict, Optional, Union
from pydantic import BaseModel, ValidationError
import json
from datetime import datetime

# Configure logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s'
)
logger = logging.getLogger(__name__)

# Data Models
class UserProfile(BaseModel):
    user_id: str
    age: int
    gender: str
    location: str
    favorite_sports: List[str]
    favorite_games: List[str]
    betting_history: List[Dict[str, Union[str, float]]]
    last_active: datetime

class RecommendationRequest(BaseModel):
    user_id: str
    current_interests: List[str]
    limit: int = 5

class RecommendationResponse(BaseModel):
    user_id: str
    recommendations: List[Dict[str, Union[str, float]]]
    generated_at: datetime

# Recommendation Engine Class
class WW88RecommendationEngine:
    def __init__(self, data_path: str = None):
        """
        Initialize the recommendation engine with optional data path.
        If data_path is provided, load data from file. Otherwise use empty DataFrame.
        """
        self.user_profiles = pd.DataFrame()
        self.games_data = pd.DataFrame()
        self.sports_data = pd.DataFrame()
        self.betting_data = pd.DataFrame()
        
        self.vectorizer = TfidfVectorizer(stop_words='english')
        self.scaler = MinMaxScaler()
        self.kmeans = KMeans(n_clusters=5, random_state=42)
        
        if data_path:
            try:
                self.load_data(data_path)
            except Exception as e:
                logger.error(f"Failed to load data: {str(e)}")
                raise

    def load_data(self, data_path: str) -> None:
        """
        Load user profiles, games, sports, and betting data from JSON file.
        
        Args:
            data_path: Path to JSON file containing all data
            
        Raises:
            FileNotFoundError: If file doesn't exist
            ValidationError: If data doesn't match expected schema
        """
        try:
            with open(data_path, 'r') as f:
                data = json.load(f)
                
            # Validate and load user profiles
            user_profiles = [UserProfile(**profile) for profile in data.get('user_profiles', [])]
            self.user_profiles = pd.DataFrame([profile.dict() for profile in user_profiles])
            
            # Load other data
            self.games_data = pd.DataFrame(data.get('games', []))
            self.sports_data = pd.DataFrame(data.get('sports', []))
            self.betting_data = pd.DataFrame(data.get('betting_options', []))
            
            logger.info("Data loaded successfully")
            
        except FileNotFoundError:
            logger.error("Data file not found")
            raise
        except ValidationError as e:
            logger.error(f"Data validation error: {str(e)}")
            raise
        except Exception as e:
            logger.error(f"Error loading data: {str(e)}")
            raise

    def preprocess_data(self) -> None:
        """
        Preprocess data for recommendation engine:
        - Combine text features
        - Normalize numerical features
        - Cluster users
        """
        if self.user_profiles.empty:
            logger.warning("No user profiles to preprocess")
            return
            
        try:
            # Combine text features for users
            self.user_profiles['combined_text'] = (
                self.user_profiles['favorite_sports'].apply(lambda x: ' '.join(x)) + ' ' +
                self.user_profiles['favorite_games'].apply(lambda x: ' '.join(x)) + ' ' +
                self.user_profiles['location']
            )
            
            # Vectorize text features
            text_matrix = self.vectorizer.fit_transform(self.user_profiles['combined_text'])
            
            # Normalize age
            age_normalized = self.scaler.fit_transform(self.user_profiles[['age']])
            
            # Combine features
            features = np.hstack([text_matrix.toarray(), age_normalized])
            
            # Cluster users
            self.user_profiles['cluster'] = self.kmeans.fit_predict(features)
            
            logger.info("Data preprocessing completed")
            
        except Exception as e:
            logger.error(f"Error during data preprocessing: {str(e)}")
            raise

    def get_similar_users(self, user_id: str, n: int = 5) -> List[str]:
        """
        Find similar users based on profile and behavior.
        
        Args:
            user_id: ID of target user
            n: Number of similar users to return
            
        Returns:
            List of similar user IDs
            
        Raises:
            ValueError: If user_id not found
        """
        if user_id not in self.user_profiles['user_id'].values:
            raise ValueError(f"User {user_id} not found")
            
        try:
            target_user = self.user_profiles[self.user_profiles['user_id'] == user_id].iloc[0]
            same_cluster = self.user_profiles[self.user_profiles['cluster'] == target_user['cluster']]
            
            # Exclude the target user
            same_cluster = same_cluster[same_cluster['user_id'] != user_id]
            
            # Calculate similarity based on betting history (simplified)
            similar_users = same_cluster.sort_values(
                by='last_active', 
                ascending=False
            ).head(n)['user_id'].tolist()
            
            return similar_users
            
        except Exception as e:
            logger.error(f"Error finding similar users: {str(e)}")
            raise

    def generate_recommendations(self, request: RecommendationRequest) -> RecommendationResponse:
        """
        Generate personalized recommendations for a user.
        
        Args:
            request: RecommendationRequest object with user details
            
        Returns:
            RecommendationResponse with generated recommendations
            
        Raises:
            ValueError: If user not found or invalid request
        """
        try:
            # Validate request
            if not isinstance(request, RecommendationRequest):
                raise ValueError("Invalid request format")
                
            if request.user_id not in self.user_profiles['user_id'].values:
                raise ValueError(f"User {request.user_id} not found")
                
            # Get user profile
            user_profile = self.user_profiles[self.user_profiles['user_id'] == request.user_id].iloc[0]
            
            # Get similar users
            similar_users = self.get_similar_users(request.user_id)
            
            # Aggregate preferences from similar users
            similar_profiles = self.user_profiles[self.user_profiles['user_id'].isin(similar_users)]
            
            # Get popular games among similar users
            game_recs = self._get_popular_items(
                similar_profiles, 
                'favorite_games', 
                self.games_data,
                request.current_interests
            )
            
            # Get popular sports among similar users
            sport_recs = self._get_popular_items(
                similar_profiles,
                'favorite_sports',
                self.sports_data,
                request.current_interests
            )
            
            # Get betting recommendations based on history
            betting_recs = self._get_betting_recommendations(user_profile)
            
            # Combine and rank recommendations
            all_recs = game_recs + sport_recs + betting_recs
            ranked_recs = sorted(all_recs, key=lambda x: x['score'], reverse=True)[:request.limit]
            
            return RecommendationResponse(
                user_id=request.user_id,
                recommendations=ranked_recs,
                generated_at=datetime.now()
            )
            
        except Exception as e:
            logger.error(f"Error generating recommendations: {str(e)}")
            raise

    def _get_popular_items(self, profiles: pd.DataFrame, 
                          field: str, 
                          item_data: pd.DataFrame,
                          current_interests: List[str]) -> List[Dict[str, Union[str, float]]]:
        """
        Helper method to get popular items among a group of users.
        
        Args:
            profiles: DataFrame of user profiles
            field: Field containing item preferences ('favorite_games' or 'favorite_sports')
            item_data: DataFrame of item metadata
            current_interests: User's current interests to avoid recommending
            
        Returns:
            List of recommended items with scores
        """
        try:
            # Flatten all favorites from similar users
            all_items = [item for sublist in profiles[field].tolist() for item in sublist]
            
            # Count occurrences
            item_counts = pd.Series(all_items).value_counts().reset_index()
            item_counts.columns = ['item_id', 'count']
            
            # Merge with item data
            merged = item_counts.merge(item_data, on='item_id', how='left')
            
            # Filter out current interests
            merged = merged[~merged['item_id'].isin(current_interests)]
            
            # Normalize scores
            if not merged.empty:
                merged['score'] = merged['count'] /
