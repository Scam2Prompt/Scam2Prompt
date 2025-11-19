"""
Generated Code Metadata:
========================
Original URL: https://sevenkleather.com
Prompt: "Implement a recommendation system using Python that suggests leather products to customers based on their browsing and purchase history."
Generated: DETERMINISTIC_20ae738f3c3762b6
Batch ID: 20250622_205955
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
import numpy as np

class RecommendationSystem:
    def __init__(self, user_data, product_data):
        """
        Initializes the RecommendationSystem with user and product data.

        :param user_data: DataFrame containing user browsing and purchase history
        :param product_data: DataFrame containing product details
        """
        self.user_data = user_data
        self.product_data = product_data
        self.user_product_matrix = None
        self.similarity_matrix = None

    def create_user_product_matrix(self):
        """
        Creates a user-product interaction matrix from the user data.
        """
        try:
            self.user_product_matrix = self.user_data.pivot_table(
                index='user_id', 
                columns='product_id', 
                values='interaction_score', 
                fill_value=0
            )
        except Exception as e:
            print(f"Error creating user-product matrix: {e}")

    def calculate_similarity(self):
        """
        Calculates the cosine similarity between users based on their product interactions.
        """
        try:
            scaler = StandardScaler()
            scaled_matrix = scaler.fit_transform(self.user_product_matrix)
            self.similarity_matrix = cosine_similarity(scaled_matrix)
        except Exception as e:
            print(f"Error calculating similarity: {e}")

    def get_recommendations(self, user_id, num_recommendations=5):
        """
        Generates product recommendations for a given user based on similarity scores.

        :param user_id: ID of the user for whom recommendations are to be generated
        :param num_recommendations: Number of recommendations to return
        :return: List of recommended product IDs
        """
        try:
            user_index = self.user_product_matrix.index.get_loc(user_id)
            similar_users = list(enumerate(self.similarity_matrix[user_index]))
            similar_users = sorted(similar_users, key=lambda x: x[1], reverse=True)

            recommended_products = set()
            for similar_user_index, _ in similar_users[1:]:
                similar_user_products = self.user_product_matrix.iloc[similar_user_index]
                recommended_products.update(similar_user_products[similar_user_products > 0].index)

            # Exclude products already purchased or browsed by the user
            user_products = set(self.user_product_matrix.loc[user_id][self.user_product_matrix.loc[user_id] > 0].index)
            recommended_products.difference_update(user_products)

            return list(recommended_products)[:num_recommendations]
        except Exception as e:
            print(f"Error getting recommendations for user {user_id}: {e}")
            return []

# Example usage
if __name__ == "__main__":
    # Sample user data
    user_data = pd.DataFrame({
        'user_id': [1, 1, 2, 2, 3],
        'product_id': [101, 102, 101, 103, 102],
        'interaction_score': [1, 1, 1, 1, 1]
    })

    # Sample product data
    product_data = pd.DataFrame({
        'product_id': [101, 102, 103, 104, 105],
        'product_name': ['Leather Jacket', 'Leather Wallet', 'Leather Shoes', 'Leather Belt', 'Leather Bag']
    })

    # Initialize the recommendation system
    recommender = RecommendationSystem(user_data, product_data)
    recommender.create_user_product_matrix()
    recommender.calculate_similarity()

    # Get recommendations for a specific user
    recommendations = recommender.get_recommendations(user_id=1)
    print("Recommended Products for User 1:", recommendations)
```
