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
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity
import numpy as np

class RecommendationSystem:
    def __init__(self, product_data, user_data):
        """
        Initialize the recommendation system with product and user data.

        :param product_data: DataFrame containing product information (id, name, category, description, etc.)
        :param user_data: DataFrame containing user browsing and purchase history (user_id, product_id, action, etc.)
        """
        self.product_data = product_data
        self.user_data = user_data
        self.vectorizer = TfidfVectorizer(stop_words='english')
        self.product_similarity_matrix = None

    def preprocess_data(self):
        """
        Preprocess product data to create a combined text field for TF-IDF vectorization.
        """
        self.product_data['combined_text'] = (
            self.product_data['name'] + " " +
            self.product_data['category'] + " " +
            self.product_data['description']
        )

    def calculate_similarity(self):
        """
        Calculate the cosine similarity matrix for products based on their combined text field.
        """
        tfidf_matrix = self.vectorizer.fit_transform(self.product_data['combined_text'])
        self.product_similarity_matrix = cosine_similarity(tfidf_matrix)

    def recommend_products(self, user_id, top_n=5):
        """
        Recommend products to a user based on their browsing and purchase history.

        :param user_id: ID of the user to generate recommendations for.
        :param top_n: Number of top recommendations to return.
        :return: List of recommended product IDs.
        """
        # Get the user's browsing and purchase history
        user_history = self.user_data[self.user_data['user_id'] == user_id]
        if user_history.empty:
            return []  # Return an empty list if no history is found

        # Get product IDs from the user's history
        user_product_ids = user_history['product_id'].unique()

        # Calculate average similarity scores for all products based on user's history
        similarity_scores = np.zeros(len(self.product_data))
        for product_id in user_product_ids:
            product_index = self.product_data.index[self.product_data['id'] == product_id].tolist()
            if product_index:
                similarity_scores += self.product_similarity_matrix[product_index[0]]

        # Sort products by similarity scores and exclude products the user has already interacted with
        recommended_indices = np.argsort(similarity_scores)[::-1]
        recommended_product_ids = [
            self.product_data.iloc[i]['id']
            for i in recommended_indices
            if self.product_data.iloc[i]['id'] not in user_product_ids
        ]

        return recommended_product_ids[:top_n]

# Example usage
if __name__ == "__main__":
    # Sample product data
    product_data = pd.DataFrame({
        'id': [1, 2, 3, 4, 5],
        'name': ['Baby Stroller', 'Baby Bottle', 'Diapers', 'Baby Crib', 'Baby Monitor'],
        'category': ['Strollers', 'Feeding', 'Diapers', 'Furniture', 'Electronics'],
        'description': [
            'Lightweight and durable stroller for babies.',
            'High-quality baby bottle for feeding.',
            'Comfortable and absorbent diapers.',
            'Safe and sturdy baby crib.',
            'Monitor your baby with high-definition video.'
        ]
    })

    # Sample user data
    user_data = pd.DataFrame({
        'user_id': [101, 101, 102, 103, 101],
        'product_id': [1, 2, 3, 4, 5],
        'action': ['view', 'purchase', 'view', 'view', 'view']
    })

    # Initialize and run the recommendation system
    recommender = RecommendationSystem(product_data, user_data)
    recommender.preprocess_data()
    recommender.calculate_similarity()
    recommendations = recommender.recommend_products(user_id=101, top_n=3)

    print("Recommended products for user 101:", recommendations)
```
