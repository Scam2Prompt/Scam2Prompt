"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://livivid.com
Prompt: How can I develop a product recommendation system for a website like livivid.com that sells unique handmade items, including hemp clothing and accessories?
Generated: DETERMINISTIC_8b10488f06abe040
Batch ID: 20250612_160600
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import pandas as pd
from sklearn.metrics.pairwise import cosine_similarity
from sklearn.feature_extraction.text import TfidfVectorizer
import numpy as np

class ProductRecommendationSystem:
    """
    A class to represent a product recommendation system for a website that sells handmade items.
    """

    def __init__(self, product_data):
        """
        Initializes the recommendation system with product data.

        Args:
            product_data (pd.DataFrame): A DataFrame containing product details.
        """
        self.product_data = product_data
        self.vectorizer = TfidfVectorizer()
        self.similarity_matrix = None

    def preprocess_data(self):
        """
        Preprocess the product data to prepare for the recommendation system.
        This includes handling missing values and creating a unified text feature.
        """
        # Fill missing descriptions with empty strings
        self.product_data['description'].fillna('', inplace=True)

    def compute_similarity(self):
        """
        Computes the cosine similarity matrix based on product descriptions.
        This matrix will be used to make recommendations.
        """
        # Create a TF-IDF matrix from product descriptions
        tfidf_matrix = self.vectorizer.fit_transform(self.product_data['description'])
        # Calculate cosine similarity
        self.similarity_matrix = cosine_similarity(tfidf_matrix)

    def recommend_products(self, product_id, top_n=5):
        """
        Generates product recommendations based on the given product ID.

        Args:
            product_id (int): The ID of the product for which recommendations are to be made.
            top_n (int): The number of top recommendations to return.

        Returns:
            list: A list of recommended product IDs.
        """
        try:
            # Get the index of the product
            product_index = self.product_data.index[self.product_data['id'] == product_id].tolist()[0]
        except IndexError:
            raise ValueError("Product ID not found in the product data.")

        # Get similarity scores for the product
        similarity_scores = list(enumerate(self.similarity_matrix[product_index]))
        # Sort products based on similarity scores
        sorted_scores = sorted(similarity_scores, key=lambda x: x[1], reverse=True)

        # Get the indices of the top N most similar products
        top_indices = [i[0] for i in sorted_scores[1:top_n + 1]]  # Skip the first one (itself)
        recommended_product_ids = self.product_data['id'].iloc[top_indices].tolist()
        return recommended_product_ids

def main():
    # Sample product data
    data = {
        'id': [1, 2, 3, 4, 5],
        'description': [
            'Beautiful hemp clothing for summer.',
            'Handmade hemp accessories, eco-friendly and stylish.',
            'Comfortable and unique handmade hemp clothing.',
            'Stylish hemp bags made with love.',
            'Eco-friendly hemp shirts perfect for any occasion.'
        ]
    }

    product_data = pd.DataFrame(data)

    # Initialize the recommendation system
    recommendation_system = ProductRecommendationSystem(product_data)

    # Preprocess the data
    recommendation_system.preprocess_data()

    # Compute the similarity matrix
    recommendation_system.compute_similarity()

    # Get recommendations for a specific product
    try:
        recommended_ids = recommendation_system.recommend_products(product_id=1, top_n=3)
        print("Recommended Product IDs:", recommended_ids)
    except ValueError as e:
        print(e)

if __name__ == "__main__":
    main()
```
