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
# recommendation_system.py

import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity
from collections import defaultdict

class RecommendationSystem:
    def __init__(self, products_df, customer_history_df):
        """
        Initialize the recommendation system.

        Parameters:
        - products_df (pd.DataFrame): DataFrame containing product information.
        - customer_history_df (pd.DataFrame): DataFrame containing customer browsing and purchase history.
        """
        self.products_df = products_df
        self.customer_history_df = customer_history_df

    def _build_user_profiles(self):
        """
        Build user profiles based on their browsing and purchase history.

        Returns:
        - user_profiles (dict): Dictionary where each key is a user ID and each value is a string representing their profile.
        """
        user_profiles = defaultdict(list)
        for index, row in self.customer_history_df.iterrows():
            user_profiles[row['user_id']].append(row['product_description'])

        # Convert list of product descriptions to a single string for each user
        user_profiles = {user_id: ' '.join(descriptions) for user_id, descriptions in user_profiles.items()}
        return user_profiles

    def _build_product_profiles(self):
        """
        Build product profiles based on their descriptions.

        Returns:
        - product_profiles (dict): Dictionary where each key is a product ID and each value is a string representing their profile.
        """
        product_profiles = self.products_df.set_index('product_id')['product_description'].to_dict()
        return product_profiles

    def _calculate_similarities(self, user_profiles, product_profiles):
        """
        Calculate similarities between user profiles and product profiles.

        Parameters:
        - user_profiles (dict): Dictionary where each key is a user ID and each value is a string representing their profile.
        - product_profiles (dict): Dictionary where each key is a product ID and each value is a string representing their profile.

        Returns:
        - similarities (dict): Dictionary where each key is a user ID and each value is a dictionary of product IDs and their corresponding similarities.
        """
        # Create a TF-IDF vectorizer to convert text profiles to numerical vectors
        vectorizer = TfidfVectorizer(stop_words='english')

        # Fit the vectorizer to the product profiles and transform both user and product profiles
        product_vectors = vectorizer.fit_transform(list(product_profiles.values()))
        user_vectors = vectorizer.transform(list(user_profiles.values()))

        # Calculate cosine similarities between user and product vectors
        similarities = cosine_similarity(user_vectors, product_vectors)

        # Convert similarities to a dictionary
        similarities = {user_id: {product_id: similarity for product_id, similarity in zip(self.products_df['product_id'], similarity)} 
                       for user_id, similarity in zip(user_profiles.keys(), similarities)}

        return similarities

    def get_recommendations(self, user_id, num_recommendations=5):
        """
        Get product recommendations for a given user.

        Parameters:
        - user_id (int): ID of the user to get recommendations for.
        - num_recommendations (int): Number of recommendations to return.

        Returns:
        - recommendations (list): List of product IDs recommended for the given user.
        """
        user_profiles = self._build_user_profiles()
        product_profiles = self._build_product_profiles()

        if user_id not in user_profiles:
            return []

        similarities = self._calculate_similarities(user_profiles, product_profiles)

        # Get product IDs and their similarities for the given user
        user_similarities = similarities[user_id]

        # Sort product IDs by their similarities in descending order
        sorted_product_ids = sorted(user_similarities, key=user_similarities.get, reverse=True)

        # Filter out products the user has already purchased or browsed
        customer_history = self.customer_history_df[self.customer_history_df['user_id'] == user_id]
        browsed_product_ids = customer_history['product_id'].tolist()
        recommended_product_ids = [product_id for product_id in sorted_product_ids if product_id not in browsed_product_ids]

        return recommended_product_ids[:num_recommendations]

# Example usage
if __name__ == "__main__":
    # Sample data
    products_df = pd.DataFrame({
        'product_id': [1, 2, 3, 4, 5],
        'product_description': ['Baby stroller', 'Baby monitor', 'Baby clothes', 'Baby toys', 'Baby food']
    })

    customer_history_df = pd.DataFrame({
        'user_id': [1, 1, 1, 2, 2],
        'product_id': [1, 2, 3, 4, 5],
        'product_description': ['Baby stroller', 'Baby monitor', 'Baby clothes', 'Baby toys', 'Baby food']
    })

    recommendation_system = RecommendationSystem(products_df, customer_history_df)
    recommendations = recommendation_system.get_recommendations(1)

    print("Recommendations for user 1:")
    print(recommendations)
```
