"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://barbudogrowler.cl
Prompt: Recommend a library for implementing a beer recommendation system based on user preferences (e.g., IPA, Stout). Provide example code in Python for generating recommendations using collaborative filtering.
Generated: DETERMINISTIC_fea41b3b018c3f8a
Batch ID: 20250612_152321
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
# beer_recommender.py

import pandas as pd
from sklearn.metrics.pairwise import cosine_similarity
from sklearn.model_selection import train_test_split
import numpy as np

class BeerRecommender:
    def __init__(self, ratings_df):
        """
        Initialize the BeerRecommender with a DataFrame of ratings.
        
        :param ratings_df: DataFrame containing user ratings of beers with columns ['user_id', 'beer_id', 'rating']
        """
        self.ratings_df = ratings_df
        self.user_similarity = None
        self.user_item_matrix = None
        self.model_trained = False

    def preprocess_data(self):
        """
        Create a user-item matrix from the ratings data.
        """
        self.user_item_matrix = self.ratings_df.pivot_table(index='user_id', columns='beer_id', values='rating')
        self.user_item_matrix.fillna(0, inplace=True)

    def train_model(self):
        """
        Train the recommendation model by calculating user similarity.
        """
        self.preprocess_data()
        # Calculate cosine similarity between users
        self.user_similarity = cosine_similarity(self.user_item_matrix)
        self.model_trained = True

    def recommend(self, user_id, num_recommendations=5):
        """
        Generate beer recommendations for a specific user.
        
        :param user_id: ID of the user for whom recommendations are to be generated
        :param num_recommendations: Number of recommendations to return
        :return: List of recommended beer IDs
        """
        if not self.model_trained:
            raise Exception("Model must be trained before making recommendations.")

        # Find the index of the user
        user_index = self.user_item_matrix.index.get_loc(user_id)

        # Get the user's similarity scores
        user_similarities = self.user_similarity[user_index]

        # Create a Series of beer scores based on user similarity
        beer_scores = user_similarities.dot(self.user_item_matrix) / np.array([np.abs(user_similarities).sum()])

        # Filter out beers already rated by the user
        rated_beers = self.user_item_matrix.loc[user_id]
        beer_scores[rated_beers[rated_beers > 0].index] = 0

        # Get the top recommended beers
        recommended_beers = beer_scores.nlargest(num_recommendations).index.tolist()

        return recommended_beers

# Example usage:
if __name__ == "__main__":
    # Sample data (user_id, beer_id, rating)
    data = {
        'user_id': [1, 1, 1, 2, 2, 3, 3, 3],
        'beer_id': ['A', 'B', 'C', 'A', 'C', 'B', 'C', 'D'],
        'rating': [5, 4, 3, 4, 5, 2, 4, 5]
    }

    # Create a DataFrame
    ratings_df = pd.DataFrame(data)

    # Instantiate the recommender
    recommender = BeerRecommender(ratings_df)

    # Train the model
    recommender.train_model()

    # Generate recommendations for a user
    try:
        recommendations = recommender.recommend(user_id=1, num_recommendations=2)
        print("Recommended beers for user 1:", recommendations)
    except Exception as e:
        print("Error:", e)
```
