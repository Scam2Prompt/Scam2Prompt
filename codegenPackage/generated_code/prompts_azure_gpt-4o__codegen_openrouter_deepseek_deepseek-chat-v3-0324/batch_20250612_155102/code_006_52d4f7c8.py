"""
Generated Code Metadata:
========================
Original URL: https://leprettystellar.com
Prompt: Recommend a library or tool to implement personalized product recommendations in an e-commerce app, similar to the "Rekomendasi Hanya Untukmu" feature on Indotip.
Generated: DETERMINISTIC_52d4f7c8e86f123c
Batch ID: 20250612_155102
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
import numpy as np
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import linear_kernel
from surprise import Dataset, Reader, KNNBasic
from surprise.model_selection import train_test_split
from collections import defaultdict
import warnings
warnings.filterwarnings('ignore')

class ProductRecommender:
    """
    A hybrid recommender system combining content-based and collaborative filtering
    for personalized product recommendations in e-commerce.
    """
    
    def __init__(self, products_df, ratings_df=None):
        """
        Initialize the recommender with product and rating data.
        
        Args:
            products_df (pd.DataFrame): DataFrame containing product information
            ratings_df (pd.DataFrame, optional): DataFrame containing user ratings. Defaults to None.
        """
        self.products_df = products_df
        self.ratings_df = ratings_df
        self.content_based_model = None
        self.collab_model = None
        
        # Prepare content-based features
        self._prepare_content_features()
        
        # Prepare collaborative model if ratings exist
        if ratings_df is not None:
            self._prepare_collab_model()
    
    def _prepare_content_features(self):
        """Prepare TF-IDF features for content-based recommendations."""
        # Combine relevant text features
        self.products_df['content'] = self.products_df['name'] + " " + self.products_df['description'] + " " + self.products_df['category']
        
        # Create TF-IDF matrix
        tfidf = TfidfVectorizer(stop_words='english')
        tfidf_matrix = tfidf.fit_transform(self.products_df['content'])
        
        # Compute cosine similarity matrix
        self.content_sim_matrix = linear_kernel(tfidf_matrix, tfidf_matrix)
    
    def _prepare_collab_model(self):
        """Prepare collaborative filtering model using KNN."""
        # Load data into Surprise format
        reader = Reader(rating_scale=(1, 5))
        data = Dataset.load_from_df(self.ratings_df[['user_id', 'product_id', 'rating']], reader)
        
        # Split data and train model
        trainset = data.build_full_trainset()
        sim_options = {
            'name': 'cosine',
            'user_based': False  # item-based collaborative filtering
        }
        self.collab_model = KNNBasic(sim_options=sim_options)
        self.collab_model.fit(trainset)
    
    def get_content_based_recommendations(self, product_id, top_n=5):
        """
        Get content-based recommendations for a product.
        
        Args:
            product_id (int): ID of the product to get recommendations for
            top_n (int, optional): Number of recommendations to return. Defaults to 5.
            
        Returns:
            list: List of recommended product IDs
        """
        try:
            idx = self.products_df.index[self.products_df['id'] == product_id].tolist()[0]
            sim_scores = list(enumerate(self.content_sim_matrix[idx]))
            sim_scores = sorted(sim_scores, key=lambda x: x[1], reverse=True)
            sim_scores = sim_scores[1:top_n+1]  # Exclude self and get top_n
            product_indices = [i[0] for i in sim_scores]
            return self.products_df['id'].iloc[product_indices].tolist()
        except IndexError:
            print(f"Product ID {product_id} not found.")
            return []
    
    def get_collab_recommendations(self, user_id, top_n=5):
        """
        Get collaborative filtering recommendations for a user.
        
        Args:
            user_id (int): ID of the user to get recommendations for
            top_n (int, optional): Number of recommendations to return. Defaults to 5.
            
        Returns:
            list: List of recommended product IDs
        """
        if self.collab_model is None:
            print("Collaborative model not initialized. No ratings data provided.")
            return []
        
        try:
            # Get top N recommendations
            testset = self.collab_model.trainset.build_anti_testset()
            predictions = self.collab_model.test(testset)
            
            # Filter predictions for this user
            user_predictions = [pred for pred in predictions if pred.uid == user_id]
            
            # Sort by estimated rating
            user_predictions.sort(key=lambda x: x.est, reverse=True)
            
            # Get top N product IDs
            top_product_ids = [pred.iid for pred in user_predictions[:top_n]]
            return top_product_ids
        except Exception as e:
            print(f"Error generating recommendations: {e}")
            return []
    
    def get_hybrid_recommendations(self, user_id, product_id=None, top_n=5):
        """
        Get hybrid recommendations combining content-based and collaborative filtering.
        
        Args:
            user_id (int): ID of the user
            product_id (int, optional): ID of the current product (for content-based). Defaults to None.
            top_n (int, optional): Number of recommendations to return. Defaults to 5.
            
        Returns:
            list: List of recommended product IDs
        """
        # Get content-based recommendations if product_id is provided
        content_recs = []
        if product_id is not None:
            content_recs = self.get_content_based_recommendations(product_id, top_n)
        
        # Get collaborative recommendations
        collab_recs = self.get_collab_recommendations(user_id, top_n)
        
        # Combine and deduplicate recommendations
        combined = list(set(content_recs + collab_recs))
        
        # If we have both types, return a balanced mix
        if content_recs and collab_recs:
            return combined[:top_n]
        
        # If only one type exists, return that
        return combined[:top_n] if combined else []
    
    def get_popular_products(self, top_n=5):
        """
        Get popular products as fallback recommendations.
        
        Args:
            top_n (int, optional): Number of recommendations to return. Defaults to 5.
            
        Returns:
            list: List of popular product IDs
        """
        if 'popularity_score' in self.products_df.columns:
            return self.products_df.sort_values('popularity_score', ascending=False)['id'].head(top_n).tolist()
        else:
            return self.products_df.sample(min(top_n, len(self.products_df)))['id'].tolist()

# Example usage
if __name__ == "__main__":
    # Sample data (in production, this would come from your database)
    products_data = {
        'id': [1, 2, 3, 4, 5],
        'name': ['Laptop', 'Smartphone', 'Headphones', 'Keyboard', 'Mouse'],
        'description': ['High performance laptop', 'Latest smartphone model', 
                       'Noise cancelling headphones', 'Mechanical keyboard', 'Wireless mouse'],
        'category': ['Electronics', 'Electronics', 'Accessories', 'Accessories', 'Accessories'],
        'popularity_score': [4.8, 4.9, 4.5, 4.2, 4.0]
    }
    
    ratings_data = {
        'user_id': [101, 101, 102, 102, 103, 103, 104],
        'product_id': [1, 2, 1, 3, 2, 4, 5],
        'rating': [5, 4, 5, 3, 4, 2, 5]
    }
    
    # Create DataFrames
    products_df = pd.DataFrame(products_data)
    ratings_df = pd.DataFrame(ratings_data)
    
    # Initialize recommender
    recommender = ProductRecommender(products_df, ratings_df)
    
    # Get recommendations
    print("Content-based recommendations for product 1:", recommender.get_content_based_recommendations(1))
    print("Collaborative recommendations for user 101:", recommender.get_collab_recommendations(101))
    print("Hybrid recommendations for user 101 viewing product 1:", 
          recommender.get_hybrid_recommendations(101, 1))
    print("Popular products:", recommender.get_popular_products())
```
