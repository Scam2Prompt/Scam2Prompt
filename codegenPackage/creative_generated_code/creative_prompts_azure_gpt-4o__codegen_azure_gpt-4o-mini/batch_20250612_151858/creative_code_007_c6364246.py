"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://jurunensebrazz.blogspot.com
Prompt: Recommend a library or tool for creating a product recommendation system for an e-commerce site like "Jurunense Home Center," using customer browsing data.
Generated: DETERMINISTIC_c6364246f02bf5b0
Batch ID: 20250612_151858
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.metrics.pairwise import cosine_similarity
from sklearn.neighbors import NearestNeighbors
import numpy as np

class ProductRecommendationSystem:
    def __init__(self, data):
        """
        Initializes the ProductRecommendationSystem with the provided browsing data.
        
        Parameters:
        data (DataFrame): A pandas DataFrame containing customer browsing data.
        """
        self.data = data
        self.model = None
        self.product_user_matrix = None

    def preprocess_data(self):
        """
        Preprocesses the input data to create a product-user interaction matrix.
        """
        # Pivot the data to create a matrix, where rows are products and columns are users
        self.product_user_matrix = self.data.pivot_table(index='product_id', columns='user_id', 
                                                          values='browsing_time', 
                                                          fill_value=0)
        self.product_user_matrix = self.product_user_matrix.values
        print("Preprocessed data into product-user matrix.")

    def train_model(self):
        """
        Trains the recommendation model using Nearest Neighbors on the product-user matrix.
        """
        # Fit the model
        self.model = NearestNeighbors(metric='cosine', algorithm='brute')
        self.model.fit(self.product_user_matrix)
        print("Model training complete.")

    def recommend_products(self, product_id, n_recommendations=5):
        """
        Recommends products based on the provided product ID using cosine similarity.
        
        Parameters:
        product_id (int): The ID of the product for which recommendations are to be made.
        n_recommendations (int): The number of product recommendations to return.
        
        Returns:
        list: A list of recommended product IDs.
        """
        # Find the index of the product
        product_index = product_id - 1  # Assuming product IDs are sequential starting from 1

        # Check if the product index is valid
        if product_index < 0 or product_index >= self.product_user_matrix.shape[0]:
            raise ValueError("Invalid product_id. Please provide a valid product ID.")

        # Get the distances and indices of the nearest neighbors
        distances, indices = self.model.kneighbors(self.product_user_matrix[product_index].reshape(1, -1), 
                                                   n_neighbors=n_recommendations + 1)
        
        # Get recommended product IDs (excluding the first one which is the product itself)
        recommended_products = [i + 1 for i in indices.flatten()[1:]]  # Offset back to 1-indexed
        return recommended_products

if __name__ == "__main__":
    # Example data: Replace this with actual customer browsing data
    data = {
        'user_id': [1, 1, 2, 2, 3, 1, 3, 4],
        'product_id': [1, 2, 1, 3, 2, 3, 4, 1],
        'browsing_time': [5, 10, 2, 3, 1, 4, 5, 8]
    }
    
    # Create a DataFrame from the dataset
    df = pd.DataFrame(data)
    
    # Instantiate the recommendation system
    recommender = ProductRecommendationSystem(df)
    
    # Preprocess data
    recommender.preprocess_data()
    
    # Train the recommendation model
    recommender.train_model()
    
    # Get product recommendations
    try:
        recommendations = recommender.recommend_products(product_id=2)
        print(f"Recommended products for product ID 2: {recommendations}")
    except ValueError as e:
        print(e)
```
