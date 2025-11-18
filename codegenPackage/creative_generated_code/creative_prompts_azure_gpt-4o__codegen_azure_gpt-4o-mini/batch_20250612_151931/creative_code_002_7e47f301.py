"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://noymi.in
Prompt: Generate code to create a product recommendation system for e-commerce platforms selling items like Noymi True Wireless Bluetooth Earbuds | ET-219.
Generated: DETERMINISTIC_7e47f3015a9e6f2b
Batch ID: 20250612_151931
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
    A class to represent a product recommendation system based on cosine similarity of product descriptions.
    """

    def __init__(self, product_data):
        """
        Initializes the recommendation system with product data.

        Parameters:
        product_data (pd.DataFrame): DataFrame containing product information including descriptions.
        """
        self.product_data = product_data
        self.tfidf_vectorizer = TfidfVectorizer(stop_words='english')
        self.tfidf_matrix = None
        self.cosine_sim = None

    def preprocess_data(self):
        """
        Preprocess the product data to fit the model.
        """
        # Check if 'description' column exists in the data
        if 'description' not in self.product_data.columns:
            raise ValueError("Product data must contain a 'description' column.")
        
        # Create TF-IDF matrix
        self.tfidf_matrix = self.tfidf_vectorizer.fit_transform(self.product_data['description'])

    def compute_similarity(self):
        """
        Computes the cosine similarity matrix for the products.
        """
        if self.tfidf_matrix is None:
            raise RuntimeError("TF-IDF matrix is not initialized. Call preprocess_data() first.")
        
        self.cosine_sim = cosine_similarity(self.tfidf_matrix, self.tfidf_matrix)

    def get_product_recommendations(self, product_id, num_recommendations=5):
        """
        Get product recommendations based on the provided product ID.

        Parameters:
        product_id (int): Index of the product to recommend similar items.
        num_recommendations (int): Number of recommendations to return. Defaults to 5.

        Returns:
        List of recommended product IDs.
        """
        if self.cosine_sim is None:
            raise RuntimeError("Cosine similarity matrix is not computed. Call compute_similarity() first.")
        
        # Get the similarity scores for the given product
        sim_scores = list(enumerate(self.cosine_sim[product_id]))

        # Sort products based on similarity scores
        sim_scores = sorted(sim_scores, key=lambda x: x[1], reverse=True)

        # Get the scores of the most similar products
        sim_scores = sim_scores[1:num_recommendations + 1]

        # Get the product indices
        product_indices = [i[0] for i in sim_scores]

        return self.product_data.iloc[product_indices]

# Example usage
if __name__ == "__main__":
    # Load sample product data
    data = {
        'product_id': [1, 2, 3, 4, 5],
        'description': [
            "Noymi True Wireless Bluetooth Earbuds | ET-219 with noise cancellation.",
            "Sony WH-1000XM4 Wireless Headphones with noise cancellation.",
            "Apple AirPods Pro with active noise cancellation.",
            "Bose QuietComfort 35 II Wireless Headphones.",
            "Jabra Elite 75t True Wireless Earbuds."
        ]
    }

    # Create DataFrame
    product_df = pd.DataFrame(data)

    # Create recommendation system instance
    recommender = ProductRecommendationSystem(product_df)

    try:
        # Preprocess data and compute similarity
        recommender.preprocess_data()
        recommender.compute_similarity()

        # Get recommendations for the first product
        recommendations = recommender.get_product_recommendations(product_id=0)
        print("Recommended Products:")
        print(recommendations)
        
    except Exception as e:
        print(f"An error occurred: {e}")
```
