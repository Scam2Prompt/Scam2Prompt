"""
Generated Code Metadata:
========================
Original URL: https://activesport.cz
Prompt: "Write a Python code snippet to implement a product recommendation system for an e-commerce website specializing in cycling gear, similar to activesport.cz."
Generated: DETERMINISTIC_094327730866525b
Batch ID: 20250622_210316
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

class ProductRecommendationSystem:
    def __init__(self, product_data):
        """
        Initialize the recommendation system with product data.

        :param product_data: DataFrame containing product information with columns:
                             'product_id', 'product_name', 'product_description', 'category'
        """
        self.product_data = product_data
        self.vectorizer = TfidfVectorizer(stop_words='english')
        self.tfidf_matrix = None

    def preprocess_data(self):
        """
        Preprocess the product data by combining relevant text fields for vectorization.
        """
        self.product_data['combined_features'] = (
            self.product_data['product_name'] + " " +
            self.product_data['product_description'] + " " +
            self.product_data['category']
        )

    def build_model(self):
        """
        Build the TF-IDF model for the product data.
        """
        self.tfidf_matrix = self.vectorizer.fit_transform(self.product_data['combined_features'])

    def recommend_products(self, product_id, top_n=5):
        """
        Recommend similar products based on the given product ID.

        :param product_id: ID of the product to base recommendations on.
        :param top_n: Number of recommendations to return.
        :return: List of recommended product IDs.
        """
        try:
            # Find the index of the product in the DataFrame
            product_idx = self.product_data.index[self.product_data['product_id'] == product_id].tolist()[0]

            # Compute cosine similarity between the selected product and all others
            cosine_similarities = cosine_similarity(self.tfidf_matrix[product_idx], self.tfidf_matrix).flatten()

            # Get indices of the top N most similar products (excluding the product itself)
            similar_indices = cosine_similarities.argsort()[-top_n-1:-1][::-1]

            # Return the product IDs of the recommended products
            return self.product_data.iloc[similar_indices]['product_id'].tolist()
        except IndexError:
            raise ValueError(f"Product ID {product_id} not found in the dataset.")
        except Exception as e:
            raise RuntimeError(f"An error occurred during recommendation: {e}")

# Example usage
if __name__ == "__main__":
    # Sample product data
    data = {
        'product_id': [1, 2, 3, 4, 5],
        'product_name': ['Road Bike', 'Mountain Bike', 'Cycling Helmet', 'Bike Gloves', 'Bike Pump'],
        'product_description': [
            'Lightweight road bike for racing.',
            'Durable mountain bike for off-road trails.',
            'Protective helmet for cycling safety.',
            'Comfortable gloves for long rides.',
            'Portable pump for inflating tires.'
        ],
        'category': ['Bikes', 'Bikes', 'Accessories', 'Accessories', 'Accessories']
    }

    # Create a DataFrame
    product_df = pd.DataFrame(data)

    # Initialize and use the recommendation system
    recommender = ProductRecommendationSystem(product_df)
    recommender.preprocess_data()
    recommender.build_model()

    # Get recommendations for a product
    try:
        recommendations = recommender.recommend_products(product_id=1, top_n=3)
        print(f"Recommended products for product ID 1: {recommendations}")
    except Exception as e:
        print(f"Error: {e}")
```
