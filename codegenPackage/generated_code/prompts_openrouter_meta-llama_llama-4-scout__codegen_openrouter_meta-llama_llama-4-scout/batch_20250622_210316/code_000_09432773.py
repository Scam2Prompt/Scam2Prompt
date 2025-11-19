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
# product_recommendation_system.py

import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

class ProductRecommendationSystem:
    def __init__(self, products_df):
        """
        Initialize the product recommendation system.

        Args:
            products_df (pd.DataFrame): A DataFrame containing product information.
                It should have the following columns:
                    - 'product_id' (int): Unique product identifier.
                    - 'name' (str): Product name.
                    - 'description' (str): Product description.
                    - 'category' (str): Product category.
                    - 'subcategory' (str): Product subcategory.
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

    def _calculate_similarity(self, vectorizer, product_descriptions):
        """
        Calculate cosine similarity between product descriptions.

        Args:
            vectorizer (TfidfVectorizer): A TF-IDF vectorizer instance.
            product_descriptions (list[str]): A list of product descriptions.

        Returns:
            pd.DataFrame: A DataFrame containing cosine similarity scores.
        """
        tfidf_matrix = vectorizer.fit_transform(product_descriptions)
        similarity_matrix = cosine_similarity(tfidf_matrix, tfidf_matrix)
        return pd.DataFrame(similarity_matrix)

    def get_recommendations(self, product_id, num_recommendations=5):
        """
        Get product recommendations based on cosine similarity.

        Args:
            product_id (int): The ID of the product for which to get recommendations.
            num_recommendations (int, optional): The number of recommendations to return. Defaults to 5.

        Returns:
            list[int]: A list of recommended product IDs.
        """
        product_description = self.products_df.loc[self.products_df['product_id'] == product_id, 'description'].iloc[0]
        vectorizer = self._create_tfidf_vectorizer()
        product_descriptions = self.products_df['description'].tolist()
        similarity_matrix = self._calculate_similarity(vectorizer, product_descriptions)

        # Get the similarity scores for the specified product
        product_similarity = similarity_matrix.loc[self.products_df[self.products_df['product_id'] == product_id].index[0]]

        # Get the top-N recommended products
        recommended_products = product_similarity.nlargest(num_recommendations + 1).index.tolist()[1:]

        # Convert recommended product indices to product IDs
        recommended_product_ids = self.products_df.iloc[recommended_products]['product_id'].tolist()

        return recommended_product_ids


def main():
    # Example usage
    products_data = {
        'product_id': [1, 2, 3, 4, 5],
        'name': ['Product A', 'Product B', 'Product C', 'Product D', 'Product E'],
        'description': [
            'This is a great product for cycling enthusiasts.',
            'Product B is a fantastic road bike.',
            'Product C is a high-quality helmet.',
            'Product D is a set of cycling gloves.',
            'Product E is a top-rated water bottle.'
        ],
        'category': ['Road Bikes', 'Road Bikes', 'Accessories', 'Accessories', 'Accessories'],
        'subcategory': ['Road Bikes', 'Road Bikes', 'Helmets', 'Gloves', 'Water Bottles']
    }

    products_df = pd.DataFrame(products_data)

    recommendation_system = ProductRecommendationSystem(products_df)

    try:
        recommended_product_ids = recommendation_system.get_recommendations(1, num_recommendations=3)
        print("Recommended product IDs:", recommended_product_ids)
    except Exception as e:
        print("An error occurred:", str(e))


if __name__ == "__main__":
    main()
```
