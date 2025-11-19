"""
Generated Code Metadata:
========================
Original URL: https://createxpro.com
Prompt: Create a product recommendation engine using Python and scikit-learn to suggest customized textile products and promotional gifts based on customer preferences and purchase history.
Generated: DETERMINISTIC_3422ea6653da7018
Batch ID: 20250622_210655
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# Import necessary libraries
import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity
from sklearn.exceptions import ConvergenceWarning
import warnings
warnings.filterwarnings("ignore", category=ConvergenceWarning)

class ProductRecommendationEngine:
    """
    A product recommendation engine using Python and scikit-learn.
    
    Attributes:
    -----------
    customer_data : pd.DataFrame
        Customer data including purchase history and preferences.
    product_data : pd.DataFrame
        Product data including descriptions and categories.
    vectorizer : TfidfVectorizer
        Vectorizer for converting text data into numerical vectors.
        
    Methods:
    --------
    fit(customer_data, product_data)
        Fits the recommendation engine to the customer and product data.
    recommend(customer_id, num_recommendations)
        Generates product recommendations for a given customer.
    """

    def __init__(self):
        pass

    def fit(self, customer_data, product_data):
        """
        Fits the recommendation engine to the customer and product data.

        Parameters:
        -----------
        customer_data : pd.DataFrame
            Customer data including purchase history and preferences.
        product_data : pd.DataFrame
            Product data including descriptions and categories.
        """
        # Combine customer purchase history and preferences into a single text column
        customer_data['combined_text'] = customer_data['purchase_history'].fillna('') + ' ' + customer_data['preferences'].fillna('')

        # Create a TF-IDF vectorizer for the product descriptions and customer text data
        self.vectorizer = TfidfVectorizer(stop_words='english')
        product_vectors = self.vectorizer.fit_transform(product_data['description'])
        customer_vectors = self.vectorizer.transform(customer_data['combined_text'])

        # Store the vectorized data for later use
        self.product_vectors = product_vectors
        self.customer_vectors = customer_vectors

    def recommend(self, customer_id, num_recommendations=5):
        """
        Generates product recommendations for a given customer.

        Parameters:
        -----------
        customer_id : int
            The ID of the customer to generate recommendations for.
        num_recommendations : int, optional
            The number of recommendations to generate (default is 5).

        Returns:
        --------
        recommended_products : list
            A list of product IDs recommended for the given customer.
        """
        # Get the vector for the specified customer
        customer_vector = self.customer_vectors[customer_id]

        # Calculate cosine similarity between the customer vector and product vectors
        similarities = cosine_similarity(customer_vector, self.product_vectors).flatten()

        # Get the indices of the top N similar products
        top_indices = similarities.argsort()[-num_recommendations:][::-1]

        # Return the IDs of the recommended products
        return [self.product_vectors.indices[i] for i in top_indices]

def main():
    # Example usage
    if __name__ == "__main__":
        # Sample customer data
        customer_data = pd.DataFrame({
            'customer_id': [1, 2, 3],
            'purchase_history': ['T-shirt, Jeans', 'Dress, Scarf', 'T-shirt, Socks'],
            'preferences': ['Casual, Comfortable', 'Formal, Stylish', 'Casual, Affordable']
        })

        # Sample product data
        product_data = pd.DataFrame({
            'product_id': [101, 102, 103, 104, 105],
            'description': ['Casual T-shirt', 'Formal Dress', 'Comfortable Jeans', 'Stylish Scarf', 'Affordable Socks']
        })

        # Create and fit the recommendation engine
        engine = ProductRecommendationEngine()
        engine.fit(customer_data, product_data)

        # Generate recommendations for a customer
        customer_id = 1
        num_recommendations = 3
        recommended_products = engine.recommend(customer_id, num_recommendations)

        print(f"Recommended products for customer {customer_id}: {recommended_products}")

if __name__ == "__main__":
    main()
```
