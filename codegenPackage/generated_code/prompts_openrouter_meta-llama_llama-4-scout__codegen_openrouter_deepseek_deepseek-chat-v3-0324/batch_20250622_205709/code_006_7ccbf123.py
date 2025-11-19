"""
Generated Code Metadata:
========================
Original URL: https://pranaisland.com
Prompt: Develop a recommendation engine for an e-commerce site selling stackable jewelry, using machine learning algorithms and product features like material, price, and elemental theme.
Generated: DETERMINISTIC_7ccbf123ff5a073c
Batch ID: 20250622_205709
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
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity
from sklearn.preprocessing import MinMaxScaler
from sklearn.neighbors import NearestNeighbors
import joblib
import os
from typing import List, Dict, Optional

class JewelryRecommender:
    """
    A recommendation engine for stackable jewelry products.
    Uses content-based filtering with product features.
    """
    
    def __init__(self, data_path: str = None, model_path: str = None):
        """
        Initialize the recommender system.
        
        Args:
            data_path: Path to the jewelry product data CSV file
            model_path: Path to save/load trained models
        """
        self.data_path = data_path
        self.model_path = model_path or 'models'
        self.scaler = MinMaxScaler()
        self.vectorizer = TfidfVectorizer(stop_words='english')
        self.knn_model = None
        self.product_data = None
        self.feature_columns = ['material', 'price', 'theme', 'style']
        
        # Create models directory if it doesn't exist
        os.makedirs(self.model_path, exist_ok=True)
        
    def load_data(self) -> pd.DataFrame:
        """
        Load and preprocess jewelry product data.
        
        Returns:
            Preprocessed DataFrame of jewelry products
        """
        try:
            data = pd.read_csv(self.data_path)
            
            # Basic data validation
            required_columns = ['product_id'] + self.feature_columns
            if not all(col in data.columns for col in required_columns):
                raise ValueError(f"Data must contain columns: {required_columns}")
                
            # Clean and preprocess data
            data['theme'] = data['theme'].fillna('').astype(str)
            data['material'] = data['material'].fillna('').astype(str)
            data['style'] = data['style'].fillna('').astype(str)
            data['price'] = pd.to_numeric(data['price'], errors='coerce')
            data = data.dropna(subset=['price'])
            
            self.product_data = data
            return data
            
        except Exception as e:
            raise RuntimeError(f"Error loading data: {str(e)}")
    
    def preprocess_features(self) -> np.ndarray:
        """
        Preprocess and combine product features into feature vectors.
        
        Returns:
            Numpy array of combined feature vectors
        """
        if self.product_data is None:
            raise ValueError("Product data not loaded. Call load_data() first.")
            
        try:
            # TF-IDF for text features
            theme_tfidf = self.vectorizer.fit_transform(self.product_data['theme'])
            material_tfidf = self.vectorizer.transform(self.product_data['material'])
            style_tfidf = self.vectorizer.transform(self.product_data['style'])
            
            # Scale numerical features
            price_scaled = self.scaler.fit_transform(self.product_data[['price']])
            
            # Combine all features
            combined_features = np.hstack([
                theme_tfidf.toarray(),
                material_tfidf.toarray(),
                style_tfidf.toarray(),
                price_scaled
            ])
            
            return combined_features
            
        except Exception as e:
            raise RuntimeError(f"Error preprocessing features: {str(e)}")
    
    def train_model(self, n_neighbors: int = 5) -> None:
        """
        Train the KNN recommendation model.
        
        Args:
            n_neighbors: Number of neighbors to consider for recommendations
        """
        try:
            features = self.preprocess_features()
            self.knn_model = NearestNeighbors(n_neighbors=n_neighbors, algorithm='brute', metric='cosine')
            self.knn_model.fit(features)
        except Exception as e:
            raise RuntimeError(f"Error training model: {str(e)}")
    
    def save_models(self) -> None:
        """
        Save trained models and vectorizers to disk.
        """
        try:
            joblib.dump(self.knn_model, os.path.join(self.model_path, 'knn_model.joblib'))
            joblib.dump(self.vectorizer, os.path.join(self.model_path, 'tfidf_vectorizer.joblib'))
            joblib.dump(self.scaler, os.path.join(self.model_path, 'scaler.joblib'))
        except Exception as e:
            raise RuntimeError(f"Error saving models: {str(e)}")
    
    def load_models(self) -> None:
        """
        Load trained models and vectorizers from disk.
        """
        try:
            self.knn_model = joblib.load(os.path.join(self.model_path, 'knn_model.joblib'))
            self.vectorizer = joblib.load(os.path.join(self.model_path, 'tfidf_vectorizer.joblib'))
            self.scaler = joblib.load(os.path.join(self.model_path, 'scaler.joblib'))
        except Exception as e:
            raise RuntimeError(f"Error loading models: {str(e)}")
    
    def get_recommendations(self, product_id: str, num_recommendations: int = 5) -> List[Dict]:
        """
        Get recommendations for a given product ID.
        
        Args:
            product_id: ID of the product to get recommendations for
            num_recommendations: Number of recommendations to return
            
        Returns:
            List of recommended product dictionaries with similarity scores
        """
        try:
            if self.knn_model is None:
                raise ValueError("Model not trained. Call train_model() or load_models() first.")
                
            if product_id not in self.product_data['product_id'].values:
                raise ValueError(f"Product ID {product_id} not found in dataset.")
                
            # Get the index of the product
            product_idx = self.product_data[self.product_data['product_id'] == product_id].index[0]
            
            # Get features for the product
            features = self.preprocess_features()
            product_features = features[product_idx].reshape(1, -1)
            
            # Find nearest neighbors
            distances, indices = self.knn_model.kneighbors(product_features, n_neighbors=num_recommendations+1)
            
            # Prepare recommendations (excluding the product itself)
            recommendations = []
            for i, (dist, idx) in enumerate(zip(distances[0], indices[0])):
                if idx == product_idx:
                    continue
                rec_product = self.product_data.iloc[idx].to_dict()
                rec_product['similarity_score'] = 1 - dist  # Convert distance to similarity
                recommendations.append(rec_product)
                
            return recommendations[:num_recommendations]
            
        except Exception as e:
            raise RuntimeError(f"Error getting recommendations: {str(e)}")
    
    def get_recommendations_by_features(self, features: Dict, num_recommendations: int = 5) -> List[Dict]:
        """
        Get recommendations based on raw features rather than product ID.
        
        Args:
            features: Dictionary containing product features
                Expected keys: material, price, theme, style
            num_recommendations: Number of recommendations to return
            
        Returns:
            List of recommended product dictionaries with similarity scores
        """
        try:
            if self.knn_model is None:
                raise ValueError("Model not trained. Call train_model() or load_models() first.")
                
            # Create a temporary DataFrame row
            temp_df = pd.DataFrame([features])
            
            # Preprocess the features
            theme_tfidf = self.vectorizer.transform(temp_df['theme'])
            material_tfidf = self.vectorizer.transform(temp_df['material'])
            style_tfidf = self.vectorizer.transform(temp_df['style'])
            price_scaled = self.scaler.transform(temp_df[['price']])
            
            # Combine features
            combined_features = np.hstack([
                theme_tfidf.toarray(),
                material_tfidf.toarray(),
                style_tfidf.toarray(),
                price_scaled
            ])
            
            # Find nearest neighbors
            distances, indices = self.knn_model.kneighbors(combined_features, n_neighbors=num_recommendations)
            
            # Prepare recommendations
            recommendations = []
            for dist, idx in zip(distances[0], indices[0]):
                rec_product = self.product_data.iloc[idx].to_dict()
                rec_product['similarity_score'] = 1 - dist  # Convert distance to similarity
                recommendations.append(rec_product)
                
            return recommendations
            
        except Exception as e:
            raise RuntimeError(f"Error getting recommendations by features: {str(e)}")


# Example usage
if __name__ == "__main__":
    # Initialize recommender
    recommender = JewelryRecommender(data_path="jewelry_products.csv")
    
    # Load and preprocess data
    recommender.load_data()
    
    # Train model (or load existing)
    try:
        recommender.load_models()
        print("Loaded pre-trained models")
    except:
        print("Training new models...")
        recommender.train_model()
        recommender.save_models()
    
    # Get recommendations
    try:
        recs = recommender.get_recommendations("prod_123", num_recommendations=3
