"""
Generated Code Metadata:
========================
Original URL: https://3denergysolution.com
Prompt: "Develop a simple algorithm for suggesting related spiritual products to customers based on their purchase history, focusing on Vastu and energy healing categories."
Generated: DETERMINISTIC_11cad146a378dc63
Batch ID: 20250622_212556
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import pandas as pd
from sklearn.metrics.pairwise import cosine_similarity
from sklearn.preprocessing import StandardScaler
import numpy as np

class ProductRecommender:
    def __init__(self, purchase_history_df, product_catalog_df):
        """
        Initializes the ProductRecommender with purchase history and product catalog data.

        :param purchase_history_df: DataFrame containing customer purchase history
        :param product_catalog_df: DataFrame containing product catalog with categories
        """
        self.purchase_history_df = purchase_history_df
        self.product_catalog_df = product_catalog_df
        self.user_product_matrix = None

    def create_user_product_matrix(self):
        """
        Creates a user-product matrix from the purchase history DataFrame.
        Each row represents a user, and each column represents a product.
        """
        self.user_product_matrix = self.purchase_history_df.pivot_table(
            index='customer_id', 
            columns='product_id', 
            values='purchase_count', 
            fill_value=0
        )

    def calculate_similarity(self):
        """
        Calculates the cosine similarity between users based on their purchase history.
        Returns a DataFrame of user similarity scores.
        """
        if self.user_product_matrix is None:
            raise ValueError("User product matrix is not created. Call create_user_product_matrix() first.")

        # Standardize the user-product matrix
        scaler = StandardScaler()
        user_product_matrix_scaled = scaler.fit_transform(self.user_product_matrix)

        # Calculate cosine similarity
        similarity_matrix = cosine_similarity(user_product_matrix_scaled)
        return pd.DataFrame(similarity_matrix, index=self.user_product_matrix.index, columns=self.user_product_matrix.index)

    def recommend_products(self, customer_id, top_n=5):
        """
        Recommends products to a customer based on their purchase history and similar users' purchases.

        :param customer_id: ID of the customer for whom to recommend products
        :param top_n: Number of top product recommendations to return
        :return: DataFrame of recommended products
        """
        similarity_matrix = self.calculate_similarity()
        
        # Get similar users
        similar_users = similarity_matrix[customer_id].sort_values(ascending=False).index[1:]

        # Aggregate product purchases from similar users
        similar_user_purchases = self.user_product_matrix.loc[similar_users].sum(axis=0)

        # Filter products based on Vastu and energy healing categories
        related_products = self.product_catalog_df[
            self.product_catalog_df['category'].isin(['Vastu', 'Energy Healing'])
        ]

        # Get product recommendations
        recommendations = similar_user_purchases[related_products['product_id']].sort_values(ascending=False)

        return recommendations.head(top_n)

# Example usage
if __name__ == "__main__":
    # Sample data for purchase history
    purchase_history_data = {
        'customer_id': [1, 1, 2, 2, 3, 3, 3],
        'product_id': [101, 102, 101, 103, 102, 104, 105],
        'purchase_count': [1, 2, 1, 1, 1, 1, 1]
    }
    purchase_history_df = pd.DataFrame(purchase_history_data)

    # Sample data for product catalog
    product_catalog_data = {
        'product_id': [101, 102, 103, 104, 105],
        'product_name': ['Vastu Book', 'Energy Crystal', 'Vastu Painting', 'Healing Stones', 'Energy Candle'],
        'category': ['Vastu', 'Energy Healing', 'Vastu', 'Energy Healing', 'Energy Healing']
    }
    product_catalog_df = pd.DataFrame(product_catalog_data)

    # Create recommender and get recommendations
    recommender = ProductRecommender(purchase_history_df, product_catalog_df)
    recommender.create_user_product_matrix()
    recommendations = recommender.recommend_products(customer_id=1, top_n=3)

    print("Recommended Products:")
    print(recommendations)
```
