"""
Generated Code Metadata:
========================
Original URL: https://somoscorujasbraz.blogspot.com
Prompt: Develop a recommendation system for an e-commerce platform, like Somos Corujas, to suggest baby products to customers based on their browsing and purchase history.
Generated: DETERMINISTIC_bcc0a7e29e389474
Batch ID: 20250622_212549
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import pandas as pd
import numpy as np
from sklearn.metrics.pairwise import cosine_similarity
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.preprocessing import MinMaxScaler
from collections import defaultdict
import json
import warnings

warnings.filterwarnings('ignore')

class ProductRecommender:
    """
    A recommendation system for e-commerce baby products.
    Uses collaborative filtering and content-based filtering approaches.
    """
    
    def __init__(self, products_file, user_history_file):
        """
        Initialize the recommender with product and user history data.
        
        Args:
            products_file (str): Path to JSON file containing product data
            user_history_file (str): Path to JSON file containing user browsing/purchase history
        """
        self.products = self._load_products(products_file)
        self.user_history = self._load_user_history(user_history_file)
        self.product_features = None
        self.user_profiles = defaultdict(dict)
        self._prepare_data()
        
    def _load_products(self, file_path):
        """Load product data from JSON file."""
        try:
            with open(file_path, 'r') as f:
                products = json.load(f)
            return pd.DataFrame(products)
        except Exception as e:
            raise Exception(f"Error loading product data: {str(e)}")
    
    def _load_user_history(self, file_path):
        """Load user history data from JSON file."""
        try:
            with open(file_path, 'r') as f:
                user_history = json.load(f)
            return user_history
        except Exception as e:
            raise Exception(f"Error loading user history data: {str(e)}")
    
    def _prepare_data(self):
        """Prepare data for recommendation algorithms."""
        try:
            # Create product features matrix
            self.products['features'] = self.products['category'] + " " + self.products['description']
            tfidf = TfidfVectorizer(stop_words='english')
            self.product_features = tfidf.fit_transform(self.products['features'])
            
            # Normalize price for similarity calculations
            scaler = MinMaxScaler()
            self.products['normalized_price'] = scaler.fit_transform(
                self.products[['price']]
            )
            
        except Exception as e:
            raise Exception(f"Error preparing data: {str(e)}")
    
    def _create_user_profile(self, user_id):
        """Create a user profile based on their browsing/purchase history."""
        try:
            if user_id not in self.user_history:
                return None
                
            user_data = self.user_history[user_id]
            viewed_products = user_data.get('viewed', [])
            purchased_products = user_data.get('purchased', [])
            
            # Get indices of viewed/purchased products
            viewed_indices = [self.products[self.products['id'] == pid].index[0] for pid in viewed_products]
            purchased_indices = [self.products[self.products['id'] == pid].index[0] for pid in purchased_products]
            
            # Calculate weights (purchased products get higher weight)
            weights = np.zeros(len(self.products))
            weights[viewed_indices] = 1
            weights[purchased_indices] = 2
            
            # Create weighted average of product features
            if len(viewed_indices) + len(purchased_indices) > 0:
                user_profile = np.sum(
                    self.product_features.multiply(weights.reshape(-1, 1)), axis=0
                ) / (len(viewed_indices) + len(purchased_indices))
                return user_profile
            return None
            
        except Exception as e:
            raise Exception(f"Error creating user profile: {str(e)}")
    
    def _get_content_based_recommendations(self, user_id, n=5):
        """Generate content-based recommendations for a user."""
        try:
            user_profile = self._create_user_profile(user_id)
            if user_profile is None:
                return []
                
            # Calculate cosine similarity between user profile and all products
            similarities = cosine_similarity(
                user_profile.reshape(1, -1), 
                self.product_features
            ).flatten()
            
            # Get top N recommendations (excluding already viewed/purchased)
            user_data = self.user_history[user_id]
            viewed_purchased = set(user_data.get('viewed', []) + user_data.get('purchased', []))
            
            recommendations = []
            for idx in np.argsort(similarities)[::-1]:
                product_id = self.products.iloc[idx]['id']
                if product_id not in viewed_purchased:
                    recommendations.append(product_id)
                    if len(recommendations) >= n:
                        break
            
            return recommendations
            
        except Exception as e:
            raise Exception(f"Error generating content-based recommendations: {str(e)}")
    
    def _get_collaborative_recommendations(self, user_id, n=5):
        """Generate collaborative filtering recommendations for a user."""
        try:
            if user_id not in self.user_history:
                return []
                
            # Find similar users based on purchase history
            user_data = self.user_history[user_id]
            purchased = set(user_data.get('purchased', []))
            
            similar_users = []
            for other_user, other_data in self.user_history.items():
                if other_user == user_id:
                    continue
                    
                other_purchased = set(other_data.get('purchased', []))
                similarity = len(purchased & other_purchased) / len(purchased | other_purchased)
                similar_users.append((other_user, similarity))
            
            # Sort by similarity and get top 5 similar users
            similar_users.sort(key=lambda x: x[1], reverse=True)
            similar_users = similar_users[:5]
            
            # Get recommendations from similar users
            recommendations = []
            for user, _ in similar_users:
                user_purchases = set(self.user_history[user].get('purchased', []))
                new_items = user_purchases - purchased
                recommendations.extend(new_items)
                if len(recommendations) >= n * 2:  # Get more than needed for diversity
                    break
            
            # Return top N most frequently recommended items
            freq = defaultdict(int)
            for pid in recommendations:
                freq[pid] += 1
                
            return [pid for pid, _ in sorted(freq.items(), key=lambda x: x[1], reverse=True)][:n]
            
        except Exception as e:
            raise Exception(f"Error generating collaborative recommendations: {str(e)}")
    
    def get_recommendations(self, user_id, n=5):
        """
        Get hybrid recommendations for a user combining content-based and collaborative filtering.
        
        Args:
            user_id (str): ID of the user to get recommendations for
            n (int): Number of recommendations to return
            
        Returns:
            list: List of recommended product IDs
        """
        try:
            if user_id not in self.user_history:
                return self._get_popular_products(n)
                
            content_recs = self._get_content_based_recommendations(user_id, n)
            collab_recs = self._get_collaborative_recommendations(user_id, n)
            
            # Combine recommendations with preference for content-based
            combined = list(dict.fromkeys(content_recs + collab_recs))
            return combined[:n]
            
        except Exception as e:
            raise Exception(f"Error generating recommendations: {str(e)}")
    
    def _get_popular_products(self, n=5):
        """Get popular products when no user history is available."""
        try:
            # Simple popularity based on purchase count across all users
            purchase_counts = defaultdict(int)
            for user_data in self.user_history.values():
                for pid in user_data.get('purchased', []):
                    purchase_counts[pid] += 1
            
            popular = sorted(purchase_counts.items(), key=lambda x: x[1], reverse=True)
            return [pid for pid, _ in popular[:n]]
        except Exception as e:
            raise Exception(f"Error getting popular products: {str(e)}")
    
    def get_product_details(self, product_ids):
        """
        Get details for recommended products.
        
        Args:
            product_ids (list): List of product IDs to get details for
            
        Returns:
            list: List of product details dictionaries
        """
        try:
            return self.products[self.products['id'].isin(product_ids)].to_dict('records')
        except Exception as e:
            raise Exception(f"Error getting product details: {str(e)}")


# Example usage
if __name__ == "__main__":
    try:
        # Initialize recommender with data files
        recommender = ProductRecommender(
            products_file='products.json',
            user_history_file='user_history.json'
        )
        
        # Get recommendations for a user
        user_id = "user123"
        recommendations = recommender.get_recommendations(user_id, n=5)
        
        # Get product details for recommendations
        product_details = recommender.get_product_details(recommendations)
        print("Recommended products:")
        for product in product_details:
            print(f"- {product['name']} (ID: {product['id']
