"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://ethn.cc
Prompt: Recommend libraries for building a recommendation system that suggests gravel bikes based on user preferences, inspired by the reviews on ETNH Gravel Magazine.
Generated: DETERMINISTIC_8fa7a78034becaf0
Batch ID: 20250612_154226
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
# Import necessary libraries
import pandas as pd
from sklearn.metrics.pairwise import cosine_similarity
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.neighbors import NearestNeighbors
import numpy as np

# Define a class to encapsulate the recommendation system
class GravelBikeRecommender:
    def __init__(self, data):
        """
        Initializes the GravelBikeRecommender with user preference data.
        
        :param data: DataFrame containing bike features and user preferences
        """
        self.data = data
        self.model = None

    def preprocess_data(self):
        """
        Preprocesses the data by handling missing values and normalizing features.
        """
        # Handle missing values by filling with median
        self.data.fillna(self.data.median(), inplace=True)
        
        # Normalize feature columns
        features = self.data.drop('BikeModel', axis=1)  # Assuming 'BikeModel' is the identifier
        self.scaler = StandardScaler()
        self.data[features.columns] = self.scaler.fit_transform(features)

    def train_model(self):
        """
        Trains the recommendation model using K-Nearest Neighbors.
        """
        try:
            # Prepare data for modeling
            feature_columns = self.data.drop('BikeModel', axis=1).columns
            X = self.data[feature_columns]
            
            # Create and fit the KNN model
            self.model = NearestNeighbors(n_neighbors=5, metric='cosine')
            self.model.fit(X)
        except Exception as e:
            print(f"Error during model training: {e}")

    def recommend(self, user_preferences):
        """
        Recommends bikes based on user preferences.
        
        :param user_preferences: A dictionary containing user preferences
        :return: List of recommended bike models
        """
        try:
            # Convert user preferences to DataFrame format
            user_df = pd.DataFrame([user_preferences])
            user_df.loc[:, user_df.columns] = self.scaler.transform(user_df)
            
            # Find nearest neighbors
            distances, indices = self.model.kneighbors(user_df)
            recommended_bikes = self.data.iloc[indices[0]]['BikeModel'].tolist()
            return recommended_bikes
        except Exception as e:
            print(f"Error during recommendation: {e}")
            return []

# Example usage
if __name__ == "__main__":
    # Sample data creation (replace with actual data loading)
    sample_data = {
        'BikeModel': ['Bike A', 'Bike B', 'Bike C', 'Bike D', 'Bike E'],
        'Price': [1200, 1500, 1300, 1600, 1250],
        'Weight': [9.5, 10.0, 9.8, 10.5, 9.7],
        'FrameMaterial': [1, 1, 0, 0, 1],  # 1: Aluminum, 0: Carbon
        'ReviewScore': [4.5, 4.7, 4.6, 4.8, 4.4]
    }
    bike_df = pd.DataFrame(sample_data)

    # Initialize recommender and run the recommendation process
    recommender = GravelBikeRecommender(bike_df)
    recommender.preprocess_data()
    recommender.train_model()

    # User preferences for recommendation
    user_preferences = {
        'Price': 1400,
        'Weight': 10.0,
        'FrameMaterial': 1,
        'ReviewScore': 4.5
    }

    # Get recommendations
    recommendations = recommender.recommend(user_preferences)
    print("Recommended Bikes:", recommendations)
```
