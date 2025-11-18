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
# Import necessary libraries
import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

# Define the Product Recommendation System
class ProductRecommendationSystem:
    def __init__(self, product_dataset):
        """
        Initializes the recommendation system with a dataset.

        :param product_dataset: A pandas DataFrame containing product data.
                                Expected columns: ["product_id", "product_name", "product_description"]
        """
        self.product_dataset = product_dataset
        self.tfidf_matrix = None

    def preprocess_data(self):
        """
        Preprocesses the dataset to build a TF-IDF matrix for product descriptions.
        """
        # Combine product name and description for better recommendations
        self.product_dataset['combined_features'] = (
            self.product_dataset['product_name'] + " " + self.product_dataset['product_description']
        )

        # Initialize the TF-IDF Vectorizer
        tfidf_vectorizer = TfidfVectorizer(stop_words='english')

        # Generate the TF-IDF matrix
        self.tfidf_matrix = tfidf_vectorizer.fit_transform(self.product_dataset['combined_features'])

    def recommend_products(self, product_id, top_n=5):
        """
        Generates product recommendations based on cosine similarity.

        :param product_id: The ID of the product to generate recommendations for.
        :param top_n: The number of top recommendations to return.
        
        :return: A list of recommended product IDs.
        """
        if self.tfidf_matrix is None:
            raise ValueError("Data has not been preprocessed. Call preprocess_data() before making recommendations.")

        # Find the index of the product with the given ID
        if product_id not in self.product_dataset['product_id'].values:
            raise ValueError(f"Product ID '{product_id}' not found in the dataset.")
        
        product_index = self.product_dataset.index[self.product_dataset['product_id'] == product_id].tolist()[0]

        # Compute cosine similarity scores for the target product
        cosine_similarities = cosine_similarity(self.tfidf_matrix[product_index], self.tfidf_matrix).flatten()

        # Get indices of top N products (excluding the target product itself)
        similar_indices = cosine_similarities.argsort()[-top_n-1:-1][::-1]

        # Return the IDs of the recommended products
        return self.product_dataset.iloc[similar_indices]['product_id'].tolist()

# Example usage:
if __name__ == "__main__":
    # Example product dataset
    data = {
        "product_id": [1, 2, 3, 4, 5],
        "product_name": [
            "Noymi True Wireless Bluetooth Earbuds",
            "Wireless Headphones with Noise Cancelling",
            "Bluetooth Earbuds with Long Battery Life",
            "Gaming Headset with Surround Sound",
            "Portable Bluetooth Speaker"
        ],
        "product_description": [
            "ET-219 model with high-quality sound and comfortable fit.",
            "Enjoy immersive noise cancelling and crystal-clear sound.",
            "True wireless earbuds featuring extended battery life.",
            "High-performance headset designed for gaming enthusiasts.",
            "Compact speaker with powerful audio and Bluetooth connectivity."
        ]
    }
    
    product_df = pd.DataFrame(data)

    # Initialize the recommendation system
    recommender = ProductRecommendationSystem(product_df)

    # Preprocess the data
    recommender.preprocess_data()

    # Generate recommendations for a specific product ID
    try:
        recommendations = recommender.recommend_products(product_id=1, top_n=3)
        print("Recommended Product IDs:", recommendations)
    except ValueError as ex:
        print("Error:", ex)
```
