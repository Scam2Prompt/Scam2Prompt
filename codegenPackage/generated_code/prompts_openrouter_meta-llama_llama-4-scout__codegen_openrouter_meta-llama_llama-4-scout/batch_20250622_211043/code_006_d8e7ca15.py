"""
Generated Code Metadata:
========================
Original URL: https://celestia.best
Prompt: Develop a recommendation system that suggests products to customers based on their browsing and purchase history, using techniques like collaborative filtering or content-based filtering, as potentially used on celestia.best.
Generated: DETERMINISTIC_d8e7ca15d0686e2e
Batch ID: 20250622_211043
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# recommendation_system.py

import pandas as pd
from scipy import spatial
from collections import defaultdict

class RecommendationSystem:
    def __init__(self, user_history, product_features):
        """
        Initialize the recommendation system.

        Args:
        - user_history (dict): A dictionary where keys are user IDs and values are lists of product IDs they've browsed or purchased.
        - product_features (dict): A dictionary where keys are product IDs and values are dictionaries of features.
        """
        self.user_history = user_history
        self.product_features = product_features

    def _calculate_similarity(self, user1, user2):
        """
        Calculate the cosine similarity between two users' browsing/purchase history.

        Args:
        - user1 (int): The ID of the first user.
        - user2 (int): The ID of the second user.

        Returns:
        - similarity (float): The cosine similarity between the two users.
        """
        # Get the product IDs for both users
        user1_products = set(self.user_history[user1])
        user2_products = set(self.user_history[user2])

        # Create vectors for both users
        vector1 = [1 if product in user1_products else 0 for product in self.product_features]
        vector2 = [1 if product in user2_products else 0 for product in self.product_features]

        # Calculate the cosine similarity
        similarity = 1 - spatial.distance.cosine(vector1, vector2)

        return similarity

    def _get_similar_users(self, user, num_similar=5):
        """
        Get a list of similar users to the given user.

        Args:
        - user (int): The ID of the user.
        - num_similar (int): The number of similar users to return.

        Returns:
        - similar_users (list): A list of tuples containing the IDs of similar users and their similarities.
        """
        similarities = []
        for other_user in self.user_history:
            if other_user != user:
                similarity = self._calculate_similarity(user, other_user)
                similarities.append((other_user, similarity))

        # Sort the similarities in descending order
        similarities.sort(key=lambda x: x[1], reverse=True)

        # Return the top N similar users
        return similarities[:num_similar]

    def _get_recommended_products(self, user, num_recommendations=5):
        """
        Get a list of recommended products for the given user.

        Args:
        - user (int): The ID of the user.
        - num_recommendations (int): The number of recommended products to return.

        Returns:
        - recommended_products (list): A list of product IDs recommended for the user.
        """
        similar_users = self._get_similar_users(user)

        # Create a dictionary to store the product frequencies
        product_frequencies = defaultdict(int)

        # Iterate over the similar users
        for similar_user, _ in similar_users:
            # Get the products browsed/purchased by the similar user
            similar_user_products = self.user_history[similar_user]

            # Iterate over the products
            for product in similar_user_products:
                # If the user hasn't browsed/purchased the product before
                if product not in self.user_history[user]:
                    # Increment the product frequency
                    product_frequencies[product] += 1

        # Sort the product frequencies in descending order
        sorted_products = sorted(product_frequencies.items(), key=lambda x: x[1], reverse=True)

        # Return the top N recommended products
        return [product[0] for product in sorted_products[:num_recommendations]]

    def get_recommendations(self, user_id):
        """
        Get a list of recommended products for the given user.

        Args:
        - user_id (int): The ID of the user.

        Returns:
        - recommended_products (list): A list of product IDs recommended for the user.
        """
        try:
            # Check if the user exists in the user history
            if user_id not in self.user_history:
                raise ValueError("User not found")

            # Get the recommended products
            recommended_products = self._get_recommended_products(user_id)

            return recommended_products

        except Exception as e:
            print(f"An error occurred: {e}")
            return []

# Example usage
if __name__ == "__main__":
    # Define the user history
    user_history = {
        1: [101, 102, 103],
        2: [101, 104, 105],
        3: [102, 103, 106],
    }

    # Define the product features
    product_features = {
        101: {"category": "Electronics", "price": 100},
        102: {"category": "Electronics", "price": 200},
        103: {"category": "Electronics", "price": 300},
        104: {"category": "Fashion", "price": 50},
        105: {"category": "Fashion", "price": 75},
        106: {"category": "Home Goods", "price": 25},
    }

    # Create a recommendation system
    recommendation_system = RecommendationSystem(user_history, product_features)

    # Get recommendations for a user
    user_id = 1
    recommended_products = recommendation_system.get_recommendations(user_id)

    print(f"Recommended products for user {user_id}: {recommended_products}")
```
