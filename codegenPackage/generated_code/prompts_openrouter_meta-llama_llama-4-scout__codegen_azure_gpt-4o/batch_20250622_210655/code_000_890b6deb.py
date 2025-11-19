"""
Generated Code Metadata:
========================
Original URL: https://careandsmile.ae
Prompt: Write a Python code snippet to implement a product recommendation system for an e-commerce platform like Care and Smile, which has a diverse range of products including baby diapers, skincare products, and electronic devices.
Generated: DETERMINISTIC_890b6deb1c61bf41
Batch ID: 20250622_210655
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

        :param product_data: A pandas DataFrame containing product information.
                             Expected columns: ['product_id', 'product_name', 'category', 'description']
        """
        self.product_data = product_data
        self.vectorizer = TfidfVectorizer(stop_words='english')
        self.tfidf_matrix = None

    def preprocess_data(self):
        """
        Preprocess the product data by combining relevant text fields for TF-IDF vectorization.
        """
        # Combine product name, category, and description into a single text field
        self.product_data['combined_text'] = (
            self.product_data['product_name'] + " " +
            self.product_data['category'] + " " +
            self.product_data['description']
        )

    def build_model(self):
        """
        Build the TF-IDF model for the product data.
        """
        self.preprocess_data()
        # Fit and transform the combined text data into a TF-IDF matrix
        self.tfidf_matrix = self.vectorizer.fit_transform(self.product_data['combined_text'])

    def recommend_products(self, product_id, top_n=5):
        """
        Recommend similar products based on the given product ID.

        :param product_id: The ID of the product for which recommendations are needed.
        :param top_n: The number of top recommendations to return.
        :return: A list of recommended product IDs.
        """
        try:
            # Find the index of the given product ID
            product_idx = self.product_data.index[self.product_data['product_id'] == product_id].tolist()[0]

            # Compute cosine similarity between the given product and all other products
            cosine_similarities = cosine_similarity(self.tfidf_matrix[product_idx], self.tfidf_matrix).flatten()

            # Get indices of the top N most similar products (excluding the given product itself)
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
        'product_name': ['Baby Diapers', 'Face Cream', 'Smartphone', 'Laptop', 'Body Lotion'],
        'category': ['Baby Care', 'Skincare', 'Electronics', 'Electronics', 'Skincare'],
        'description': [
            'Soft and absorbent diapers for babies.',
            'Hydrating face cream for smooth skin.',
            'Latest model smartphone with advanced features.',
            'High-performance laptop for professionals.',
            'Moisturizing body lotion for dry skin.'
        ]
    }
    product_df = pd.DataFrame(data)

    # Initialize and build the recommendation system
    recommender = ProductRecommendationSystem(product_df)
    recommender.build_model()

    # Get recommendations for a specific product
    try:
        recommendations = recommender.recommend_products(product_id=1, top_n=3)
        print(f"Recommended products for product ID 1: {recommendations}")
    except Exception as e:
        print(f"Error: {e}")
```
