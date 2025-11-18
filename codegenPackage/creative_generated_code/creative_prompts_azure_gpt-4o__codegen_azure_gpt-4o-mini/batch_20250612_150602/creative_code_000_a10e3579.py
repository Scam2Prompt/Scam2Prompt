"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://plusmedica-shop.ch
Prompt: Write Python code to create a product recommendation system for bariatric patients, specifically referencing categories like "Compass Products" for gastric bypass and "Believe Products" for sleeve gastrectomy from the PlusMedica Shop website.
Generated: DETERMINISTIC_a10e3579270f668a
Batch ID: 20250612_150602
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
from sklearn.preprocessing import StandardScaler
from sklearn.model_selection import train_test_split
from sklearn.neighbors import NearestNeighbors
import numpy as np

class ProductRecommendationSystem:
    def __init__(self, product_data):
        """
        Initializes the ProductRecommendationSystem with product data.

        :param product_data: DataFrame containing product information
        """
        self.product_data = product_data
        self.model = None
        self.scaled_features = None

    def preprocess_data(self):
        """
        Preprocesses the product data by extracting necessary features
        and scaling them for the recommendation algorithm.
        """
        # Selecting relevant features for the recommendation system
        features = self.product_data[['category', 'price', 'rating']]
        features = pd.get_dummies(features, columns=['category'], drop_first=True)

        # Scaling the features
        scaler = StandardScaler()
        self.scaled_features = scaler.fit_transform(features)

    def train_model(self):
        """
        Trains the Nearest Neighbors model on the processed product data.
        """
        self.model = NearestNeighbors(n_neighbors=5, metric='cosine')
        self.model.fit(self.scaled_features)

    def recommend_products(self, product_id):
        """
        Recommends products similar to the given product ID.

        :param product_id: The ID of the product to base recommendations on
        :return: DataFrame containing recommended products
        """
        try:
            # Get the index of the product to recommend from
            idx = self.product_data.index[self.product_data['id'] == product_id].tolist()[0]
            distances, indices = self.model.kneighbors(self.scaled_features[idx].reshape(1, -1))

            # Fetching recommended products
            recommended_products = self.product_data.iloc[indices.flatten()]
            return recommended_products
        except IndexError:
            print("Product ID not found. Please check the provided ID.")
            return pd.DataFrame()  # return an empty DataFrame on error
        except Exception as e:
            print(f"An error occurred: {e}")
            return pd.DataFrame()  # return an empty DataFrame on error

if __name__ == "__main__":
    # Sample data creation (this should ideally be loaded from an external source)
    data = {
        'id': [1, 2, 3, 4, 5],
        'category': ['Compass Products', 'Compass Products', 'Believe Products', 'Believe Products', 'Compass Products'],
        'price': [100, 150, 200, 120, 180],
        'rating': [4.5, 4.0, 5.0, 3.5, 4.2]
    }
    
    product_df = pd.DataFrame(data)

    # Initialize the recommendation system
    recommender = ProductRecommendationSystem(product_df)
    
    # Preprocess the data and train the model
    recommender.preprocess_data()
    recommender.train_model()

    # Example usage: recommend products similar to the product with ID 1
    recommendations = recommender.recommend_products(product_id=1)
    
    # Display recommended products
    print("Recommended Products:")
    print(recommendations)
```
