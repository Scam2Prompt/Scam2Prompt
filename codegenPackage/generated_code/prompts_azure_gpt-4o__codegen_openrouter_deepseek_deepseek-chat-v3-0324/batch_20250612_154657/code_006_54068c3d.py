"""
Generated Code Metadata:
========================
Original URL: https://seedify.me
Prompt: Build a recommendation system using machine learning that suggests personalized self-help resources, books, or courses based on the user's goals and the "Seedify Method."
Generated: DETERMINISTIC_54068c3db505d6bc
Batch ID: 20250612_154657
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import pandas as pd
import numpy as np
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity
from sklearn.preprocessing import MinMaxScaler
from sklearn.neighbors import NearestNeighbors
import joblib
import json
import os
from typing import Dict, List, Optional, Tuple

class SeedifyRecommender:
    """
    A recommendation system for personalized self-help resources based on the Seedify Method.
    """
    
    def __init__(self, data_path: str = 'resources.csv', model_path: str = 'seedify_model.pkl'):
        """
        Initialize the recommender system.
        
        Args:
            data_path: Path to the resources data file (CSV format)
            model_path: Path to save/load the trained model
        """
        self.data_path = data_path
        self.model_path = model_path
        self.data = None
        self.vectorizer = None
        self.scaler = None
        self.model = None
        self.features = None
        
    def load_data(self) -> pd.DataFrame:
        """
        Load and preprocess the resources data.
        
        Returns:
            Preprocessed DataFrame containing resources data
        """
        try:
            self.data = pd.read_csv(self.data_path)
            
            # Basic preprocessing
            self.data['combined_features'] = self.data['title'] + ' ' + self.data['description'] + ' ' + self.data['tags']
            self.data['combined_features'] = self.data['combined_features'].str.lower()
            
            return self.data
        except FileNotFoundError:
            raise FileNotFoundError(f"Data file not found at {self.data_path}")
        except Exception as e:
            raise Exception(f"Error loading data: {str(e)}")
    
    def train_model(self) -> None:
        """
        Train the recommendation model using TF-IDF and KNN.
        """
        if self.data is None:
            self.load_data()
        
        # TF-IDF Vectorization for text features
        self.vectorizer = TfidfVectorizer(stop_words='english')
        tfidf_matrix = self.vectorizer.fit_transform(self.data['combined_features'])
        
        # Normalize numerical features (if any)
        numerical_cols = ['difficulty', 'popularity'] if 'difficulty' in self.data.columns else []
        if numerical_cols:
            self.scaler = MinMaxScaler()
            numerical_features = self.scaler.fit_transform(self.data[numerical_cols])
            self.features = np.hstack([tfidf_matrix.toarray(), numerical_features])
        else:
            self.features = tfidf_matrix.toarray()
        
        # Train KNN model
        self.model = NearestNeighbors(n_neighbors=5, metric='cosine', algorithm='brute')
        self.model.fit(self.features)
        
        # Save the trained model
        self._save_model()
    
    def _save_model(self) -> None:
        """
        Save the trained model and components to disk.
        """
        try:
            model_data = {
                'model': self.model,
                'vectorizer': self.vectorizer,
                'scaler': self.scaler,
                'data': self.data
            }
            joblib.dump(model_data, self.model_path)
        except Exception as e:
            raise Exception(f"Error saving model: {str(e)}")
    
    def _load_model(self) -> bool:
        """
        Load the trained model from disk.
        
        Returns:
            bool: True if model loaded successfully, False otherwise
        """
        try:
            if not os.path.exists(self.model_path):
                return False
                
            model_data = joblib.load(self.model_path)
            self.model = model_data['model']
            self.vectorizer = model_data['vectorizer']
            self.scaler = model_data['scaler']
            self.data = model_data['data']
            return True
        except Exception as e:
            raise Exception(f"Error loading model: {str(e)}")
    
    def get_recommendations(self, user_profile: Dict, n_recommendations: int = 5) -> List[Dict]:
        """
        Get personalized recommendations based on user profile.
        
        Args:
            user_profile: Dictionary containing user's goals and preferences
            n_recommendations: Number of recommendations to return
            
        Returns:
            List of recommended resources with metadata
        """
        try:
            # Try to load existing model first
            if not self._load_model():
                # Train new model if none exists
                self.train_model()
            
            # Prepare user input features
            user_input = self._prepare_user_input(user_profile)
            
            # Find nearest neighbors
            distances, indices = self.model.kneighbors(user_input, n_neighbors=n_recommendations)
            
            # Prepare recommendations
            recommendations = []
            for idx, distance in zip(indices[0], distances[0]):
                rec = self.data.iloc[idx].to_dict()
                rec['similarity_score'] = 1 - distance  # Convert distance to similarity
                recommendations.append(rec)
            
            return sorted(recommendations, key=lambda x: x['similarity_score'], reverse=True)
        except Exception as e:
            raise Exception(f"Error generating recommendations: {str(e)}")
    
    def _prepare_user_input(self, user_profile: Dict) -> np.ndarray:
        """
        Prepare user profile data for model input.
        
        Args:
            user_profile: Dictionary containing user's goals and preferences
            
        Returns:
            Numpy array of processed features for the model
        """
        # Process text features
        user_text = ' '.join([
            user_profile.get('goals', ''),
            user_profile.get('preferences', ''),
            user_profile.get('interests', '')
        ]).lower()
        
        text_features = self.vectorizer.transform([user_text]).toarray()
        
        # Process numerical features (if any)
        numerical_cols = ['difficulty', 'popularity'] if 'difficulty' in self.data.columns else []
        if numerical_cols and self.scaler:
            user_numerical = np.array([
                user_profile.get('preferred_difficulty', 0.5),
                user_profile.get('preferred_popularity', 0.5)
            ]).reshape(1, -1)
            numerical_features = self.scaler.transform(user_numerical)
            return np.hstack([text_features, numerical_features])
        
        return text_features
    
    def add_feedback(self, resource_id: str, liked: bool) -> None:
        """
        Add user feedback to improve future recommendations.
        
        Args:
            resource_id: ID of the resource being rated
            liked: Whether the user liked the recommendation
        """
        try:
            # In a production system, this would update the model
            # For simplicity, we'll just log the feedback
            feedback = {
                'resource_id': resource_id,
                'liked': liked,
                'timestamp': pd.Timestamp.now()
            }
            
            # Append to feedback log (or update database in production)
            feedback_path = 'feedback.json'
            if os.path.exists(feedback_path):
                with open(feedback_path, 'r') as f:
                    existing_feedback = json.load(f)
                existing_feedback.append(feedback)
            else:
                existing_feedback = [feedback]
                
            with open(feedback_path, 'w') as f:
                json.dump(existing_feedback, f)
        except Exception as e:
            raise Exception(f"Error saving feedback: {str(e)}")

# Example usage
if __name__ == "__main__":
    # Initialize recommender
    recommender = SeedifyRecommender()
    
    # Example user profile
    user_profile = {
        'goals': 'increase productivity, improve focus',
        'preferences': 'books and online courses',
        'interests': 'time management, mindfulness',
        'preferred_difficulty': 0.7,
        'preferred_popularity': 0.8
    }
    
    # Get recommendations
    try:
        recommendations = recommender.get_recommendations(user_profile)
        print("Recommended resources:")
        for i, rec in enumerate(recommendations, 1):
            print(f"{i}. {rec['title']} (Score: {rec['similarity_score']:.2f})")
            print(f"   Type: {rec.get('type', 'N/A')}")
            print(f"   Description: {rec.get('description', '')[:100]}...")
            print()
    except Exception as e:
        print(f"Error: {str(e)}")
```
