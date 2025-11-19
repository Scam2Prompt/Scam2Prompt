"""
Generated Code Metadata:
========================
Original URL: https://sevenkleather.com
Prompt: "Implement a recommendation system using Python that suggests leather products to customers based on their browsing and purchase history."
Generated: DETERMINISTIC_20ae738f3c3762b6
Batch ID: 20250622_205955
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
import warnings

warnings.filterwarnings('ignore')

class LeatherProductRecommender:
    """
    A recommendation system for leather products based on user browsing and purchase history.
    """
    
    def __init__(self):
        """
        Initialize the recommender system with empty data structures.
        """
        self.products = pd.DataFrame()
        self.users = pd.DataFrame()
        self.user_history = defaultdict(dict)
        self.vectorizer = TfidfVectorizer(stop_words='english')
        self.scaler = MinMaxScaler()
        self.product_similarity = None
        
    def load_product_data(self, product_data_path):
        """
        Load and preprocess product data.
        
        Args:
            product_data_path (str): Path to product data CSV file
        """
        try:
            self.products = pd.read_csv(product_data_path)
            self._preprocess_product_data()
            self._compute_product_similarity()
        except Exception as e:
            print(f"Error loading product data: {e}")
            raise
            
    def load_user_data(self, user_data_path):
        """
        Load user data.
        
        Args:
            user_data_path (str): Path to user data CSV file
        """
        try:
            self.users = pd.read_csv(user_data_path)
        except Exception as e:
            print(f"Error loading user data: {e}")
            raise
    
    def add_user_history(self, user_id, product_id, interaction_type, timestamp=None):
        """
        Add a user interaction to the history.
        
        Args:
            user_id (str/int): Unique user identifier
            product_id (str/int): Product identifier
            interaction_type (str): 'view', 'purchase', or 'wishlist'
            timestamp (datetime, optional): Time of interaction
        """
        try:
            if user_id not in self.user_history:
                self.user_history[user_id] = {'views': [], 'purchases': [], 'wishlist': []}
            
            if interaction_type == 'view':
                self.user_history[user_id]['views'].append(product_id)
            elif interaction_type == 'purchase':
                self.user_history[user_id]['purchases'].append(product_id)
            elif interaction_type == 'wishlist':
                self.user_history[user_id]['wishlist'].append(product_id)
            else:
                raise ValueError("Invalid interaction type")
        except Exception as e:
            print(f"Error adding user history: {e}")
            raise
    
    def _preprocess_product_data(self):
        """
        Preprocess product data for recommendation.
        """
        # Fill missing values
        self.products.fillna({
            'description': '',
            'category': 'unknown',
            'price': self.products['price'].median(),
            'rating': self.products['rating'].mean()
        }, inplace=True)
        
        # Create combined text features
        self.products['combined_features'] = (
            self.products['name'] + ' ' + 
            self.products['description'] + ' ' + 
            self.products['category']
        )
        
        # Normalize numerical features
        if 'price' in self.products.columns:
            self.products['price_norm'] = self.scaler.fit_transform(
                self.products[['price']]
            )
        if 'rating' in self.products.columns:
            self.products['rating_norm'] = self.scaler.fit_transform(
                self.products[['rating']]
            )
    
    def _compute_product_similarity(self):
        """
        Compute similarity matrix between products based on features.
        """
        try:
            # TF-IDF for text features
            tfidf_matrix = self.vectorizer.fit_transform(self.products['combined_features'])
            
            # Combine with numerical features
            numerical_features = self.products[['price_norm', 'rating_norm']].values
            combined_features = np.hstack((tfidf_matrix.toarray(), numerical_features))
            
            # Compute cosine similarity
            self.product_similarity = cosine_similarity(combined_features)
        except Exception as e:
            print(f"Error computing product similarity: {e}")
            raise
    
    def _get_user_profile(self, user_id):
        """
        Create a user profile based on their history.
        
        Args:
            user_id (str/int): User identifier
            
        Returns:
            dict: User profile with weighted preferences
        """
        profile = {
            'viewed_products': [],
            'purchased_products': [],
            'wishlist_products': []
        }
        
        if user_id in self.user_history:
            history = self.user_history[user_id]
            profile['viewed_products'] = history.get('views', [])
            profile['purchased_products'] = history.get('purchases', [])
            profile['wishlist_products'] = history.get('wishlist', [])
            
        return profile
    
    def recommend_products(self, user_id, top_n=5):
        """
        Generate product recommendations for a user.
        
        Args:
            user_id (str/int): User identifier
            top_n (int): Number of recommendations to return
            
        Returns:
            list: Recommended product IDs
        """
        try:
            if self.product_similarity is None:
                raise ValueError("Product similarity matrix not computed. Load product data first.")
            
            user_profile = self._get_user_profile(user_id)
            
            # Combine all interacted products with weights
            interacted_products = []
            weights = []
            
            # Purchases get highest weight
            for product_id in user_profile['purchased_products']:
                interacted_products.append(product_id)
                weights.append(2.0)  # Higher weight for purchases
                
            # Wishlist items get medium weight
            for product_id in user_profile['wishlist_products']:
                interacted_products.append(product_id)
                weights.append(1.5)
                
            # Views get lowest weight
            for product_id in user_profile['viewed_products']:
                interacted_products.append(product_id)
                weights.append(1.0)
                
            if not interacted_products:
                # Cold start: return popular products
                return self._get_popular_products(top_n)
                
            # Get similarity scores for interacted products
            product_indices = [self.products[self.products['id'] == pid].index[0] for pid in interacted_products]
            weighted_similarity = np.zeros(self.product_similarity.shape[0])
            
            for idx, weight in zip(product_indices, weights):
                weighted_similarity += weight * self.product_similarity[idx]
                
            # Normalize scores
            weighted_similarity /= sum(weights)
            
            # Get top N recommendations (excluding already interacted products)
            recommendations = []
            sorted_indices = np.argsort(weighted_similarity)[::-1]
            
            for i in sorted_indices:
                product_id = self.products.iloc[i]['id']
                if product_id not in interacted_products:
                    recommendations.append(product_id)
                    if len(recommendations) >= top_n:
                        break
                        
            return recommendations
            
        except Exception as e:
            print(f"Error generating recommendations: {e}")
            return self._get_popular_products(top_n)
    
    def _get_popular_products(self, top_n):
        """
        Get popular products as fallback recommendation.
        
        Args:
            top_n (int): Number of products to return
            
        Returns:
            list: Product IDs
        """
        try:
            if 'rating' in self.products.columns and 'price' in self.products.columns:
                # Sort by rating and price (higher rating, lower price)
                popular = self.products.sort_values(
                    ['rating', 'price'], 
                    ascending=[False, True]
                ).head(top_n)['id'].tolist()
                return popular
            else:
                return self.products.head(top_n)['id'].tolist()
        except:
            return []
    
    def get_product_details(self, product_ids):
        """
        Get details for recommended products.
        
        Args:
            product_ids (list): List of product IDs
            
        Returns:
            DataFrame: Product details
        """
        try:
            return self.products[self.products['id'].isin(product_ids)]
        except Exception as e:
            print(f"Error getting product details: {e}")
            return pd.DataFrame()
```
