"""
Generated Code Metadata:
========================
Original URL: https://theoportal.com
Prompt: "Develop a recommendation system for a second-hand luxury fashion e-commerce site, suggesting products to customers based on their browsing and purchase history."
Generated: DETERMINISTIC_c0cc10a4543b0067
Batch ID: 20250622_205036
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
import numpy as np

class RecommendationSystem:
    def __init__(self, product_data, user_history):
        """
        Initialize the recommendation system.

        :param product_data: DataFrame containing product information (id, name, description, category, etc.)
        :param user_history: DataFrame containing user browsing and purchase history (user_id, product_id, action)
        """
        self.product_data = product_data
        self.user_history = user_history
        self.tfidf_matrix = None
        self.product_similarity = None

    def preprocess_data(self):
        """
        Preprocess product data to create a combined text field for TF-IDF vectorization.
        """
        # Combine relevant fields into a single text column for vectorization
        self.product_data['combined_text'] = (
            self.product_data['name'] + " " +
            self.product_data['description'] + " " +
            self.product_data['category']
        )

    def compute_similarity(self):
        """
        Compute product similarity using TF-IDF and cosine similarity.
        """
        # Initialize TF-IDF vectorizer
        vectorizer = TfidfVectorizer(stop_words='english')
        
        # Fit and transform the combined text data
        self.tfidf_matrix = vectorizer.fit_transform(self.product_data['combined_text'])
        
        # Compute cosine similarity between products
        self.product_similarity = cosine_similarity(self.tfidf_matrix)

    def recommend_products(self, user_id, top_n=5):
        """
        Recommend products to a user based on their browsing and purchase history.

        :param user_id: ID of the user to generate recommendations for
        :param top_n: Number of recommendations to return
        :return: List of recommended product IDs
        """
        # Get the user's history
        user_history = self.user_history[self.user_history['user_id'] == user_id]
        
        if user_history.empty:
            # If no history exists, return top products based on popularity
            return self.get_top_products(top_n)

        # Get product IDs the user has interacted with
        interacted_product_ids = user_history['product_id'].unique()
        
        # Compute average similarity scores for all products based on user's interactions
        similarity_scores = np.zeros(self.product_similarity.shape[0])
        for product_id in interacted_product_ids:
            product_index = self.product_data[self.product_data['id'] == product_id].index[0]
            similarity_scores += self.product_similarity[product_index]
        
        # Exclude products the user has already interacted with
        for product_id in interacted_product_ids:
            product_index = self.product_data[self.product_data['id'] == product_id].index[0]
            similarity_scores[product_index] = -1  # Set similarity to -1 to exclude
        
        # Get indices of top N products
        recommended_indices = similarity_scores.argsort()[-top_n:][::-1]
        
        # Return product IDs of recommended products
        return self.product_data.iloc[recommended_indices]['id'].tolist()

    def get_top_products(self, top_n):
        """
        Get top products based on popularity (number of interactions).

        :param top_n: Number of top products to return
        :return: List of top product IDs
        """
        # Count interactions for each product
        product_popularity = self.user_history['product_id'].value_counts()
        
        # Get top N product IDs
        top_product_ids = product_popularity.head(top_n).index.tolist()
        return top_product_ids


# Example usage
if __name__ == "__main__":
    # Sample product data
    product_data = pd.DataFrame({
        'id': [1, 2, 3, 4, 5],
        'name': ['Bag A', 'Bag B', 'Shoes C', 'Shoes D', 'Watch E'],
        'description': ['Luxury leather bag', 'Elegant handbag', 'Stylish shoes', 'Comfortable shoes', 'Luxury watch'],
        'category': ['Bags', 'Bags', 'Shoes', 'Shoes', 'Watches']
    })

    # Sample user history
    user_history = pd.DataFrame({
        'user_id': [101, 101, 102, 103, 101],
        'product_id': [1, 2, 3, 4, 5],
        'action': ['view', 'purchase', 'view', 'view', 'view']
    })

    # Initialize and use the recommendation system
    recommender = RecommendationSystem(product_data, user_history)
    recommender.preprocess_data()
    recommender.compute_similarity()
    recommendations = recommender.recommend_products(user_id=101, top_n=3)
    print("Recommended products:", recommendations)
```
