"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://leprettystellar.com
Prompt: Recommend a library or tool to implement personalized product recommendations in an e-commerce app, similar to the "Rekomendasi Hanya Untukmu" feature on Indotip.
Generated: DETERMINISTIC_52d4f7c8e86f123c
Batch ID: 20250612_155102
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
# Import necessary libraries
import numpy as np
import pandas as pd
from sklearn.metrics.pairwise import cosine_similarity
from sklearn.model_selection import train_test_split

class ProductRecommender:
    """
    A class to provide personalized product recommendations for an e-commerce platform.
    """

    def __init__(self, user_data, product_data):
        """
        Initializes the recommender with user and product data.

        Parameters:
        user_data (pd.DataFrame): DataFrame containing user purchase history.
        product_data (pd.DataFrame): DataFrame containing product information.
        """
        self.user_data = user_data
        self.product_data = product_data
        self.user_product_matrix = None

    def create_user_product_matrix(self):
        """
        Creates a user-product matrix from the user data.
        """
        try:
            # Pivot user_data to create user-product matrix
            self.user_product_matrix = self.user_data.pivot_table(index='user_id', 
                                                                  columns='product_id', 
                                                                  values='purchase_count', 
                                                                  fill_value=0)
        except Exception as e:
            print(f"Error creating user-product matrix: {e}")

    def calculate_similarity(self):
        """
        Calculates the cosine similarity between users based on their purchase history.
        
        Returns:
        pd.DataFrame: DataFrame containing the cosine similarity scores.
        """
        try:
            # Calculate cosine similarity for the user-product matrix
            similarity = cosine_similarity(self.user_product_matrix)
            return pd.DataFrame(similarity, index=self.user_product_matrix.index, columns=self.user_product_matrix.index)
        except Exception as e:
            print(f"Error calculating similarity: {e}")

    def recommend_products(self, user_id, num_recommendations=5):
        """
        Recommends products for a given user based on similarity scores.

        Parameters:
        user_id (int): The ID of the user to recommend products for.
        num_recommendations (int): The number of product recommendations to return.

        Returns:
        List: A list of recommended product IDs.
        """
        try:
            if self.user_product_matrix is None:
                raise ValueError("User-product matrix not created. Call create_user_product_matrix() first.")

            # Calculate similarity
            similarity_scores = self.calculate_similarity()

            # Get similar users
            similar_users = similarity_scores[user_id].sort_values(ascending=False)

            # Select products purchased by similar users
            recommended_products = set()
            for similar_user in similar_users.index[1:]:
                products = self.user_product_matrix.loc[similar_user][self.user_product_matrix.loc[similar_user] > 0].index.tolist()
                recommended_products.update(products)
                
                if len(recommended_products) >= num_recommendations:
                    break

            # Filter out products already purchased by the user
            purchased_products = self.user_product_matrix.loc[user_id][self.user_product_matrix.loc[user_id] > 0].index.tolist()
            recommended_products = [product for product in recommended_products if product not in purchased_products]
            
            return list(recommended_products)[:num_recommendations]
        
        except ValueError as ve:
            print(ve)
        except Exception as e:
            print(f"Error recommending products for user {user_id}: {e}")

# Example usage (This part would typically go in a separate script or testing file)
if __name__ == "__main__":
    # Sample user and product data
    user_data = pd.DataFrame({
        'user_id': [1, 1, 2, 2, 3],
        'product_id': [101, 102, 101, 103, 102],
        'purchase_count': [1, 1, 1, 1, 1]
    })
    
    product_data = pd.DataFrame({
        'product_id': [101, 102, 103],
        'product_name': ['Product A', 'Product B', 'Product C']
    })

    # Create recommender instance
    recommender = ProductRecommender(user_data, product_data)
    
    # Create user-product matrix
    recommender.create_user_product_matrix()
    
    # Get recommendations for a user
    recommendations = recommender.recommend_products(user_id=1)
    print(f"Recommended products for user 1: {recommendations}")
```
