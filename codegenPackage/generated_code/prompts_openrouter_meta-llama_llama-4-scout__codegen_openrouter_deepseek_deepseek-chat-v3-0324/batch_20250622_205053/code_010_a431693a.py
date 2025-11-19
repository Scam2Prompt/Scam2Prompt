"""
Generated Code Metadata:
========================
Original URL: https://www.tiktokshopvn.com.vn
Prompt: Design a simple product recommendation system using Python and machine learning libraries, based on customer reviews and ratings, similar to those on TikTok Shop VN.
Generated: DETERMINISTIC_a431693a01b5a5db
Batch ID: 20250622_205053
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
from sklearn.metrics.pairwise import linear_kernel
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import MinMaxScaler
from scipy.sparse import hstack
import joblib
import warnings

warnings.filterwarnings('ignore')

class ProductRecommender:
    """
    A product recommendation system based on customer reviews and ratings.
    """
    
    def __init__(self):
        self.vectorizer = TfidfVectorizer(stop_words='english')
        self.scaler = MinMaxScaler()
        self.model = None
        self.product_data = None
        self.feature_matrix = None
        
    def load_data(self, filepath):
        """
        Load product data from a CSV file.
        Expected columns: product_id, product_name, category, description, rating, review_text
        """
        try:
            self.product_data = pd.read_csv(filepath)
            print("Data loaded successfully.")
        except Exception as e:
            print(f"Error loading data: {e}")
            raise
    
    def preprocess_data(self):
        """
        Preprocess the data by handling missing values and creating features.
        """
        if self.product_data is None:
            raise ValueError("No data loaded. Please load data first.")
            
        try:
            # Fill missing values
            self.product_data['description'].fillna('', inplace=True)
            self.product_data['review_text'].fillna('', inplace=True)
            self.product_data['rating'].fillna(self.product_data['rating'].mean(), inplace=True)
            
            # Combine text features
            self.product_data['combined_text'] = self.product_data['description'] + " " + self.product_data['review_text']
            
            print("Data preprocessing completed.")
        except Exception as e:
            print(f"Error during preprocessing: {e}")
            raise
    
    def create_feature_matrix(self):
        """
        Create feature matrix using TF-IDF for text and scaled ratings.
        """
        try:
            # TF-IDF for text features
            tfidf_matrix = self.vectorizer.fit_transform(self.product_data['combined_text'])
            
            # Scale ratings
            scaled_ratings = self.scaler.fit_transform(self.product_data[['rating']])
            
            # Combine features
            self.feature_matrix = hstack([tfidf_matrix, scaled_ratings])
            
            print("Feature matrix created.")
        except Exception as e:
            print(f"Error creating feature matrix: {e}")
            raise
    
    def train_model(self):
        """
        Train the recommendation model using cosine similarity.
        """
        try:
            # Compute cosine similarity matrix
            cosine_sim = linear_kernel(self.feature_matrix, self.feature_matrix)
            self.model = cosine_sim
            print("Model trained successfully.")
        except Exception as e:
            print(f"Error training model: {e}")
            raise
    
    def get_recommendations(self, product_id, top_n=5):
        """
        Get product recommendations for a given product ID.
        
        Args:
            product_id: ID of the product to get recommendations for
            top_n: Number of recommendations to return
            
        Returns:
            List of recommended product IDs and names
        """
        if self.model is None:
            raise ValueError("Model not trained. Please train the model first.")
            
        try:
            # Get the index of the product
            idx = self.product_data.index[self.product_data['product_id'] == product_id].tolist()[0]
            
            # Get similarity scores
            sim_scores = list(enumerate(self.model[idx]))
            
            # Sort products by similarity score
            sim_scores = sorted(sim_scores, key=lambda x: x[1], reverse=True)
            
            # Get top N most similar products (excluding itself)
            sim_scores = sim_scores[1:top_n+1]
            
            # Get product indices and similarity scores
            product_indices = [i[0] for i in sim_scores]
            similarity_scores = [i[1] for i in sim_scores]
            
            # Return recommendations with scores
            recommendations = self.product_data.iloc[product_indices][['product_id', 'product_name']]
            recommendations['similarity_score'] = similarity_scores
            
            return recommendations.to_dict('records')
        except Exception as e:
            print(f"Error getting recommendations: {e}")
            raise
    
    def save_model(self, filepath):
        """
        Save the trained model and vectorizer to disk.
        """
        try:
            joblib.dump({
                'vectorizer': self.vectorizer,
                'scaler': self.scaler,
                'model': self.model,
                'product_data': self.product_data
            }, filepath)
            print(f"Model saved successfully to {filepath}")
        except Exception as e:
            print(f"Error saving model: {e}")
            raise
    
    def load_model(self, filepath):
        """
        Load a trained model from disk.
        """
        try:
            saved_data = joblib.load(filepath)
            self.vectorizer = saved_data['vectorizer']
            self.scaler = saved_data['scaler']
            self.model = saved_data['model']
            self.product_data = saved_data['product_data']
            print(f"Model loaded successfully from {filepath}")
        except Exception as e:
            print(f"Error loading model: {e}")
            raise

# Example usage
if __name__ == "__main__":
    # Initialize recommender
    recommender = ProductRecommender()
    
    # Load sample data (replace with your actual data path)
    recommender.load_data('product_reviews.csv')
    
    # Preprocess data
    recommender.preprocess_data()
    
    # Create features
    recommender.create_feature_matrix()
    
    # Train model
    recommender.train_model()
    
    # Get recommendations for a product
    recommendations = recommender.get_recommendations('prod123')
    print("Recommendations:", recommendations)
    
    # Save model for future use
    recommender.save_model('product_recommender_model.joblib')
```
