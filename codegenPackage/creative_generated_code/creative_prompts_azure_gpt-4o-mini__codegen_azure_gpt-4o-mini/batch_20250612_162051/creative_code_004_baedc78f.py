"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://aatmanamjewels.com
Prompt: Illustrate how to implement a product recommendation system for a jewelry website, using the unique features of Atmanam Jewels as a reference.
Generated: DETERMINISTIC_baedc78f428c5801
Batch ID: 20250612_162051
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
import numpy as np
from sklearn.metrics.pairwise import cosine_similarity
from sklearn.preprocessing import StandardScaler
from sklearn.model_selection import train_test_split
from sklearn.neighbors import NearestNeighbors

class ProductRecommendationSystem:
    def __init__(self, product_data):
        """
        Initialize the recommendation system with product data.

        Parameters:
        product_data (DataFrame): A pandas DataFrame containing product details.
        """
        self.product_data = product_data
        self.model = None

    def preprocess_data(self):
        """
        Preprocess the product data by handling missing values and scaling features.
        """
        # Fill missing values with the median
        self.product_data.fillna(self.product_data.median(), inplace=True)

        # Scale numerical features
        scaler = StandardScaler()
        numerical_cols = ['price', 'carat', 'rating']
        self.product_data[numerical_cols] = scaler.fit_transform(self.product_data[numerical_cols])

    def train_model(self):
        """
        Train the nearest neighbors model for product recommendations.
        """
        try:
            # Prepare features for training
            features = self.product_data[['price', 'carat', 'rating']].values
            self.model = NearestNeighbors(n_neighbors=5, algorithm='auto')
            self.model.fit(features)
        except Exception as e:
            print(f"Error in training model: {e}")

    def recommend_products(self, product_id):
        """
        Recommend products similar to the given product ID.

        Parameters:
        product_id (int): The ID of the product to find recommendations for.

        Returns:
        DataFrame: A DataFrame containing recommended products.
        """
        try:
            # Get the features of the specified product
            product_index = self.product_data[self.product_data['id'] == product_id].index[0]
            product_features = self.product_data[['price', 'carat', 'rating']].iloc[product_index].values.reshape(1, -1)

            # Find the nearest neighbors
            distances, indices = self.model.kneighbors(product_features)

            # Retrieve recommended products
            recommended_products = self.product_data.iloc[indices.flatten()]
            return recommended_products
        except IndexError:
            print(f"Product ID {product_id} not found.")
            return pd.DataFrame()  # Return empty DataFrame if product not found
        except Exception as e:
            print(f"Error in recommending products: {e}")
            return pd.DataFrame()  # Return empty DataFrame on error

# Sample data creation
data = {
    'id': [1, 2, 3, 4, 5],
    'name': ['Gold Ring', 'Diamond Necklace', 'Silver Bracelet', 'Platinum Earrings', 'Emerald Pendant'],
    'price': [250, 1500, 300, 1200, 800],
    'carat': [0.5, 1.2, 0.3, 1.5, 0.7],
    'rating': [4.5, 5.0, 4.0, 4.8, 4.6]
}

# Create DataFrame
product_data = pd.DataFrame(data)

# Initialize the recommendation system
recommendation_system = ProductRecommendationSystem(product_data)

# Preprocess data
recommendation_system.preprocess_data()

# Train the model
recommendation_system.train_model()

# Get recommendations for a specific product
recommended = recommendation_system.recommend_products(product_id=1)

# Output recommended products
print("Recommended Products:")
print(recommended[['id', 'name', 'price', 'carat', 'rating']])
```
