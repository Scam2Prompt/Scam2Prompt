"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://biogreenasia.com
Prompt: How can I implement a product recommendation system for a website like Bio Green Asia that features 100% natural food supplements and cleaning products?
Generated: DETERMINISTIC_1b0a021894aa5965
Batch ID: 20250612_163924
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
# Import necessary libraries
import numpy as np
import pandas as pd
from sklearn.metrics.pairwise import cosine_similarity
from sklearn.feature_extraction.text import CountVectorizer

class ProductRecommendationSystem:
    """
    A product recommendation system for Bio Green Asia.
    This system uses content-based filtering to recommend products based on their features.
    """

    def __init__(self, product_data):
        """
        Initialize the recommendation system with product data.
        
        :param product_data: A pandas DataFrame containing product details (id, name, description, category, etc.)
        """
        self.product_data = product_data
        self.similarity_matrix = None

    def preprocess_data(self):
        """
        Preprocess the product data to generate a 'combined_features' column.
        This column combines key attributes like 'name', 'category', and 'description'.
        """
        self.product_data['combined_features'] = self.product_data.apply(
            lambda row: f"{row['name']} {row['category']} {row['description']}", axis=1
        )

    def calculate_similarity(self):
        """
        Calculate similarity scores between products using cosine similarity.
        """
        # Convert combined features into a matrix of token counts
        count_vectorizer = CountVectorizer()
        count_matrix = count_vectorizer.fit_transform(self.product_data['combined_features'])
        
        # Compute cosine similarity between all products
        self.similarity_matrix = cosine_similarity(count_matrix)

    def recommend_products(self, product_id, top_n=5):
        """
        Recommend top N similar products for a given product ID.
        
        :param product_id: ID of the product to base recommendations on
        :param top_n: Number of recommendations to return
        :return: A list of recommended product IDs
        """
        if self.similarity_matrix is None:
            raise ValueError("Similarity matrix not calculated. Call calculate_similarity() first.")
        
        if product_id not in self.product_data['id'].values:
            raise ValueError(f"Product ID {product_id} not found in the product data.")
        
        # Find the index of the given product in the DataFrame
        product_index = self.product_data.index[self.product_data['id'] == product_id][0]
        
        # Get similarity scores for the given product
        similarity_scores = list(enumerate(self.similarity_matrix[product_index]))
        
        # Sort products based on similarity scores in descending order
        sorted_scores = sorted(similarity_scores, key=lambda x: x[1], reverse=True)
        
        # Extract top N product indices (excluding the given product itself)
        top_products = [self.product_data.iloc[i]['id'] for i, _ in sorted_scores[1:top_n + 1]]
        
        return top_products

# Example usage
if __name__ == "__main__":
    # Create sample product data
    product_data = pd.DataFrame([
        {"id": 1, "name": "Organic Green Tea", "category": "Food Supplements", "description": "Rich in antioxidants"},
        {"id": 2, "name": "Eco-Friendly Cleaner", "category": "Cleaning Products", "description": "Safe for the environment"},
        {"id": 3, "name": "Natural Multivitamin", "category": "Food Supplements", "description": "Boosts immunity"},
        {"id": 4, "name": "Bio Degradable Detergent", "category": "Cleaning Products", "description": "Effective on tough stains"},
        {"id": 5, "name": "Herbal Weight Loss Tea", "category": "Food Supplements", "description": "Helps in weight management"}
    ])

    # Initialize the recommendation system
    recommender = ProductRecommendationSystem(product_data)

    # Preprocess data and calculate similarity matrix
    recommender.preprocess_data()
    recommender.calculate_similarity()

    # Get recommendations for a product
    recommended_products = recommender.recommend_products(product_id=1, top_n=3)
    print(f"Recommended products for Product ID 1: {recommended_products}")
```
