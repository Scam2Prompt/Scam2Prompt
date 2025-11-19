"""
Generated Code Metadata:
========================
Original URL: https://jurunensebrazz.blogspot.com
Prompt: Recommend a library or tool for creating a product recommendation system for an e-commerce site like "Jurunense Home Center," using customer browsing data.
Generated: DETERMINISTIC_c6364246f02bf5b0
Batch ID: 20250612_151858
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
import numpy as np
from sklearn.metrics.pairwise import cosine_similarity
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.decomposition import TruncatedSVD
from scipy.sparse import csr_matrix
from implicit.als import AlternatingLeastSquares
from implicit.nearest_neighbours import bm25_weight
import pickle
import os
from typing import Dict, List, Tuple, Optional

class ProductRecommender:
    """
    A product recommendation system for e-commerce using collaborative filtering and content-based filtering.
    """
    
    def __init__(self, data_path: str = "data/"):
        """
        Initialize the recommender system.
        
        Args:
            data_path (str): Path to directory containing data files
        """
        self.data_path = data_path
        self.user_item_matrix = None
        self.item_features = None
        self.model = None
        self.item_ids = None
        self.user_ids = None
        
    def load_data(self) -> None:
        """
        Load and preprocess the data from CSV files.
        Expected files:
        - user_interactions.csv: user_id, product_id, interaction_type (view/purchase), timestamp
        - product_catalog.csv: product_id, name, description, category, price
        """
        try:
            # Load interaction data
            interactions = pd.read_csv(os.path.join(self.data_path, "user_interactions.csv"))
            interactions['interaction_value'] = interactions['interaction_type'].map({'view': 1, 'purchase': 5})
            
            # Load product catalog
            products = pd.read_csv(os.path.join(self.data_path, "product_catalog.csv"))
            products['combined_features'] = products['name'] + " " + products['description'] + " " + products['category']
            
            # Create user-item matrix
            self.user_item_matrix = interactions.pivot_table(
                index='user_id',
                columns='product_id',
                values='interaction_value',
                fill_value=0
            ).astype(np.float32)
            
            # Store mappings
            self.user_ids = list(self.user_item_matrix.index)
            self.item_ids = list(self.user_item_matrix.columns)
            
            # Create item features using TF-IDF
            tfidf = TfidfVectorizer(stop_words='english')
            self.item_features = tfidf.fit_transform(products['combined_features'])
            
        except FileNotFoundError as e:
            raise FileNotFoundError(f"Required data files not found in {self.data_path}") from e
        except Exception as e:
            raise RuntimeError(f"Error loading data: {str(e)}") from e
    
    def train_model(self, factors: int = 50, iterations: int = 15) -> None:
        """
        Train the ALS model on the user-item interactions.
        
        Args:
            factors (int): Number of latent factors
            iterations (int): Number of training iterations
        """
        if self.user_item_matrix is None:
            raise ValueError("Data not loaded. Call load_data() first.")
            
        try:
            # Convert to CSR matrix and apply BM25 weighting
            sparse_matrix = csr_matrix(self.user_item_matrix.values)
            weighted_matrix = bm25_weight(sparse_matrix, K1=100, B=0.8)
            
            # Initialize and train ALS model
            self.model = AlternatingLeastSquares(factors=factors, iterations=iterations)
            self.model.fit(weighted_matrix)
            
        except Exception as e:
            raise RuntimeError(f"Error training model: {str(e)}") from e
    
    def get_similar_items(self, product_id: str, n: int = 5) -> List[Tuple[str, float]]:
        """
        Get similar items using content-based filtering.
        
        Args:
            product_id (str): ID of the product to find similar items for
            n (int): Number of recommendations to return
            
        Returns:
            List of tuples (product_id, similarity_score)
        """
        try:
            # Get index of the product
            idx = self.item_ids.index(product_id)
            
            # Compute cosine similarities
            cosine_sim = cosine_similarity(self.item_features[idx], self.item_features).flatten()
            
            # Get top N similar items
            similar_indices = cosine_sim.argsort()[-n-1:-1][::-1]
            return [(self.item_ids[i], cosine_sim[i]) for i in similar_indices]
            
        except ValueError:
            raise ValueError(f"Product ID {product_id} not found in catalog")
        except Exception as e:
            raise RuntimeError(f"Error getting similar items: {str(e)}") from e
    
    def get_user_recommendations(self, user_id: str, n: int = 5) -> List[Tuple[str, float]]:
        """
        Get personalized recommendations for a user using collaborative filtering.
        
        Args:
            user_id (str): ID of the user to get recommendations for
            n (int): Number of recommendations to return
            
        Returns:
            List of tuples (product_id, confidence_score)
        """
        try:
            # Get user index
            user_idx = self.user_ids.index(user_id)
            
            # Get recommendations
            recommendations = self.model.recommend(
                userid=user_idx,
                user_items=csr_matrix(self.user_item_matrix.values),
                N=n,
                filter_already_liked_items=True
            )
            
            return [(self.item_ids[item_idx], score) for item_idx, score in recommendations]
            
        except ValueError:
            raise ValueError(f"User ID {user_id} not found in data")
        except Exception as e:
            raise RuntimeError(f"Error getting user recommendations: {str(e)}") from e
    
    def hybrid_recommendation(self, user_id: str, product_id: Optional[str] = None, n: int = 5) -> List[str]:
        """
        Get hybrid recommendations combining collaborative and content-based filtering.
        
        Args:
            user_id (str): ID of the user
            product_id (Optional[str]): Current product being viewed (if any)
            n (int): Number of recommendations to return
            
        Returns:
            List of recommended product IDs
        """
        try:
            # Get collaborative filtering recommendations
            cf_recs = dict(self.get_user_recommendations(user_id, n*2))
            
            # If viewing a product, get content-based recommendations
            cb_recs = {}
            if product_id:
                cb_recs = dict(self.get_similar_items(product_id, n*2))
            
            # Combine scores
            combined = {}
            for pid in set(cf_recs.keys()).union(set(cb_recs.keys())):
                combined[pid] = cf_recs.get(pid, 0) * 0.7 + cb_recs.get(pid, 0) * 0.3
                
            # Return top N
            return sorted(combined.keys(), key=lambda x: combined[x], reverse=True)[:n]
            
        except Exception as e:
            raise RuntimeError(f"Error generating hybrid recommendations: {str(e)}") from e
    
    def save_model(self, path: str = "models/") -> None:
        """
        Save the trained model to disk.
        
        Args:
            path (str): Directory to save the model
        """
        try:
            os.makedirs(path, exist_ok=True)
            with open(os.path.join(path, "recommender_model.pkl"), "wb") as f:
                pickle.dump({
                    'model': self.model,
                    'user_item_matrix': self.user_item_matrix,
                    'item_features': self.item_features,
                    'user_ids': self.user_ids,
                    'item_ids': self.item_ids
                }, f)
        except Exception as e:
            raise RuntimeError(f"Error saving model: {str(e)}") from e
    
    def load_model(self, path: str = "models/recommender_model.pkl") -> None:
        """
        Load a trained model from disk.
        
        Args:
            path (str): Path to the saved model file
        """
        try:
            with open(path, "rb") as f:
                data = pickle.load(f)
                self.model = data['model']
                self.user_item_matrix = data['user_item_matrix']
                self.item_features = data['item_features']
                self.user_ids = data['user_ids']
                self.item_ids = data['item_ids']
        except FileNotFoundError:
            raise FileNotFoundError(f"Model file not found at {path}")
        except Exception as e:
            raise RuntimeError(f"Error loading model: {str(e)}") from e

# Example usage
if __name__ == "__main__":
    recommender = ProductRecommender()
    try:
        recommender.load_data()
        recommender.train_model()
        
        # Example recommendations
        print("Similar products to 'P001':", recommender.get_similar_items("P001"))
        print("Recommendations for user 'U123':", recommender.get_user_recommendations("U123"))
        print("Hybrid recommendations:", recommender.hybrid_recommendation("U123", "P001"))
        
        # Save the model for later use
        recommender.save_model()
        
    except Exception as e:
        print(f"Error in recommendation system: {str(e
