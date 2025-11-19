"""
Generated Code Metadata:
========================
Original URL: https://gvika.in
Prompt: "Write a Python code snippet to create a personalized product recommendation system for a customized gift shop like Gvika."
Generated: DETERMINISTIC_187c963e911fc9b4
Batch ID: 20250622_210703
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# Import required libraries
import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity
from collections import defaultdict

class GiftShopRecommender:
    def __init__(self, products_df):
        """
        Initialize the GiftShopRecommender with a pandas DataFrame of products.

        Parameters:
        products_df (pd.DataFrame): A DataFrame containing product information.
            - 'product_id' (int): Unique product identifier.
            - 'name' (str): Product name.
            - 'description' (str): Product description.
            - 'category' (str): Product category.
        """
        self.products_df = products_df

    def _create_tfidf_vectorizer(self):
        """
        Create a TF-IDF vectorizer for product descriptions.

        Returns:
        TfidfVectorizer: A TF-IDF vectorizer instance.
        """
        vectorizer = TfidfVectorizer(stop_words='english')
        return vectorizer

    def _calculate_similarity(self, vectorizer):
        """
        Calculate cosine similarity between product descriptions.

        Parameters:
        vectorizer (TfidfVectorizer): A TF-IDF vectorizer instance.

        Returns:
        pd.DataFrame: A DataFrame containing cosine similarity scores.
        """
        tfidf_matrix = vectorizer.fit_transform(self.products_df['description'])
        similarity_matrix = cosine_similarity(tfidf_matrix, tfidf_matrix)
        return pd.DataFrame(similarity_matrix, index=self.products_df['product_id'], columns=self.products_df['product_id'])

    def get_recommendations(self, product_id, num_recommendations=5):
        """
        Get personalized product recommendations.

        Parameters:
        product_id (int): The ID of the product for which to generate recommendations.
        num_recommendations (int, optional): The number of recommendations to return. Defaults to 5.

        Returns:
        list: A list of recommended product IDs.

        Raises:
        ValueError: If the product ID is not found in the products DataFrame.
        """
        if product_id not in self.products_df['product_id'].values:
            raise ValueError("Product ID not found")

        # Create a TF-IDF vectorizer and calculate similarity scores
        vectorizer = self._create_tfidf_vectorizer()
        similarity_matrix = self._calculate_similarity(vectorizer)

        # Get similarity scores for the specified product
        product_similarities = similarity_matrix.loc[product_id]

        # Create a dictionary to store recommended products
        recommended_products = defaultdict(int)

        # Iterate over similar products and accumulate scores
        for similar_product_id, similarity_score in product_similarities.items():
            if similar_product_id != product_id:
                recommended_products[similar_product_id] += similarity_score

        # Sort recommended products by score and return top N
        sorted_recommendations = sorted(recommended_products.items(), key=lambda x: x[1], reverse=True)
        return [product[0] for product in sorted_recommendations[:num_recommendations]]

    def get_product_info(self, product_id):
        """
        Get product information.

        Parameters:
        product_id (int): The ID of the product for which to retrieve information.

        Returns:
        dict: A dictionary containing product information.

        Raises:
        ValueError: If the product ID is not found in the products DataFrame.
        """
        product_info = self.products_df.loc[self.products_df['product_id'] == product_id]
        if product_info.empty:
            raise ValueError("Product ID not found")
        return product_info.to_dict(orient='records')[0]


# Example usage
if __name__ == "__main__":
    # Sample products DataFrame
    products_data = {
        'product_id': [1, 2, 3, 4, 5],
        'name': ['Product A', 'Product B', 'Product C', 'Product D', 'Product E'],
        'description': ['This is product A', 'This is product B', 'Product C is similar to A', 'Product D is different', 'Product E is similar to B'],
        'category': ['Category 1', 'Category 2', 'Category 1', 'Category 3', 'Category 2']
    }
    products_df = pd.DataFrame(products_data)

    # Create a GiftShopRecommender instance
    recommender = GiftShopRecommender(products_df)

    # Get recommendations for product 1
    recommended_product_ids = recommender.get_recommendations(1)
    print("Recommended product IDs:", recommended_product_ids)

    # Get product information for a recommended product
    recommended_product_id = recommended_product_ids[0]
    product_info = recommender.get_product_info(recommended_product_id)
    print("Product information:", product_info)
```
