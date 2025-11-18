"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://chandkalaco.com
Prompt: Suggest a framework for building a recommendation system for products in categories such as "عطر و ادکلن مردانه" and "لوازم جانبی لپ تاپ," based on user preferences.
Generated: DETERMINISTIC_2b5cae45a3bd824d
Batch ID: 20250612_151752
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
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.model_selection import train_test_split
from sklearn.neighbors import NearestNeighbors
import numpy as np

class RecommendationSystem:
    def __init__(self, products):
        """
        Initialize the RecommendationSystem with a DataFrame of products.
        
        :param products: DataFrame containing product information with at least 'id', 'name', 'category', 'description' columns
        """
        self.products = products
        self.tfidf_matrix = None
        self.model = None

    def preprocess_data(self):
        """
        Preprocess product descriptions using TF-IDF vectorization.
        """
        # Vectorize product descriptions
        tfidf_vectorizer = TfidfVectorizer(stop_words='english')
        self.tfidf_matrix = tfidf_vectorizer.fit_transform(self.products['description'])

    def fit_model(self):
        """
        Fit a Nearest Neighbors model based on the TF-IDF matrix to perform recommendations.
        """
        self.model = NearestNeighbors(metric='cosine', algorithm='brute')
        self.model.fit(self.tfidf_matrix)

    def recommend(self, product_id, n_recommendations=5):
        """
        Recommend products based on a given product_id.
        
        :param product_id: The ID of the product to recommend similar products for
        :param n_recommendations: The number of recommendations to return
        :return: DataFrame containing recommended products
        """
        try:
            # Validate product_id exists in the dataset
            if product_id not in self.products['id'].values:
                raise ValueError("Product ID not found in the dataset.")

            # Get the index of the product
            product_idx = self.products[self.products['id'] == product_id].index[0]

            # Find the nearest neighbors
            distances, indices = self.model.kneighbors(self.tfidf_matrix[product_idx], n_neighbors=n_recommendations + 1)

            # Exclude the first product (itself)
            recommended_indices = indices.flatten()[1:]
            return self.products.iloc[recommended_indices]

        except Exception as e:
            print(f"Error occurred while recommending products: {e}")
            return pd.DataFrame()  # Return empty DataFrame on error

# Example usage:
if __name__ == "__main__":
    # Sample product DataFrame
    data = {
        'id': [1, 2, 3, 4, 5],
        'name': ['Men\'s Perfume A', 'Men\'s Perfume B', 'Laptop Accessory A', 'Laptop Accessory B', 'Men\'s Perfume C'],
        'category': ['عطر و ادکلن مردانه', 'عطر و ادکلن مردانه', 'لوازم جانبی لپ تاپ', 'لوازم جانبی لپ تاپ', 'عطر و ادکلن مردانه'],
        'description': ['A fresh scent for men.', 'A robust and masculine fragrance.', 
                        'High-quality laptop sleeve.', 'Versatile laptop stand.', 
                        'A light and refreshing cologne.']
    }
    
    products_df = pd.DataFrame(data)
    
    # Create recommendation system instance
    recommender = RecommendationSystem(products=products_df)
    
    # Preprocess data and fit the model
    recommender.preprocess_data()
    recommender.fit_model()
    
    # Get recommendations for a specific product
    recommendations = recommender.recommend(product_id=1, n_recommendations=3)
    print(recommendations)
```
