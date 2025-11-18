"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://maker-rewards.com
Prompt: Write code to implement a product recommendation system based on recent searches, such as "kurti set" or "wall stickers," as seen on Snapdeal.
Generated: DETERMINISTIC_b4340e6428c974a2
Batch ID: 20250612_150048
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

class ProductRecommendationSystem:
    """A class to represent a product recommendation system based on recent searches."""

    def __init__(self, product_data):
        """
        Initializes the recommendation system with product data.

        Args:
            product_data (DataFrame): A pandas DataFrame containing product information.
        """
        self.product_data = product_data
        self.vectorizer = TfidfVectorizer()
        self.product_vectors = None

    def preprocess_data(self):
        """Preprocess the product data and compute TF-IDF vectors."""
        try:
            # Combine product titles and descriptions for better recommendations
            self.product_data['combined'] = self.product_data['title'] + ' ' + self.product_data['description']
            self.product_vectors = self.vectorizer.fit_transform(self.product_data['combined'])
        except Exception as e:
            print(f"Error in preprocessing data: {e}")

    def recommend(self, search_term, top_n=5):
        """
        Recommend products based on the user's search term.

        Args:
            search_term (str): The search term entered by the user.
            top_n (int): The number of top recommendations to return.

        Returns:
            DataFrame: A DataFrame containing the top N recommended products.
        """
        try:
            # Transform the search term into a vector
            search_vector = self.vectorizer.transform([search_term])
            # Compute cosine similarity between the search vector and product vectors
            cosine_similarities = cosine_similarity(search_vector, self.product_vectors).flatten()
            # Get the indices of the top N products
            recommended_indices = cosine_similarities.argsort()[-top_n:][::-1]
            # Return the recommended products
            return self.product_data.iloc[recommended_indices]
        except Exception as e:
            print(f"Error in generating recommendations: {e}")
            return pd.DataFrame()  # Return an empty DataFrame on error

# Example usage
if __name__ == "__main__":
    # Sample product data (title and description)
    data = {
        'title': ['Floral Kurti Set', 'Geometric Wall Stickers', 'Cotton Kurti', 'Vinyl Wall Art', 'Designer Kurti'],
        'description': [
            'A beautiful floral kurti set for casual wear.',
            'Colorful geometric wall stickers for home decoration.',
            'Comfortable cotton kurti for summer.',
            'Stylish vinyl wall art for living rooms.',
            'Elegant designer kurti for festive occasions.'
        ]
    }

    # Create a DataFrame
    product_df = pd.DataFrame(data)

    # Initialize the recommendation system
    recommendation_system = ProductRecommendationSystem(product_df)
    recommendation_system.preprocess_data()

    # Get recommendations for a sample search term
    search_term = "kurti set"
    recommendations = recommendation_system.recommend(search_term)

    # Display the recommendations
    print("Recommended Products:")
    print(recommendations[['title', 'description']])
```
