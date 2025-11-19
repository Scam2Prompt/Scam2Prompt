"""
Generated Code Metadata:
========================
Original URL: https://somoscorujasbraz.blogspot.com
Prompt: Develop a recommendation system for an e-commerce platform, like Somos Corujas, to suggest baby products to customers based on their browsing and purchase history.
Generated: DETERMINISTIC_bcc0a7e29e389474
Batch ID: 20250622_212549
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
from sklearn.preprocessing import StandardScaler
from sklearn.model_selection import train_test_split
from sklearn.neighbors import NearestNeighbors
import numpy as np

class RecommendationSystem:
    def __init__(self, data):
        """
        Initializes the RecommendationSystem with user data.

        :param data: DataFrame containing user browsing and purchase history
        """
        self.data = data
        self.model = None
        self.user_item_matrix = None

    def preprocess_data(self):
        """
        Preprocesses the data to create a user-item interaction matrix.
        """
        # Create a user-item interaction matrix
        self.user_item_matrix = self.data.pivot_table(index='user_id', columns='product_id', values='interaction', fill_value=0)

    def fit_model(self):
        """
        Fits the recommendation model using Nearest Neighbors.
        """
        # Standardize the user-item matrix
        scaler = StandardScaler()
        scaled_matrix = scaler.fit_transform(self.user_item_matrix)

        # Fit the Nearest Neighbors model
        self.model = NearestNeighbors(metric='cosine')
        self.model.fit(scaled_matrix)

    def recommend_products(self, user_id, n_recommendations=5):
        """
        Recommends products for a given user based on their interaction history.

        :param user_id: ID of the user for whom to recommend products
        :param n_recommendations: Number of product recommendations to return
        :return: List of recommended product IDs
        """
        if self.user_item_matrix is None:
            raise ValueError("Model has not been fitted. Please call fit_model() after preprocessing data.")

        # Check if user_id exists in the user-item matrix
        if user_id not in self.user_item_matrix.index:
            raise ValueError(f"User ID {user_id} not found in the data.")

        # Get the user's interaction vector
        user_vector = self.user_item_matrix.loc[user_id].values.reshape(1, -1)

        # Standardize the user vector
        scaler = StandardScaler()
        user_vector_scaled = scaler.fit_transform(user_vector)

        # Find nearest neighbors
        distances, indices = self.model.kneighbors(user_vector_scaled, n_neighbors=n_recommendations + 1)

        # Get recommended product IDs
        recommended_indices = indices.flatten()[1:]  # Skip the first index as it is the user itself
        recommended_products = self.user_item_matrix.index[recommended_indices]

        return recommended_products.tolist()

# Example usage
if __name__ == "__main__":
    # Sample data creation
    data = {
        'user_id': [1, 1, 2, 2, 3, 3, 4, 4],
        'product_id': [101, 102, 101, 103, 102, 104, 101, 105],
        'interaction': [1, 1, 1, 1, 1, 1, 1, 1]  # 1 indicates interaction (browsing or purchase)
    }
    
    df = pd.DataFrame(data)

    # Initialize the recommendation system
    recommender = RecommendationSystem(df)

    # Preprocess the data
    recommender.preprocess_data()

    # Fit the model
    recommender.fit_model()

    # Get recommendations for a specific user
    try:
        recommendations = recommender.recommend_products(user_id=1, n_recommendations=3)
        print("Recommended Products for User 1:", recommendations)
    except ValueError as e:
        print("Error:", e)
```
